---
version-requirements:
  claude-code: "v2.1.0+"
version-last-verified: "2026-04-06"
measurement-claims:
  - claim: "Two distinct MCP server architectures validated: structured tools (Inspector, Pydantic schemas) vs orchestrated playbooks (TME MCP, multi-step execution)"
    source: "Direct analysis — mndr-review-automation + tme-mcp-server"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "Localhost-only enforcement prevents remote MCP connections via constructor validation"
    source: "Direct analysis — mndr-review-automation lib/inspector_client.py"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "Exponential backoff retry with configurable attempts eliminates transient MCP failures"
    source: "Direct analysis — mndr-review-automation lib/tme_playbook_client.py"
    date: "2026-04-06"
    revalidate: "2026-10-06"
status: PRODUCTION
last-verified: "2026-04-06"
evidence-tier: A
applies-to-signals: [harness-mcp]
revalidate-by: 2026-10-06
---

# MCP Client Integration: Patterns from Two Server Architectures

**Evidence Tier**: A — Direct production analysis of InspectorClient + TmePlaybookClient + TME MCP server

## Purpose

This document analyzes **MCP client integration patterns** from two production implementations — comparing how applications consume MCP servers, not how to build them. The existing [MCP Patterns](./mcp-patterns.md) document covers failure modes and OWASP mapping; this document covers the **client-side engineering**: connection lifecycle, error handling, caching, and the architectural difference between structured tool servers and orchestrated playbook servers.

---

## Two Server Architectures Compared

| Aspect | Inspector MCP (Entity Enrichment) | TME MCP (Playbook Orchestration) |
|--------|----------------------------------|----------------------------------|
| **Purpose** | Entity profiles, alert context, log search | Investigation playbooks, structured queries, schema search |
| **Tool style** | Typed convenience methods per tool | Registry/engine pattern with multi-step execution |
| **Schema validation** | None (free-form results) | Pydantic `QueryDescriptor` + JSON schema indexes |
| **Result handling** | `structuredContent` preferred, text fallback | JSON strings with metadata wrapping |
| **Error handling** | Returns `None` on all failures | Exponential backoff retry + JSON error context |
| **Authorization** | None (localhost-only security) | Admin token header + middleware filtering |
| **Caching** | Per-entity thread-safe cache | Schema indexes in memory, playbook registry |
| **Middleware** | N/A (client only) | PingMiddleware, LoggingMiddleware, AdminGateMiddleware |

---

## Connection Protocol: JSON-RPC 2.0 over Streamable HTTP

Both clients implement the same MCP Streamable HTTP transport:

### Session Lifecycle

**1. Initialize** (POST `/mcp`, no session header):

```python
resp = requests.post(
    self.mcp_url,
    json={
        "jsonrpc": "2.0",
        "method": "initialize",
        "params": {
            "protocolVersion": "2025-03-26",
            "capabilities": {},
            "clientInfo": {"name": "mndr-review-automation", "version": "1.0.0"},
        },
        "id": _next_id(),
    },
)
self.session_id = resp.headers.get("Mcp-Session-Id")
```

**2. Tool calls** (POST `/mcp`, with `Mcp-Session-Id` header):

```python
resp = requests.post(
    self.mcp_url,
    json={
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {"name": tool_name, "arguments": arguments},
        "id": _next_id(),
    },
    headers={"Content-Type": "application/json", "Mcp-Session-Id": self.session_id},
    timeout=self.timeout,
)
```

**3. Cleanup** (DELETE `/mcp`, with session header):

```python
requests.delete(
    self.mcp_url,
    headers={"Mcp-Session-Id": self.session_id},
    timeout=10,
)
```

### Context Manager Pattern

Both clients implement `__enter__`/`__exit__` for automatic cleanup:

```python
with InspectorClient(base_url="http://localhost:8080") as client:
    profile = client.profile_entity("10.0.0.1")
# session automatically cleaned up
```

---

## Client Pattern 1: Structured Entity Tools (InspectorClient)

The InspectorClient wraps raw MCP tool calls in typed convenience methods with caching.

### Typed Wrappers

```python
def profile_entity(self, entity: str, time_window: int = 1440) -> Optional[dict]:
    """Build activity profile for an IP address. Cached per entity."""

def get_alert_context(self, source_ip=None, dest_ip=None, signature=None,
                       severity=None, time_window=1440, limit=100) -> Optional[dict]:
    """Retrieve security alerts (Suricata, notices, intel)."""

def search_logs(self, log_type: str, filters=None, time_window=1440,
                aggregation=None, limit=100) -> Optional[dict]:
    """Search any Corelight log type with filters and aggregations."""
```

**Design principle**: Typed wrappers serve two purposes — they provide IDE autocompletion and documentation, and they **normalize the result format** so callers don't need to handle both `structuredContent` and text content types.

### Result Handling Priority

```python
result = data.get("result", {})
if "structuredContent" in result:
    return result["structuredContent"]  # Preferred: typed data
content = result.get("content", [])
text_parts = [c.get("text", "") for c in content if c.get("type") == "text"]
return {"text": "\n".join(text_parts)}  # Fallback: text extraction
```

### Thread-Safe Entity Caching

```python
def __init__(self, ...):
    self._entity_cache: dict = {}
    self._cache_lock = threading.Lock()

def profile_entity(self, entity, time_window=1440):
    with self._cache_lock:
        if entity in self._entity_cache:
            return self._entity_cache[entity]
    result = self._call_tool("profile_entity", {...})
    if result:
        with self._cache_lock:
            self._entity_cache[entity] = result
    return result
```

**Why thread-safe**: The mndr-review-automation pipeline processes multiple findings concurrently. Without the lock, two threads profiling the same IP could both miss the cache and issue duplicate MCP calls.

### Error Philosophy: Graceful Degradation

The InspectorClient returns `None` on all failures — `ConnectionError`, `Timeout`, HTTP errors, JSON parse errors. No exceptions propagate to callers.

**Why**: Entity enrichment is optional in the pipeline. A failing MCP server should degrade the analysis quality (missing entity profiles), not halt the pipeline. The caller checks `if profile is not None` and proceeds with or without enrichment.

---

## Client Pattern 2: Orchestrated Playbooks (TmePlaybookClient)

The TmePlaybookClient adds retry logic and calls an MCP server that executes multi-step investigation playbooks.

### Retry with Exponential Backoff

```python
def _with_retry(self, func):
    last_exc = None
    for attempt in range(1 + self.max_retries):
        try:
            return func()
        except (requests.ConnectionError, requests.Timeout) as e:
            last_exc = e
            if attempt < self.max_retries:
                wait = self.retry_backoff * (2 ** attempt)
                time.sleep(wait)
    return None
```

**Configuration via environment**:

- `TME_MCP_RETRIES=2` (default: 3 total attempts)
- `TME_MCP_RETRY_BACKOFF=1.0` (default: 1s, 2s, 4s)

**Why retry here but not InspectorClient**: Playbook execution is a heavier operation (multi-step, 300s timeout). A transient network blip during a 5-minute playbook run is worth retrying. Entity profiling is lightweight (60s timeout) — if it fails, move on.

### Server-Side: FastMCP with Middleware Stack

The TME MCP server uses FastMCP with a composable middleware stack:

```python
_middleware = [PingMiddleware(interval_ms=15000), LoggingMiddleware()]
if admin_mode:
    _middleware.append(AdminGateMiddleware(token=admin_token))

mcp = FastMCP(name="Corelight Code Execution Server",
              lifespan=server_lifespan,
              middleware=_middleware)
```

**Middleware layers**:

| Middleware | Purpose | Mechanism |
|-----------|---------|-----------|
| PingMiddleware | Keep-alive for long-running playbooks | 15s interval heartbeat |
| LoggingMiddleware | Correlation ID tracing | `uuid[:12]` per tool call, structured logging |
| AdminGateMiddleware | Tool-level authorization | `X-Admin-Token` header check; filters admin tools from `list_tools` |

### Schema Validation: Query Builder Pattern

The TME MCP server validates all queries through a Pydantic `QueryDescriptor`:

```python
class QueryDescriptor(BaseModel):
    index: str = "corelight"
    sourcetypes: list[str] = []
    filters: list[Filter] = []
    fields: list[str] = []
    sort: list[SortClause] = []
    limit: int = 100
    aggregation: Optional[Aggregation] = None
```

Queries are built → compiled (per connector: Splunk SPL, CrowdStrike XQL, etc.) → executed. This query builder pattern ensures agents cannot construct malformed or injection-vulnerable queries — the `QueryCompiler` only accepts validated descriptors.

### Rich Error Responses

Server tools return JSON error objects with full diagnostic context:

```json
{
    "error": "Unknown log type: 'connn'",
    "valid_log_types": ["conn", "dns", "http", "ssl", ...],
    "hint": "Did you mean 'conn'?"
}
```

This gives the calling agent enough context to self-correct without a human diagnosing "tool call failed."

---

## Security: Localhost-Only Enforcement

### Client-Side Enforcement

```python
if not self.base_url.startswith(("http://localhost", "http://127.0.0.1")):
    raise ValueError(f"InspectorClient only connects to localhost. Got: {self.base_url}")
```

Enforced in `__init__()` — before any connection is attempted. This prevents configuration errors from accidentally routing MCP traffic to remote endpoints.

### Server-Side Authorization

The AdminGateMiddleware hides admin tools from unauthorized callers and rejects admin tool calls:

```python
async def on_list_tools(self, context, call_next):
    tools = await call_next(context)
    if self._is_authorized():
        return tools
    return [t for t in tools if not t.name.startswith(_ADMIN_TOOL_PREFIX)]
```

Non-admin callers don't even see admin tools in the tool list — they can't attempt calls they're not authorized for.

---

## Diagnostic: Choosing Between Architectures

```
Does your MCP server execute multi-step workflows?
├── No → Structured tool pattern (InspectorClient-style)
│   ├── Typed convenience wrappers per tool
│   ├── Return None on failure (graceful degradation)
│   └── Cache results if tools are idempotent
└── Yes → Orchestrated pattern (TmePlaybookClient-style)
    ├── Retry with exponential backoff
    ├── Middleware for auth + tracing + keep-alive
    ├── Schema validation via query builder
    └── Rich error responses for agent self-correction
```

---

## Anti-Patterns

| Anti-Pattern | Symptom | Fix |
|-------------|---------|-----|
| Remote MCP without enforcement | Configuration typo routes PII to cloud endpoint | Constructor-level localhost validation |
| Exception propagation from optional enrichment | Pipeline crashes when MCP server is down | Return `None` pattern; caller checks and degrades gracefully |
| No retry for long-running operations | Transient failures during 5-minute playbooks | Exponential backoff with configurable attempts |
| Raw JSON-RPC in application code | Protocol details leak into business logic | Typed wrappers that handle `structuredContent` vs text fallback |
| Missing correlation IDs | Cannot trace tool calls across middleware layers | LoggingMiddleware with `uuid[:12]` per call |
| Flat tool list without authorization | All callers see admin tools | AdminGateMiddleware filtering in `on_list_tools` |

---

## Sources

### Tier A (Direct Production Observation)

- InspectorClient analysis (April 2026) — `mndr-review-automation/lib/inspector_client.py` (272 lines), thread-safe caching, localhost enforcement, graceful degradation
- TmePlaybookClient analysis (April 2026) — `mndr-review-automation/lib/tme_playbook_client.py` (256 lines), exponential backoff, context manager pattern
- TME MCP server analysis (April 2026) — `tme-mcp-server/server.py` (1,216 lines), FastMCP middleware stack, Pydantic query validation, schema indexes

### Tier B (Validated / Expert Practitioner)

- MCP Streamable HTTP specification (2025-03-26 protocol version) — JSON-RPC 2.0, `Mcp-Session-Id` header, POST/DELETE lifecycle
- OWASP MCP Top 10 — Security considerations for MCP server implementations

### Related Analysis

- [MCP Patterns](./mcp-patterns.md) — 7 failure modes + OWASP mapping (server-side focus); this document covers client-side integration
- [MCP vs Skills Economics](./mcp-vs-skills-economics.md) — Cost/performance trade-offs between MCP and Skills
- [Safety & Sandboxing](./safety-and-sandboxing.md) — Security stack context for localhost enforcement
- [Local+Cloud LLM Orchestration](./local-cloud-llm-orchestration.md) — How Inspector MCP enrichment fits in the hybrid pipeline

---

*Last updated: April 2026*

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/mcp-patterns.md`](analysis/mcp-patterns.md) [EXTRACTED (1.00)] — references
- [`analysis/mcp-vs-skills-economics.md`](analysis/mcp-vs-skills-economics.md) [EXTRACTED (1.00)] — references
- [`AUDIT-CONTEXT.md`](AUDIT-CONTEXT.md) [EXTRACTED (1.00)] — references
- [`INDEX.md`](INDEX.md) [EXTRACTED (1.00)] — references

<!-- graphify-footer:end -->
