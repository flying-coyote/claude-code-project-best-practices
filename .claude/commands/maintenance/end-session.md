# End of Session Checklist

Run through this checklist before ending a productive session.

## Required

- [ ] **Completed items logged**: Add finished work to PLAN.md "Completed This Cycle" section
- [ ] **PLAN.md date updated**: Update "Last Updated" to today's date
- [ ] **Changes committed**: All modifications committed with appropriate emoji prefix

## Recommended

- [ ] **Push to remote**: `git push origin master`
- [ ] **Milestone check**: If significant work complete, consider `/maintenance:archive-completed`

## Quick Commands

```bash
# Check for uncommitted changes
git status

# Stage and commit all changes
git add -A
git commit -m "📚 [description]"

# Push to remote
git push origin master

# View what would be archived
head -50 PLAN.md | grep -A 20 "Completed This Cycle"
```

## Commit Message Prefixes

| Prefix | Use For |
|--------|---------|
| `📚` | Documentation and patterns |
| `🔧` | Configuration and infrastructure |
| `✅` | Validation and testing |
| `📊` | Research and analysis |

## Example Session End

```bash
# 1. Update PLAN.md with completed work (manual edit)

# 2. Stage changes
git add PLAN.md patterns/*.md skills/README.md

# 3. Commit with description
git commit -m "📚 Add Claude Code v2.1 features to documentation"

# 4. Push to remote
git push origin master
```

## Note

The Stop hook will remind you about uncommitted changes and unpushed commits, but this checklist ensures you've also updated the documentation with what you accomplished.
