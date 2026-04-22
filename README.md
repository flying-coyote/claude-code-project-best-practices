# Claude Code Best Practices: Evidence-Based Analysis

An **analytical layer** for Claude Code: evidence assessment, comparative analysis, quantified behavioral insights, and an adaptive routing audit that maps *your project's signals* to the specific guidance that applies.

## What This Project Uniquely Provides

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

If you can't verify a recommendation against the cited doc, the audit failed — that's the design.

> **Looking for implementation tooling instead?** See [everything-claude-code](https://github.com/affaan-m/everything-claude-code) (119K+ stars, comprehensive skill/agent library) or [superpowers](https://github.com/obra/superpowers) (disciplined methodology plugin). This project is the analytical layer that complements them — use alongside, not instead of.

---

## Quick Start: Adaptive Routing Audit (one copy-paste)

Copy-paste this into Claude Code in **any project**. It collects signals, fetches the [routing map](AUDIT-CONTEXT.md), and conditionally fetches 4–8 of the 28 analysis docs based on what it observes. One prompt; 6–10 network fetches; 1–5 minutes typical round-trip.

```
Audit this project against Claude Code best practices using the adaptive routing protocol.

STEP 1 — COLLECT SIGNALS (run in parallel where possible):
- Read CLAUDE.md: check ./CLAUDE.md and .claude/CLAUDE.md. Note line count. Grep for vague descriptors, unanchored triggers, and references:
  grep -nEi "\b(best practices|idiomatic|robust|proper|clean code)\b" CLAUDE.md .claude/CLAUDE.md 2>/dev/null
  grep -nEi "\b(where applicable|as needed|if relevant|consider edge cases)\b" CLAUDE.md .claude/CLAUDE.md 2>/dev/null
  grep -nE "see (rules/|\.claude/|[A-Z])" CLAUDE.md .claude/CLAUDE.md 2>/dev/null
- Commit patterns (90 days): git log --oneline --since="90 days ago" | head -50
  Files touched: git log --since="90 days ago" --name-only --format="" | sort | uniq -c | sort -rn | head -20
  If commit count < 10, retry with --since="365 days ago".
- Harness layout: ls -la .claude/ .claude/hooks/ .claude/rules/ .claude/skills/ .claude/agents/ .claude/commands/ 2>/dev/null
  cat .claude/settings.json 2>/dev/null | head -40
- Model version detection: grep -REi "opus-4-?[567]|sonnet-4-?[567]|claude-[0-9]" .claude/ .github/workflows/ 2>/dev/null
- Session diagnostics: npx -y claude-doctor 2>/dev/null || echo "claude-doctor not available"
- Project type: read README.md first 30 lines to classify.

STEP 2 — FETCH ROUTING MAP:
WebFetch https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/AUDIT-CONTEXT.md

STEP 3 — ROUTE TO APPLICABLE ADVISORIES:
For each Signal row in AUDIT-CONTEXT.md matching your observations, fetch the listed docs from https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/{path}. Include the three Always Fetch docs unconditionally. Apply the Anti-Bloat Rule (target 4–8 signal-triggered + 3 baseline = 7–11 total).

STEP 4 — PRODUCE AUDIT:
Use the structured output format in ONE-LINE-PROMPT.md. Every recommendation MUST cite signal key, source doc, and evidence-tier read from the doc's YAML frontmatter (not prose). Act on edit-thrashing and error-loop counts only; treat composite health percentage as directional. Prefer positive examples over MUST NOT rules (per the Anthropic Opus 4.7 migration guide).

Edge cases (no .claude/ directory, bare repo, claude-doctor unavailable, no model field in settings.json): see ONE-LINE-PROMPT.md "EDGE CASES" block — handle silently, do not fail the audit.
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
