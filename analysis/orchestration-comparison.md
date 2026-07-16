---
evidence-tier: Mixed
convergence: single-source
applies-to-signals: [harness-custom-agents, harness-background-tasks, harness-dynamic-workflows, project-type-framework-selection, harness-comprehensive]
last-verified: 2026-07-16
revalidate-by: 2026-12-15
status: PRODUCTION
---

# Orchestration Approaches: Comparative Analysis

> **Merged 2026-07-16 (Absorption Scan 2026-07 §1).** framework-selection-guide.md folded in here — one external-framework doc instead of two (~60% overlap). Selection function verified un-absorbed (superpowers is a compared object, not a comparator).

<!-- separate banner -->

> **Collapsed 2026-07-10 (Reduction Phase 4).** The native-orchestration half is now first-party (workflows/`ultracode` v2.1.154, agent teams v2 v2.1.178, nested subagents v2.1.172, background-by-default v2.1.198 — see the official docs). Kept delta: the external-framework comparison (now including cross-model-family review), when-NOT-to-orchestrate, and the portfolio's measured evidence.

**Evidence Tier**: Mixed (A-B) — Vendor documentation + production-validated community patterns

## Purpose

This document provides an **evidence-based comparison** of agent orchestration approaches for Claude Code. Instead of documenting how each works (covered extensively in [everything-claude-code](https://github.com/affaan-m/everything-claude-code)), this focuses on *when to choose which approach and why*.

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
- Sessions where output quality visibly degrades as context accumulates

Key artifacts: `STATE.md` (position, decisions, blockers), `.planning/` (research, plans, summaries), and XML task specs with embedded verification.

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

**Source**: Dexter Horthy / HumanLayer (Tier B, Authority 4/5; conference talk March 2026, validated across "thousands of engineers") — **upstream frozen: 12-factor-agents no activity since 2025-09, ACE since 2025-12; treat as historical reference (verified 2026-07-16)**

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
- Design doc (200 lines) replaces plan review (1000 lines) as the human-agent alignment artifact — Horthy calls it "brain surgery on the agent before you proceed downstream": align on a 200-line doc (target state, patterns, resolved decisions, open questions) instead of reviewing a 1000-line plan and then the code that diverges from it; this targets long plans only
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

## Framework Selection (merged 2026-07-16)

Folded in from `framework-selection-guide.md` (archived snapshot: [`archive/framework-selection-guide.md`](../archive/framework-selection-guide.md)): the selection-specific material the comparison sections above did not already carry — the five-framework selection table, the two frameworks without sections above (Claude-Flow, RLM), the universally useful patterns, the selection anti-patterns, and the selection summary. Convergence note carried over: this guidance is single-source, so adopting any of these frameworks as standing infrastructure requires converged adoption evidence or an explicit owner exception.

### Framework Selection Table

**Sources per row** (full citations in [SOURCES.md](../SOURCES.md)):

| Framework | Agent Model | Context Strategy | State Management | Evidence | Primary source |
|-----------|-------------|------------------|------------------|----------|---|
| **GSD** | ~5 workflow agents | Fresh per subagent | STATE.md + .planning/ | Tier B | glittercowboy/get-shit-done |
| **CAII** | 7 cognitive agents | On-the-fly injection | Task-specific memories | Tier B | skribblez2718/caii |
| **CRISPY** | Single agent, 7 phases | Phase-scoped | Design doc + vertical plans | Tier B | Dexter Horthy conference talk, March 2026 (upstream frozen — see the CRISPY section flag; verified 2026-07-16) |
| **Claude-Flow** | 60+ specialized | Vector retrieval | ReasoningBank | Tier B (docs only) | ruvnet/claude-flow (enterprise-focused docs) |
| **RLM** | Model-managed | REPL variable + recursive | Sub-call outputs | Tier B (emerging) | Zhang/Kraska/Khattab (arXiv:2512.24601) |

GSD, CAII, and CRISPY are compared in depth in the sections above; the two rows without sections above follow.

### Claude-Flow (Reference Only)

Claude-Flow is reference-only — almost never implement directly. 60+ agents is extreme complexity, the 250% extension claim is unverified, vector memory and swarm topologies assume infrastructure most projects lack, and there's no production validation data. Reference it for enterprise-scale design ideas, advanced orchestration patterns, and swarm topology options. Documentation: [SOURCES.md](../SOURCES.md) (no dedicated pattern file — intentionally).

### RLM — Recursive Language Models (Emerging)

RLM is emerging: monitor for future adoption, apply its principles now through prompting, treat it as unvalidated for Claude. Innovation: the model manages context through REPL variable access — peek, grep, partition, and recurse into sub-calls instead of a single pass over the full context (context rot). Offered as a theoretical explanation for why GSD's fresh-context approach works; the paper reports CodeQA accuracy improving 24% → 62%. Limitations: needs RL training unavailable for Claude, published results use GPT-5/GPT-5-mini only, REPL adds implementation complexity. Short of full RLM, the technique still transfers: recursive exploration prompts, explicit context partitioning, programmatic filtering. Documentation: [Recursive Context Management](./behavioral-insights.md).

### Universally Useful Patterns

Some patterns extracted from these frameworks work with ANY orchestration:

| Pattern | Origin | Universal Value |
|---------|--------|-----------------|
| [Johari Window](./behavioral-insights.md) | CAII | Surface unknowns before implementation |
| STATE.md | GSD | Cross-session memory (even without full GSD) |
| Design Doc (CRISPY section above) | CRISPY (upstream frozen, verified 2026-07-16) | 200-line alignment artifact before plan generation |
| Vertical Planning (CRISPY section above) | CRISPY (upstream frozen, verified 2026-07-16) | Testable slices vs. untestable horizontal layers |
| Atomic Commits | GSD | One task = one commit (good practice anyway) |

### Selection Anti-Patterns

- **Mixing frameworks without architecture**: combining CAII's 7 agents inside GSD's workflow phases fails — the two carry incompatible assumptions (CAII deterministic, GSD stateless executors) and no hybrid pattern is validated. Borrow specific patterns (Johari Window, STATE.md) rather than running one framework's agents as another's executors.
- **Implementing Claude-Flow directly**: 60 specialized agents assumes 100+ simultaneous users and a vendor-reported $500K+/year compute cost; reference the principles and implement CAII's 7 agents instead.
- **Choosing based on novelty**: RLM requires RL training unavailable for Claude and all published results are GPT-5/GPT-5-mini; use RLM-inspired prompting now, adopt directly once it's Claude-validated.

### Selection Summary

1. **GSD for session continuity** — STATE.md when projects span sessions.
2. **CAII for agent architecture** — building reusable agent systems.
3. **CRISPY for complex planning** — design doc alignment, vertical slicing (RPI successor). (Upstream frozen — 12-factor-agents no activity since 2025-09, ACE since 2025-12; treat as historical reference, verified 2026-07-16.)
4. **Claude-Flow for reference only** — enterprise patterns, don't implement directly.
5. **RLM is emerging** — monitor for adoption; apply the principles now through prompting.

**When in doubt**: start with Claude Code's native mechanisms (official features overview, "Match features to your goal"). Reach for an external framework only once you hit specific friction — multi-session continuity, reusable agent architecture, or 1000+ line plans.

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
- **Cross-session continuity** — the scenario where GSD's STATE.md and CAII's Memory agent claim differentiation — was solved in the portfolio via dedicated memory files + CLAUDE.md routing (see [`memory-systems-genealogy-baseline.md`](../archive/memory-systems-genealogy-baseline.md), archived 2026-07-10), not via orchestrator-managed state. The need appeared most clearly in the genealogy portfolio's 3-project subset, where memory-system patterns — not orchestrator state — carried the load.
- **CRISPY-style phase decomposition** maps to the agent-driven workflow lifecycle phases observed in the portfolio (planning → research → implementation → verification); the portfolio evidence is consistent with the "split mega-prompts into <40-instruction phases" prescription. (CRISPY upstream frozen — see the CRISPY section flag; verified 2026-07-16.)
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
- [glittercowboy/get-shit-done](https://github.com/glittercowboy/get-shit-done) — GSD orchestration. STATE.md for cross-session memory, fresh context per executor, .planning/ directory structure. README advises "overkill for simple tasks."
- [skribblez2718/caii](https://github.com/skribblez2718/caii) — CAII cognitive agents
- Google TTD-DR Paper — Self-Evolution Algorithm
- Dexter Horthy / HumanLayer: CRISPY methodology, design doc pattern, vertical planning, "don't use prompts for control flow" principle (Authority 4/5; conference talk March 2026, validated across "thousands of engineers"). Upstream frozen — 12-factor-agents no activity since 2025-09, ACE since 2025-12; treat as historical reference (verified 2026-07-16).
- [ruvnet/claude-flow](https://github.com/ruvnet/claude-flow) — 60+ specialized agents, vector memory, swarm topologies, ReasoningBank. Enterprise-focused docs only; no production validation data referenced.
- Zhang / Kraska / Khattab: [arXiv:2512.24601](https://arxiv.org/abs/2512.24601) — Recursive Language Models. CodeQA accuracy 24% → 62% improvement. Status: emerging; all published results use GPT-5/GPT-5-mini, not Claude.

**Tier C (Low Confidence)**:
- Chase AI: Measured orchestration overhead benchmarks (Authority 2/5, single task type only)
- Jon Wiggins — Loop-engineering harness / Errorta (author-promotes-own-tool bias flagged; macOS-only alpha, not adoptable on this fleet; full entry in [SOURCES.md](../SOURCES.md))
- Claude-Flow cost estimate: $500K+/year compute. **Vendor-reported — not independently benchmarked.**

## Related Analysis

- [Harness Engineering](./harness-engineering.md) — Orchestration is one layer of the broader harness stack; see the 6-layer model and diagnostic framework
- [Agent-Driven Development](./agent-driven-development.md) — Parallel agent strategies and specialized agent design (finding-reviewer case study) from production repos
- [Scheduled & Looping Primitives](./scheduled-and-looping-primitives.md) — the unattended/scheduled face: `/loop`, `/goal`, Routines, Desktop scheduled tasks, and the audit signals for each
- [Behavioral Insights](./behavioral-insights.md) — Context strategies (recursive context management, Johari Window) applicable with any framework
- [Spec-Driven Development](../archive/patterns-v1/spec-driven-development.md) — The foundational methodology underlying all of these (v1 archive)

---

*Last updated: 2026-07-16 (Absorption Scan 2026-07 §1 — framework-selection-guide.md merged in: five-framework selection table, Claude-Flow and RLM sections, universally useful patterns, selection anti-patterns and summary; CRISPY/Horthy content flagged upstream-frozen; ECC URL corrected to affaan-m). Prior: 2026-07-10 (Reduction Phase 4 — native-mechanism half collapsed to the official docs; added the Errorta/Jon Wiggins cross-model-family-review paragraph; measured numbers and portfolio evidence preserved). Prior: 2026-06-15 (dynamic workflows; subagent 5-levels-deep recursion; `harness-dynamic-workflows`/`harness-background-tasks` signals). Prior: April 2026.*

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/harness-engineering.md`](analysis/harness-engineering.md) [EXTRACTED (1.00) ×2] — references
- [`analysis/agent-driven-development.md`](analysis/agent-driven-development.md) [EXTRACTED (1.00)] — references
- [`analysis/memory-systems-archetype-a-curated-kb.md`](analysis/memory-systems-archetype-a-curated-kb.md) [INFERRED (0.60)] — semantically_similar_to

<!-- graphify-footer:end -->
