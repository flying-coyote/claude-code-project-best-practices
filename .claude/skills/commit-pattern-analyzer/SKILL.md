---
name: Commit Pattern Analyzer
description: |
  Analyze recent git commits in a target project to surface patterns, identify
  improvement opportunities, and generate recommendations weighted by source
  authority and recency. Trigger when user says "analyze commits", "review my
  recent work", "what patterns do you see", or when evaluating a project for
  best-practice alignment.
allowed-tools: Read, Grep, Glob, Bash
---

# Commit Pattern Analyzer

Surface actionable recommendations by analyzing how work is actually being done,
not just what the code looks like.

## Trigger Conditions

**Activate when**:
- User says "analyze commits", "review my recent work", "what patterns do you see"
- Evaluating a project for best-practice alignment
- After running ONE-LINE-PROMPT.md evaluation
- User asks "how can I improve my workflow"

**Skip when**:
- User is asking about a specific bug or feature (use normal tools)
- Repository has fewer than 10 commits
- User explicitly asks for code review, not workflow review

## Workflow

### Step 1: Gather Commit Data
```bash
# In the target project:
git log --oneline --since="14 days ago" --format="%H|%s|%an|%ad" --date=short
git log --since="14 days ago" --stat --format="" | sort | uniq -c | sort -rn | head -20
git log --since="14 days ago" --format="%s" | grep -i "Co-Authored-By" | wc -l
```

### Step 2: Identify Patterns
Analyze the commit data for:
- **File types changed most**: Which areas of code get the most attention?
- **Commit message patterns**: Are messages descriptive? Conventional commits?
- **AI co-authoring ratio**: What % of commits are Co-Authored-By AI?
- **Commit frequency**: Bursts vs steady? Time of day?
- **Refactoring vs feature work ratio**: How much is new vs maintenance?
- **Test co-location**: Are tests committed alongside features?

### Step 3: Cross-Reference Against Analysis Docs
Map observed patterns to the 26 analysis documents in `analysis/`:
- High AI co-authoring → `agent-driven-development.md` patterns
- CLAUDE.md changes → `claude-md-progressive-disclosure.md`
- Skill/workflow changes → `mcp-vs-skills-economics.md`
- Test patterns → `agent-evaluation.md`
- Large commits → `harness-engineering.md` (one feature at a time)

### Step 4: Weight Recommendations
Apply source-authority-matrix weighting:
- Recommendations backed by Tier 5 (Foundational) sources → high priority
- Recommendations backed by Tier 3 (Practitioner) sources → medium priority
- Recommendations backed by Tier 2 (Commentator) sources → note, don't push

### Step 5: Output
```markdown
## Commit Pattern Analysis: [project-name]

**Period**: [date range]
**Commits analyzed**: [count]
**AI co-authoring rate**: [X%]

### Patterns Observed
1. [pattern] — [frequency/evidence]
2. [pattern] — [frequency/evidence]

### Recommendations (by priority)

#### High Priority (Foundational source backing)
- [recommendation] — Source: [name] (Authority [tier], Weight [score])

#### Medium Priority (Practitioner source backing)
- [recommendation] — Source: [name] (Authority [tier], Weight [score])

#### Worth Noting (Commentator source backing)
- [observation] — Source: [name] (Authority [tier], Weight [score])
```

## Don't

- Recommend changes without checking actual commit evidence
- Weight YouTube-sourced recommendations equally with Anthropic engineering blog
- Produce recommendations longer than the analysis — be concise
- Criticize workflow choices without understanding project constraints
