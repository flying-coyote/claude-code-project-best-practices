---
name: pattern-reviewer
description: Validates new patterns against project quality standards. Trigger when user adds a pattern or says "review pattern".
allowed-tools: Read, Glob, Grep
---

# Pattern Reviewer

Validate patterns against this repository's quality standards.

## When to Activate

- User adds a new pattern to patterns/
- User says "review pattern", "validate pattern", "check pattern"

**Skip when**: Just reading patterns, making typo fixes

## Validation Checklist

### Required

- [ ] **Evidence Tier** label (A, B, or C)
- [ ] Source citation with URL
- [ ] Overview/problem statement
- [ ] Implementation guidance with examples
- [ ] **Anti-Patterns** section (Problem/Symptom/Solution format)
- [ ] **Related Patterns** section with valid links
- [ ] "Last updated: [Month Year]" footer

### Recommended

- [ ] SDD phase stated
- [ ] Listed in SOURCES.md if new source
- [ ] Cross-references verified

## Output Format

```markdown
## Pattern Review: [pattern-name.md]

**Verdict**: [PASS/NEEDS WORK]

**Source Quality**: [PASS/FAIL] - Tier [A/B/C], [source name]
**Structure**: [PASS/FAIL] - Missing: [sections]
**Content**: [PASS/FAIL] - [issues]

### Required Changes
1. [change]
```

## Don't

- Rubber-stamp without checking every item
- Focus on formatting over missing sections
- Rewrite the pattern (flag issues for author)
