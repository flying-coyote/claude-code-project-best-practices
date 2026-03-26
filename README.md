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

### Core Analysis (14 documents)

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

### Source Database

| Document | Purpose |
|----------|---------|
| [SOURCES.md](SOURCES.md) | Comprehensive source database with evidence tiers |
| [SOURCES-QUICK-REFERENCE.md](SOURCES-QUICK-REFERENCE.md) | Top 20 sources at a glance |

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

## Thought Leaders & Sources

### Tier A (Primary/Vendor)

| Source | Key Contribution |
|--------|-----------------|
| **Boris Cherny** (Claude Code Creator) | Quantified behavioral insights, five-layer architecture |
| **Anthropic Engineering Blog** | Auto mode, agent skills, hooks reference, eval methodology |
| **OWASP MCP Top 10** | MCP security framework |

### Tier B (Validated Practitioners)

| Source | Key Contribution |
|--------|-----------------|
| **Nate B. Jones** | Agent principles, Specification Gap, OB1 memory architecture |
| **IndyDevDan** | Trust-based engineering, hooks mastery, agent-scoped patterns |
| **everything-claude-code** | Comprehensive tooling reference (110K stars) |
| **superpowers** | Disciplined methodology, anti-rationalization |

Full database: [SOURCES.md](SOURCES.md)

## Project Status

**v2.0** — Repositioned from 36-pattern best practices guide to focused analytical layer. Prior patterns archived in `archive/patterns-v1/`.

## Contributing

Contributions welcome, especially:
- Evidence-based analysis of new claims
- Quantified behavioral observations
- Comparative evaluations of tools and approaches
- Source verification and revalidation

## License

MIT License - Use freely, attribution appreciated.
