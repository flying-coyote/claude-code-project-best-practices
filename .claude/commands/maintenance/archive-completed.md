# Archive Completed Work

Promote completed items from PLAN.md to ARCHIVE.md and push to remote.

## When to Run

- Version milestone reached (v1.3 → v1.4)
- Significant feature or work package complete
- Monthly rollup (even without version bump)
- Before starting major new work phase

## Steps

1. **Review Completed This Cycle** in PLAN.md:
   ```bash
   # View current completed items
   head -50 PLAN.md | grep -A 20 "Completed This Cycle"
   ```

2. **Determine archive scope**:
   - Is this a version bump? Update version number
   - Is this a feature completion? Name the milestone
   - Is this a monthly rollup? Use "Month YYYY Maintenance"

3. **Update ARCHIVE.md**:
   - Add new milestone section at top of "Completed Milestones"
   - Include date and description
   - List completed items with context
   - Update "Metrics at Archive Time" if significant

4. **Clear PLAN.md**:
   - Empty the "Completed This Cycle" table (leave header row)
   - Update "Current Status" metrics if changed
   - Update "Last Updated" date

5. **Commit and push**:
   ```bash
   git add PLAN.md ARCHIVE.md
   git commit -m "📚 Archive completed work: [milestone name]"
   git push origin master
   ```

## Archive Entry Template

```markdown
### [Version or Milestone Name] (Date)
- [Item 1 from Completed This Cycle]
- [Item 2 from Completed This Cycle]
- Key metrics: [patterns count], [skills count]
```

## Example

**Before** (PLAN.md):
```markdown
## Completed This Cycle

| Item | Completed | Notes |
|------|-----------|-------|
| Research Claude Code updates | Jan 10, 2026 | Added 14 new features |
| Self-compliance audit | Jan 10, 2026 | Fixed 3 issues |
```

**After** (ARCHIVE.md):
```markdown
### January 2026 Maintenance (January 10, 2026)
- Researched Claude Code updates, added 14 new features to documentation
- Completed self-compliance audit, fixed 3 minor issues
- Key metrics: 20 patterns, 10 example skills
```

## Verification

After running this workflow:
- [ ] ARCHIVE.md has new milestone section
- [ ] PLAN.md "Completed This Cycle" table is empty
- [ ] PLAN.md "Last Updated" date is current
- [ ] Changes committed with `📚` prefix
- [ ] Changes pushed to origin/master
