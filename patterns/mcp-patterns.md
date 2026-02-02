# MCP Patterns and Security

**Sources**:
- [Nate B. Jones - MCP Implementation Guide](https://natesnewsletter.substack.com/p/the-mcp-implementation-guide-solving) (Evidence Tier B)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) (Evidence Tier A)
- [OWASP Guide for Securely Using Third-Party MCP Servers](https://genai.owasp.org/resource/cheatsheet-a-practical-guide-for-securely-using-third-party-mcp-servers-1-0/) (Evidence Tier A)

**Evidence Tier**: A (Industry standard - OWASP security framework)

## The Core Problem

Teams are connecting MCP wrong. The Model Context Protocol is powerful, but its **300-800ms baseline latency** destroys user experience when placed in the wrong locations.

**MCP belongs in**: Decision support, development assistance, background analysis
**MCP does NOT belong in**: Checkout flows, real-time trading, transaction paths

---

## The 7 Failure Modes

### 1. Universal Router Trap

**Mistake**: Routing all requests through MCP
**Symptom**: Everything gets slower
**Impact**: 300-800ms added to every operation

**Reality Check**:
- Not every request needs AI analysis
- Simple operations should stay simple
- MCP is for intelligence, not routing

**Fix**: Route selectively. Only send requests that need AI analysis.

### 2. Kitchen Sink Server Pattern

**Mistake**: Creating overly permissive MCP servers with too many capabilities
**Symptom**: Security nightmares, confused AI behavior
**Impact**: Command injection vulnerabilities, data exposure

**Security Reality**: ~43% of MCP servers have command injection vulnerabilities. Only ~10 of 5,960+ available servers are genuinely trustworthy.

**Fix**:
- Minimal capabilities per server
- Explicit permission boundaries
- Security audit before deployment

### 3. Real-Time Context Delusion

**Mistake**: Using MCP in latency-sensitive paths
**Symptom**: Destroyed conversion rates, frustrated users
**Impact**: E-commerce abandonment, failed transactions

**Where It Kills**:
- Checkout flows
- Search results
- Form submissions
- Real-time pricing

**Fix**: Keep MCP out of user-facing transaction paths.

### 4. Permission Overexposure

**Mistake**: Granting broad permissions "to make it work"
**Symptom**: AI accessing data it shouldn't
**Impact**: Data leakage, compliance violations

**Fix**:
- Principle of least privilege
- Scoped tokens per context
- Regular permission audits

### 5. Transaction Path Integration

**Mistake**: Placing MCP in critical business workflows
**Symptom**: Transaction failures when MCP has issues
**Impact**: Revenue loss, customer trust erosion

**Fix**: MCP for analysis, not execution. Keep transactions on traditional rails.

### 6. Hot Path Placement

**Mistake**: MCP on frequently-accessed endpoints
**Symptom**: Scale issues, cascading failures
**Impact**: System-wide degradation under load

**Fix**: Background processing, caching, async patterns.

### 7. Deployment Timeline Mismatch

**Mistake**: Expecting MCP to be production-ready immediately
**Symptom**: Rushing immature integrations to production
**Impact**: Reliability issues, rollbacks, lost confidence

**Fix**: Staged deployment, shadow mode testing, gradual rollout.

---

## Production-Proven Patterns

### Intelligence Layer Pattern (Block)

**Approach**: Background analysis without touching production systems
**Example**: Block analyzes millions of transactions for fraud patterns—MCP runs analysis, not transactions

**Architecture**:
```
[Transactions] → [Traditional System] → [Database]
                         ↓
                  [Batch Export]
                         ↓
                   [MCP Analysis]
                         ↓
                [Intelligence Dashboard]
```

**Key**: MCP never touches the transaction path.

### Sidecar Pattern (Zapier)

**Approach**: Enhance workflows without blocking users
**Result**: 89% AI adoption through non-blocking integration

**How It Works**:
- User completes action normally
- Sidecar process triggers AI enhancement
- Results appear asynchronously
- No user-perceived latency

**Best For**: Workflow enhancement, content enrichment, smart suggestions

### Batch Pattern

**Approach**: Process overnight, consume in morning
**Example**: Analyze day's data → Generate morning report

**Benefits**:
- Zero real-time impact
- Full dataset analysis
- Cost-efficient (off-peak compute)
- Predictable delivery

**Architecture**:
```
[Day's Data] → [Overnight Batch] → [MCP Processing] → [Morning Report]
```

---

## When MCP IS the Right Choice

While the failure modes above highlight what to avoid, MCP excels in specific development scenarios. For Claude Code specifically:

### Ideal MCP Use Cases

| Use Case | Why MCP Works | Example Servers |
|----------|---------------|-----------------|
| **Database Inspection** | Read-only analysis, no transaction impact | Postgres, SQLite, MongoDB |
| **Knowledge Search** | Background retrieval, user controls timing | Obsidian, Notion, memory servers |
| **External APIs** | Development assistance, not production paths | GitHub, Linear, Jira |
| **File System Access** | Controlled scope, sandboxed operations | filesystem (with constraints) |
| **Development Tools** | Analysis during development, not runtime | Security scanners, linters |
| **Knowledge Extraction** | Transcript/content retrieval, learning workflows | YouTube transcript, podcast servers |

### Database Inspection Pattern

**Best Use Case**: Understanding data structure and querying during development.

```
Claude Code → MCP (Postgres) → Read Schema/Query Data
                ↓
        Development Insights (not production transactions)
```

**Implementation**:
```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres",
               "postgresql://user:pass@localhost/dev_db"]
    }
  }
}
```

**Key Constraint**: Connect to development/read-replica databases, never production write paths.

### Knowledge Base Pattern

**Best Use Case**: Searching documentation, notes, and project context.

```
Claude Code → MCP (Obsidian/Notion) → Search Knowledge Base
                ↓
        Relevant Context for Current Task
```

**Why It Works**:
- User controls when to invoke (not in hot paths)
- Latency acceptable for research operations
- Enhances context without blocking workflow

### External Service Integration Pattern

**Best Use Case**: Fetching project context from external tools during development.

```
Claude Code → MCP (GitHub/Linear) → Fetch Issues/PRs
                ↓
        Context for Implementation Decisions
```

**Implementation Guidance**:
- Read-only operations preferred
- Write operations require explicit user confirmation
- Never automate without human-in-the-loop

### Knowledge Extraction Pattern (YouTube, Podcasts)

**Best Use Case**: Extracting transcripts and content from video/audio platforms for knowledge management.

```
Claude Code → MCP (YouTube Transcript) → Fetch Transcript
                ↓
        Structured Knowledge for Research/Learning
```

**Recommended Server**: `@kimtaeyoon83/mcp-server-youtube-transcript` (449+ stars, actively maintained)

**Configuration**:
```json
{
  "mcpServers": {
    "youtube-transcript": {
      "command": "npx",
      "args": ["-y", "@kimtaeyoon83/mcp-server-youtube-transcript"]
    }
  }
}
```

**Why It Works**:
- Zero-setup (remote hosted or npx)
- Read-only (fetches public transcripts only)
- User controls when to invoke
- Ideal for learning workflows and content synthesis

**Two-Part Pattern for Personal Playlists**:

MCP servers only access public YouTube content. For personal playlists (Liked, Watch Later, Favorites), combine with a local extraction tool:

```
Part 1: Personal Playlist Export (local tool)
┌─────────────────────────────────────────────────┐
│ yt-playlist-export (browser cookies)            │
│ - Likes (LL), Watch Later (WL), Favorites       │
│ - Outputs: video_id, title, channel, url        │
└─────────────────────────────────────────────────┘
                    ↓
Part 2: Transcript Extraction (MCP server)
┌─────────────────────────────────────────────────┐
│ youtube-transcript MCP server                   │
│ - Accepts video_id from Part 1                  │
│ - Returns full transcript with timestamps       │
└─────────────────────────────────────────────────┘
                    ↓
           Knowledge Base Integration
```

**Implementation**:
```bash
# Part 1: Install playlist export tool
pip install yt-playlist-export

# Export liked videos (requires browser cookies)
yt-playlist-export --playlist LL --output liked-videos.json

# Part 2: MCP server provides get_transcript tool
# Claude Code can then fetch transcripts for each video_id
```

**Security Notes**:
- yt-playlist-export reads browser cookies (run locally only)
- MCP transcript servers are read-only and safe
- No OAuth tokens stored—uses existing browser session

**Alternative: Direct Python API**:

For batch processing or when MCP setup is impractical, use `youtube-transcript-api` directly:

```bash
pip install youtube-transcript-api
```

```python
from youtube_transcript_api import YouTubeTranscriptApi

api = YouTubeTranscriptApi()
entries = api.fetch("VIDEO_ID", languages=['en'])

for entry in entries:
    print(f"[{int(entry.start)//60}:{int(entry.start)%60:02d}] {entry.text}")
```

**Note**: YouTube may rate-limit or block cloud IPs. Use browser cookies or proxy for production workflows.

**Best For**: Content creators tracking inspiration, researchers aggregating expert content, learning from curated video lists.

### Quick-Start MCP Configuration

For development workflows, start with high-value, low-risk servers:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem",
               "/path/to/allowed/directory"]
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

**Selection Criteria**:
1. **Official servers first** - Anthropic-maintained servers are most trustworthy
2. **Read-only when possible** - Reduces risk surface
3. **Scoped access** - Limit filesystem to specific directories
4. **Development databases only** - Never connect to production

### Dynamic Tool Updates (v2.1.0+)

MCP servers now support `list_changed` notifications, enabling dynamic updates without reconnection:

**How it works**:
- Server notifies Claude Code when tools/prompts/resources change
- Claude Code refreshes available tools automatically
- No session restart required

**Use cases**:
- Development servers that add tools at runtime
- Context-sensitive tool availability
- Feature flags controlling tool exposure

**Implementation** (server-side):
```typescript
// Server sends notification when tools change
server.notification({
  method: "notifications/tools/list_changed"
});
```

**Benefit**: Hot-swappable MCP capabilities during active sessions.

### MCP vs Alternatives Decision

Before adding MCP, consider if alternatives suffice:

| Need | MCP Required? | Alternative |
|------|--------------|-------------|
| Database queries | Yes, for rich interaction | Direct CLI with Bash tool |
| File reading | No | Native Read tool |
| Git operations | No | Native Bash with git |
| API calls | Maybe | WebFetch for simple GET |
| Knowledge search | Yes, for integrated experience | Manual file reading |

**Rule of Thumb**: Use MCP when you need persistent, stateful connections or rich protocol interactions that native tools can't provide.

---

## Decision Framework

```
Is this request time-sensitive?
├── YES → Keep MCP out
│   └── Use traditional processing
└── NO → Consider MCP
    └── Is this analysis or execution?
        ├── Analysis → Good MCP fit
        └── Execution → Keep traditional
```

---

## OWASP MCP Security Framework

The [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) identifies critical security risks in MCP deployments. Key attack patterns:

### Attack Patterns

| Attack | Description | Impact |
|--------|-------------|--------|
| **Tool Poisoning** | Malicious commands embedded in tool descriptions | LLM executes hidden instructions, unauthorized data access |
| **Rug Pull** | Legitimate tool replaced with malicious version | Complete compromise of trusted workflow |
| **Schema Poisoning** | Corrupted interface definitions mislead the model | Model takes unintended actions |
| **Tool Shadowing** | Fake/duplicate tools intercept interactions | Data interception, altered responses |
| **Memory Poisoning** | Agent's memory corrupted with false information | Persistent manipulation of agent behavior |
| **Cross-Server Interference** | Multiple MCP servers create unintended execution chains | Privilege escalation, data leakage |
| **Supply Chain Attacks** | Compromised dependencies in MCP packages | Execution-level backdoors |

### Defense-in-Depth Checklist

Based on [OWASP's Practical Guide](https://genai.owasp.org/resource/cheatsheet-a-practical-guide-for-securely-using-third-party-mcp-servers-1-0/):

**Server Verification**:
- [ ] Pin MCP server version at approval time
- [ ] Use hash/checksum to verify tool descriptions unchanged
- [ ] Verify server source is from trusted registry
- [ ] Check for known vulnerabilities before deployment

**Authorization & Access**:
- [ ] Enforce OAuth 2.1/OIDC authentication
- [ ] Apply least-privilege per server
- [ ] Implement human-in-the-loop for sensitive operations
- [ ] Use scoped tokens per context (no broad permissions)

**Runtime Protection**:
- [ ] Sandbox MCP servers (container isolation)
- [ ] Implement behavioral monitoring for anomalies
- [ ] Content security policies for tool descriptions
- [ ] Rate limiting and circuit breakers

**Governance**:
- [ ] Maintain trusted MCP registry
- [ ] Require dual sign-off (security + domain owners)
- [ ] Staged deployment with monitoring
- [ ] Periodic re-validation of approved servers

### Quick Security Assessment

Before adding any MCP server, answer:

```
1. Is the source verified and trusted?
   └── NO → Don't use it

2. Does it request more permissions than needed?
   └── YES → Reduce scope or reject

3. Can it be sandboxed?
   └── NO → Extra scrutiny on data access

4. Is there a less privileged alternative?
   └── YES → Use the alternative
```

---

## Security Checklist (Consolidated)

Before deploying any MCP server:

**Implementation Security**:
- [ ] Minimal capabilities (no kitchen sink)
- [ ] Scoped permissions per context
- [ ] Audit logging enabled
- [ ] Command injection review
- [ ] Data exposure assessment
- [ ] Rate limiting configured
- [ ] Graceful degradation path

**OWASP Compliance**:
- [ ] Server version pinned and checksummed
- [ ] OAuth 2.1/OIDC authentication enforced
- [ ] Sandboxing implemented
- [ ] Human-in-the-loop for sensitive operations
- [ ] Listed in trusted internal registry
- [ ] Periodic re-validation scheduled

---

## MCP Context Budget Management

**Source**: [January 2026 Production Experience](https://dev.to/valgard/claude-code-must-haves-january-2026-kem)

> "MCP tools can consume 40%+ context. Example: 81,986 tokens just for MCP tools at startup (41% of the 200k context window!)—almost half the available context before even a single line of code was loaded."

### The Hidden Cost of MCP

Each MCP server adds tool definitions to your context. With multiple servers enabled, you can lose significant context capacity before doing any actual work.

**Measured impact from production**:

| Configuration | MCP Tool Tokens | Remaining Context |
|--------------|-----------------|-------------------|
| 0 MCP servers | 0 | 200K (100%) |
| 2-3 servers | ~20K | 180K (90%) |
| 5-6 servers | ~50K | 150K (75%) |
| 10+ servers | ~82K+ | 118K (59%) |

### The Sweet Spot

Based on production experience, the recommended configuration:

```
4 plugins + 2 MCPs = optimal balance
```

**Recommended core MCPs**:
- Context7 (documentation search)
- Sequential Thinking (complex reasoning)

**Activate on-demand**:
- Database servers (when debugging data)
- Git servers (when complex git operations needed)
- Specialized domain servers (project-specific)

### Configuration Strategy

Use `disabledMcpServers` in project config to disable unused servers per project:

```json
// .mcp.json
{
  "mcpServers": {
    "postgres": { "command": "..." },
    "memory": { "command": "..." },
    "youtube": { "command": "..." }
  }
}

// .claude/settings.json (project-level)
{
  "disabledMcpServers": ["youtube", "memory"]
}
```

**Result**: Only `postgres` loads for this project, saving ~30K tokens.

### Monitoring Context Usage

Check your MCP context consumption:

```bash
# Launch with debug flag
claude --mcp-debug

# Look for tool registration messages
# Count tools registered per server
```

**Rule of thumb**: If you have >15 MCP tools registered, you're likely over-budget.

### Dynamic Loading Pattern (v2.1.0+)

With `list_changed` notifications, servers can register tools dynamically:

```
Session start:
├── Core tools only (~5 tools)
├── User requests specific capability
├── Server registers additional tools
└── Context grows incrementally
```

**Benefit**: Start lean, expand as needed—not all tools at once.

---

## Building MCP Servers for Claude Code

When building custom MCP servers for your project, follow these implementation lessons learned from production deployments.

### Start with a Specification

**Write a spec before coding**. Define:
1. **Tools** (2-4 max) - What actions can be performed
2. **Resources** (1-3) - What data can be read
3. **Input/Output schemas** - Exact JSON structure

```markdown
## Tool: validate_patterns
Purpose: Check pattern files for issues
Input: { action: "validate_all" | "validate_single", pattern_id?: string }
Output: { summary: { valid: int, broken: int }, results: [...] }
```

**Lesson learned**: The original spec had 4 workflows; we simplified to 2. Spec first lets you evaluate scope before investing in code.

### Simplify Ruthlessly

**Start with 2 workflows, not 4**. You can always add more.

| Original Spec | Simplified | Rationale |
|---------------|------------|-----------|
| extraction_workflow | Removed | Manual updates sufficient for docs repo |
| changelog_workflow | Folded into sync | Same data sources |
| validation_workflow | validate_patterns | Core value |
| synthesis_workflow | sync_documentation | Core value |

**Lesson learned**: A documentation repo doesn't need automated thought-leader monitoring. Match complexity to actual project needs.

### Directory Structure

Organize for maintainability:

```
mcp-server/
├── pyproject.toml              # Dependencies (mcp>=1.0, pydantic, httpx)
├── .gitignore                  # Exclude .venv/, __pycache__/
├── README.md                   # Usage examples
├── src/your_mcp_server/
│   ├── __init__.py
│   ├── server.py               # Entry point with @server decorators
│   ├── tools/                  # One file per tool
│   │   ├── __init__.py
│   │   └── your_tool.py
│   ├── resources/              # Resource registries
│   │   └── your_registry.py
│   └── parsers/                # File parsing logic
│       └── your_parser.py
└── tests/
    └── test_your_tool.py
```

### Configuration via .mcp.json

Use `.mcp.json` in project root:

```json
{
  "mcpServers": {
    "your-server": {
      "command": "./mcp-server/.venv/bin/python",
      "args": ["-m", "your_mcp_server.server"],
      "cwd": "./mcp-server/src",
      "env": {
        "REPO_ROOT": "../.."
      }
    }
  }
}
```

**Key points**:
- Use virtual environment path for `command` (not system Python)
- Set `cwd` to source directory
- Pass project paths via `env` variables

### Parser Pitfalls

**Strip code blocks before link extraction**. Markdown examples contain fake links that cause false validation errors.

```python
def _strip_code_blocks(self, content: str) -> str:
    """Remove code blocks to avoid false link detection."""
    content = re.sub(r'```[\s\S]*?```', '', content)
    content = re.sub(r'`[^`]+`', '', content)
    return content
```

**Lesson learned**: Pattern files contained example links inside code blocks. The naive parser flagged these as broken.

### Handle Multiple Link Formats

Different files use different link formats:

```python
# Must handle: patterns/xxx.md, ./xxx.md, /xxx.md
RELATED_PATTERN = re.compile(r'(?:patterns/|\./|/)([a-z0-9-]+)\.md')
```

**Lesson learned**: Initial regex only matched `patterns/xxx.md` but actual files used `./xxx.md`.

### Async Tool Functions

MCP tools should be async for network operations:

```python
async def validate_patterns(
    action: str,
    pattern_registry: PatternRegistry,
) -> dict[str, Any]:
    # External link validation needs async HTTP
    async with httpx.AsyncClient() as client:
        response = await client.head(url, timeout=5.0)
```

### Test Before Integration

Run the server directly before Claude Code integration:

```bash
# Install in venv
cd mcp-server && pip install -e .

# Test module loads
PYTHONPATH=src python -c "from your_server.server import server; print('OK')"

# Verify with claude mcp list
claude mcp list  # Should show: your-server: ... - ✓ Connected
```

### Virtual Environment Management

**Always use a project-local venv**:

```bash
cd mcp-server
python3 -m venv .venv
.venv/bin/pip install -e .
```

**Add to .gitignore immediately**:
```
.venv/
__pycache__/
*.egg-info/
.pytest_cache/
```

**Lesson learned**: Accidentally committed `.venv/` (600K+ files) on first attempt. Create `.gitignore` before any `git add`.

### Incremental Validation

Build validation in layers:

1. **Structure** - Required sections present
2. **Internal links** - Referenced files exist
3. **External links** - URLs reachable (with timeout, sampling)
4. **Evidence** - Tier claims match sources
5. **Cross-refs** - Bidirectional references complete

**Lesson learned**: Running all validations at once makes debugging hard. Build and test incrementally.

---

## Application to Claude Code

Claude Code's MCP integration should follow these patterns:

| Pattern | Claude Code Application |
|---------|------------------------|
| Intelligence Layer | Code analysis tools (linting, security scan) |
| Sidecar | Background documentation updates |
| Batch | Repository analysis overnight |

**Never** put MCP servers in:
- File save operations (use native filesystem)
- Git commits (use native git)
- Interactive typing (latency kills UX)

---

## SDD Phase Alignment

**Phase**: Cross-phase (security applies to all phases)

| SDD Phase | MCP Security Application |
|-----------|-------------------------|
| **Specify** | Define MCP requirements and security constraints |
| **Plan** | Design MCP architecture with security controls |
| **Tasks** | Include security verification in task breakdown |
| **Implement** | Apply defense-in-depth, verify compliance |

---

## Anti-Patterns

The 7 Failure Modes documented above represent the primary anti-patterns. Additionally:

### ❌ MCP as First Solution
**Problem**: Reaching for MCP when simpler alternatives exist
**Symptom**: Complex MCP setup for tasks native tools handle
**Solution**: Check if WebFetch, Bash, or native file tools suffice before adding MCP

### ❌ Trusting Community Servers Blindly
**Problem**: Installing MCP servers without security review
**Symptom**: ~43% of servers have command injection vulnerabilities
**Solution**: Apply OWASP MCP checklist, prefer official servers, review before trusting

### ❌ MCP for Real-Time Operations
**Problem**: Placing MCP in latency-sensitive paths
**Symptom**: 300-800ms baseline destroys user experience
**Solution**: Use Intelligence Layer/Sidecar/Batch patterns instead

### ❌ Over-Permissioned Servers
**Problem**: Granting broad permissions "to make it work"
**Symptom**: Data leakage, compliance violations, AI accessing unintended data
**Solution**: Principle of least privilege, scoped tokens, regular audits

---

## Related Patterns

- [Advanced Tool Use](./advanced-tool-use.md) - Tool Search for token efficiency
- [Context Engineering](./context-engineering.md) - Security in context design
- [Plugins and Extensions](./plugins-and-extensions.md) - When to use MCP vs alternatives
- [Spec-Driven Development](./spec-driven-development.md) - Write spec before MCP implementation

## Reference Implementation

This repository includes a working MCP server example:

```
mcp-server/                      # Best Practices MCP Server
├── src/best_practices_mcp/
│   ├── server.py               # 2 tools: validate_patterns, sync_documentation
│   ├── tools/                  # Tool implementations
│   ├── resources/              # Pattern and source registries
│   └── parsers/                # Markdown parsing with code block handling
└── tests/                      # 9 passing tests
```

**Usage**: `claude mcp list` should show `best-practices: ... - ✓ Connected`

---

## Sources

- [Nate B. Jones - MCP Implementation Guide](https://natesnewsletter.substack.com/p/the-mcp-implementation-guide-solving)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- [OWASP Guide for Securely Using Third-Party MCP Servers v1.0](https://genai.owasp.org/resource/cheatsheet-a-practical-guide-for-securely-using-third-party-mcp-servers-1-0/)

*Last updated: February 2026*
