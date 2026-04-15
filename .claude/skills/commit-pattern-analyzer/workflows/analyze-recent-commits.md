# Workflow: Analyze Recent Commits

## Purpose
Extract patterns from a project's recent git history to understand how work
is being done, not just what the code looks like.

## Steps

### 1. Collect Raw Data (Bash)
```bash
# Commit messages and authors (90 days)
git log --oneline --since="90 days ago"

# Files changed most frequently
git log --since="90 days ago" --name-only --format="" | sort | uniq -c | sort -rn | head -30

# File types changed
git log --since="90 days ago" --name-only --format="" | sed 's/.*\.//' | sort | uniq -c | sort -rn

# AI co-authoring rate
total=$(git log --since="90 days ago" --oneline | wc -l)
ai=$(git log --since="90 days ago" --format="%b" | grep -c "Co-Authored-By")
echo "AI co-authored: $ai / $total"

# Commit size distribution
git log --since="90 days ago" --format="%h" | while read hash; do
  echo "$hash $(git diff --stat $hash^..$hash 2>/dev/null | tail -1)"
done

# Time of day pattern
git log --since="90 days ago" --format="%ad" --date=format:"%H" | sort | uniq -c | sort -rn
```

### 2. Categorize Changes
For each commit, classify:
- **feature**: New functionality
- **fix**: Bug fix
- **refactor**: Code restructuring without behavior change
- **config**: Configuration, CLAUDE.md, skills, rules
- **test**: Test additions or modifications
- **docs**: Documentation
- **chore**: Dependencies, CI, build

### 3. Identify Patterns
Look for:
- **Commit clustering**: Multiple commits in short bursts (suggests iteration cycles)
- **File hotspots**: Same files changed repeatedly (may need refactoring)
- **Missing tests**: Features without corresponding test commits
- **Large commits**: >500 lines changed in one commit (anti-pattern per harness-engineering)
- **Config evolution**: CLAUDE.md or skill changes (good sign — active tuning)
- **Skill/workflow usage**: Are skills being created, modified, used?

### 4. Output Raw Analysis
```markdown
## Raw Commit Analysis

**Project**: [name]
**Period**: [start] — [end]
**Total commits**: [N]
**AI co-authoring rate**: [X%]

### Change Distribution
| Category | Count | % |
|----------|-------|---|
| feature | | |
| fix | | |
| refactor | | |
| config | | |
| test | | |

### Hotspot Files (top 10)
| File | Changes | Category |
|------|---------|----------|

### Patterns Detected
- [pattern with evidence]

### Anomalies
- [anything unusual]
```

Pass this output to `recommend-from-patterns.md` for weighted recommendations.
