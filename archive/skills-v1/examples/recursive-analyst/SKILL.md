---
name: recursive-analyst
description: Apply Self-Evolution Algorithm for complex research and analysis. Trigger when user needs comprehensive analysis, high-stakes decisions, or requests "deep research", "multiple perspectives", "leave no stone unturned". Spawns parallel candidates (conservative/balanced/creative), refines each through judge feedback, and synthesizes best elements through crossover.
allowed-tools: Read, Grep, Glob, WebFetch, WebSearch, Task
---

# Recursive Analyst

> **ARCHIVED — not current guidance, and only partly succeeded.** Archived in the v2.0 repositioning (March 2026, DECISIONS.md § Reposition as Analytical Layer) or a later reduction. **Partially superseded.** [`analysis/orchestration-comparison.md`](../../../../analysis/orchestration-comparison.md) § "Self-Evolution: Quality Through Diversity" carries this skill's decision layer — the same conservative/balanced/creative → judge-refinement → crossover structure, the same 3x / ~9x / ~13x token costs, and worth-it/not-worth-it criteria matching the Activate/Skip conditions below — and [`analysis/harness-engineering.md`](../../../../analysis/harness-engineering.md) § "Ablation Evidence: Verifiers Hurt, Self-Evolution Helps" adds measured evidence this file lacks (self-evolution +4.8 SWE / +2.7 OSWorld, the only consistently helpful module; multi-candidate search alone scored −2.4 / −5.6). Neither carries the operational half: the judge rubric (completeness / accuracy / depth / coherence, 0–1 each), the early-stop thresholds (score > 0.9, or improvement < 0.03 with score > 0.7), the four-step crossover reconciliation, the output template, and the "Don't" anti-patterns survive only here and in the sibling `templates/` prompts. Read the successors for *whether and at what cost*; read this file for *how*. The scoring dimensions and termination thresholds are also recorded in [`SOURCES.md`](../../../../SOURCES.md) § "Self-Evolution Algorithm Sources." Its v1-era specifics and dates are a snapshot, preserved as recorded — do not treat them as current. (Marked 2026-08-28; successor determined by mapping plus adversarial verification, which overturned 35 of 39 successor claims — see `analysis/prose-corpus-discoverability.md`.)

Multi-candidate analysis with parallel exploration and synthesis through conservative/balanced/creative perspectives.

## Trigger Conditions

**Activate**: "deep research", "comprehensive analysis", "high-stakes decision", "multiple perspectives", "leave no stone unturned", complex trade-offs

**Skip**: Simple lookups, single-pass tasks, quick answers, token-constrained, already using ultrathink-analyst

## Workflow

### Phase 1: Multi-Candidate Spawn (Parallel)

Launch 3 Task calls in a SINGLE message:

| Candidate | Approach |
|-----------|----------|
| **Conservative** | Low-risk, evidence-heavy, proven solutions |
| **Balanced** | Pragmatic, trade-off aware, best practices |
| **Creative** | Challenge assumptions, explore innovations |

### Phase 2: Recursive Refinement (Per Candidate)

For each candidate, iterate up to 3 times:

1. **Judge**: Score completeness, accuracy, depth, coherence (0-1 each)
2. **Stop if**: Score > 0.9 OR (improvement < 0.03 AND score > 0.7) OR iteration 3
3. **Revise**: Improve based on judge feedback, focusing on lowest scores

### Phase 3: Crossover Synthesis

1. Identify unique strengths from each candidate
2. Note agreement areas (high confidence)
3. Reconcile conflicts (favor higher-scored)
4. Merge into superior output

## Output Format

```markdown
# Recursive Analysis: [Topic]

## Candidate Contributions
| Candidate | Score | Key Contribution |
|-----------|-------|------------------|
| Conservative | X.XX | [Unique strength] |
| Balanced | X.XX | [Unique strength] |
| Creative | X.XX | [Unique strength] |

## Agreement Areas (High Confidence)
- [Points all candidates agreed on]

## Reconciled Conflicts
| Conflict | Resolution | Rationale |
|----------|------------|-----------|
| [Issue] | Adopted [X] | [Why] |

## Merged Result
[Synthesized output combining strengths]

## Confidence: [HIGH/MEDIUM/LOW]
Agreement rate: X/Y key points
```

## Token Usage

~13x single-pass analysis. Use when quality justifies cost (high-stakes, comprehensive research).

## Don't

- Use for simple lookups
- Skip parallel spawning (sequential loses diversity)
- Force crossover when one candidate clearly dominates
- Ignore disagreements between candidates
