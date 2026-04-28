---
name: analysis-reviewer
description: Validates new analysis documents against project quality standards. Trigger when user adds an analysis doc or says "review analysis".
allowed-tools: Read, Glob, Grep
---

# Analysis Reviewer

Validate analysis documents against this repository's quality standards.

## When to Activate

- User adds a new analysis document to analysis/
- User says "review analysis", "validate analysis", "check analysis"

**Skip when**: Just reading analysis docs, making typo fixes

## Validation Checklist

### Required

- [ ] **Evidence Tier** label (A, B, or C) with claim strength (1-5)
- [ ] Source citation with URL
- [ ] Overview/claim statement
- [ ] Comparative analysis or quantified metrics
- [ ] **Limitations and Trade-offs** section
- [ ] **Related Analysis** section with valid links to other analysis/ docs
- [ ] "Last updated: [Month Year]" footer

### Recommended

- [ ] Listed in SOURCES.md if new source
- [ ] Cross-references verified (all links point to analysis/, not patterns/)
- [ ] Production evidence cited where applicable

## Output Format

```markdown
## Analysis Review: [analysis-name.md]

**Verdict**: [PASS/NEEDS WORK]

**Source Quality**: [PASS/FAIL] - Tier [A/B/C], [source name]
**Structure**: [PASS/FAIL] - Missing: [sections]
**Content**: [PASS/FAIL] - [issues]
**Cross-References**: [PASS/FAIL] - [stale links found]

### Required Changes
1. [change]
```

## Don't

- Rubber-stamp without checking every item
- Focus on formatting over missing sections
- Rewrite the analysis (flag issues for author)
- Allow references to archived patterns/ directory
