# Judge Prompt Template

> **ARCHIVED — but nothing live replaces it.** Archived in the v2.0 repositioning (March 2026, DECISIONS.md § Reposition as Analytical Layer) or a later reduction. No successor: analysis/orchestration-comparison.md does not cover this file's material. Its Self-Evolution section names the judge-feedback refinement step and prices it (one table row: "Each candidate iterated 3x with judge feedback | ~9x"), but carries none of this template's substance — no scoring prompt text, no Completeness/Accuracy/Depth/Coherence criteria or 0.0-1.0 scale, no Scores / Top 3 Issues / Specific Feedback output format, no per-domain criteria table, and no usage guidance on low-temperature evaluation or plateau detection across iterations. Grepping analysis/ for this template's distinctive strings returns nothing; the only live-doc mentions of judges or rubrics are that cost row, citations of Simon Willison's unrelated "Judgement" post, and agent-evaluation.md's bare listing of Hamel Husain's "write-judge-prompt" skill as a first-party pointer. This archived template remains the corpus's only reusable scoring prompt, and it is uncovered. This is a **coverage gap, not a currency gap** — the material is unreplaced, not merely out of date, so a reader who discards it is left with nothing. Its specifics are v1-era; its subject is still uncovered. (Marked 2026-08-28; successor determined by mapping plus adversarial verification, which overturned 35 of 39 successor claims — see `analysis/prose-corpus-discoverability.md`.)

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
