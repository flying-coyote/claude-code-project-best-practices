---
name: hypothesis-validator
description: Apply systematic hypothesis validation when user formulates research claims or proposes testable hypotheses. Trigger on "I hypothesize that...", "Can you validate this claim?", or research findings requiring evidence assessment. Use confidence scoring and evidence tier classification.
allowed-tools: Read, Grep, Glob, Edit, Write
---

# Hypothesis Validator

Validate research hypotheses using systematic methodology: assess testability, classify evidence, assign confidence levels.

## Trigger Conditions

**Activate**: "I hypothesize that...", "validate this claim", "what evidence supports", research claims, confidence assessment requests

**Skip**: Reading others' research (passive), well-established facts, brainstorming marked exploratory

## Evidence Tiers

| Tier | Type | Weight |
|------|------|--------|
| 1 | Production deployments, measured outcomes | Highest |
| 2 | Peer-reviewed research, replication | High |
| 3 | Expert consensus, documented reasoning | Medium |
| 4 | Vendor claims, theoretical assertions | Low |
| 5 | Speculation, opinion, unverified | Minimal |

## Confidence Levels

| Level | Criteria |
|-------|----------|
| HIGH (>80%) | 2+ Tier 1 sources OR multiple Tier 2 + Tier 1, no contradictions |
| MEDIUM (50-80%) | 1+ Tier 2-3 sources, some validation, minor contradictions |
| LOW (<50%) | Only Tier 4-5, theoretical only, significant contradictions |

## Steps

1. **Identify**: Extract testable hypothesis (independent/dependent variables, scope)
2. **Assess**: Classify all evidence by tier, identify gaps
3. **Score**: Assign confidence level with justification
4. **Analyze**: Document contradictions, attempt reconciliation
5. **Document**: Track with ID, status, validation plan

## Output Format

```markdown
# Hypothesis: [Title]

**Statement**: [Clear, testable hypothesis with scope]
**Confidence**: [HIGH/MEDIUM/LOW] ([XX]%)

**Evidence**:
- Tier 1: [Finding]
- Tier 2: [Finding]

**Contradictions**: [Any conflicts and resolution status]

**Language Guide**:
- HIGH: "demonstrates", "shows"
- MEDIUM: "suggests", "indicates"
- LOW: "hypothesizes", "may"

**Validation Plan**: [What's needed to increase confidence]
```

## Don't

- Accept vendor claims without independent validation
- Use "proves" or "always" with MEDIUM/LOW confidence
- Ignore contradictions when scoring
- Present LOW confidence as validated fact
- Skip evidence tier classification
