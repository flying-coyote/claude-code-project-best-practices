# Workflow: Recommend From Patterns

## Purpose
Take raw commit analysis and produce weighted recommendations by cross-referencing
against the best-practices analysis documents and source authority matrix.

## Input
Raw commit analysis output from `analyze-recent-commits.md`.

## Steps

### 1. Map Patterns to Analysis Documents

| Pattern Observed | Relevant Analysis Doc | Key Recommendation |
|-----------------|----------------------|-------------------|
| High AI co-authoring (>80%) | agent-driven-development.md | Verify harness completeness, check CLAUDE.md coverage |
| Large commits (>500 lines) | harness-engineering.md | One feature at a time, external artifact checkpoints |
| No CLAUDE.md changes in 14 days | claude-md-progressive-disclosure.md | Review if config matches current workflow |
| Missing test commits | agent-evaluation.md | Task-based evals, test co-location |
| Frequent skill/rule edits | mcp-vs-skills-economics.md | Skills preferred over MCP for cost |
| Same file changed 5+ times | behavioral-insights.md | Context rot risk, may need refactoring |
| Config/YAML heavy changes | domain-knowledge-architecture.md | Verify domain knowledge encoding |
| Cross-repo commits same day | cross-project-sync.md | Check dependency cascading |

### 2. Weight Each Recommendation

For each recommendation, identify the backing source from SOURCES-QUICK-REFERENCE.md
and apply the authority x recency weight:

**Priority tiers:**
- **High** (Effective Weight >= 0.65): Backed by Foundational or recent Authoritative sources
- **Medium** (Effective Weight 0.35-0.64): Backed by Practitioner sources
- **Low** (Effective Weight < 0.35): Backed by Commentator sources — mention but don't push

### 3. Generate Recommendations

For each recommendation:
1. State the observation (what the commits show)
2. State the recommendation (what to change)
3. Cite the source with authority tier and effective weight
4. Estimate effort (trivial / small / medium / large)

### 4. Output

```markdown
## Recommendations for [project-name]

Based on [N] commits over [period], weighted by source authority.

### High Priority (Foundational/Authoritative backing)
1. **[Recommendation]**
   - Observed: [commit pattern evidence]
   - Source: [name] (Authority [tier], Weight [score])
   - Effort: [trivial/small/medium/large]

### Medium Priority (Practitioner backing)
1. **[Recommendation]**
   ...

### Worth Noting (Commentator backing)
1. **[Observation]**
   ...

### What's Working Well
- [Positive patterns to keep doing, with evidence]
```

## Don't
- Recommend changes the user is already doing (check commits for evidence)
- Stack-rank by personal preference — use the authority weights
- Ignore positive patterns — always include "What's Working Well"
