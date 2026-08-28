# Crossover Prompt Template

> **ARCHIVED — but nothing live replaces it.** Archived in the v2.0 repositioning (March 2026, DECISIONS.md § Reposition as Analytical Layer) or a later reduction. No live successor covers this file. analysis/orchestration-comparison.md names the crossover-synthesis step in a single cost-table row ("Best elements merged", ~13x total) but carries none of this template's substance: the fill-in prompt text, the four synthesis instructions, the conflict-reconciliation rule favouring higher-scored candidates, the prescribed output format, and the task-type weighting table have no counterpart anywhere in analysis/ (greps for "reconcile", "{query}", "{candidate", "Unique Strengths", "Agreement Areas", and "Merged Result" all return zero live hits). The technique survives as a cost line item; the instrument that performs it exists only here. This is a **coverage gap, not a currency gap** — the material is unreplaced, not merely out of date, so a reader who discards it is left with nothing. Its specifics are v1-era; its subject is still uncovered. (Marked 2026-08-28; successor determined by mapping plus adversarial verification, which overturned 35 of 39 successor claims — see `analysis/prose-corpus-discoverability.md`.)

Minimal template for synthesizing multiple candidate outputs into a superior merged result.

---

## Template

```
Synthesize these candidate analyses into a single superior output.

ORIGINAL QUERY: {query}

CANDIDATE 1 (Conservative - Score: {score_1}):
{candidate_1}

CANDIDATE 2 (Balanced - Score: {score_2}):
{candidate_2}

CANDIDATE 3 (Creative - Score: {score_3}):
{candidate_3}

SYNTHESIS INSTRUCTIONS:

1. **Identify Unique Strengths**: What does each candidate contribute that others missed?

2. **Note Agreement**: Where all candidates reached the same conclusion (high confidence).

3. **Reconcile Conflicts**: Where candidates disagree, favor higher-scored. Document the conflict and resolution.

4. **Merge**: Create a unified output that incorporates the best elements of each while maintaining coherence.

OUTPUT FORMAT:

## Candidate Contributions
- Conservative: [unique contribution]
- Balanced: [unique contribution]
- Creative: [unique contribution]

## Agreement Areas (High Confidence)
- [Point all agreed on]

## Reconciled Conflicts
- [Conflict]: Adopted [X] because [rationale]

## Merged Result
[Superior synthesized output]
```

---

## Customization

Adjust weighting based on task:

| Task Type | Weighting Approach |
|-----------|-------------------|
| Risk assessment | Favor Conservative |
| Innovation | Favor Creative |
| Practical decisions | Favor Balanced |
| Equal importance | Use score-based weighting |

---

## Usage Notes

- Higher-scored candidates should have more influence
- Ensure merged result is coherent, not a patchwork
- Document which candidate contributed which elements
