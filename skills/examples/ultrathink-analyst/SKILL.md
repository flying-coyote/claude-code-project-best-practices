---
name: UltraThink Analyst
description: Apply comprehensive FRAME-ANALYZE-SYNTHESIZE methodology for deep analysis of complex problems, strategic decisions, architectural choices, or research questions. Trigger when user says "ultrathink", "deep analysis", "systematic analysis", "comprehensive evaluation", or asks to analyze complex multi-dimensional problems.
allowed-tools: Read, Grep, Glob, WebFetch, WebSearch
---

# UltraThink Analyst

Apply rigorous FRAME-ANALYZE-SYNTHESIZE methodology to complex multi-dimensional problems.

## Trigger Conditions

**Activate**: "ultrathink", "deep analysis", "systematic analysis", "comprehensive evaluation", "analyze thoroughly", complex multi-dimensional problems, strategic decisions, architectural choices

**Skip**: Simple factual questions, quick answers needed, routine implementation, user wants brief response

## 3-Phase Protocol

### FRAME (F-R-A-M-E): Problem Definition
- **F**undamentals: Core elements, stakeholders, success criteria
- **R**elationships: Dependencies, feedback loops, causal chains
- **A**ssumptions: Hidden premises, biases, validation needs
- **M**odels: Frameworks, hypotheses, measurement approaches
- **E**vidence: Data support, source credibility, gaps

### ANALYZE (A-N-A-L-Y-Z-E): Deep Investigation
- **A**lternatives: Other approaches, competing methodologies
- **N**egatives: Failure modes, unintended consequences
- **A**dvantages: Benefits, competitive advantages, ROI
- **L**imitations: Constraints, feasibility boundaries
- **Y**ield: Expected results, success metrics
- **Z**ones: Scope, applicable contexts
- **E**volution: Change over time, adaptability

### SYNTHESIZE: Integration
Key insights, prioritized recommendations, action plan, validation approach.

## Output Format

```markdown
## FRAME
- Fundamentals: [core elements, success criteria]
- Assumptions: [what we're taking for granted]
- Evidence: [data supporting, gaps]

## ANALYZE
- Alternatives: [options with trade-offs]
- Negatives: [failure modes, risks]
- Limitations: [constraints]

## SYNTHESIZE
### Key Insights
1. [insight]

### Recommendations
PRIMARY: [main recommendation]
RISKS: [key risks and mitigations]

### Next Steps
1. [action]
```

## Don't

- Jump to solutions without FRAME phase
- Ignore alternative viewpoints
- Accept assumptions without validation
- Skip failure mode analysis
- Use UltraThink for simple questions (overkill)
