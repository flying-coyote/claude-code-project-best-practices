# Pattern Quality Checklist

Practical validation tool for reviewing new or updated patterns before merging.

---

## Required (All Patterns)

### Source & Evidence
- [ ] Has authoritative source (Tier A or B per SOURCES.md)
- [ ] Source URL is valid and accessible
- [ ] Evidence tier stated in frontmatter or header
- [ ] Claims include measurement dates and revalidation windows
- [ ] No unsourced quantitative claims (percentages, multipliers, etc.)

### Structure
- [ ] YAML frontmatter includes: `status`, `last-verified`
- [ ] Status is one of: `PRODUCTION`, `EMERGING`, `EXPERIMENTAL`
- [ ] Has Overview section explaining the pattern
- [ ] Has at least one concrete example or code snippet
- [ ] Has Related Patterns section with links to 2+ patterns

### Content Quality
- [ ] Passes the "Would removing this cause mistakes?" test
- [ ] Provides actionable guidance (not just theory)
- [ ] Includes anti-patterns or "what not to do" section
- [ ] No duplicate coverage of existing patterns (check decision matrix)

### Integration
- [ ] Listed in README.md pattern decision matrix
- [ ] Listed in README.md SDD phase tables
- [ ] Added to SOURCES.md if new source introduced
- [ ] Cross-references updated in related patterns
- [ ] ARCHITECTURE.md pattern listing updated

### Formatting
- [ ] Passes `npm run lint` (markdownlint)
- [ ] No broken internal links
- [ ] Tables render correctly in GitHub markdown
- [ ] Code blocks have language specifiers

---

## Conditional

### If PRODUCTION status
- [ ] Validated across 2+ real projects
- [ ] Includes specific metrics or outcomes
- [ ] Has implementation checklist

### If introduces measurement claims
- [ ] `measurement-claims` in YAML frontmatter
- [ ] Each claim has: `source`, `date`, `revalidate`
- [ ] Revalidation date is within 12 months

### If introduces new source
- [ ] Source added to SOURCES.md with full citation
- [ ] Source added to SOURCES-QUICK-REFERENCE.md if Tier A/B
- [ ] Evidence tier classification justified

---

## Quick Validation (5-minute check)

For minor updates, verify at minimum:

1. `npm run lint` passes
2. No broken cross-references
3. Frontmatter `last-verified` date updated
4. Changed content has source attribution

---

## Using This Checklist

**New pattern**: Complete all Required items + applicable Conditional items.

**Pattern update**: Use Quick Validation for minor edits. Full checklist for structural changes.

**Automated via skill**: Run `/pattern-reviewer` for automated validation against these criteria.
