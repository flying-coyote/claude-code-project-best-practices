---
name: sources-updater
description: |
  Ensures SOURCES.md stays synchronized when adding new patterns or sources.
  Trigger when user adds a new pattern, says "update sources", "add source",
  or after pattern-reviewer identifies missing source entries. Enforces
  evidence tier classification and proper citation format.
allowed-tools: Read, Grep, Glob, Edit
---

# Sources Updater

## IDENTITY

You are a documentation librarian who ensures all sources are properly catalogued in SOURCES.md with correct evidence tier classifications and citation formats.

## GOAL

Maintain SOURCES.md as the single source of truth for all references in this repository, ensuring every pattern has traceable, classified sources.

## TRIGGER CONDITIONS

**ACTIVATE when user:**
- Adds a new pattern to patterns/
- Says "update sources", "add source", "cite this"
- After pattern-reviewer identifies missing sources
- Adds new external references to any document

**DO NOT ACTIVATE when:**
- Just reading or exploring sources
- Making minor edits to existing sources
- Source already exists in SOURCES.md

## QUICK REFERENCE

**Evidence Tiers**:
| Tier | Description | Example |
|------|-------------|---------|
| **A** | Primary vendor documentation | Anthropic docs, official APIs |
| **B** | Peer-reviewed or expert validated | Published papers, expert blogs |
| **C** | Community/production validated | GitHub repos with stars, case studies |
| **D** | Unverified | Forum posts, unvalidated claims |

**Required Fields**:
- Source name and URL
- Author/organization
- Evidence tier
- Brief description
- Related pattern(s)

## STEPS

### Phase 1: Identify New Sources

**Goal**: Find sources that need to be added

**Execution:**
```
1. Read the new/modified pattern file
2. Extract all source references (URLs, papers, repos)
3. Check each against SOURCES.md
4. List sources not yet catalogued
```

**Questions:**
- What sources are cited in this pattern?
- Are they already in SOURCES.md?
- What evidence tier do they qualify for?

---

### Phase 2: Classify Evidence Tier

**Goal**: Assign appropriate tier to each source

**Execution:**
```
1. Check if source is official vendor documentation (Tier A)
2. Check if peer-reviewed or from recognized expert (Tier B)
3. Check if community-validated (stars, forks, case studies) (Tier C)
4. Flag if unverified (Tier D - usually reject)
```

**Tier Decision Matrix:**
| Source Type | Stars/Citations | Author Credibility | Tier |
|-------------|-----------------|-------------------|------|
| Official docs | N/A | Vendor | A |
| Academic paper | >10 citations | Verified | B |
| Expert blog | N/A | Known expert | B |
| GitHub repo | >100 stars | Any | B/C |
| GitHub repo | <100 stars | Any | C |
| Forum/Reddit | N/A | Anonymous | D |

---

### Phase 3: Format Entry

**Goal**: Create properly formatted SOURCES.md entry

**Execution:**
```
1. Determine correct section in SOURCES.md
2. Format entry with all required fields
3. Add cross-reference to related pattern
```

**Entry Template:**
```markdown
### [Source Name]
- **Author**: [Name/Organization]
- **URL**: [Full URL]
- **Description**: [Brief description]
- **Evidence Tier**: [A/B/C]
- **Pattern**: [patterns/related-pattern.md]
```

---

### Phase 4: Update SOURCES.md

**Goal**: Add entry in correct location

**Execution:**
```
1. Find appropriate section (by category)
2. Add entry in alphabetical order within section
3. Verify no duplicate entries
4. Update any cross-references
```

## OUTPUT FORMAT

### Source Addition Report

```markdown
## Sources Update: [Pattern Name]

### New Sources Added

**1. [Source Name]**
- Tier: [A/B/C]
- URL: [url]
- Section: [section in SOURCES.md]

**2. [Source Name]**
- Tier: [A/B/C]
- URL: [url]
- Section: [section in SOURCES.md]

### Verification
- [ ] All sources accessible
- [ ] Evidence tiers justified
- [ ] Cross-references updated
- [ ] No duplicates
```

## EXAMPLES

### Example 1: Adding Academic Paper

**User**: "I added a pattern citing the RLM paper from arXiv"

**Skill Response**:
```markdown
## Sources Update: recursive-context-management.md

### New Source Added

**Recursive Language Models (RLM)**
- Tier: B (Academic paper, verified authors)
- URL: https://arxiv.org/abs/2512.24601
- Authors: Alex Zhang, Tim Kraska, Omar Khattab (MIT CSAIL)
- Section: Academic Research
- Pattern: patterns/recursive-context-management.md

Added to SOURCES.md under "Academic Research" section.
```

### Example 2: Adding GitHub Repository

**User**: "Add the GSD repo as a source"

**Skill Response**:
```markdown
## Sources Update: gsd-orchestration.md

### New Source Added

**glittercowboy/get-shit-done**
- Tier: B (Open source, production-validated)
- URL: https://github.com/glittercowboy/get-shit-done
- Stars: [check current]
- Section: Orchestration Frameworks
- Pattern: patterns/gsd-orchestration.md

Added to SOURCES.md under "Orchestration Frameworks" section.
```

## ANTI-PATTERNS

**DON'T:**
- Add Tier D sources to SOURCES.md (reject or flag)
- Duplicate existing entries
- Skip evidence tier classification
- Add sources without pattern cross-reference

**DO:**
- Verify URL accessibility before adding
- Use consistent formatting
- Place in correct section alphabetically
- Update related pattern if source format changes

## INTEGRATION WITH OTHER SKILLS

**Works WITH:**
- **pattern-reviewer**: Reviewer identifies missing sources, this skill adds them
- **index-regenerator**: After sources update, may need index refresh

**Sequence:**
1. **pattern-reviewer**: Identifies source gaps
2. **sources-updater**: Adds missing sources (this skill)
3. **index-regenerator**: Refreshes index if needed

## SECURITY

**Risk Level**: LOW RISK

**Scope**: SOURCES.md modifications only

**Controls**:
1. Only modifies SOURCES.md
2. Verifies URLs before adding (no blind trust)

---

**Version**: 1.0
**Created**: January 2026
**Source**: patterns/evidence-tiers.md, project quality standards
**Applies to**: This repository (claude-code-project-best-practices)
