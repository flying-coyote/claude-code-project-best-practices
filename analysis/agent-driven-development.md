---
version-requirements:
  claude-code: "v2.1.0+"
version-last-verified: "2026-04-06"
measurement-claims:
  - claim: "100% agent co-authored commits across 81 commits in third-brain knowledge management hub"
    source: "Direct git history analysis — third-brain repository"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "95% agent co-authored commits (83/87) with PreToolUse security enforcement in mndr-review-automation"
    source: "Direct git history analysis — mndr-review-automation repository"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "22 commits in a single day during focused agent session (mndr-review-automation, 2026-03-31)"
    source: "Direct git history analysis — mndr-review-automation repository"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "Progressive infrastructure maturity from 0 harness components (tme-mcp-server, 10% co-authored) to full harness (mndr-review-automation, 95% co-authored)"
    source: "Direct portfolio analysis — 7 repositories"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "Hub-spoke cross-repo coordination tracking 4 repos with 120 commits in 14 days"
    source: "Direct analysis — third-brain cross-repo-progress.json"
    date: "2026-04-06"
    revalidate: "2026-10-06"
status: PRODUCTION
last-verified: "2026-07-10"
evidence-tier: Mixed
applies-to-signals: [commit-ai-coauthoring, commit-bursts, commit-cross-repo, harness-comprehensive]
revalidate-by: 2026-10-06
---

# Agent-Driven Development: Patterns from a 7-Repo Portfolio

> **Collapsed 2026-07-10 (Reduction Phase 4).** The how-to half is now first-party (official best-practices § Automate and scale + headless docs). Kept delta: the 7-repo portfolio's measured maturity model.

**Evidence Tier**: Mixed (A-B) — Direct production observation across 7 repositories (Tier A), corroborated by expert practitioner evidence (Tier B)

## Purpose

This document reports **quantified evidence of agent-driven development in practice** across a portfolio of 7 production repositories spanning security data pipelines, automated review generation, sensor monitoring, and knowledge management.

**How this differs from companion documents**:

- [Harness Engineering](./harness-engineering.md) provides a **diagnostic framework** for agent infrastructure — this provides the **portfolio evidence** that framework draws on
- [Orchestration Comparison](./orchestration-comparison.md) compares **which** orchestration approach to use — this shows measured outcomes across multiple projects

---

## The Portfolio: 7 Repositories as Evidence

All evidence comes from a single-developer portfolio of production repositories, providing controlled comparison of agent-driven development across different project types and maturity levels.

| Repository | Domain | Commits | Co-authored | Co-auth % | Infrastructure |
|-----------|--------|---------|-------------|-----------|----------------|
| third-brain | Knowledge management hub | 81 | 81 | 100% | Full (hooks, rules, scheduled tasks, cross-repo tracking) |
| mndr-review-automation | MNDR review pipeline | 87 | 83 | 95% | Full (PreToolUse security, specialized agents, 1,216 tests) |
| health-inventory | Sensor monitoring | 143 | 109 | 76% | Standard (hooks, rules, scheduled pipeline) |
| zeek-iceberg-demo | Data pipeline reference | 24 | 24+ | ~100% | Standard (hooks, commands, demo workflows) |
| network-visualization-services | PS service framework | 19 | 15 | 78% | Minimal+ (hooks, cross-repo permissions, engagement commands) |
| Splunk-db-connect-benchmark | Performance testing | 13 | 10 | 76% | Minimal+ (hooks, validation commands) |
| tme-mcp-server | MCP server infrastructure | 89 | 9 | 10% | None (no CLAUDE.md, no hooks, no rules) |

**Key observation**: tme-mcp-server's 10% co-authoring rate versus mndr-review-automation's 95% is not a model capability difference — both use the same Claude Code. The difference is entirely harness infrastructure. This directly validates the [Harness Engineering](./harness-engineering.md) thesis: "The model is not the bottleneck; the harness is."

**Session infrastructure prevalence**: SessionStart hooks appear in 5 of 7 repos, CLAUDE.md in 6 of 7, domain rules files in 3 of 7, and Stop hooks in 3 of 7 — adoption tracks the maturity levels below, not project age.

---

## Infrastructure Maturity Model

Not every project needs a full harness. The 7-repo portfolio reveals a natural progression with four distinct maturity levels, each appropriate for different project stages.

### Maturity Levels

#### Level 0: No Infrastructure

**Example**: tme-mcp-server (89 commits, 10% co-authored)

No CLAUDE.md, no hooks, no rules, no commands. Agent-driven development is possible but friction-heavy — the agent must rediscover project context every session and has no guardrails against convention violations.

**When this is appropriate**: Prototyping, exploratory work, projects where the human developer is the primary author and the agent assists occasionally.

#### Level 1: Minimal Infrastructure

**Example**: Splunk-db-connect-benchmark (13 commits, 76% co-authored)

CLAUDE.md (210 lines) + SessionStart hook + validation commands. The agent knows what the project is, gets context at session start, and has commands to verify its work (`/validate`, `/status`, `/benchmark`).

**Components**: CLAUDE.md, SessionStart hook, 1-4 custom commands

**When to advance**: When you find yourself correcting the agent for the same convention violations repeatedly — that's the signal to add rules files.

#### Level 2: Standard Infrastructure

**Example**: health-inventory (143 commits, 76% co-authored)

CLAUDE.md + SessionStart/Stop hooks + domain rules (4 files). The agent operates within documented conventions and checks for uncommitted work before ending sessions. Rules files encode domain knowledge: sensor inventory naming (`<type>_YYYY-MM.csv`), health score thresholds (CRITICAL <75, WARNING <85), collector inheritance patterns.

**Components**: CLAUDE.md, SessionStart + Stop hooks, 3-5 rules files

**When to advance**: When the project handles sensitive data, needs specialized agent roles, or coordinates across multiple repositories.

#### Level 3: Full Harness

**Example**: mndr-review-automation (87 commits, 95% co-authored)

CLAUDE.md (166 lines) + PreToolUse security hooks + domain rules + specialized agents + 1,216 tests. Security boundaries are enforced programmatically (not by instruction), specialized agents handle domain-specific review tasks, and comprehensive tests validate every pipeline stage.

**Components**: CLAUDE.md, PreToolUse hooks, rules, custom agents, comprehensive test suites, cross-repo integration

**Full harness infrastructure from mndr-review-automation**:

| Component | Implementation | Purpose |
|-----------|---------------|---------|
| CLAUDE.md (166 lines) | Security boundaries, architecture, key paths, test inventory | Agent context and constraints |
| PreToolUse hook (72 lines) | Blocks `data/staging/`, `token_map.json`, `.env`, raw CSVs, outbound network | Customer data isolation |
| Rules: data-isolation.md | Explicit BLOCKED/SAFE file lists | Readable security policy |
| Rules: tests.md | 1,216 tests, mock patterns, tokenization requirements | Test-driven constraints |
| Rules: lib-conventions.md | MLX in-process only, pure functions, no proxy libraries | Supply chain safety |
| Rules: config-templates.md | 126 query templates, LLM prompt conventions | Domain consistency |
| Agent: finding-reviewer | Sonnet model, Read/Bash/Grep/Glob tools, structured coaching output | Escalation review |
| 1,216 tests / 57 suites | Validators, scrubbers, tokenizers, clients, builders, analyzers | Behavioral verification |

### Maturity Progression is Not Linear

The co-authoring data reveals a counterintuitive pattern: **Level 2 (Standard) repos don't necessarily have higher co-authoring rates than Level 1 (Minimal)**. health-inventory (Level 2) is at 76% — the same as Splunk-db-connect-benchmark (Level 1). The jump happens at Level 3: mndr-review-automation reaches 95%.

**Diagnostic**: If your co-authoring rate plateaus despite adding hooks and rules, the bottleneck is likely missing validation infrastructure (tests, quality checks) rather than missing configuration. The agent can follow conventions but can't verify its own output without test suites.

---

## Cross-Repo Coordination Patterns

third-brain operates as a coordination hub tracking multiple spoke repositories. Its `cross-repo-progress.json` maintains real-time state:

```json
{
  "repos": {
    "third-brain": { "role": "hub", "recent_commits_14d": 22 },
    "mndr-review-automation": { "role": "spoke", "recent_commits_14d": 74 },
    "behavior-analytics": { "role": "spoke", "recent_commits_14d": 3 },
    "claude-code-project-best-practices": { "role": "spoke", "recent_commits_14d": 21 }
  },
  "summary": { "total_repos": 4, "total_recent_commits": 120 }
}
```

The hub session starts with awareness of all spoke activity: mndr-review-automation's 74 recent commits (high velocity) flag it for coordination priority, while behavior-analytics' 3 commits flag it for deprioritization.

third-brain also runs a scheduled cron task (`17 9 * * 1-5` — weekday mornings) that checks corelight-inspector for upstream changes affecting mndr-review-automation — tool signatures, log schemas, MCP transport protocol, version bumps — and summarizes impact on `lib/inspector_client.py`. Without it, upstream API changes would surface only when mndr-review-automation's tests break, potentially during a customer engagement.

network-visualization-services maintains a `settings.local.json` (354 lines) granting read access across 9 project repositories via regex patterns, letting a single agent session assess dependencies and coordinate across the portfolio without separate sessions per repo.

---

## Security Boundary Patterns

CLAUDE.md instructions alone achieve ~80% adherence ([Behavioral Insights](./behavioral-insights.md)); mndr-review-automation closes the gap with a 72-line PreToolUse hook enforcing data isolation programmatically.

| Layer | Mechanism | Coverage |
|-------|-----------|----------|
| **Instruction** | CLAUDE.md "Security Boundaries — READ THIS FIRST" section | ~80% (instruction adherence) |
| **Hook enforcement** | PreToolUse blocks Read, Bash, Glob, Grep for `data/staging/`, `token_map.json`, `.env`, raw CSVs, and outbound network | ~100% (programmatic) |
| **Data architecture** | Tokenized files in `data/assembled/`; raw data in `data/staging/` (never read) | Structural (can't leak what's already tokenized) |

The instruction and hook layers are deliberately redundant: the instruction tells the agent *why* the boundary exists, the hook enforces it regardless of adherence, and the data architecture makes the boundary irrelevant on the happy path since the tokenized files already contain everything the agent needs.

Cross-reference: [Safety & Sandboxing](./safety-and-sandboxing.md) for the full 4-layer security stack analysis.

---

## Quantified Development Velocity

### Commit Burst Patterns

Agent-driven development produces characteristic burst patterns — concentrated commits during focused sessions, followed by quiet periods.

| Repository | Peak Day | Commits | Context |
|-----------|----------|---------|---------|
| third-brain | 2026-04-04 | 24 | Program review + pipeline fixes + prioritized plan execution |
| mndr-review-automation | 2026-03-31 | 22 | Infrastructure sprint (concurrency, pipeline tiers, context tables) |
| mndr-review-automation | 2026-03-27 | 16 | Detection query library build (39 use cases) |
| health-inventory | 2026-03-10 | 25 | Initial setup burst (collectors, evaluators, pipeline) |

**What bursts indicate**: A commit burst is not "vibe coding" — it's concentrated execution once the approach is settled, not undirected work (see Corroborating External Evidence below for the practitioner framing of this same pattern at enterprise scale).

### Co-Authoring Ratios as Infrastructure Signal

The co-authoring ratio across the portfolio is not a measure of agent capability — it's a measure of infrastructure maturity.

| Co-auth Range | Repos | Infrastructure Pattern |
|--------------|-------|----------------------|
| 90-100% | third-brain, mndr-review-automation | Full harness with security, specialized agents, comprehensive tests |
| 75-80% | health-inventory, network-visualization-services, Splunk-db-connect-benchmark | Standard infrastructure with hooks and rules or commands |
| <15% | tme-mcp-server | No harness infrastructure |

**The 75-95% gap**: The jump from ~76% to 95% co-authoring corresponds to adding validation infrastructure (test suites, quality checks, specialized review agents). Without validation, agents plateau — they can write code but can't confirm it works, forcing human verification that breaks the agent-driven flow.

### Test-Driven Progression

mndr-review-automation's test growth correlates with co-authoring rate:

- Early phase: Basic pipeline tests → agent handles simple tasks
- Mid phase: 261 tests → agent handles complex generation
- Current: 1,216 tests across 57 suites → agent handles end-to-end pipeline including escalation coaching and iterative revision

**Evidence-based progression markers visible in commit history**: "261 unit tests", "99 tests", "118 tests" — test counts appear in commit messages as validation artifacts. This isn't accidental; the agent includes test counts because the rules file (`rules/tests.md`) establishes test coverage as a completeness criterion.

---

## Anti-Patterns

| Anti-Pattern | Source | Symptom | Fix |
|-------------|--------|---------|-----|
| Full harness from day one | tme-mcp-server → mndr-review-automation progression | Over-engineering delays first commit; harness becomes stale before project has shape | Start at Level 0-1; add infrastructure when you hit specific friction (repeated corrections → add rules; data sensitivity → add hooks) |
| No security boundaries with sensitive data | mndr-review-automation design decision | Customer data in agent context or commit history; compliance violation | PreToolUse hook enforcement + tokenized data architecture (instruction-only is ~80% reliable) |
| Single-repo thinking | Pre-hub-spoke pattern | Changes in one repo break another; context lost between sessions | Hub-spoke coordination with cross-repo-progress.json; scheduled dependency checks |
| Agent without validation phase | Lifecycle analysis | Agent declares "done" without verification; broken builds discovered later | Test suites as completeness criteria in rules files; validation commands (`/validate`, `/status`) |
| Over-constraining permissions | Comparison across repos | Agent blocked from routine operations; human approval fatigue | Pre-allow common operations in settings.json; restrict only what's genuinely dangerous |
| Reviewer that can edit | finding-reviewer design | Review agent "fixes" instead of coaches; downstream model never improves | Restrict reviewer to Read-only tools; structured coaching output format |

---

## Corroborating External Evidence

The portfolio patterns are independently validated by two high-credibility practitioners:

**Nick Schrock (Dagster)** — Merged 1,000+ PRs in 3 weeks with approximately 5 manual IDE edits. His review-loop workflow (local dev → cloud code review → one command → agent applies feedback → CI errors → agent fixes) mirrors the burst-and-validate pattern above at enterprise scale. Key quote: "This isn't vibe coding. The process is still software engineering forward." (Tier B: December 2025)

**Matthias Vallentin (Tenzir)** — 3x velocity improvement with agents handling commits, changelogs, docs, and releases. Framed as engineering organization transformation, not individual productivity. Same team whose production data showed 50% cost reduction through MCP architecture choices (see [MCP vs Skills Economics](./mcp-vs-skills-economics.md)). (Tier B: December 2025)

Both practitioners emphasize that velocity gains came from harness engineering (review loops, CI integration, permission management) — not from model improvements. This corroborates the portfolio evidence that infrastructure maturity, not model capability, determines agent-driven development effectiveness.

---

## Sources

### Tier A (Direct Production Observation)

- 7-repository portfolio analysis (April 2026) — Git history, infrastructure configuration, commit patterns, co-authoring ratios, and development velocity data from: third-brain, mndr-review-automation, health-inventory, zeek-iceberg-demo, network-visualization-services, Splunk-db-connect-benchmark, tme-mcp-server
- third-brain cross-repo-progress.json (April 2026) — Hub-spoke coordination state tracking 4 repositories with 120 recent commits
- mndr-review-automation PreToolUse hook (April 2026) — 72-line security enforcement script blocking customer data access
- mndr-review-automation finding-reviewer agent (April 2026) — Specialized Sonnet-model agent with restricted tools and structured coaching output

### Tier B (Validated / Expert Practitioner)

- Nick Schrock (Dagster founder): 1,000+ PRs in 3 weeks, review-loop development workflow (December 2025)
- Matthias Vallentin (Tenzir CEO): 3x velocity improvement, engineering organization transformation (December 2025)
- Boris Cherny (Claude Code creator): Parallel sessions, Five-Layer Architecture, 100% AI-authored code since November 2025 (March 2026)

### Related Analysis

- [Harness Engineering](./harness-engineering.md) — Infrastructure philosophy and diagnostic framework that this document operationalizes with portfolio evidence
- [Orchestration Comparison](./orchestration-comparison.md) — Comparison of orchestration approaches referenced in parallel agent strategies
- [Behavioral Insights](./behavioral-insights.md) — Context thresholds and ~80% CLAUDE.md adherence rate explaining why hooks are needed for security
- [Safety & Sandboxing](./safety-and-sandboxing.md) — 4-layer security stack analysis complementing the security boundary patterns here

---

*Last updated: April 2026*

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/harness-engineering.md`](analysis/harness-engineering.md) [EXTRACTED (1.00)] — references
- [`analysis/cross-project-synchronization.md`](analysis/cross-project-synchronization.md) [EXTRACTED (1.00) ×2] — references
- [`analysis/claude-md-progressive-disclosure.md`](analysis/claude-md-progressive-disclosure.md) [EXTRACTED (1.00)] — references
- [`analysis/secure-code-generation.md`](analysis/secure-code-generation.md) [INFERRED (0.85)] — semantically_similar_to

<!-- graphify-footer:end -->
