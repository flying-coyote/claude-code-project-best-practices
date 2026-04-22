# Claude Code Best Practices: Evidence-Based Analysis

An **analytical layer** for Claude Code — evidence assessment, comparative analysis, and quantified behavioral insights that comprehensive tooling repos don't provide.

**Philosophy**: We don't duplicate implementation guides. We evaluate claims, compare approaches, and surface the behavioral insights that make the difference between naive and expert usage.

> **Looking for implementation guides?** See [everything-claude-code](https://github.com/anthropics-solutions/everything-claude-code) (110K+ stars, 125+ skills, 28+ agents) for batteries-included tooling, or [superpowers](https://github.com/obraun-cl/superpowers) for disciplined methodology with anti-rationalization patterns.

## What This Project Uniquely Provides

| Capability | Why It Matters | Where Else? |
|-----------|---------------|-------------|
| **Evidence tier system** (A-D source + 1-5 claim strength) | Know which advice to trust | Nowhere |
| **Quantified behavioral insights** (80% CLAUDE.md adherence, 60% context threshold, etc.) | Calibrate expectations from data, not vibes | Scattered across interviews |
| **Comparative analysis** (MCP vs Skills economics, orchestration approaches) | Make informed architectural decisions | Nowhere as analysis |
| **Security analysis** (OWASP MCP Top 10, auto mode classifier, sandbox architecture) | Understand real security boundaries | OWASP (raw), not Claude-specific |
| **Tool ecosystem evaluation** (Claude Code vs Aider vs Cursor vs Codex) | Choose the right tool for the task | Marketing pages only |

## Analysis Documents

### Core Analysis (28 documents)

| Document | What It Covers |
|----------|---------------|
| [evidence-tiers.md](analysis/evidence-tiers.md) | Dual-tier classification system for evaluating claims |
| [behavioral-insights.md](analysis/behavioral-insights.md) | Quantified Claude Code behavior: context thresholds, instruction adherence, thinking trade-offs |
| [orchestration-comparison.md](analysis/orchestration-comparison.md) | When to use native subagents vs GSD vs CAII vs agent teams |
| [mcp-vs-skills-economics.md](analysis/mcp-vs-skills-economics.md) | Cost/performance analysis: Skills 50% cheaper than MCP |
| [mcp-patterns.md](analysis/mcp-patterns.md) | 7 failure modes + OWASP security mapping |
| [mcp-daily-essentials.md](analysis/mcp-daily-essentials.md) | Optimal plugin/MCP configuration (4 plugins + 2 MCPs) |
| [plugins-and-extensions.md](analysis/plugins-and-extensions.md) | Skills vs MCP vs Hooks vs Commands decision framework |
| [safety-and-sandboxing.md](analysis/safety-and-sandboxing.md) | 4-layer security stack, auto mode analysis, sandbox architecture |
| [secure-code-generation.md](analysis/secure-code-generation.md) | OWASP-aware code generation patterns |
| [tool-ecosystem.md](analysis/tool-ecosystem.md) | Claude Code vs alternatives + Specification Gap framework |
| [framework-selection-guide.md](analysis/framework-selection-guide.md) | Orchestration framework decision matrix |
| [agent-evaluation.md](analysis/agent-evaluation.md) | Eval methodology from Anthropic engineering |
| [agent-principles.md](analysis/agent-principles.md) | 6 production reliability principles |
| [confidence-scoring.md](analysis/confidence-scoring.md) | HIGH/MEDIUM/LOW assessment framework |
| [harness-engineering.md](analysis/harness-engineering.md) | Harness philosophy, diagnostic framework, infrastructure patterns |
| [domain-knowledge-architecture.md](analysis/domain-knowledge-architecture.md) | Domain knowledge encoding for LLM-assisted development |
| [agent-driven-development.md](analysis/agent-driven-development.md) | Agent-driven methodology with 7-repo quantified evidence |
| [local-cloud-llm-orchestration.md](analysis/local-cloud-llm-orchestration.md) | Hybrid MLX+Claude architecture, tokenization boundary, hallucination scrubbing |
| [mcp-client-integration.md](analysis/mcp-client-integration.md) | Two MCP server architectures compared (structured tools vs orchestrated playbooks) |
| [federated-query-architecture.md](analysis/federated-query-architecture.md) | 15/15 benchmark queries, 86-99% cost savings, TCO calculator |
| [automated-config-assessment.md](analysis/automated-config-assessment.md) | Baseline-deviation-remediation pattern, 3,816+ sensors, 100% detection |
| [claude-md-progressive-disclosure.md](analysis/claude-md-progressive-disclosure.md) | 3-tier CLAUDE.md evolution across 6 repos, ~150 instruction budget |
| [memory-system-patterns.md](analysis/memory-system-patterns.md) | Auto-memory sizing by project type, 4 memory types, staleness patterns |
| [evidence-based-revalidation.md](analysis/evidence-based-revalidation.md) | Hypothesis confidence tracking, revalidation before demos |
| [security-data-pipeline.md](analysis/security-data-pipeline.md) | Zeek → OCSF → Parquet → Iceberg pipeline, 30K records/sec |
| [cross-project-synchronization.md](analysis/cross-project-synchronization.md) | Cross-repo dependency cascading, 4-phase enrichment cascade |
| [session-quality-tools.md](analysis/session-quality-tools.md) | claude-doctor signal reliability, score interpretation, evidence-filtered CLAUDE.md rules |
| [model-migration-anti-patterns.md](analysis/model-migration-anti-patterns.md) | Six prompt anti-patterns that break on Opus 4.7; cross-version diagnostic matrix |

### Source Database

| Document | Purpose |
|----------|---------|
| [SOURCES.md](SOURCES.md) | Comprehensive source database with evidence tiers |
| [SOURCES-QUICK-REFERENCE.md](SOURCES-QUICK-REFERENCE.md) | Top 20 sources at a glance |

## Quick Start: One-Prompt Project Review

Copy-paste this into Claude Code in **any project**. The prompt collects signals from your repo, fetches a routing map ([AUDIT-CONTEXT.md](AUDIT-CONTEXT.md)), and selectively fetches only the analysis docs that apply to what it actually observed — typically 4–8 of the 28. Every recommendation cites the source doc and evidence tier.

```
Audit this project against Claude Code best practices.

STEP 1 — COLLECT SIGNALS (in parallel where possible):
- Read CLAUDE.md (check ./CLAUDE.md and .claude/CLAUDE.md; note line count and whether it references other files).
- Run: git log --oneline --since="90 days ago" | head -50
- Run: git log --since="90 days ago" --name-only --format="" | sort | uniq -c | sort -rn | head -20
- Inspect harness: ls -la .claude/ .claude/rules/ .claude/hooks/ .claude/skills/ .claude/agents/ .claude/commands/ .claude/settings.json 2>/dev/null
- Check model version in use: grep -r "opus\|sonnet\|haiku\|claude-" .claude/settings.json 2>/dev/null; also note model from recent CI config, agent frontmatter, or MCP settings.
- Run session diagnostics: npx -y claude-doctor 2>/dev/null || echo "claude-doctor not available"
- Note project type (docs, data pipeline, library, multi-repo, research, etc.) from README/structure.

STEP 2 — FETCH ROUTING MAP:
Fetch https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/AUDIT-CONTEXT.md

STEP 3 — ROUTE TO APPLICABLE ADVISORIES:
For each Signal row in AUDIT-CONTEXT.md that matches what you observed, fetch the listed analysis doc(s) from https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/{path}. Also fetch the "Always Fetch" docs. Do not fetch docs whose signal you did not observe.

STEP 4 — PRODUCE AUDIT:
Use the structured output format in ONE-LINE-PROMPT.md. Every recommendation must cite the analysis doc it came from and that doc's evidence tier. For claude-doctor output, act on edit-thrashing and error-loop counts; treat composite health percentage as directional only. Prefer positive examples over MUST NOT rules (per the Anthropic Opus 4.7 migration guide).
```

See [ONE-LINE-PROMPT.md](ONE-LINE-PROMPT.md) for the full output format, customization flags, and rationale for the routing design.

## How to Use This Repo

**For practitioners**: Browse `analysis/` for evidence-based guidance on specific decisions. Each document includes source attribution and evidence tier ratings.

**For evaluators**: Use [evidence-tiers.md](analysis/evidence-tiers.md) to assess claims from any source. The dual-tier system (source quality A-D + claim strength 1-5) works for any AI tooling claim.

**For tool selection**: Start with [tool-ecosystem.md](analysis/tool-ecosystem.md) for high-level comparison, then dive into specific analysis documents for detailed trade-offs.

## Key Findings

Highlights from our analysis (see individual documents for full evidence):

- **CLAUDE.md is followed ~80% of the time** — use hooks for 100% enforcement (Boris Cherny, March 2026)
- **Context quality degrades at 60%, not when full** — proactive intervention saves quality (Boris Cherny)
- **Skills are 50% cheaper than equivalent MCP** — but MCP offers better isolation (Tenzir)
- **Auto mode approves 93% of tool calls** — viable for most workflows (Anthropic, March 2026)
- **Custom subagents can "gatekeep context"** — prefer native delegation unless truly specialized (Boris Cherny)
- **Extended thinking often reduces total time** — fewer steering corrections outweigh 2-3x latency (Boris Cherny)
- **Agent-driven repos achieve 95-100% co-authoring** — with full harness infrastructure (7-repo portfolio analysis)
- **PreToolUse hooks enforce ~100% vs ~80% for CLAUDE.md alone** — hooks are the security boundary, not instructions (production observation)
- **Federated query saves 86-99% vs Splunk** — ClickHouse 0.19s vs Splunk 27.52s for equivalent queries (zeek-iceberg-demo)
- **CLAUDE.md follows 3-tier progressive disclosure** — 42-57 lines (minimal) → 99-112 (resource map) → 166-209 (rules+security) across 6 repos

## Thought Leaders & Sources

### Tier A (Primary/Vendor)

| Source | Key Contribution |
|--------|-----------------|
| **Boris Cherny** (Claude Code Creator) | Quantified behavioral insights, five-layer architecture |
| **Anthropic Engineering Blog** | Auto mode, agent skills, hooks reference, eval methodology |
| **OWASP MCP Top 10** | MCP security framework |
| **7-Repo Portfolio Analysis** | Agent-driven development evidence, infrastructure maturity, cross-repo coordination |

### Tier B (Validated Practitioners)

| Source | Key Contribution |
|--------|-----------------|
| **Nate B. Jones** | Agent principles, Specification Gap, OB1 memory architecture |
| **IndyDevDan** | Trust-based engineering, hooks mastery, agent-scoped patterns |
| **everything-claude-code** | Comprehensive tooling reference (110K stars) |
| **superpowers** | Disciplined methodology, anti-rationalization |

Full database: [SOURCES.md](SOURCES.md)

## Project Status

**v2.1** — 28 analysis documents. Production evidence integrated from 7-repo portfolio. Covers agent-driven development, security data pipelines, federated query architecture, cross-project synchronization, session quality diagnostics, and more. Prior v1 patterns archived in `archive/patterns-v1/`.

## Contributing

Contributions welcome, especially:
- Evidence-based analysis of new claims
- Quantified behavioral observations
- Comparative evaluations of tools and approaches
- Source verification and revalidation

## License

MIT License - Use freely, attribution appreciated.
