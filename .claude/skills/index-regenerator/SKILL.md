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

Maintain INDEX.md as accurate reflection of repository structure.

## When to Activate

- User says "update index", "regenerate index"
- After batch adding/removing files
- When INDEX.md counts appear stale

**Skip when**: Single file change (PostToolUse hook handles it)

## Steps

1. Glob all markdown files (exclude hidden dirs, node_modules)
2. Group by directory, count per directory
3. Generate INDEX.md with timestamp and summary table
4. Report changes from previous version

## INDEX.md Format

```markdown
# Index
*Auto-generated: YYYY-MM-DD HH:MM*

## Summary
**Total documents**: N

| Directory | Count |
|-----------|-------|
| patterns | X |
| skills | Y |

## [Category]
- [file.md](path/to/file.md)
```

## Output

```markdown
## Index Regenerated

**Timestamp**: [date]
**Total Files**: [N]

### Changes
- Added: [files]
- Removed: [files]
```

## Don't

- Include hidden files or node_modules
- Break existing link formats
- Remove manually-added sections
