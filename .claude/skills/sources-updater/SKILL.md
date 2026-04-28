---
name: sources-updater
description: |
  Ensures SOURCES.md stays synchronized when adding new analysis documents or sources.
  Trigger when user adds a new analysis doc, says "update sources", "add source",
  or after pattern-reviewer identifies missing source entries. Enforces
  evidence tier classification and proper citation format.
allowed-tools: Read, Grep, Glob, Edit
---

# Sources Updater

Maintain SOURCES.md as the single source of truth for all references.

## When to Activate

- User adds a new analysis document
- User says "update sources", "add source"
- After pattern-reviewer identifies missing sources

**Skip when**: Source already exists in SOURCES.md

## Evidence Tiers

| Tier | Description | Example |
|------|-------------|---------|
| **A** | Primary vendor docs | Anthropic docs, official APIs |
| **B** | Expert/peer-reviewed | Papers, recognized expert blogs |
| **C** | Community-validated | GitHub repos with stars, case studies |
| **D** | Unverified (reject) | Forum posts, anonymous claims |

## Steps

1. Read the analysis document, extract source references
2. Check each against SOURCES.md
3. Classify evidence tier
4. Add entry in correct section, alphabetically

## Entry Format

```markdown
### [Source Name]
- **Author**: [Name/Organization]
- **URL**: [Full URL]
- **Evidence Tier**: [A/B/C]
- **Analysis**: [analysis/related-analysis.md]
```

## Don't

- Add Tier D sources
- Create duplicate entries
- Skip tier classification
- Add sources without analysis document cross-reference
