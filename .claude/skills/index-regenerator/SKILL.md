---
name: index-regenerator
description: |
  Regenerates INDEX.md to reflect current file structure. Trigger when user
  says "update index", "regenerate index", after adding/removing files, or
  when INDEX.md shows stale counts. Provides more control than the PostToolUse
  hook which runs automatically.
allowed-tools: Read, Glob, Bash, Write
---

# Index Regenerator

## IDENTITY

You are a documentation indexer who maintains INDEX.md as an accurate reflection of the repository's file structure with proper categorization and counts.

## GOAL

Regenerate INDEX.md with accurate file counts, proper categorization, and sorted listings that reflect the current state of the repository.

## TRIGGER CONDITIONS

**ACTIVATE when user:**
- Says "update index", "regenerate index", "refresh index"
- After batch adding/removing files
- When INDEX.md counts appear stale
- After major refactoring

**DO NOT ACTIVATE when:**
- PostToolUse hook is sufficient (single file changes)
- Just reading INDEX.md
- User wants manual index control

## QUICK REFERENCE

**INDEX.md Structure**:
```markdown
# Index
*Auto-generated: YYYY-MM-DD HH:MM*

## Summary
**Total documents**: N

| Directory | Count |
|-----------|-------|
| patterns | X |
| skills | Y |
...

## [Category]
- [file.md](path/to/file.md)
```

**Excluded Files**:
- Hidden files (.*)
- node_modules/
- .git/
- Non-markdown files (unless specified)

## STEPS

### Phase 1: Scan Repository

**Goal**: Get current file structure

**Execution:**
```
1. Glob for all markdown files
2. Exclude hidden directories and node_modules
3. Group by directory
4. Count files per directory
```

**Command:**
```bash
find . -name "*.md" -not -path "*/\.*" -not -path "*/node_modules/*" | sort
```

---

### Phase 2: Categorize Files

**Goal**: Organize files into logical sections

**Execution:**
```
1. Group root-level files
2. Group patterns/ files
3. Group skills/ files (including examples)
4. Group other directories (presets, templates, etc.)
```

**Categories:**
| Directory | Section Name |
|-----------|--------------|
| . (root) | Root Files |
| patterns/ | Patterns |
| skills/ | Skills |
| skills/examples/* | Skill Examples |
| presets/ | Presets |
| templates/ | Templates |
| research/ | Research |

---

### Phase 3: Generate INDEX.md

**Goal**: Create formatted index

**Execution:**
```
1. Add header with timestamp
2. Create summary table with counts
3. List files by category
4. Sort alphabetically within categories
```

**Template:**
```markdown
# Index

*Auto-generated: [TIMESTAMP]*

## Summary

**Total documents**: [TOTAL]

| Directory | Count |
|-----------|-------|
| [dir1] | [count1] |
| [dir2] | [count2] |

## [Category Name]

- [filename.md](path/filename.md)
- [filename2.md](path/filename2.md)
```

---

### Phase 4: Write and Verify

**Goal**: Update INDEX.md and confirm accuracy

**Execution:**
```
1. Write new INDEX.md content
2. Verify file count matches glob
3. Check for broken links
4. Report changes from previous version
```

## OUTPUT FORMAT

### Index Regeneration Report

```markdown
## Index Regenerated

**Timestamp**: [YYYY-MM-DD HH:MM]
**Total Files**: [N]

### Changes from Previous
- Added: [list of new files]
- Removed: [list of removed files]
- Net change: +/-[N] files

### Directory Summary
| Directory | Previous | Current | Change |
|-----------|----------|---------|--------|
| patterns | X | Y | +/-Z |
| skills | X | Y | +/-Z |

INDEX.md updated successfully.
```

## EXAMPLES

### Example 1: After Adding Patterns

**User**: "Regenerate index after adding the new orchestration patterns"

**Skill Response**:
```markdown
## Index Regenerated

**Timestamp**: 2026-01-27 10:30
**Total Files**: 70

### Changes from Previous
- Added:
  - patterns/gsd-orchestration.md
  - patterns/cognitive-agent-infrastructure.md
  - patterns/johari-window-ambiguity.md
- Removed: (none)
- Net change: +3 files

### Directory Summary
| Directory | Previous | Current | Change |
|-----------|----------|---------|--------|
| patterns | 28 | 31 | +3 |

INDEX.md updated successfully.
```

### Example 2: Stale Index Check

**User**: "The index looks outdated"

**Skill Response**:
```markdown
## Index Analysis

**Current INDEX.md**: 63 files (dated 2026-01-20)
**Actual file count**: 70 files

**Missing from index**:
- patterns/framework-selection-guide.md
- patterns/mcp-vs-skills-economics.md
- patterns/recursive-context-management.md
- REFACTORING-PLAN-2026-01.md
- (3 more)

Regenerating INDEX.md now...

[Proceeds to regenerate]
```

## ANTI-PATTERNS

**DON'T:**
- Include hidden files or directories
- Include non-markdown files without explicit request
- Break existing link formats
- Remove manual sections (if any exist)

**DO:**
- Preserve any manually-added sections
- Sort alphabetically within categories
- Include accurate timestamps
- Report what changed

## INTEGRATION WITH OTHER SKILLS

**Works WITH:**
- **pattern-reviewer**: After pattern approved, index updates
- **sources-updater**: After sources change, index may need refresh

**Sequence:**
1. **pattern-reviewer**: Approves new pattern
2. **sources-updater**: Updates SOURCES.md
3. **index-regenerator**: Updates INDEX.md (this skill)

## SECURITY

**Risk Level**: LOW RISK

**Scope**: INDEX.md modifications only

**Controls**:
1. Only reads and writes INDEX.md
2. Does not modify source files

---

**Version**: 1.0
**Created**: January 2026
**Source**: Project infrastructure requirements
**Applies to**: This repository (claude-code-project-best-practices)
