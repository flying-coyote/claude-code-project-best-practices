---
convergence: single-source
---

# Claude Code Best Practices: Evidence-Based Analysis

**A portable, evidence-based audit you can run against any Claude Code project to get recommendations specific to *that project* — not generic best-practice advice.**

## The Problem This Solves

Claude Code best-practice content is scattered across vendor docs, interviews, blogs, and community repos. Two problems follow:

1. **Trust** — a recommendation from the Claude Code creator and a recommendation from a random blog post both read as "best practice." You cannot tell which to act on without doing the triage yourself.
2. **Applicability** — advice that is load-bearing for an agent-heavy data pipeline is noise for a static site generator. Generic best-practice lists waste attention; project-specific recommendations do not.

This project solves both by pairing an **evidence-tier system** (every source labelled A–D — so authority is visible, not asserted) with an **adaptive routing audit**: one copy-paste prompt that inspects *your* repo and conditionally fetches only the 4–8 of 24 routable analysis docs that match what it found. Every recommendation cites signal + source + tier, so you can verify or ignore it.

The audit runs in two passes that complement each other. The first is the **INSPECT** pass — the presence/absence and count checks that ask what a project *has* (does a `CLAUDE.md` exist, is `.mcp.json` present, which model version is pinned), and it routes those signals to the matching docs. That pass is good at telling you which conventions you are missing and weak at telling you whether the conventions you already have are the right ones, because a presence check passes the moment a mechanism exists regardless of whether it still serves its purpose. The second pass — **RETHINK** — is the intent-alignment layer that closes that gap: for each central mechanism the project already has, it asks what the mechanism is *for* and checks the mechanism against that stated intent, so the audit catches intent-mechanism drift, the case where what a project has (a glob still pointing at a moved directory, an ARCHITECTURE.md frozen at an outgrown doc count, a write-scoped permission nobody decided to keep) has come apart from why it has it. This repo's own self-audit surfaced exactly this drift in itself, which is why the RETHINK pass is first-class rather than an afterthought; the routing and per-mechanism intent checks live in [`AUDIT-CONTEXT.md`](AUDIT-CONTEXT.md) and [`analysis/intent-alignment-audit.md`](analysis/intent-alignment-audit.md).

Convergence status: the drift/staleness detection this audit performs is **single-source** practice — we found no independent external adoption that survived verification — so under this repo's convergence rule, adopting it as standing infrastructure requires converged status or an explicit owner exception.

## What You Get

| Capability | Why It Matters | Where Else? |
|-----------|---------------|-------------|
| **Adaptive routing audit** (signal → 4–8 docs of 27) | Your project's context determines which advice you get | No packaged equivalent found; the instrument is ours |
| **Intent-alignment pass** (RETHINK: each mechanism vs its stated *why*) | Catches intent-mechanism drift the presence checks miss — a stale glob, an outgrown doc count, an unintended permission | Inspired by Daniel Miessler's diagnosis; the instrument is ours |
| **Evidence tier system** (A–D source tiers; the 1–5 claim-strength axis is RETIRED as of 2026-07-12) | Know which advice to trust | Adapted from evidence-based-medicine tier systems; the application here is ours |
| **Quantified behavioral insights** (80% CLAUDE.md adherence, 60% context threshold) | Calibrate expectations from data, not vibes | Scattered across interviews |
| **Comparative analysis** (orchestration/framework selection, CLI-vs-MCP measurements) | Make informed architectural decisions | The sources exist separately; the comparative synthesis is ours |
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

- **Practitioners with a specific repo**: run the one-prompt audit; get 4–8 cited recommendations scoped to your project rather than 24 docs to read.
- **Evaluators weighing claims from any AI tooling source**: the evidence-tier system (A–D source quality) applies to any claim, not just claims in this repo.
- **Teams standardizing practice across multiple Claude Code projects**: the audit output is structured and comparable — diff two repos' audits to surface drift.

## Where This Sits

The ecosystem now has seven distinguishable lanes, and this project deliberately occupies only the last one — pruning itself into the other six as they mature. The per-doc ledger of who covers what, the retained delta, and the trigger that hands each slice off is [ABSORPTION-MAP.md](ABSORPTION-MAP.md).

| Lane | Occupant(s) | Our relationship |
|---|---|---|
| First-party baseline | [Claude Code docs](https://code.claude.com/docs), [anthropics/skills](https://github.com/anthropics/skills), [official plugin marketplace](https://github.com/anthropics/claude-plugins-official) | Every doc here is a delta against this baseline (Decision 11); when a slice goes native, the doc collapses or retires |
| Tooling / reference config | [ECC](https://github.com/affaan-m/everything-claude-code) (renamed from everything-claude-code — pin the `affaan-m` owner, unrelated same-name repos exist), [claude-code-templates](https://github.com/davila7/claude-code-templates), [wshobson/agents](https://github.com/wshobson/agents) | Use alongside; batteries-included implementations, not evidence-graded analysis |
| Methodology | [superpowers](https://github.com/obra/superpowers) | Use alongside; independently implements patterns equivalent to our archived v1 skills (re-verified at v6.1.1, 2026-07-16) |
| Mechanics documentation | [ClaudeLog](https://claudelog.com) | Follow for how-it-works explainers; we keep the measured numbers it doesn't publish |
| Standards | [AGENTS.md](https://agents.md) (Linux Foundation), [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/), [CoSAI Project CodeGuard](https://project-codeguard.org) | Map to and adopt where they cover the substance — CodeGuard's own Claude Code integration absorbed two of our three rule-import options (2026-07-16) |
| Thought-leader canons | Willison, Osmani, Ronacher, Ng, Karpathy, Miessler | Follow-and-track (the `follows:` frontmatter lane): blog-form canons carry the conceptual load for a slice, but never clear the Supported bar for infrastructure adoption |
| Evidence-graded audit | **this repo** | Sole occupant; temporary by charter — shrinking coverage is success |

**Not implementation how-to.** If a recommendation says "add a PreToolUse hook," this project explains *why and when*; it does not paste the hook code. Pair this project with the lanes above — use alongside, not instead of.

---

## Quick Start: Adaptive Routing Audit (one copy-paste)

Copy-paste this into Claude Code in **any project**. It collects signals, fetches the [routing map](AUDIT-CONTEXT.md), and conditionally fetches 4–8 of the 24 routable analysis docs based on what it observes. One prompt; 6–10 network fetches; 1–5 minutes typical round-trip.

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
| Evaluating a claim from any AI tooling source | [`analysis/evidence-tiers.md`](analysis/evidence-tiers.md) | The A–D source-tier system applies broadly (the 1–5 claim-strength axis is RETIRED; A–D is the only tier system) |
| Choosing a tool or framework | [`analysis/orchestration-comparison.md`](analysis/orchestration-comparison.md) | Native-mechanism selection is first-party now; the Framework Selection section (merged 2026-07-16) keeps the external-framework comparison |
| Contributing an analysis doc | [`CONTRIBUTING.md`](CONTRIBUTING.md) → Integration Checklist | Start from [`analysis/CANONICAL-DOC-TEMPLATE.md`](analysis/CANONICAL-DOC-TEMPLATE.md) |

---

## Core Analysis (25 files)

*The `analysis/` directory contains 25 `.md` files: 24 routable analysis docs plus `CANONICAL-DOC-TEMPLATE.md`, a non-routable template excluded from the count (post the 2026-07-16 absorption wave: one retirement in progress, two merges).*

| Document | What It Covers |
|----------|---------------|
| [evidence-tiers.md](analysis/evidence-tiers.md) | A–D source-tier classification + HIGH/MEDIUM/LOW confidence framework (merged 2026-07-16; the 1–5 claim-strength axis is retired) |
| [intent-alignment-audit.md](analysis/intent-alignment-audit.md) | The RETHINK layer: nine why-questions a presence/absence audit can't ask (EMERGING) |
| [behavioral-insights.md](analysis/behavioral-insights.md) | Quantified Claude Code behavior: context thresholds, instruction adherence, prompt sensitivity across model versions |
| [model-migration-anti-patterns.md](analysis/model-migration-anti-patterns.md) | Six prompt anti-patterns that break on Opus 4.7; cross-version diagnostic matrix |
| [harness-engineering.md](analysis/harness-engineering.md) | Harness philosophy, diagnostic framework, infrastructure patterns |
| [scheduled-and-looping-primitives.md](analysis/scheduled-and-looping-primitives.md) | Unattended execution: `/loop`, `/goal`, Routines, Desktop scheduled tasks, the Ralph lineage, and the "loop engineering" framing (EMERGING) |
| [claude-md-progressive-disclosure.md](analysis/claude-md-progressive-disclosure.md) | 3-tier CLAUDE.md evolution across 6 repos, ~150 instruction budget |
| [agent-driven-development.md](analysis/agent-driven-development.md) | Agent-driven methodology with 7-repo quantified evidence |
| [agent-evaluation.md](analysis/agent-evaluation.md) | Eval methodology from Anthropic engineering |
| [orchestration-comparison.md](analysis/orchestration-comparison.md) | When to use native subagents vs GSD vs CAII vs agent teams + framework-selection decision table (merged 2026-07-16) |
| [mcp-patterns.md](analysis/mcp-patterns.md) | The single MCP doc: OWASP security mapping + 4-plugin/2-MCP sweet-spot evidence (absorbed mcp-daily-essentials 2026-07-10) |
| [mcp-vs-skills-economics.md](analysis/mcp-vs-skills-economics.md) | RETIRING toward first-party `/usage` — historical Tenzir A/B record + the controlled-comparison instrument |
| [plugins-and-extensions.md](analysis/plugins-and-extensions.md) | Skills vs MCP vs Hooks vs Commands decision framework |
| [safety-and-sandboxing.md](analysis/safety-and-sandboxing.md) | 4-layer security stack, auto mode analysis, sandbox architecture |
| [secure-code-generation.md](analysis/secure-code-generation.md) | OWASP-aware code generation patterns |
| [domain-knowledge-architecture.md](analysis/domain-knowledge-architecture.md) | Domain knowledge encoding for LLM-assisted development |
| [memory-system-patterns.md](analysis/memory-system-patterns.md) | Auto-memory sizing by project type, 4 memory types, staleness patterns |
| [memory-systems-archetype-recommendations.md](analysis/memory-systems-archetype-recommendations.md) | Consolidated recommendations across 7 memory-system archetypes (code monorepo, second brain, egress-constrained, cross-project portfolio, work-state tracker, session archive, team-shared memory as in-doc sections; curated KB in its own file) + cross-cutting migration/never-combine/license tables |
| [memory-systems-recommendation-methodology.md](analysis/memory-systems-recommendation-methodology.md) | Methodology + self-critique behind the archetype recommendations: scale thresholds (200/500/6k), 8 challengeable assumptions, evidence discipline |
| [memory-systems-archetype-a-curated-kb.md](analysis/memory-systems-archetype-a-curated-kb.md) | Archetype A — curated analytical knowledge bases (Karpathy LLM Wiki paradigm, graphify+footer, Lum1104 alternative) |
| [memory-systems-graphify-vs-understand-anything.md](analysis/memory-systems-graphify-vs-understand-anything.md) | A/B comparison of two LLM-driven graph-builders + ~25% EXTRACTED-edge hallucination spot-check finding |
| [evidence-based-revalidation.md](analysis/evidence-based-revalidation.md) | Hypothesis confidence tracking, revalidation before demos |
| [automated-config-assessment.md](analysis/automated-config-assessment.md) | Baseline-deviation-remediation pattern + Hoosier 12/12 ground-truth measurement |
| [cross-project-synchronization.md](analysis/cross-project-synchronization.md) | Cross-repo dependency cascading, 4-phase enrichment cascade |

### Meta and Source Files

| Document | Purpose |
|----------|---------|
| [AUDIT-CONTEXT.md](AUDIT-CONTEXT.md) | Signal → advisory routing map (the audit's core mechanism) |
| [ONE-LINE-PROMPT.md](ONE-LINE-PROMPT.md) | Full prompt + output format + edge cases |
| [SOURCES.md](SOURCES.md) | Comprehensive source database with evidence tiers |
| [SOURCES-QUICK-REFERENCE.md](SOURCES-QUICK-REFERENCE.md) | Top 30 authority-weighted sources |
| [ABSORPTION-MAP.md](ABSORPTION-MAP.md) | Per-doc external-absorber ledger: who covers what, lane, retained delta, advance trigger (derived; frontmatter is canonical) |
| [analysis/CANONICAL-DOC-TEMPLATE.md](analysis/CANONICAL-DOC-TEMPLATE.md) | Template for new analysis docs; canonical frontmatter schema |
| [DECISIONS.md](DECISIONS.md) | Architecture decision records |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution guide + integration checklist |
| [PLAN.md](PLAN.md) | Current priorities and recent activity |

---

## Key Findings (Selected)

- **CLAUDE.md is followed ~80% of the time** — use hooks for 100% enforcement (Boris Cherny, March 2026).
- **Context quality degrades at 60% capacity, not when full** — proactive intervention saves quality.
- **Opus 4.7 interprets prompts literally** — 4.6-tuned prompts with vague descriptors, edge-case gestures, or unanchored triggers may silently no-op ([Anthropic migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide), April 2026).
- **Skills were 50% cheaper than equivalent MCP in Tenzir's pre-tool-search A/B** (January 2026, historical) — the live per-category cost signal is first-party `/usage` now; the durable point is the controlled same-workflow comparison an observational monitor can't produce.
- **Auto mode approves 93% of tool calls** — viable for most workflows (Anthropic, March 2026).
- **Custom subagents can "gatekeep context"** — prefer native delegation unless truly specialized (Boris Cherny).
- **Agent-driven repos achieve 95–100% co-authoring** with full harness infrastructure (7-repo portfolio).
- **PreToolUse hooks enforce ~100% vs ~80% for CLAUDE.md alone** — hooks are the security boundary, not instructions.
- **Federated query saves 86–99% vs centralized** — zeek-iceberg-demo: 0.19s vs 27.52s for equivalent queries.
- **CLAUDE.md follows 3-tier progressive disclosure** — 42–57 lines (minimal) → 99–112 (resource map) → 166–209 (rules + security) across 6 repos.
- **"Loop engineering" is the orchestration face of harness engineering, not a new paradigm** — Boris Cherny's "I write loops" (WorkOS, June 2026) productized as `/loop`/`/goal`/Routines; per the 2026-07-12 re-attribution (SOURCES.md), Osmani named the five-component anatomy and presents the framing as his own, quoting Steinberger for one line — do not credit a single coiner. Delegation is still narrow — developers fully delegate only 0–20% of tasks (Anthropic 2026 Agentic Coding Trends Report).

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
| **Simon Willison** | "Designing agentic loops" canon (followed by harness-engineering.md); per-release model analyses |
| **Addy Osmani** | Loop engineering, Agentic Autonomy Levels, own-the-outer-loop (followed canons) |
| **Armin Ronacher** | Inner agent loop vs outer harness loop; the most critical voice on autonomous-loop limits |
| **Nate B. Jones** | Agent principles, Specification Gap, OB1 memory architecture |
| **ECC** (renamed from everything-claude-code) | Comprehensive tooling reference — the tooling lane |
| **superpowers** | Disciplined methodology, anti-rationalization — the methodology lane (re-verified v6.1.1) |
| **ClaudeLog** | Community mechanics documentation — the how-it-works lane (followed by behavioral-insights.md) |

Full database: [SOURCES.md](SOURCES.md).

---

## Project Status

**v2.1** — 24 routable analysis docs (44→27 in the 2026-07-10 Reduction Phases 0-6; 27→25 files in the 2026-07-16 absorption wave — first third-party sweep, five docs entered the follow lane, one retirement toward `/usage`, two merges; see ABSORPTION-MAP.md) with production evidence from a 7-repo portfolio, covering agent-driven development, security data pipelines, federated query architecture, cross-project synchronization, session quality diagnostics, Opus 4.8 migration readiness (with a volatile Fable 5 / Mythos 5 currency note), unattended-execution primitives (`/loop`, `/goal`, Routines, scheduled tasks) plus the "loop engineering" framing, and 7 memory-system archetypes (curated KB through team-shared memory) with empirical Pass-2 testbed findings on this repo (graphify vs understand-anything A/B + ~25% EXTRACTED-edge hallucination spot-check).

**Archive**: Prior v1 patterns (24 docs) live in `archive/patterns-v1/` — preserved for historical comparison, not active guidance. See [ARCHIVE.md](ARCHIVE.md).

---

## Contributing

Contributions welcome, especially: evidence-based analysis of new claims, quantified behavioral observations, comparative evaluations, and source verification.

**Adding a new analysis doc?** Follow the Integration Checklist in [CONTRIBUTING.md](CONTRIBUTING.md) — updates are coordinated across `SOURCES.md`, `AUDIT-CONTEXT.md` (routing), `README.md` (this file's table), and `INDEX.md`. Start from the [`CANONICAL-DOC-TEMPLATE.md`](analysis/CANONICAL-DOC-TEMPLATE.md).

## License

MIT License — use freely, attribution appreciated.
