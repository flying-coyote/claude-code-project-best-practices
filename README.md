# Claude Code Best Practices: Evidence-Based Analysis

**A portable, evidence-based audit you can run against any Claude Code project to get recommendations specific to *that project* — not generic best-practice advice.**

## The Problem This Solves

Claude Code best-practice content is scattered across vendor docs, interviews, blogs, and community repos. Two problems follow:

1. **Trust** — a recommendation from the Claude Code creator and a recommendation from a random blog post both read as "best practice." You cannot tell which to act on without doing the triage yourself.
2. **Applicability** — advice that is load-bearing for an agent-heavy data pipeline is noise for a static site generator. Generic best-practice lists waste attention; project-specific recommendations do not.

This project solves both by pairing an **evidence-tier system** (every source and claim labelled A/B/C — so authority is visible, not asserted) with an **adaptive routing audit**: one copy-paste prompt that inspects *your* repo and conditionally fetches only the 4–8 of 28 analysis docs that match what it found. Every recommendation cites signal + source + tier, so you can verify or ignore it.

## What You Get

| Capability | Why It Matters | Where Else? |
|-----------|---------------|-------------|
| **Adaptive routing audit** (signal → 4–8 docs of 28) | Your project's context determines which advice you get | Nowhere |
| **Evidence tier system** (A–D source + 1–5 claim strength) | Know which advice to trust | Nowhere |
| **Quantified behavioral insights** (80% CLAUDE.md adherence, 60% context threshold) | Calibrate expectations from data, not vibes | Scattered across interviews |
| **Comparative analysis** (MCP vs Skills economics, orchestration approaches) | Make informed architectural decisions | Nowhere as analysis |
| **Model-migration diagnostics** (Opus 4.6 → 4.7 silent no-op risks) | Catch prompts that break on the version you ship | Not systematically |
| **Security analysis** (OWASP MCP Top 10, auto mode classifier, sandboxing) | Understand real security boundaries | OWASP (raw), not Claude-specific |

### Concrete Example: What an Audit Recommendation Looks Like

Every recommendation from the audit cites its source doc, evidence tier, and the project signal that triggered the match:

```markdown
**Migrate implicit subagent dispatch in `.claude/agents/builder.md:14`**
- Signal: `model-version-4-7` (settings.json references `claude-opus-4-7`)
- Source: `analysis/model-migration-anti-patterns.md` (evidence-tier: Mixed)
- Action: Replace "Dispatch the work to available subagents" with
  "Use the Explore subagent to scan src/, then the Plan subagent to design the change."
```

If you cannot verify a recommendation against the cited doc, the audit failed — that is the design.

## Who It Is For

- **Practitioners with a specific repo**: run the one-prompt audit; get 4–8 cited recommendations scoped to your project rather than 28 docs to read.
- **Evaluators weighing claims from any AI tooling source**: the evidence-tier system (A–D source quality + 1–5 claim strength) applies to any claim, not just claims in this repo.
- **Teams standardizing practice across multiple Claude Code projects**: the audit output is structured and comparable — diff two repos' audits to surface drift.

## What It Is *Not*

- **Not a tooling library.** See [everything-claude-code](https://github.com/affaan-m/everything-claude-code) (119K+ stars, 125+ skills, 28+ agents) for batteries-included tooling.
- **Not a methodology framework.** See [superpowers](https://github.com/obra/superpowers) for disciplined workflow patterns (TDD enforcement, systematic debugging).
- **Not implementation how-to.** If a recommendation says "add a PreToolUse hook," this project explains *why and when*; it does not paste the hook code. Pair this project with the two above — use alongside, not instead of.

---

## Quick Start: Adaptive Routing Audit (one copy-paste)

Copy-paste this into Claude Code in **any project**. It collects signals, fetches the [routing map](AUDIT-CONTEXT.md), and conditionally fetches 4–8 of the 28 analysis docs based on what it observes. One prompt; 6–10 network fetches; 1–5 minutes typical round-trip.

```
Audit this project with the adaptive routing protocol at
https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/AUDIT-CONTEXT.md

1. WebFetch AUDIT-CONTEXT.md. Run every command in its "Signal Collection Commands" section.
2. For each Signal row whose condition your output matches, queue the listed docs. Add the three "Always Fetch" docs unconditionally. Apply the Anti-Bloat Rule (drop to ≤8 signal-triggered fetches).
3. WebFetch each queued doc from https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/{path}.
4. Produce the audit using the output format in ONE-LINE-PROMPT.md. Every recommendation must cite signal key, source doc, and evidence-tier (read from YAML frontmatter, not prose). Edge cases (no .claude/, bare repo, missing claude-doctor, no model field): handle silently per ONE-LINE-PROMPT.md "EDGE CASES" block.
```

See [ONE-LINE-PROMPT.md](ONE-LINE-PROMPT.md) for the full output format, worked-example recommendation, edge-case handling, and customization flags.

---

## How to Use This Repo

| You are... | Start with... | Then... |
|---|---|---|
| An external practitioner with a specific project | The Quick Start audit above | Follow the 4–8 cited docs the audit returns |
| Evaluating a claim from any AI tooling source | [`analysis/evidence-tiers.md`](analysis/evidence-tiers.md) | The dual-tier system (A–D source + 1–5 claim strength) applies broadly |
| Choosing a tool or framework | [`analysis/tool-ecosystem.md`](analysis/tool-ecosystem.md) + [`analysis/framework-selection-guide.md`](analysis/framework-selection-guide.md) | Narrow via the specific decision doc |
| Contributing an analysis doc | [`CONTRIBUTING.md`](CONTRIBUTING.md) → Integration Checklist | Start from [`analysis/CANONICAL-DOC-TEMPLATE.md`](analysis/CANONICAL-DOC-TEMPLATE.md) |

---

## Core Analysis (28 documents)

| Document | What It Covers |
|----------|---------------|
| [evidence-tiers.md](analysis/evidence-tiers.md) | Dual-tier classification system for evaluating claims |
| [behavioral-insights.md](analysis/behavioral-insights.md) | Quantified Claude Code behavior: context thresholds, instruction adherence, prompt sensitivity across model versions |
| [model-migration-anti-patterns.md](analysis/model-migration-anti-patterns.md) | Six prompt anti-patterns that break on Opus 4.7; cross-version diagnostic matrix |
| [harness-engineering.md](analysis/harness-engineering.md) | Harness philosophy, diagnostic framework, infrastructure patterns |
| [claude-md-progressive-disclosure.md](analysis/claude-md-progressive-disclosure.md) | 3-tier CLAUDE.md evolution across 6 repos, ~150 instruction budget |
| [agent-driven-development.md](analysis/agent-driven-development.md) | Agent-driven methodology with 7-repo quantified evidence |
| [agent-principles.md](analysis/agent-principles.md) | 6 production reliability principles |
| [agent-evaluation.md](analysis/agent-evaluation.md) | Eval methodology from Anthropic engineering |
| [orchestration-comparison.md](analysis/orchestration-comparison.md) | When to use native subagents vs GSD vs CAII vs agent teams |
| [framework-selection-guide.md](analysis/framework-selection-guide.md) | Orchestration framework decision matrix |
| [mcp-patterns.md](analysis/mcp-patterns.md) | 7 failure modes + OWASP security mapping |
| [mcp-vs-skills-economics.md](analysis/mcp-vs-skills-economics.md) | Cost/performance analysis: Skills 50% cheaper than MCP |
| [mcp-daily-essentials.md](analysis/mcp-daily-essentials.md) | Optimal plugin/MCP configuration (4 plugins + 2 MCPs) |
| [mcp-client-integration.md](analysis/mcp-client-integration.md) | Two MCP server architectures compared |
| [plugins-and-extensions.md](analysis/plugins-and-extensions.md) | Skills vs MCP vs Hooks vs Commands decision framework |
| [safety-and-sandboxing.md](analysis/safety-and-sandboxing.md) | 4-layer security stack, auto mode analysis, sandbox architecture |
| [secure-code-generation.md](analysis/secure-code-generation.md) | OWASP-aware code generation patterns |
| [tool-ecosystem.md](analysis/tool-ecosystem.md) | Claude Code vs alternatives + Specification Gap framework |
| [domain-knowledge-architecture.md](analysis/domain-knowledge-architecture.md) | Domain knowledge encoding for LLM-assisted development |
| [memory-system-patterns.md](analysis/memory-system-patterns.md) | Auto-memory sizing by project type, 4 memory types, staleness patterns |
| [session-quality-tools.md](analysis/session-quality-tools.md) | claude-doctor signal reliability, score interpretation, gap statements |
| [confidence-scoring.md](analysis/confidence-scoring.md) | HIGH/MEDIUM/LOW assessment framework |
| [evidence-based-revalidation.md](analysis/evidence-based-revalidation.md) | Hypothesis confidence tracking, revalidation before demos |
| [local-cloud-llm-orchestration.md](analysis/local-cloud-llm-orchestration.md) | Hybrid MLX+Claude architecture, tokenization boundary, hallucination scrubbing |
| [federated-query-architecture.md](analysis/federated-query-architecture.md) | 15/15 benchmark queries, 86–99% cost savings, TCO calculator |
| [automated-config-assessment.md](analysis/automated-config-assessment.md) | Baseline-deviation-remediation pattern, 3,816+ sensors, 100% detection |
| [security-data-pipeline.md](analysis/security-data-pipeline.md) | Zeek → OCSF → Parquet → Iceberg pipeline, 30K records/sec |
| [cross-project-synchronization.md](analysis/cross-project-synchronization.md) | Cross-repo dependency cascading, 4-phase enrichment cascade |

### Meta and Source Files

| Document | Purpose |
|----------|---------|
| [AUDIT-CONTEXT.md](AUDIT-CONTEXT.md) | Signal → advisory routing map (the audit's core mechanism) |
| [ONE-LINE-PROMPT.md](ONE-LINE-PROMPT.md) | Full prompt + output format + edge cases |
| [SOURCES.md](SOURCES.md) | Comprehensive source database with evidence tiers |
| [SOURCES-QUICK-REFERENCE.md](SOURCES-QUICK-REFERENCE.md) | Top 29 authority-weighted sources |
| [analysis/CANONICAL-DOC-TEMPLATE.md](analysis/CANONICAL-DOC-TEMPLATE.md) | Template for new analysis docs; canonical frontmatter schema |
| [DECISIONS.md](DECISIONS.md) | Architecture decision records |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution guide + integration checklist |
| [PLAN.md](PLAN.md) | Current priorities and recent activity |

---

## Key Findings (Selected)

- **CLAUDE.md is followed ~80% of the time** — use hooks for 100% enforcement (Boris Cherny, March 2026).
- **Context quality degrades at 60% capacity, not when full** — proactive intervention saves quality.
- **Opus 4.7 interprets prompts literally** — 4.6-tuned prompts with vague descriptors, edge-case gestures, or unanchored triggers may silently no-op ([Anthropic migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide), April 2026).
- **Skills are 50% cheaper than equivalent MCP** — but MCP offers better isolation (Tenzir).
- **Auto mode approves 93% of tool calls** — viable for most workflows (Anthropic, March 2026).
- **Custom subagents can "gatekeep context"** — prefer native delegation unless truly specialized (Boris Cherny).
- **Agent-driven repos achieve 95–100% co-authoring** with full harness infrastructure (7-repo portfolio).
- **PreToolUse hooks enforce ~100% vs ~80% for CLAUDE.md alone** — hooks are the security boundary, not instructions.
- **Federated query saves 86–99% vs centralized** — zeek-iceberg-demo: 0.19s vs 27.52s for equivalent queries.
- **CLAUDE.md follows 3-tier progressive disclosure** — 42–57 lines (minimal) → 99–112 (resource map) → 166–209 (rules + security) across 6 repos.

---

## Thought Leaders & Sources

### Tier A (Primary/Vendor)

| Source | Key Contribution |
|--------|-----------------|
| **Boris Cherny** (Claude Code creator) | Quantified behavioral insights, five-layer architecture |
| **Anthropic Engineering Blog** | Auto mode, agent skills, hooks reference, eval methodology, Opus 4.7 migration guide |
| **OWASP MCP Top 10** | MCP security framework |
| **7-Repo Portfolio Analysis** | Agent-driven development evidence, infrastructure maturity, cross-repo coordination |

### Tier B (Validated Practitioners)

| Source | Key Contribution |
|--------|-----------------|
| **Nate B. Jones** | Agent principles, Specification Gap, OB1 memory architecture |
| **IndyDevDan** | Trust-based engineering, hooks mastery, agent-scoped patterns |
| **Simon Willison** | Opus 4.7 system-prompt analysis (selective-literalism counter-signal) |
| **everything-claude-code** | Comprehensive tooling reference (119K stars) |
| **superpowers** | Disciplined methodology, anti-rationalization |

Full database: [SOURCES.md](SOURCES.md).

---

## Project Status

**v2.1** — 28 analysis documents with production evidence from a 7-repo portfolio, covering agent-driven development, security data pipelines, federated query architecture, cross-project synchronization, session quality diagnostics, and Opus 4.7 migration readiness.

**Archive**: Prior v1 patterns (24 docs) live in `archive/patterns-v1/` — preserved for historical comparison, not active guidance. See [ARCHIVE.md](ARCHIVE.md).

---

## Contributing

Contributions welcome, especially: evidence-based analysis of new claims, quantified behavioral observations, comparative evaluations, and source verification.

**Adding a new analysis doc?** Follow the Integration Checklist in [CONTRIBUTING.md](CONTRIBUTING.md) — updates are coordinated across `SOURCES.md`, `AUDIT-CONTEXT.md` (routing), `README.md` (this file's table), and `INDEX.md`. Start from the [`CANONICAL-DOC-TEMPLATE.md`](analysis/CANONICAL-DOC-TEMPLATE.md).

## License

MIT License — use freely, attribution appreciated.
