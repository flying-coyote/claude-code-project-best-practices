# Judge Prompt Template

Minimal template for evaluating candidate outputs in the recursive refinement loop.

---

## Template

```
Evaluate this output against the following criteria.

QUERY: {query}

OUTPUT TO EVALUATE:
{output}

EVALUATION CRITERIA:

1. **Completeness** (0.0-1.0): Does it address all aspects of the query?
2. **Accuracy** (0.0-1.0): Are claims supported by evidence?
3. **Depth** (0.0-1.0): Is the analysis sufficiently comprehensive?
4. **Coherence** (0.0-1.0): Is there logical flow and organization?

Provide your evaluation:

## Scores
- Completeness: [score]
- Accuracy: [score]
- Depth: [score]
- Coherence: [score]
- **Overall**: [average]

## Top 3 Issues to Address
1. [Most important issue]
2. [Second issue]
3. [Third issue]

## Specific Feedback
[Detailed feedback for improvement]
```

---

## Customization

Adapt criteria to your domain:

| Domain | Additional Criteria |
|--------|-------------------|
| Research | Citation quality, methodology rigor |
| Code review | Test coverage, security, maintainability |
| Business analysis | ROI clarity, risk assessment, stakeholder impact |

---

## Usage Notes

- Use low-temperature evaluation for consistency
- Focus feedback on actionable improvements
- Track scores across iterations to detect plateau
