# Weekly Maintenance Review

Conduct weekly review of project status and documentation currency.

## Steps

1. **Gather week's activity**:
   ```bash
   git log --since="7 days ago" --oneline
   git diff --stat HEAD~10..HEAD 2>/dev/null || git diff --stat
   ```

2. **Review accomplishments**:
   - What patterns were added or updated?
   - What issues were resolved?
   - What quality improvements were made?

3. **Identify blockers**:
   - Any patterns waiting for sources?
   - Any skills needing validation?
   - Any structural issues discovered?

4. **Set next week priorities**:
   - What patterns should be added next?
   - What existing patterns need updates?
   - What documentation needs refresh?

5. **Update PLAN.md**:
   - Add completed items to "Completed This Cycle" section
   - Update current priorities
   - Note any blockers
   - Update metrics if counts changed
   - Update "Last Updated" date

6. **Commit**:
   ```
   git add PLAN.md
   git commit -m "📋 Weekly review [date]"
   ```

## Expected Outcome

PLAN.md reflects current week's accomplishments and next week's priorities.
