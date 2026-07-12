---
version-requirements:
  claude-code: "v2.0.0+"  # MCP support
version-last-verified: "2026-02-27"
measurement-claims:
  - claim: "MCP baseline latency: 300-800ms"
    source: "Nate B. Jones"
    date: "2025-10-15"
    revalidate: "2026-10-15"
  - claim: "~43% of MCP servers have command injection vulnerabilities (stale-pending-reverify: dated third-party security survey; revalidate window lapsed 2026-03-20, ecosystem has grown since)"
    source: "OWASP security audit"
    date: "2025-09-20"
    revalidate: "2026-10-10"
  - claim: "Only ~10 of 5,960+ MCP servers are genuinely trustworthy (stale-pending-reverify: dated third-party security survey; revalidate window lapsed 2026-03-20, ecosystem has grown since)"
    source: "OWASP security analysis"
    date: "2025-09-20"
    revalidate: "2026-10-10"
  - claim: "Tool Search achieves 89% token reduction (77K to 8.7K tokens)"
    source: "H-MCP-CONTEXT-01 hypothesis"
    date: "2026-04-15"
    revalidate: "2026-10-15"
  - claim: "15% of OpenClaw skills contain harmful instructions"
    source: "Jenova Research"
    date: "2026-03-01"
    revalidate: "2026-09-01"
  - claim: "MCP tool definitions consumed 81,986 tokens at startup (41% of a 200K context window) (stale-pending-remeasure: MCP tool search v2.1.121 changed token economics)"
    source: "valgard production analysis"
    date: "2026-01"
    revalidate: "2026-10-10"
  - claim: "Sweet spot: 4 plugins + 2 MCPs for optimal context usage (fallback config for non-Tool-Search setups; superseded as default guidance by deferred tool loading)"
    source: "valgard production analysis"
    date: "2026-01"
    revalidate: "2027-01-01"
status: PRODUCTION
last-verified: "2026-07-10"
evidence-tier: A
convergence: converged  # vendor-native MCP support (Claude Code v2.0.0+) + independent standards work (OWASP MCP Top 10, OASIS CoSAI CodeGuard) + multi-client adoption
applies-to-signals: [harness-mcp, commit-security-paths]
revalidate-by: 2026-10-15
---

# MCP Patterns and Security

> **Collapsed 2026-07-10 (Reduction Phase 4).** Mechanism documentation is now first-party (official MCP docs; tool search with deferred definitions default-on since v2.1.121). This is now the single MCP doc — it absorbed the still-true residue of mcp-daily-essentials.md (retired this pass). Kept delta: the OWASP MCP Top 10 mapping, the 4-plugin + 2-MCP sweet-spot evidence, and the token-economics measurements (flagged stale-pending-remeasure post-tool-search).

**Sources**:
- [Nate B. Jones - MCP Implementation Guide](https://natesnewsletter.substack.com/p/the-mcp-implementation-guide-solving) (Tier B)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) (Tier A)
- [OWASP Guide for Securely Using Third-Party MCP Servers](https://genai.owasp.org/resource/cheatsheet-a-practical-guide-for-securely-using-third-party-mcp-servers-1-0/) (Tier A)
- [valgard MCP Context Budget Analysis](https://dev.to/valgard/claude-code-must-haves-january-2026-kem) (Tier B, absorbed via mcp-daily-essentials.md)

**Evidence Tier**: A (anchored by the OWASP security framework; component claims carry their own tier — see Sources)

## The Core Problem

MCP is powerful, but its 300-800ms baseline latency destroys user experience when placed in the wrong location. MCP belongs in decision support, development assistance, and background analysis. It does not belong in checkout flows, real-time trading, or other transaction paths.

---

## The 7 Failure Modes

Seven anti-patterns account for most production MCP failures:

| # | Failure Mode | Mistake | Symptom / Impact | Fix |
|---|---|---|---|---|
| 1 | Universal Router Trap | Routing all requests through MCP | Everything gets slower — 300-800ms added to every operation | Route selectively; only send requests that need AI analysis |
| 2 | Kitchen Sink Server Pattern | Overly permissive servers with too many capabilities | Command injection vulnerabilities, data exposure — ~43% of servers affected, only ~10 of 5,960+ genuinely trustworthy (OWASP audit; stale-pending-reverify — dated survey, see frontmatter) | Minimal capabilities per server, explicit permission boundaries, security audit before deployment |
| 3 | Real-Time Context Delusion | Using MCP in latency-sensitive paths | Destroyed conversion rates in checkout flows, search results, form submissions, real-time pricing | Keep MCP out of user-facing transaction paths |
| 4 | Permission Overexposure | Granting broad permissions "to make it work" | Data leakage, compliance violations | Principle of least privilege, scoped tokens per context, regular permission audits |
| 5 | Transaction Path Integration | Placing MCP in critical business workflows | Transaction failures cascade when MCP has issues | MCP for analysis, not execution — keep transactions on traditional rails |
| 6 | Hot Path Placement | MCP on frequently-accessed endpoints | Scale issues, cascading failures under load | Background processing, caching, async patterns |
| 7 | Deployment Timeline Mismatch | Expecting MCP to be production-ready immediately | Reliability issues, rollbacks, lost confidence | Staged deployment, shadow-mode testing, gradual rollout |


---

## Production-Proven Patterns

**Intelligence Layer** (Block): background analysis without touching production systems — MCP runs fraud-pattern analysis on millions of transactions via batch export from the traditional system, never the transaction path itself.

**Sidecar** (Zapier): the user completes an action normally; a sidecar process triggers AI enhancement asynchronously, and results appear without user-perceived latency. Reported 89% AI adoption through this non-blocking integration.

**Batch**: process overnight, consume in the morning — analyze the day's data, generate a morning report. Zero real-time impact, full-dataset analysis, cost-efficient off-peak compute, predictable delivery.

---

## When MCP Is the Right Choice

### Ideal Use Cases

| Use Case | Why MCP Works | Example Servers |
|---|---|---|
| Database inspection | Read-only analysis, no transaction impact | Postgres, SQLite, MongoDB |
| Knowledge search | Background retrieval, user controls timing | Obsidian, Notion, memory servers |
| External APIs | Development assistance, not production paths | GitHub, Linear, Jira |
| File system access | Controlled scope, sandboxed operations | filesystem (with constraints) |
| Development tools | Analysis during development, not runtime | Security scanners, linters |
| Knowledge extraction | Transcript/content retrieval, learning workflows | YouTube transcript, podcast servers |

Across all of these: connect to development or read-replica databases, never production write paths; prefer read-only operations, and require explicit user confirmation for anything that writes.

### MCP vs. Native Alternatives

| Need | MCP Required? | Alternative |
|---|---|---|
| Database queries | Yes, for rich interaction | Direct CLI with Bash tool |
| File reading | No | Native Read tool |
| Git operations | No | Native Bash with git |
| API calls | Maybe | WebFetch for simple GET |
| Knowledge search | Yes, for integrated experience | Manual file reading |

Rule of thumb: reach for MCP when you need a persistent, stateful connection or a rich protocol interaction that native tools can't provide — not as the default first move.

### Server Selection Criteria

1. Official servers first — Anthropic-maintained servers are the most trustworthy.
2. Read-only when possible — reduces the risk surface.
3. Scoped access — limit filesystem servers to specific directories.
4. Development databases only — never connect to production.

### Which Specialized MCPs Are Worth the Context Cost

Absorbed from mcp-daily-essentials.md (retired 2026-07-10), which tracked the "top 4 daily MCP servers" question:

| Server | Pre-Tool-Search Context Cost | When to Enable | When to Skip |
|---|---|---|---|
| Context7 | ~15K tokens | Framework/library work, fast-moving APIs | Rarely — near-universal value |
| Sequential Thinking | ~10K tokens | Algorithm design, complex business logic, debugging logic errors | Simple CRUD operations only |
| Playwright (MCP) | ~20K tokens | Frontend/E2E testing, visual regression | Backend-only, no UI testing — or prefer the Playwright CLI (below) |
| DeepWiki | ~18K tokens (varies by repo size) | Exploring unfamiliar codebases, open-source contribution | Single, familiar codebase |

Context-cost figures above predate Tool Search's deferred loading (stale-pending-remeasure: MCP tool search v2.1.121 changed token economics) — treat as static-loading upper bounds, not current per-session costs; see MCP Context Budget: Then and Now, below.

---

## CLI vs MCP: The Token Efficiency Case

The Playwright team's `@playwright/cli` (February 2026) provides measured evidence for preferring CLI over MCP in coding-agent workflows; mcp-daily-essentials.md's community estimates extend the pattern to two more capabilities:

| Capability | MCP Token Cost | CLI Token Cost | Reduction |
|---|---|---|---|
| Browser automation (Playwright) | ~114,000 | ~27,000 | ~76% (4x) — measured, [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli), Tier B |
| GitHub operations | ~20,000 (GitHub MCP) | ~5,000 (`gh` CLI) | ~75% — community estimate, Tier B |
| File operations | ~15,000 (Filesystem MCP) | ~2,000 (native tools) | ~87% — community estimate, Tier B |

The architectural difference: MCP streams full page/response data (accessibility trees, screenshots, query results) into the LLM context window. CLI tools save that output to disk and return a file path or a compact reference; the agent reads only what it needs.

```bash
playwright-cli snapshot          # → compact YAML with refs (e21, e35)
playwright-cli click e21         # → minimal response
playwright-cli screenshot        # → file path, not image bytes
```

This is a different token-economics lever than Tool Search: Tool Search defers the cost of loading tool *definitions* at startup, while CLI-vs-MCP cuts the cost of tool *output* per call. The two are complementary, so none of the figures above carry the stale-pending-remeasure flag.

**Prefer CLI** when the agent has filesystem access (Claude Code, Copilot, Cursor) and the tool's output is large. **MCP is still better** when agents are sandboxed without filesystem access, or when you need persistent stateful connections (database sessions, streaming APIs).

---

## Decision Framework

```
Is this request time-sensitive?
├── YES → Keep MCP out; use traditional processing
└── NO → Consider MCP
    └── Is this analysis or execution?
        ├── Analysis → Good MCP fit
        └── Execution → Keep traditional
```

---

## OWASP MCP Security Framework

The [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) identifies critical security risks in MCP deployments.

### Attack Patterns

| Attack | Description | Impact |
|---|---|---|
| Tool Poisoning | Malicious commands embedded in tool descriptions | LLM executes hidden instructions, unauthorized data access |
| Rug Pull | Legitimate tool replaced with malicious version | Complete compromise of trusted workflow |
| Schema Poisoning | Corrupted interface definitions mislead the model | Model takes unintended actions |
| Tool Shadowing | Fake/duplicate tools intercept interactions | Data interception, altered responses |
| Memory Poisoning | Agent's memory corrupted with false information | Persistent manipulation of agent behavior |
| Cross-Server Interference | Multiple MCP servers create unintended execution chains | Privilege escalation, data leakage |
| Supply Chain Attacks | Compromised dependencies in MCP packages | Execution-level backdoors |

### Defense-in-Depth Checklist

Based on [OWASP's Practical Guide](https://genai.owasp.org/resource/cheatsheet-a-practical-guide-for-securely-using-third-party-mcp-servers-1-0/):

**Server Verification**
- [ ] Pin MCP server version at approval time
- [ ] Use hash/checksum to verify tool descriptions unchanged
- [ ] Verify server source is from a trusted registry
- [ ] Check for known vulnerabilities before deployment

**Authorization & Access**
- [ ] Enforce OAuth 2.1/OIDC authentication
- [ ] Apply least-privilege per server
- [ ] Implement human-in-the-loop for sensitive operations
- [ ] Use scoped tokens per context (no broad permissions)

**Runtime Protection**
- [ ] Sandbox MCP servers (container isolation)
- [ ] Implement behavioral monitoring for anomalies
- [ ] Content security policies for tool descriptions
- [ ] Rate limiting and circuit breakers
- [ ] Audit logging enabled for all tool invocations
- [ ] Graceful degradation path when a server is unavailable

**Governance**
- [ ] Maintain a trusted MCP registry
- [ ] Require dual sign-off (security + domain owners)
- [ ] Staged deployment with monitoring
- [ ] Periodic re-validation of approved servers

### Skill Supply Chain Risk

**Source**: H-AGENT-SECURITY-01 hypothesis

The supply chain risk extends beyond MCP servers to skills specifically. Jenova Research (March 2026) found that 15% of OpenClaw skills contain harmful instructions. In a single week, 230 malicious plugins were published on ClawHub using the ClickFix technique — embedding malicious instructions that appear benign during casual review.

This is distinct from the MCP server command injection rate documented under Kitchen Sink Server Pattern above: MCP vulnerabilities are implementation flaws in server code, while skill supply chain attacks are intentional hostile instructions embedded in skill definitions that the model follows faithfully.

> **Implication**: the Quick Security Assessment below was designed for MCP servers. Skill vetting requires additional scrutiny of instruction content, not just permission scope — a malicious skill can cause harm using only the permissions you explicitly grant it.

### Quick Security Assessment

Before adding any MCP server or skill, answer:

```
1. Is the source verified and trusted?
   └── NO → Don't use it

2. Does it request more permissions than needed?
   └── YES → Reduce scope or reject

3. Can it be sandboxed?
   └── NO → Extra scrutiny on data access

4. Is there a less privileged alternative?
   └── YES → Use the alternative

5. [Skills only] Have you reviewed the instruction content for hidden directives?
   └── NO → Read every instruction line before installing
   └── 15% of community skills contain harmful instructions (Jenova Research, March 2026)
```

---

## CodeGuard MCP Security Extensions

[CoSAI Project CodeGuard](https://github.com/cosai-oasis/project-codeguard) provides MCP-specific security rules that extend the OWASP guidance above:

| Control | Description |
|---|---|
| SPIFFE/SPIRE | Cryptographic workload identities for MCP server authentication |
| Transport Security | Stdio recommended for local; HTTP SSE requires mutual TLS, CORS/CSRF, payload limits |
| Cryptographic Attestation | Signatures + SBOM for all server code; client-side verification |
| OpenTelemetry | Immutable audit logging of tool usage, parameters, and originating prompts |
| Two-Stage Commits | High-impact tools require draft/preview then explicit confirmation with rollback |

See [Secure Code Generation](./secure-code-generation.md) for the full CodeGuard integration guide.

---

## MCP Context Budget: Then and Now

**The pre-Tool-Search problem** (stale-pending-remeasure: MCP tool search v2.1.121 changed token economics). Production measurements from January 2026 (valgard) found MCP tool definitions consuming 81,986 tokens at startup — 41% of a 200K context window — before a single line of code was loaded. Static-loading configurations scaled roughly:

| Configuration | MCP Tool Tokens | Remaining Context |
|---|---|---|
| 0 MCP servers | 0 | 200K (100%) |
| 2-3 servers | ~20K | 180K (90%) |
| 5-6 servers | ~50K | 150K (75%) |
| 10+ servers | ~82K+ | 118K (59%) |

**The sweet-spot heuristic** (absorbed from mcp-daily-essentials.md, retired 2026-07-10). valgard's production analysis settled on 4 plugins + 2 MCPs — Context7 + Sequential Thinking as the universal core, ~25K tokens combined — with database, git, and domain-specific servers activated on demand via `disabledMcpServers` in project-level `.claude/settings.json`. This was a single-workload measurement, never validated across project types, and mcp-daily-essentials.md documented several cases where "4 + 2" undershot or overshot: heavy documentation work did better on Context7 alone (more budget left for reading), security/data-pipeline work often justified 3+ specialized servers, and pure-reasoning exploration sometimes wanted zero MCPs.

**What changed**: Claude Code's Tool Search achieves an 89% token reduction (77K → 8.7K tokens; H-MCP-CONTEXT-01 hypothesis, 5/5 confidence, validated April 2026) by deferring tool schema loading until a tool is actually needed, gated on a 10K-token threshold rather than loading every definition at session start. Input schema overhead ran 60-80% of MCP tool token budgets (Speakeasy Dynamic Toolsets finding); lazy schema loading removes that cost until invocation. Workflow consolidation — 4-5 high-level tools outperforming 50+ granular ones — is now independently confirmed across 5 implementations.

**Rule of thumb, updated**: "4 plugins + 2 MCPs" and ">15 tools = over-budget" apply to static loading only, and remain a reasonable fallback for setups not running Tool Search. With Tool Search enabled (default since v2.1.121), the binding constraint shifts from "how many tools fit in context" to "how many tools can be discovered efficiently" — a materially higher ceiling this doc has not yet re-measured, hence the stale-pending-remeasure flags throughout this section.

---

## Related Patterns

- [Advanced Tool Use](../archive/patterns-v1/advanced-tool-use.md) — Tool Search for token efficiency
- [Context Engineering](./behavioral-insights.md) — security in context design
- [Plugins and Extensions](./plugins-and-extensions.md) — when to use MCP vs alternatives
- [Safety and Sandboxing](./safety-and-sandboxing.md) — OS-level security for MCP servers
- [Secure Code Generation](./secure-code-generation.md) — CodeGuard framework for secure AI-generated code
- [MCP vs Skills Economics](./mcp-vs-skills-economics.md) — token efficiency comparison across MCP and skills

`mcp-daily-essentials.md` is retired — its still-true content is absorbed here 2026-07-10. `mcp-client-integration.md` (client-side JSON-RPC session lifecycle, retry patterns) was deleted in an earlier 2026-07 reduction pass; the official MCP docs now cover connection mechanics.

## Sources

- [Nate B. Jones - MCP Implementation Guide](https://natesnewsletter.substack.com/p/the-mcp-implementation-guide-solving)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- [OWASP Guide for Securely Using Third-Party MCP Servers v1.0](https://genai.owasp.org/resource/cheatsheet-a-practical-guide-for-securely-using-third-party-mcp-servers-1-0/)
- H-MCP-CONTEXT-01 hypothesis (5/5 confidence, validated April 2026)
- H-AGENT-SECURITY-01 hypothesis (skill supply chain risk)
- Jenova Research: OpenClaw skill security analysis (March 2026)
- Speakeasy Dynamic Toolsets: input schema token overhead analysis
- [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) (Tier B)
- [valgard MCP Context Budget Analysis](https://dev.to/valgard/claude-code-must-haves-january-2026-kem) (Tier B, absorbed via mcp-daily-essentials.md)
- [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) (community MCP recommendations, absorbed via mcp-daily-essentials.md)
- [CoSAI Project CodeGuard](https://github.com/cosai-oasis/project-codeguard)

*Last updated: 2026-07-10 (collapsed; absorbed mcp-daily-essentials.md).*

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/behavioral-insights.md`](analysis/behavioral-insights.md) [EXTRACTED (1.00)] — references
- [`analysis/mcp-vs-skills-economics.md`](analysis/mcp-vs-skills-economics.md) [EXTRACTED (1.00)] — references
- [`AUDIT-CONTEXT.md`](AUDIT-CONTEXT.md) [EXTRACTED (1.00)] — references
- [`INDEX.md`](INDEX.md) [EXTRACTED (1.00)] — references

<!-- graphify-footer:end -->
