---
evidence-tier: Mixed
convergence: single-source
applies-to-signals: [harness-custom-agents, harness-background-tasks, harness-dynamic-workflows]
last-verified: 2026-07-10
revalidate-by: 2026-12-15
status: PRODUCTION
---

# Orchestration Approaches: Comparative Analysis

> **Collapsed 2026-07-10 (Reduction Phase 4).** The native-orchestration half is now first-party (workflows/`ultracode` v2.1.154, agent teams v2 v2.1.178, nested subagents v2.1.172, background-by-default v2.1.198 — see the official docs). Kept delta: the external-framework comparison (now including cross-model-family review), when-NOT-to-orchestrate, and the portfolio's measured evidence.

**Evidence Tier**: Mixed (A-B) — Vendor documentation + production-validated community patterns

## Purpose

This document provides an **evidence-based comparison** of agent orchestration approaches for Claude Code. Instead of documenting how each works (covered extensively in [everything-claude-code](https://github.com/anthropics-solutions/everything-claude-code)), this focuses on *when to choose which approach and why*.

---

## When Not to Orchestrate

Most work should start with the main agent and escalate only when needed — premature orchestration adds complexity without benefit (Boris Cherny, March 2026).

```
Single task, single session?
  -> NO orchestration needed. Use the main agent directly.

Task needs parallel research?
  -> Native subagents. Zero setup — see the official sub-agents docs.

Multi-session project with state continuity?
  -> GSD pattern (STATE.md externalization).

Agents need to talk to each other or coordinate on a shared task list?
  -> Agent teams — see the official agent-teams docs.

Building reusable multi-agent system?
  -> CAII cognitive agents or custom .claude/agents/.

60+ agents, enterprise scale?
  -> External tools (Claude-Flow, Auto-Claude).
```

Adoption note: the external frameworks compared below carry single-source adoption evidence (this doc's convergence tag), and the standing rule is that adopting any of them as fleet infrastructure requires converged status or an explicit owner exception — the native-first branches above are vendor-native and unaffected.

---

## External Framework Comparison

The patterns below are external to Claude Code and keep independent value now that the native mechanism half — subagents, agent teams, workflows — is documented first-party in the official docs. Quick mapping: multi-session continuity favors GSD (STATE.md survives session boundaries); a scalable agent architecture that doesn't grow with domain count favors CAII (fixed 7 agents regardless of scope); domain-deep specialization favors custom agents under `.claude/agents/` (dedicated prompts, tools, and model per role); complex research synthesis favors Self-Evolution's diversity sampling (multiple perspectives, iterative refinement).

### Approach Comparison Matrix

| Factor | GSD | CAII | Domain-Specific |
|--------|-----|------|-----------------|
| **Agent count** | ~5 workflow | 7 fixed cognitive | N (grows with scope) |
| **Context strategy** | Fresh per executor | On-the-fly injection | Specialized |
| **State management** | STATE.md + .planning/ | Task-specific memories | Varies |
| **Orchestration** | Human checkpoints | Deterministic state machine | Varies |
| **Setup cost** | Low (directory structure) | Medium (Python orchestration) | High |
| **Maintenance** | Low | Low (7 constant agents) | High (grows) |
| **Evidence tier** | B (community) | B (community) | C (varies) |

### GSD: Multi-Session State Continuity

**Source**: glittercowboy/get-shit-done (Tier B)

GSD's unique contribution is **state externalization** — all project state persists in files, not conversation memory.

**Core principles**:
1. Fresh context per executor (200K tokens purely for implementation)
2. Thin orchestrator (coordinates but doesn't execute)
3. State in STATE.md (survives context resets and session boundaries)
4. One task = one atomic commit

**When GSD adds value over native subagents**:
- Project spans multiple sessions
- Multiple people/agents contribute to same project
- Need audit trail of decisions (STATE.md history)
- Complex workflow with human checkpoints (discuss/verify phases)

**When GSD is overkill**:
- Single-session tasks
- Quick fixes
- Exploratory work (structure premature)

### CAII: Cognitive Function Architecture

**Source**: skribblez2718/caii (Tier B)

CAII's unique insight: organize agents by *how they think*, not *what they work on*. Seven fixed cognitive agents handle any domain:

| Agent | Cognitive Function | Maps To |
|-------|-------------------|---------|
| Clarification | Ambiguity → specs | Johari Window / SAAE protocol |
| Research | Knowledge gathering | Explore subagent |
| Analysis | Problem decomposition | Plan subagent |
| Synthesis | Finding integration | general-purpose subagent |
| Generation | Artifact creation (TDD) | general-purpose subagent |
| Validation | Quality verification | Explore subagent |
| Memory | Progress monitoring | Hooks + external files |

**When CAII adds value**:
- Building reusable agent systems across multiple domains
- Agent count growing uncontrollably with each new project type
- Need deterministic orchestration (Python state machine, not prompt-based)
- Want system that improves over time via memory capture

**When CAII is overkill**:
- Well-defined single tasks
- Time-critical work (multi-phase adds latency)
- Already have working domain agents

### CRISPY: Structured Phase Decomposition (RPI Evolution)

**Source**: Dexter Horthy / Human Layer (Tier B, Authority 4/5)

CRISPY is the evolution of Research-Plan-Implement (RPI). Where RPI used 3 phases with 85+ instruction mega-prompts, CRISPY splits into 7 phases with each phase under 40 instructions.

**The 7 Phases**:
1. **Questions** — Surface unknowns before committing to a direction
2. **Research** — Gather codebase context and domain knowledge
3. **Design** — Produce a 200-line design doc (the key alignment artifact)
4. **Structure** — Define component boundaries and interfaces
5. **Plan** — Generate implementation steps (vertical slices, not horizontal layers)
6. **Work** — Execute implementation
7. **Implement + PR** — Finalize and submit

**Key principles**:
- "Don't use prompts for control flow; use control flow for control flow" — each phase is a discrete step, not a section within a mega-prompt
- Design doc (200 lines) replaces plan review (1000 lines) as the human-agent alignment artifact
- Vertical planning enforced: models default to horizontal (all DB, then all services, then all API), which produces untestable 1200+ line plans; vertical slicing creates testable checkpoints

**Relationship to other patterns**:
- Replaces RPI's monolithic approach with discrete, manageable phases
- Compatible with any orchestration layer (native subagents, GSD, CAII)
- The design doc pattern is independently useful regardless of phase adoption

### Self-Evolution: Quality Through Diversity

**Source**: Google TTD-DR Paper + OptILLM (Tier B)

Not a full orchestration framework, but a pattern applicable within any framework. Spawns multiple candidates with different analytical approaches, then synthesizes the best elements.

| Step | What Happens | Token Cost |
|------|-------------|------------|
| Multi-candidate init | 3 parallel subagents (conservative/balanced/creative) | 3x |
| Refinement loop | Each candidate iterated 3x with judge feedback | ~9x |
| Crossover synthesis | Best elements merged | ~13x total |

**When worth the cost**:
- High-stakes decisions (architecture, security)
- Complex research synthesis
- When single-pass quality is insufficient
- Quality-critical output where 13x tokens is justified

**When not worth it**:
- Simple factual lookups
- Time-critical responses
- Token-constrained environments

### Cross-Model-Family Review (Errorta / Jon Wiggins)

**Source**: Jon Wiggins, Medium (~2026-07; reviewed 2026-07-10) + [errorta.app](https://errorta.app/) — Tier C, author-promotes-own-tool bias flagged; Errorta itself is a macOS-only alpha, not adoptable on this fleet (full entry: [SOURCES.md](../SOURCES.md)).

Wiggins' loop-engineering harness restates several practices already anchored elsewhere in this comparison — fresh context per role, deterministic verification, fail-closed checkpoints — but it adds one dimension the corpus didn't carry as a named practice: **cross-model-family review** — "shared weights share failure modes," so the reviewing checkpoint should run a different model family than the drafting one, on the reasoning that a reviewer built on the same weights as the writer inherits the writer's blind spots along with its competence. This fleet already practices it in both directions: Gemini Deep Research drafts are verified by Claude locally, and a 2026-06 D-audit found roughly 60% of a Gemini-drafted analysis's claims failed verification against primary sources — a cross-family check catching same-family blind spots, running the opposite direction from Wiggins' own example (Gemini drafts checked by Claude, not the reverse). The addition here is the name, not the mechanism: the practice was already running and already verified before the article gave it a label.

---

## Measured Orchestration Overhead

**Source**: Chase AI (Tier C, Authority 2/5)

Measured token and time costs for a **simple greenfield web app task** across three approaches:

| Approach | Tokens | Time | Notes |
|----------|--------|------|-------|
| GSD | 1.2M | 105 min | Full orchestrator + executor workflow |
| Superpowers | 250K | 60 min | Prompt-based orchestration layer |
| Vanilla Claude Code | 200K | 20 min | No orchestration framework |

**Heavy caveats**: This data covers one task type only — a simple greenfield web app. It does NOT test:
- Complex brownfield codebases (where context management matters most)
- Multi-session projects (where GSD's state persistence pays off)
- Team handoff scenarios (where STATE.md provides continuity)
- Tasks requiring parallel execution

The overhead numbers are real, but the scenarios where orchestration tools claim differentiation were not tested. Do not use this data to dismiss orchestration for complex work.

---

## Production Evidence (7-Repo Portfolio)

The orchestration-choice guidance here is corroborated by the 7-repo portfolio evidence aggregated in [`agent-driven-development.md`](agent-driven-development.md) and the cross-repo coordination patterns documented in [`cross-project-synchronization.md`](cross-project-synchronization.md). Notable signals:

- **Native subagents (Explore, Plan, general-purpose) handled the dominant share** of orchestration across all 7 portfolio repos; no repo adopted GSD, CAII, Claude-Flow, or RLM as a primary orchestrator. This supports the "Native is the default" recommendation.
- **Cross-session continuity** — the scenario where GSD's STATE.md and CAII's Memory agent claim differentiation — was solved in the portfolio via dedicated memory files + CLAUDE.md routing (see [`memory-systems-genealogy-baseline.md`](../archive/memory-systems-genealogy-baseline.md), archived 2026-07-10), not via orchestrator-managed state.
- **Agent Teams and Routines** (the two newer Anthropic-hosted patterns) had not yet been adopted in the portfolio as of the April 2026 audit; absence here is a coverage gap, not a verdict.

Limitation: this is single-practitioner direct-observation evidence (Tier A by observation type, not Tier A by statistical scale). Do not generalize to "no team has ever needed GSD" — only to "GSD's claimed differentiation was not load-bearing in this portfolio."

Two data points survive from the now-superseded native-mechanism sections for scale calibration: agent teams' own case study (16 parallel agents, ~2,000 sessions, a 100K-line C compiler compiling the Linux kernel, ~$20,000 API cost) and the advisor pattern's benchmark claims (2% higher multilingual SWE-bench, 11% lower cost vs. non-advisor baselines). Both Tier A by source, neither independently reproduced.

---

## Anti-Patterns Across All Approaches

| Anti-Pattern | Applies To | Instead |
|-------------|-----------|---------|
| Orchestrator does implementation | GSD, CAII | Orchestrator coordinates only |
| Accumulated context across tasks | All | Fresh context per executor |
| Parallel write operations | All | Only parallelize reads; sequence writes |
| Domain agent proliferation | Domain-specific | Use CAII cognitive functions or native subagents |
| Skipping state externalization | GSD | Always update STATE.md after significant actions |
| Over-delegation | All | Reserve orchestration for 30+ second tasks |

---

## Sources

**Tier A (Vendor)**:
- [Claude Code Sub-agents Documentation](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Agent Teams Documentation](https://code.claude.com/docs/en/agent-teams)
- [Building a C Compiler with Parallel Claudes](https://www.anthropic.com/engineering/building-a-c-compiler-with-parallel-claudes)
- Boris Cherny: premature-orchestration principle (March 2026)
- Anthropic: Advisor strategy benchmark claims (April 2026)

**Tier B (Validated)**:
- [glittercowboy/get-shit-done](https://github.com/glittercowboy/get-shit-done) — GSD orchestration
- [skribblez2718/caii](https://github.com/skribblez2718/caii) — CAII cognitive agents
- Google TTD-DR Paper — Self-Evolution Algorithm
- Dexter Horthy / Human Layer: CRISPY methodology, design doc pattern (Authority 4/5)

**Tier C (Low Confidence)**:
- Chase AI: Measured orchestration overhead benchmarks (Authority 2/5, single task type only)
- Jon Wiggins — Loop-engineering harness / Errorta (author-promotes-own-tool bias flagged; macOS-only alpha, not adoptable on this fleet; full entry in [SOURCES.md](../SOURCES.md))

## Related Analysis

- [Harness Engineering](./harness-engineering.md) — Orchestration is one layer of the broader harness stack; see the 6-layer model and diagnostic framework
- [Agent-Driven Development](./agent-driven-development.md) — Parallel agent strategies and specialized agent design (finding-reviewer case study) from production repos
- [Scheduled & Looping Primitives](./scheduled-and-looping-primitives.md) — the unattended/scheduled face: `/loop`, `/goal`, Routines, Desktop scheduled tasks, and the audit signals for each

---

*Last updated: 2026-07-10 (Reduction Phase 4 — native-mechanism half collapsed to the official docs; added the Errorta/Jon Wiggins cross-model-family-review paragraph; measured numbers and portfolio evidence preserved). Prior: 2026-06-15 (dynamic workflows; subagent 5-levels-deep recursion; `harness-dynamic-workflows`/`harness-background-tasks` signals). Prior: April 2026.*

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/harness-engineering.md`](analysis/harness-engineering.md) [EXTRACTED (1.00) ×2] — references
- [`analysis/agent-driven-development.md`](analysis/agent-driven-development.md) [EXTRACTED (1.00)] — references
- [`analysis/framework-selection-guide.md`](analysis/framework-selection-guide.md) [EXTRACTED (1.00) ×5] — references
- [`analysis/memory-systems-archetype-a-curated-kb.md`](analysis/memory-systems-archetype-a-curated-kb.md) [INFERRED (0.60)] — semantically_similar_to

<!-- graphify-footer:end -->
