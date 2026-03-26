# Recursive Evolution Pattern (Self-Evolution Algorithm)

**Source**: Google TTD-DR Paper, OptILLM implementation, AI-Engineering-101 tutorial
**Evidence Tier**: B (Community implementations with production validation)

## Overview

The Self-Evolution Algorithm treats complex tasks as a diffusion process with iterative refinement. Instead of single-pass generation, it:

1. Spawns multiple candidates with diverse configurations
2. Iteratively refines each through judge feedback
3. Synthesizes best elements through crossover

**SDD Phase**: Cross-phase (enhances Tasks and Implement phases)

> "Self-evolution uses a 'Judge' to critique components (Plan, Search, Answer) and loop until quality improves."
> — Google Deep Researcher

---

## When to Use

| Scenario | Why Self-Evolution Helps |
|----------|-------------------------|
| **Complex research synthesis** | Multiple perspectives, iterative depth |
| **High-stakes decisions** | Reduced single-point-of-failure risk |
| **Creative problem-solving** | Diversity sampling explores solution space |
| **Quality-critical output** | Judge loop ensures threshold met |

### Poor Fits

| Scenario | Why Not |
|----------|---------|
| Simple factual lookups | Overhead exceeds benefit |
| Time-critical responses | Parallel candidates add latency |
| Low-stakes tasks | Single-pass sufficient |
| Token-constrained contexts | 3x+ token usage |

---

## Algorithm Components

### 1. Multi-Candidate Initialization

Spawn N candidates (typically 3) with varying configurations to explore different solution spaces:

| Candidate | Style | Focus |
|-----------|-------|-------|
| **Conservative** | Evidence-heavy, low-risk | Established patterns, proven approaches |
| **Balanced** | Pragmatic, trade-off aware | Best practices, practical solutions |
| **Creative** | Exploratory, novel angles | Innovation potential, alternative perspectives |

**Implementation Principle**: Different prompt styles, not model parameters (Claude Code doesn't expose temperature).

### 2. Recursive Refinement Loop (per candidate)

For each candidate, iterate M times (typically 3):

```
┌─────────────────────────────────────────────────────┐
│                REFINEMENT LOOP                      │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌──────────┐     ┌──────────┐     ┌──────────┐   │
│  │ GENERATE │ ──► │ EVALUATE │ ──► │  REVISE  │   │
│  │   O_n    │     │  (Judge) │     │  O_{n+1} │   │
│  └──────────┘     └──────────┘     └──────────┘   │
│       │                                   │        │
│       └───────────── LOOP ◄──────────────┘        │
│                                                     │
│  Terminate when:                                   │
│  - Quality > 0.9 (high confidence)                 │
│  - Improvement < 0.03 with Quality > 0.7           │
│  - Max iterations reached                          │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### 3. Environment Judge

The Judge evaluates each output against criteria:

| Dimension | Question |
|-----------|----------|
| **Completeness** | Does it address all aspects of the query? |
| **Accuracy** | Are claims supported by evidence? |
| **Depth** | Is analysis sufficiently comprehensive? |
| **Coherence** | Is there logical flow and organization? |

The Judge provides:
- **Score** (0.0-1.0): Normalized quality measure
- **Feedback**: Specific critique for improvement
- **Issues**: Top 3 problems to address

### 4. Crossover Synthesis

After all candidates refined:

1. **Identify Strengths**: What unique value does each candidate provide?
2. **Note Agreement**: Where candidates agree = high confidence
3. **Reconcile Conflicts**: Favor higher-scored candidates
4. **Merge**: Produce superior output combining best elements

---

## Claude Code Implementation

### Using Parallel Subagents

Spawn 3 candidates simultaneously using the Task tool:

```markdown
# In your prompt or skill:

## Phase 1: Multi-Candidate Initialization

Launch 3 subagents IN PARALLEL with a single message containing
multiple Task tool calls:

[Task 1: Conservative Candidate]
- subagent_type: "general-purpose"
- prompt: "Analyze [TOPIC] with a CONSERVATIVE approach:
  - Focus on established patterns and proven solutions
  - Prioritize evidence-based claims
  - Favor low-risk recommendations
  - Cite authoritative sources"

[Task 2: Balanced Candidate]
- subagent_type: "general-purpose"
- prompt: "Analyze [TOPIC] with a BALANCED approach:
  - Consider trade-offs explicitly
  - Apply best practices pragmatically
  - Acknowledge alternatives
  - Provide actionable recommendations"

[Task 3: Creative Candidate]
- subagent_type: "general-purpose"
- prompt: "Analyze [TOPIC] with a CREATIVE approach:
  - Explore novel angles and alternatives
  - Challenge assumptions
  - Consider innovative solutions
  - Think beyond conventional patterns"
```

### Using Skills

For repeatable methodology, create a `recursive-analyst` skill that:
1. Spawns parallel candidates via Task tool
2. Applies Judge criteria to each result
3. Synthesizes through crossover prompt

See: `skills/examples/recursive-analyst/SKILL.md`

---

## Termination Conditions

From OptILLM production implementation:

| Condition | When to Stop |
|-----------|--------------|
| **Quality Threshold** | Completeness > 0.9 |
| **Diminishing Returns** | Improvement < 0.03 AND Completeness > 0.7 |
| **Max Iterations** | Reached configured limit (default: 3) |

**Principle**: Stop iterating when additional refinement provides minimal benefit.

---

## Quality Dimensions (OptILLM Production)

The OptILLM implementation scores across 6 dimensions:

1. **Completeness**: Addresses all query aspects
2. **Accuracy**: Information reliability
3. **Depth**: Analysis comprehensiveness
4. **Coherence**: Logical organization
5. **Citations**: Source integration quality
6. **Improvement**: Iteration-to-iteration gains

These map to the repo's existing confidence scoring pattern.

---

## Integration with Existing Patterns

| Pattern | Integration |
|---------|-------------|
| **Subagent Orchestration** | Extends with Diversity Sampling pattern |
| **Confidence Scoring** | Judge output maps to HIGH/MEDIUM/LOW |
| **UltraThink Analyst** | Can trigger recursive-analyst for deep analysis |
| **Hypothesis Validator** | Crossover synthesis can validate competing claims |

---

## Example Workflow

### Research Synthesis Task

**User**: "Analyze whether we should migrate from PostgreSQL to DuckDB for analytics"

**Recursive Evolution Process**:

1. **Spawn 3 Candidates** (parallel):
   - Conservative: Focus on migration risks, established patterns
   - Balanced: Compare trade-offs, total cost analysis
   - Creative: Explore hybrid architectures, novel approaches

2. **Refine Each** (3 iterations):
   - Judge evaluates completeness, accuracy, depth
   - Candidates incorporate feedback
   - Track scores for crossover weighting

3. **Crossover Synthesis**:
   - Conservative contributed: Risk matrix, rollback plan
   - Balanced contributed: Decision framework, timeline
   - Creative contributed: Hybrid Postgres+DuckDB architecture
   - **Merged**: Comprehensive recommendation with risk-aware implementation plan

---

## Anti-Patterns

**DON'T**:
- Run self-evolution for simple tasks (overhead exceeds benefit)
- Skip the Judge step (refinement without feedback is just repetition)
- Use identical prompts for candidates (defeats diversity purpose)
- Ignore crossover synthesis (parallel work wasted without merge)

**DO**:
- Reserve for complex, high-stakes analysis
- Ensure Judge criteria align with task goals
- Differentiate candidate approaches meaningfully
- Weight crossover by candidate scores

---

## Token Usage Considerations

Self-Evolution uses significantly more tokens:

| Approach | Token Multiplier |
|----------|-----------------|
| Single-pass | 1x |
| 3 candidates (no refinement) | ~3x |
| 3 candidates × 3 iterations | ~9x |
| + Judge evaluations | ~12x |
| + Crossover synthesis | ~13x |

**Recommendation**: Use for quality-critical tasks where the improvement justifies the cost.

---

## Related Patterns

- [Subagent Orchestration](./subagent-orchestration.md) - Parallel execution patterns
- [Confidence Scoring](./confidence-scoring.md) - Quality assessment framework
- [Long-Running Agent](./long-running-agent.md) - External artifacts for context bridging
- [UltraThink Analyst](../skills/examples/ultrathink-analyst/SKILL.md) - Deep analysis methodology

---

## Sources

- [Google TTD-DR Paper](https://arxiv.org/abs/2502.04675) - Test-Time Diffusion Deep Researcher
- [OptILLM deep_research](https://github.com/codelion/optillm/tree/main/optillm/plugins/deep_research) - Production implementation
- [AI-Engineering-101](https://github.com/SauravP97/AI-Engineering-101/tree/main/self-evolution-google) - Educational implementation
- [Google Self-Evolution Algorithm Video](https://www.youtube.com/watch?v=example) - Saurav Prateek tutorial

*Last updated: January 2026*
