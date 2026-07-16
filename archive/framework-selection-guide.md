---
version-requirements:
  claude-code: "v2.0.0+"
version-last-verified: "2026-02-27"
status: ARCHIVED
last-verified: "2026-07-10"
notes: "Comparative guide - native subagents handle ~80% of use cases"
evidence-tier: B
convergence: single-source
applies-to-signals: [project-type-framework-selection, harness-comprehensive]
revalidate-by: 2026-10-22
---

# Framework Selection Guide

> **MERGED INTO orchestration-comparison.md (2026-07-16, Absorption wave Phase 3).** One external-framework doc instead of two; unique content preserved there. This copy is the pre-merge snapshot, kept for history.

<!-- separate banner -->

> **Collapsed 2026-07-10 (Reduction Phase 4).** Native-mechanism selection is now a first-party decision table (official features overview, "Match features to your goal"). Kept delta: the external-framework comparison.

**Purpose**: Compare external orchestration frameworks (GSD, CAII, CRISPY, Claude-Flow, RLM) for projects that outgrow native subagents. **Evidence Tier**: B (synthesized from validated patterns and production implementations). Convergence status for this guidance is single-source, so adopting any of these frameworks as standing infrastructure requires converged adoption evidence or an explicit owner exception.

---

## Framework Comparison

**Sources per row** (full citations in [SOURCES.md](../SOURCES.md)):

| Framework | Agent Model | Context Strategy | State Management | Evidence | Primary source |
|-----------|-------------|------------------|------------------|----------|---|
| **GSD** | ~5 workflow agents | Fresh per subagent | STATE.md + .planning/ | Tier B | glittercowboy/get-shit-done |
| **CAII** | 7 cognitive agents | On-the-fly injection | Task-specific memories | Tier B | skribblez2718/caii |
| **CRISPY** | Single agent, 7 phases | Phase-scoped | Design doc + vertical plans | Tier B | Dexter Horthy conference talk (March 2026) |
| **Claude-Flow** | 60+ specialized | Vector retrieval | ReasoningBank | Tier B (docs only) | ruvnet/claude-flow (enterprise-focused docs) |
| **RLM** | Model-managed | REPL variable + recursive | Sub-call outputs | Tier B (emerging) | Zhang/Kraska/Khattab (arXiv:2512.24601) |

---

## Detailed Guidance

### GSD Orchestration

GSD suits complex, multi-session projects needing continuity. Key innovation: each executor gets a fresh 200K context instead of accumulating context across a session, while `STATE.md` carries continuity forward. Best for multi-day features, team handoffs, complex dependencies, and sessions where quality visibly degrades. Key artifacts: `STATE.md` (position, decisions, blockers), `.planning/` (research, plans, summaries), XML task specs with embedded verification. Documentation: [GSD Orchestration](../analysis/orchestration-comparison.md).

### CAII Cognitive Agents

CAII suits teams building scalable, maintainable agent architectures: 7 fixed agents by cognitive function — Clarification, Research, Analysis, Synthesis, Generation (TDD), Validation, Memory — keep agent count constant instead of growing with scope. Best for reusable agent systems, deterministic orchestration, and long-term systems that need to improve over time. The [Johari Window](../analysis/behavioral-insights.md) methodology, borrowed from CAII, is valuable with any framework. Documentation: [Cognitive Agent Infrastructure](../analysis/orchestration-comparison.md).

### Claude-Flow (Reference Only)

Claude-Flow is reference-only — almost never implement directly. 60+ agents is extreme complexity, the 250% extension claim is unverified, vector memory and swarm topologies assume infrastructure most projects lack, and there's no production validation data. Reference it for enterprise-scale design ideas, advanced orchestration patterns, and swarm topology options. Documentation: SOURCES.md (no dedicated pattern file — intentionally).

### RLM — Recursive Language Models (Emerging)

RLM is emerging: monitor for future adoption, apply its principles now through prompting, treat it as unvalidated for Claude. Innovation: the model manages context through REPL variable access — peek, grep, partition, and recurse into sub-calls instead of a single pass over the full context (context rot). Offered as a theoretical explanation for why GSD's fresh-context approach works; the paper reports CodeQA accuracy improving 24% → 62%. Limitations: needs RL training unavailable for Claude, published results use GPT-5/GPT-5-mini only, REPL adds implementation complexity. Short of full RLM, the technique still transfers: recursive exploration prompts, explicit context partitioning, programmatic filtering. Documentation: [Recursive Context Management](../analysis/behavioral-insights.md).

### CRISPY: Structured Phase Decomposition (RPI Successor)

CRISPY (the RPI successor) suits complex implementation tasks where mega-prompts produce poor plans. Status: production-validated. Source: Dexter Horthy / Human Layer (Authority 4/5), confirmed across "thousands of engineers." It splits RPI's 3 monolithic phases (85+ instructions, hard to debug) into 7 phases of under 40 instructions each with discrete control flow — "don't use prompts for control flow; use control flow for control flow." The 7 phases: Questions, Research, Design (200-line design doc), Structure, Plan (vertical slices), Work, Implement + PR. Best for features where a single planning pass produces 1000+ line plans and plan-to-implementation divergence wastes review effort.

The design doc is the central alignment artifact — Horthy calls it "brain surgery on the agent before you proceed downstream": align on a 200-line doc (target state, patterns, resolved decisions, open questions) instead of reviewing a 1000-line plan and then the code that diverges from it; this targets long plans only. CRISPY also replaces horizontal planning (all schema, then all service layer, then all API endpoints — untestable until everything is done) with vertical slicing: one complete feature slice (DB + service + API + test) at a time, independently verifiable. Documentation: [Orchestration Comparison — CRISPY](../analysis/orchestration-comparison.md).

---

## Universally Useful Patterns

Some patterns extracted from these frameworks work with ANY orchestration:

| Pattern | Origin | Universal Value |
|---------|--------|-----------------|
| [Johari Window](../analysis/behavioral-insights.md) | CAII | Surface unknowns before implementation |
| STATE.md | GSD | Cross-session memory (even without full GSD) |
| [Design Doc](../analysis/orchestration-comparison.md) | CRISPY | 200-line alignment artifact before plan generation |
| [Vertical Planning](../analysis/orchestration-comparison.md) | CRISPY | Testable slices vs. untestable horizontal layers |
| Atomic Commits | GSD | One task = one commit (good practice anyway) |

---

## Anti-Patterns

- **Mixing frameworks without architecture**: combining CAII's 7 agents inside GSD's workflow phases fails — the two carry incompatible assumptions (CAII deterministic, GSD stateless executors) and no hybrid pattern is validated. Borrow specific patterns (Johari Window, STATE.md) rather than running one framework's agents as another's executors.
- **Implementing Claude-Flow directly**: 60 specialized agents assumes 100+ simultaneous users and a vendor-reported $500K+/year compute cost; reference the principles and implement CAII's 7 agents instead.
- **Choosing based on novelty**: RLM requires RL training unavailable for Claude and all published results are GPT-5/GPT-5-mini; use RLM-inspired prompting now, adopt directly once it's Claude-validated.

---

## Production Evidence

This guidance is corroborated by the 7-repo portfolio evidence in [`agent-driven-development.md`](../analysis/agent-driven-development.md) and [`cross-project-synchronization.md`](../analysis/cross-project-synchronization.md). Notable signals:

- **Multi-session continuity needs** (the GSD differentiator) appeared in the genealogy portfolio's 3-project subset, where memory-system patterns ([`memory-systems-genealogy-baseline.md`](memory-systems-genealogy-baseline.md), archived 2026-07-10) — not orchestrator state — carried the load.
- **CRISPY-style phase decomposition** maps to the agent-driven workflow lifecycle phases observed in the portfolio (planning → research → implementation → verification); the portfolio evidence is consistent with the "split mega-prompts into <40-instruction phases" prescription.

Limitation: portfolio is one practitioner; treat these as Tier A direct-observation evidence at single-practitioner scale, not statistical validation.

---

## Sources

### Tier B

- [glittercowboy/get-shit-done](https://github.com/glittercowboy/get-shit-done) — GSD framework. STATE.md for cross-session memory, fresh context per executor, .planning/ directory structure. README advises "overkill for simple tasks."
- [skribblez2718/caii](https://github.com/skribblez2718/caii) — Cognitive Agent Infrastructure. 7 fixed agents by cognitive function (Clarification, Research, Analysis, Synthesis, Generation, Validation, Memory); deterministic orchestration.
- Dexter Horthy / Human Layer — CRISPY framework conference talk, March 2026. Authority 4/5, validated across "thousands of engineers." Source for the 7-phase decomposition, design doc pattern, vertical planning, and the "don't use prompts for control flow" principle.
- [ruvnet/claude-flow](https://github.com/ruvnet/claude-flow) — 60+ specialized agents, vector memory, swarm topologies, ReasoningBank. Enterprise-focused docs only; no production validation data referenced.
- Zhang / Kraska / Khattab: [arXiv:2512.24601](https://arxiv.org/abs/2512.24601) — Recursive Language Models. CodeQA accuracy 24% → 62% improvement. Status: emerging; all published results use GPT-5/GPT-5-mini, not Claude.

### Tier C

- Claude-Flow cost estimate: $500K+/year compute. **Vendor-reported — not independently benchmarked.**

---

## Related Patterns

- [Spec-Driven Development](patterns-v1/spec-driven-development.md) - The foundational methodology (always use)
- [Context Engineering](../analysis/behavioral-insights.md) - Context strategies for all frameworks

---

## Summary

1. **GSD for session continuity** — STATE.md when projects span sessions.
2. **CAII for agent architecture** — building reusable agent systems.
3. **CRISPY for complex planning** — design doc alignment, vertical slicing (RPI successor).
4. **Claude-Flow for reference only** — enterprise patterns, don't implement directly.
5. **RLM is emerging** — monitor for adoption; apply the principles now through prompting.

**When in doubt**: start with Claude Code's native mechanisms (official features overview, "Match features to your goal"). Reach for an external framework only once you hit specific friction — multi-session continuity, reusable agent architecture, or 1000+ line plans.

---

*Last updated: April 2026*

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/harness-engineering.md`](../analysis/harness-engineering.md) [EXTRACTED (1.00)] — references

<!-- graphify-footer:end -->
