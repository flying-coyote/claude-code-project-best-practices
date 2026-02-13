# Workflow Schedule Change: Weekly → Daily

**Date**: February 13, 2026
**Change**: Monitoring frequency increased from weekly to daily
**Rationale**: AI coding sector is evolving rapidly

---

## What Changed

### Schedule Updates

| Workflow | Old Schedule | New Schedule |
|----------|-------------|-------------|
| source-monitoring.yml | Monday 9am UTC | **Every day 9am UTC** |
| link-checker.yml | Sunday 12am UTC | **Every day 12am UTC** |

### Cron Changes

```yaml
# source-monitoring.yml
OLD: - cron: '0 9 * * 1'  # Every Monday
NEW: - cron: '0 9 * * *'  # Every day

# link-checker.yml
OLD: - cron: '0 0 * * 0'  # Every Sunday
NEW: - cron: '0 0 * * *'  # Every day
```

### Issue Title Changes

```
OLD: 📋 Weekly source review - February 13, 2026
NEW: 📋 Daily source review - February 13, 2026

OLD: Labels: ['documentation', 'weekly-review']
NEW: Labels: ['documentation', 'daily-review']
```

---

## Impact Analysis

### Issue Volume

**Before (Weekly)**:
```
source-monitoring.yml:
- Runs: 1x per week (Monday)
- Issues created: ~5-7 per week
- Total: ~5-7 issues/week

link-checker.yml:
- Runs: 1x per week (Sunday)
- Issues created: 0-1 per week (only if links broken)
- Total: 0-1 issues/week

Combined: ~5-8 issues/week
```

**After (Daily)**:
```
source-monitoring.yml:
- Runs: 7x per week (every day)
- Issues created: ~1-2 per day (conditional)
- Total: ~7-14 issues/week

link-checker.yml:
- Runs: 7x per week (every day)
- Issues created: 0-1 per week (only if links broken)
- Total: 0-1 issues/week

Combined: ~7-15 issues/week
```

**Net increase**: ~2-9 more issues per week

### GitHub Actions Usage

**Before (Weekly)**:
```
source-monitoring: 22s × 1 run/week = 22 seconds/week
link-checker: 120s × 1 run/week = 120 seconds/week
Total: 142 seconds/week = ~9.5 minutes/month
```

**After (Daily)**:
```
source-monitoring: 22s × 7 runs/week = 154 seconds/week
link-checker: 120s × 7 runs/week = 840 seconds/week
Total: 994 seconds/week = ~66 minutes/month
```

**Cost**: Still $0 (public repo = unlimited minutes)

### Issue Management

**Weekly workflow**:
- Check issues Monday morning
- Process 5-8 issues
- Week to complete before next batch

**Daily workflow**:
- Check issues daily at 9am UTC
- Process 1-2 issues per day
- More immediate but requires daily attention

---

## Reasoning

### Why Daily?

1. **Rapid Evolution**: AI coding tools releasing updates weekly/bi-weekly
   - Claude Code: v2.1.42 released since last check
   - New releases would be caught next-day instead of next-week

2. **Community Activity**: High velocity in practitioner content
   - IndyDevDan, Aniket Panjwani posting multiple times per week
   - Daily check ensures we don't miss trending patterns

3. **Framework Updates**: Active development in standards
   - GitHub Spec Kit, agentskills.io, BMAD all updating frequently
   - Daily monitoring aligns with their release cadence

4. **Competitive Intelligence**: Staying current matters
   - Reddit/HN discussions happen daily
   - Catching trends early provides advantage

5. **Issue Hygiene**: Smaller, more frequent batches
   - Easier to process 1-2 issues daily vs 5-8 weekly
   - Less context switching, more continuous awareness

### Why Not Hourly?

- GitHub Actions minimum interval: 5 minutes
- But: Overkill for documentation/pattern tracking
- Most sources update daily/weekly, not hourly
- Would create noise without signal

### Why Not Keep Weekly?

- Week-long gaps risk missing important updates
- Fast-moving sector requires faster response
- Daily checklist acts as "morning standup" for the repo

---

## Conditional Logic

Workflows won't create issues every day blindly. They only create issues when:

### source-monitoring.yml

**Always created**:
- Daily source review checklist (aggregates everything)

**Conditionally created** (only if detected):
- New Claude Code release
- Recent commits in awesome-claude-code (last 7 days)
- New Anthropic blog post
- Self-compliance issues (patterns modified OR gaps exist)
- Documentation maintenance (INDEX.md stale OR PLAN.md needs archiving)
- Community engagement (open PRs OR untriaged issues)

**Expected pattern**:
- Checklist: 1 per day (7/week)
- Conditional issues: 0-2 per day (~5-10/week)
- Total: ~12-17 issues/week

### link-checker.yml

**Only creates issues if**:
- Links are broken (rare)
- Tier A sources are down (critical)

**Expected pattern**:
- Most days: 0 issues
- Occasionally: 1 issue if links break
- Total: 0-2 per week

---

## Management Strategy

### Daily Routine

**9:00am UTC** (1am PST / 4am EST):
- source-monitoring.yml runs
- Issues appear in flying-coyote repo

**Suggested workflow**:
```
Morning (within 24h):
1. Review daily checklist issue
2. Scan for new release/blog issues
3. Mark high-priority items
4. Schedule deep work for important finds

Throughout day:
5. Process 1-2 issues as time allows
6. Close issues when addressed

End of day:
7. Any unfinished items roll to tomorrow
```

### If Overwhelmed

**Option 1: Filter by priority**
```bash
# High priority only
gh issue list --label tier-a,source-update

# Skip daily checklists, focus on detections
gh issue list --label source-update,community
```

**Option 2: Batch process**
```
Monday: Process all issues from weekend
Rest of week: Stay current with daily issues
```

**Option 3: Reduce frequency**
```
Edit workflows back to:
- Every other day: cron: '0 9 */2 * *'
- Three times per week: cron: '0 9 * * 1,3,5'
```

**Option 4: Auto-close checklists**
```
Add workflow to auto-close daily checklist after 48h
Keep only actionable detection issues open
```

---

## Monitoring the Change

### Success Metrics (After 1 Week)

- [ ] Caught updates within 24h (vs 7 days previously)
- [ ] Issue volume manageable (not overwhelming)
- [ ] Signal-to-noise ratio high (issues are actionable)
- [ ] No major sources missed
- [ ] Triage time < 10 min/day

### Adjustment Criteria

**Too many issues** → Increase thresholds for conditional creation
**Too few issues** → Frequency is good, sources are stable
**Missing updates** → Add more sources or check more frequently
**Noise > signal** → Filter better, raise detection thresholds

### Review After

- 1 week: Check volume and signal quality
- 1 month: Evaluate if daily is sustainable
- 3 months: Decide if this is the right cadence

---

## Rollback Plan

If daily proves too frequent:

```bash
# Edit workflow files
vim .github/workflows/source-monitoring.yml
vim .github/workflows/link-checker.yml

# Change cron back to weekly
OLD: - cron: '0 9 * * *'
NEW: - cron: '0 9 * * 1'  # Monday only

# Commit and push
git add .github/workflows/
git commit -m "⚡ Revert to weekly schedule"
git push origin master
```

---

## Documentation Updates

Updated files to reflect daily schedule:
- [x] .github/workflows/source-monitoring.yml
- [x] .github/workflows/link-checker.yml
- [x] .github/workflows/README.md
- [x] WORKFLOWS-SETUP.md
- [ ] WORKFLOWS-SUMMARY.md (TODO if needed)
- [ ] PLAN.md (TODO: update review cadence)

---

## Testing

Trigger manual run to verify daily schedule works:

```bash
gh workflow run source-monitoring.yml
gh workflow run link-checker.yml

# Check issues created
gh issue list --limit 10

# Verify titles say "Daily" not "Weekly"
gh issue view <issue-number>
```

---

## Cost Analysis

### Current (Daily)

```
Minutes per month: ~66 minutes
Cost (public repo): $0
Cost (private repo): $0 (well under 2,000 min/month free tier)

Headroom remaining:
Private repo scenario: 2,000 - 66 = 1,934 minutes
Could run 30x more frequently and still be free
```

### If We Added More Jobs

```
Could add:
- 50 more sources to check
- 20 more jobs per workflow
- Run twice per day (every 12 hours)

And still:
- Cost $0 (public repo)
- Complete in < 5 minutes per run
- Stay well under all GitHub limits
```

---

## Next Steps

1. **Monitor first week** (Feb 13-20, 2026)
   - Track issue volume
   - Measure triage time
   - Assess signal quality

2. **Adjust if needed** (Feb 20, 2026)
   - Tune conditional thresholds
   - Add filters if too noisy
   - Consider auto-closing daily checklists

3. **Document learnings** (Mar 1, 2026)
   - Update PLAN.md with findings
   - Add to ARCHIVE.md
   - Refine workflow based on experience

---

## Comparison to Alternatives

| Approach | Pros | Cons | Our Choice |
|----------|------|------|------------|
| **Hourly** | Immediate detection | Noise, overkill | ❌ Too frequent |
| **Daily** | Fast response, manageable | ~10-15 issues/week | ✅ **Selected** |
| **Weekly** | Low volume, easy to batch | 7-day delay | ❌ Too slow |
| **On-demand** | Full control | Easy to forget | ❌ Not automated |

---

## Philosophy

> "This space is evolving rapidly. Daily reviews ensure we don't miss important developments."

The AI coding sector is moving at unprecedented speed:
- Claude Code: Releasing every 2-4 weeks
- Practitioners: Publishing daily content
- Standards: Active development (Spec Kit, agentskills.io)
- Community: Daily activity in awesome lists

**Daily monitoring aligns with the sector's pace.**

---

**Created**: February 13, 2026
**Status**: ACTIVE - Monitoring starts tomorrow (Feb 14, 2026)
**Review Date**: February 20, 2026 (1 week evaluation)
