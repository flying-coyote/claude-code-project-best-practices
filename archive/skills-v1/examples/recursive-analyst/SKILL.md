---
name: recursive-analyst
description: Apply Self-Evolution Algorithm for complex research and analysis. Trigger when user needs comprehensive analysis, high-stakes decisions, or requests "deep research", "multiple perspectives", "leave no stone unturned". Spawns parallel candidates (conservative/balanced/creative), refines each through judge feedback, and synthesizes best elements through crossover.
allowed-tools: Read, Grep, Glob, WebFetch, WebSearch, Task
---

# Recursive Analyst

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
