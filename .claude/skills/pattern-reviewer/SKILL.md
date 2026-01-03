---
name: pattern-reviewer
description: Validates new patterns against project quality standards before merge. Trigger when user adds a new pattern, says "review pattern", or submits pattern for inclusion.
allowed-tools: Read, Glob, Grep
---

# Pattern Reviewer

Validates patterns against claude-code-project-best-practices quality standards.

## When to Activate

**ACTIVATE when user:**
- Adds a new pattern to patterns/
- Says "review pattern", "validate pattern", or "check pattern quality"
- Submits a pattern for inclusion in the repository
- Asks if a pattern meets quality standards

**DO NOT activate when:**
- User is just reading or exploring patterns
- User is making minor edits (typos, formatting)
- Pattern is already approved and being referenced

## Validation Checklist

### 1. Source Quality (Required)

- [ ] Has **Evidence Tier** label (A, B, or C minimum)
- [ ] Cites authoritative source with URL
- [ ] Source is accessible and verifiable
- [ ] Claims match cited sources

**Tier Requirements:**
- Tier A: Primary vendor documentation (preferred)
- Tier B: Peer-reviewed or expert validated (acceptable)
- Tier C: Community/production validated (acceptable with corroboration)
- Tier D: Not acceptable for patterns

### 2. Structure Compliance (Required)

- [ ] Has header with Source, Evidence Tier, SDD Phase
- [ ] Has clear "Overview" or problem statement
- [ ] Has practical implementation guidance
- [ ] Has **Anti-Patterns** section with Problem/Symptom/Solution format
- [ ] Has **Related Patterns** section with valid links
- [ ] Has "Last updated: [Month Year]" footer

### 3. Content Quality (Required)

- [ ] Actionable guidance (not just principles)
- [ ] Examples where applicable
- [ ] Tables for comparisons/matrices
- [ ] Code blocks properly formatted
- [ ] No broken internal links

### 4. SDD Alignment (Recommended)

- [ ] States which SDD phase it supports
- [ ] Explains how it fits the 4-phase model
- [ ] References related SDD patterns

### 5. Cross-Reference Integrity

- [ ] All "Related Patterns" links are valid
- [ ] Pattern is referenced in SOURCES.md (if new source)
- [ ] Pattern is listed in INDEX.md (auto-generated)
- [ ] Pattern is mentioned in README.md if high-traffic

## Output Format

```markdown
## Pattern Review: [pattern-name.md]

### Summary
[PASS/NEEDS WORK] - [Brief assessment]

### Checklist Results

**Source Quality**: [PASS/FAIL]
- Evidence Tier: [tier]
- Source: [source name]
- Issues: [any issues]

**Structure Compliance**: [PASS/FAIL]
- Missing sections: [list]
- Issues: [any issues]

**Content Quality**: [PASS/FAIL]
- Issues: [any issues]

**SDD Alignment**: [PASS/N/A]
- Phase: [phase]
- Issues: [any issues]

### Required Changes
1. [Change 1]
2. [Change 2]

### Recommendations (Optional)
1. [Suggestion 1]
```

## Quick Reference

**Minimum viable pattern:**
1. Source + Evidence Tier header
2. Problem statement
3. Solution with examples
4. Anti-Patterns section
5. Related Patterns section
6. Last updated footer

**Common issues:**
- Missing Evidence Tier label
- Anti-Patterns section missing or incomplete
- No "Last updated" date
- Broken Related Patterns links
- Claims without source attribution

## Integration

**Works WITH:**
- **evidence-tiers.md** - Source classification
- **CONTRIBUTING.md** - Contribution guidelines
- **SOURCES.md** - Source tracking

**Sequence:**
1. Author writes pattern draft
2. Pattern Reviewer validates
3. Author fixes issues
4. Merge to patterns/
5. Update SOURCES.md if new source
