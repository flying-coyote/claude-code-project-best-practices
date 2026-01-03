# Crossover Prompt Template

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
