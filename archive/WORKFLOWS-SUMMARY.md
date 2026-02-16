# GitHub Actions Workflows - Implementation Summary

## What Was Created

### New Workflow Files
1. **.github/workflows/source-monitoring.yml** - 7 weekly monitoring jobs
2. **.github/workflows/link-checker.yml** - 3 weekly validation jobs
3. **.github/link-check-config.json** - Link checker configuration
4. **.github/workflows/README.md** - Complete workflow documentation
5. **WORKFLOWS-SETUP.md** - Setup and usage guide

## Weekly Automation Schedule

Every **Monday 9am UTC**, 7 jobs run:

| Job | What It Monitors | Issue Created When |
|-----|------------------|-------------------|
| **check-anthropic-releases** | Claude Code releases | New release detected |
| **check-awesome-lists** | Community curated lists | Recent commits found |
| **check-anthropic-blog** | Anthropic engineering blog | New post detected |
| **check-practitioner-sources** | IndyDevDan, Fabric, frameworks | Activity + always creates weekly checklist |
| **self-compliance-audit** | Dogfooding gaps + recent patterns | Gaps exist OR patterns modified |
| **documentation-maintenance** | INDEX.md, PLAN.md freshness | INDEX stale OR items to archive |
| **community-engagement** | Open PRs and untriaged issues | PRs or untriaged issues exist |

Every **Sunday 12am UTC**, 3 jobs run:

| Job | What It Validates | Issue Created When |
|-----|-------------------|-------------------|
| **check-links** | All markdown links | Broken links found |
| **markdown-lint** | Markdown formatting | Lint errors (comments on PR) |
| **check-source-accessibility** | Tier A primary sources | Critical sources down |

## Expected Weekly Issues

Starting next Monday (and every Monday after), expect these issues:

### Always Created
- **📋 Weekly source review** - Comprehensive checklist with activity highlights

### Conditionally Created
- **📚 Review Claude Code v2.X.X release** - When new release
- **🔍 Review awesome-claude-code updates** - When community activity
- **📚 Review potential new Anthropic blog post** - When new post detected
- **✅ Self-compliance audit** - When patterns modified OR gaps exist
- **📊 Documentation maintenance** - When INDEX.md stale OR PLAN.md has items
- **🤝 Community engagement triage** - When open PRs or untriaged issues
- **🔗 Broken links detected** - When link checker finds issues (Sundays)
- **🚨 CRITICAL: Tier A sources inaccessible** - When primary sources down

## Next Steps

### 1. Commit and Push (Required)

```bash
cd "/Users/jeremy.wiley/Git projects/claude-code-project-best-practices"

# Stage all new workflow files
git add .github/

# Commit with descriptive message
git commit -m "🔧 Add comprehensive weekly automation workflows

- Add source-monitoring.yml: 7 jobs for weekly maintenance
  - Anthropic releases, awesome lists, blog monitoring
  - Practitioner sources and framework updates
  - Self-compliance audit (dogfooding)
  - Documentation maintenance (INDEX.md, PLAN.md)
  - Community engagement (PR/issue triage)

- Add link-checker.yml: 3 jobs for validation
  - Markdown link checking
  - Markdown linting
  - Tier A source accessibility

- Add workflow documentation
  - .github/workflows/README.md: Complete reference
  - WORKFLOWS-SETUP.md: Setup and usage guide
  - WORKFLOWS-SUMMARY.md: Implementation summary

**Philosophy**: All monitoring now weekly due to fast-moving AI sector

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

# Push to remote
git push origin master
```

### 2. Verify Workflows Are Active

After pushing, check that workflows are enabled:

```bash
# List all workflows
gh workflow list

# You should see:
# - Claude Code Review
# - Source Monitoring
# - Link Checker
```

### 3. Test Manually (Optional)

Trigger workflows manually to test:

```bash
# Trigger source monitoring
gh workflow run source-monitoring.yml

# Trigger link checker
gh workflow run link-checker.yml

# Check run status
gh run list --limit 5

# View logs if needed
gh run view <run-id> --log
```

### 4. First Issues Arrive Monday

**Timeline**:
- **Sunday 12am UTC**: Link checker creates first issues (if problems found)
- **Monday 9am UTC**: Source monitoring creates 1-7 issues depending on:
  - New releases (likely YES - check hasn't run before)
  - Community activity (likely YES - awesome lists active)
  - Blog posts (maybe - depends if new post since SOURCES.md last updated)
  - Weekly checklist (YES - always created)
  - Self-compliance (maybe - if patterns modified or gaps exist)
  - Documentation maintenance (maybe - check INDEX.md freshness)
  - Community engagement (maybe - check if open PRs/issues exist)

**First run will likely create 5-10 issues** as it discovers the current state.

### 5. Triage First Batch

When issues arrive:

1. **Don't panic** - This is expected first-time discovery
2. **Review each issue** - They have checklists
3. **Prioritize**:
   - Critical (Tier A sources down) = Immediate
   - New releases = High priority
   - Weekly checklist = Work through methodically
   - Maintenance = Schedule when convenient
4. **Close when done** - Check off items and close
5. **Adjust if needed** - Too noisy? Tune in workflow files

### 6. Establish Weekly Routine

**Recommended workflow**:

**Sunday evening** (after link checker runs):
- Check for broken link issues
- Fix any broken links before Monday

**Monday morning** (after source monitoring):
- Triage new issues
- Read the weekly checklist issue
- Decide which items to tackle this week
- Schedule time for high-priority items

**Throughout the week**:
- Work through checklist
- Close issues as completed
- Document learnings in PLAN.md

**Next Monday**:
- New batch arrives
- Previous week's issues should mostly be closed

## Tuning and Customization

### If Too Many Issues

**Problem**: Getting overwhelmed with issues

**Solutions**:
1. Reduce frequency (change from weekly to bi-weekly):
   ```yaml
   # Change in source-monitoring.yml
   - cron: '0 9 * * 1,15'  # 1st and 15th of month
   ```

2. Make some checks conditional (only create issue if significant activity):
   ```yaml
   # Add threshold checks before creating issues
   if: steps.check-something.outputs.activity_level > 5
   ```

3. Combine multiple checks into single weekly summary issue

### If Missing Important Updates

**Problem**: Update slipped through

**Solutions**:
1. Add additional sources to monitor
2. Increase frequency to 2x/week for critical sources
3. Add Slack/email notifications for critical issues

### If False Positives

**Problem**: Link checker flagging valid links

**Solutions**:
1. Add to ignore list in `.github/link-check-config.json`
2. Adjust timeout/retry settings
3. Add custom headers for specific domains

## Cost and Performance

### GitHub Actions Free Tier
- **Public repos**: Unlimited minutes
- **Private repos**: 2,000 minutes/month

### Estimated Usage
- Source monitoring: ~5 minutes/week = 260 min/year
- Link checker: ~5 minutes/week = 260 min/year
- **Total**: ~520 minutes/year (negligible for public repo)

### Performance
- All 7 source monitoring jobs run in **parallel** (~3-5 min total)
- Link checker jobs run in **parallel** (~3-5 min total)
- Issues created asynchronously

## Monitoring the Monitors

### Check Workflow Health

```bash
# View recent runs
gh run list --limit 20

# View specific workflow
gh run list --workflow=source-monitoring.yml

# Check for failures
gh run list --status failure

# View failed run logs
gh run view <run-id> --log

# Re-run if transient failure
gh run rerun <run-id>
```

### Common Issues

| Problem | Cause | Solution |
|---------|-------|----------|
| Workflow not triggering | Not on default branch | Ensure on `master` |
| API rate limiting | Too many requests | Add delays between calls |
| Link check failures | Site blocking bots | Add to ignore list |
| Permission errors | Missing GITHUB_TOKEN | Should auto-work in Actions |

## Philosophy and Benefits

### Why Weekly for Everything?

The AI coding space is evolving **rapidly**:

- Claude Code: New releases every 2-4 weeks
- Community: Daily contributions to awesome lists
- Practitioners: Weekly blog posts, videos, courses
- Frameworks: Active development on Spec Kit, agentskills.io

**Quarterly reviews miss too much**. Weekly cadence ensures this repository stays current.

### Benefits Realized

1. **Never Miss Updates**: Automated monitoring catches everything
2. **Stay Current**: Weekly reviews keep pace with sector evolution
3. **Dogfooding Enforced**: Self-compliance audit prevents doc/practice drift
4. **Documentation Fresh**: Automatic staleness detection
5. **Community Responsive**: PR/issue triage reminders ensure engagement
6. **Link Health**: Broken links caught before users report them
7. **Reduced Manual Work**: Automation creates issues with checklists

### Trade-offs

**Pros**:
- Complete coverage of external sources
- Proactive vs reactive monitoring
- Checklists reduce cognitive load
- Never forget maintenance tasks

**Cons**:
- 5-10 issues created weekly (needs triage)
- Can feel overwhelming at first
- Requires discipline to process issues
- May need tuning to reduce noise

**Recommendation**: Start with default settings, tune after 2-3 weeks based on signal-to-noise ratio.

## Questions?

### Workflow Questions
- See `.github/workflows/README.md`
- Check YAML syntax: https://www.yamllint.com/

### Setup Questions
- See `WORKFLOWS-SETUP.md`

### Philosophy Questions
- See PLAN.md:110-115 for review cadence rationale
- See SOURCES.md for evidence tier system

## Success Metrics

After 1 month, evaluate:

- ✅ **Catching updates**: Did workflows detect important releases/posts?
- ✅ **Manageable volume**: Is issue count sustainable?
- ✅ **Actionable issues**: Do issues have clear next steps?
- ✅ **Reducing manual work**: Less time checking sources manually?
- ✅ **Documentation current**: Is PLAN.md/INDEX.md staying fresh?
- ✅ **Community responsive**: Are PRs/issues triaged promptly?

If any ❌, tune the workflows accordingly.

---

## Final Checklist

Before considering this complete:

- [ ] Commit and push workflow files to master
- [ ] Verify workflows appear in GitHub Actions UI
- [ ] Optionally test manual trigger
- [ ] Document any project-specific adjustments needed
- [ ] Wait for first batch of issues Monday
- [ ] Triage first batch to establish routine
- [ ] Tune sensitivity after 2-3 weeks if needed
- [ ] Update PLAN.md with automation success metrics

---

**Created**: February 13, 2026
**Status**: Ready to commit and deploy
**Next Action**: Commit, push, and wait for Monday's issues
