# GitHub Actions Workflows Setup

> **ARCHIVED — not current guidance, and only partly succeeded.** Archived in the v2.0 repositioning (March 2026, DECISIONS.md § Reposition as Analytical Layer) or a later reduction. Superseded in part. The live operating reference for this same automation is `.github/workflows/README.md`, which covers the same ground in more detail — per-job descriptions, `gh workflow run` and GitHub-UI manual triggers, `link-check-config.json` settings, the monitoring schedule, issue labels, permissions, and rate-limit and false-positive troubleshooting. Not carried over there: how to edit the cron schedule, GitHub Actions cost and minute budgeting, the workflow-health commands `gh run view <id> --log` and `gh run rerun <id>`, local validation via `act`/yamllint, and the "Too Many Issues Created" troubleshooting entry with its debouncing remedy — that last one being the failure mode this repository went on to hit (916 unread auto-filed link-check issues). Those gaps are live: they apply to `link-checker.yml`, which still runs. `analysis/prose-corpus-discoverability.md` is NOT a successor to this file — it records the standing judgment that the link checker "fires into a void," but contains none of this file's setup or operating material, and no `analysis/` doc covers GitHub Actions at all (`grep -ril "github actions" analysis/` returns 0 files). Dead rather than superseded: `source-monitoring.yml` and its jobs, deleted 2026-07-10 (ARCHIVE.md Phase 6) — note this file documents seven such jobs and `.github/workflows/README.md` only four, and that README still documents the deleted workflow too, so the currency defect is shared, not fixed. The Quick Start path `/Users/jeremy.wiley/Git projects/...` resolves nowhere. Its v1-era specifics and dates are a snapshot, preserved as recorded — do not treat them as current. (Marked 2026-08-28; successor determined by mapping plus adversarial verification, which overturned 35 of 39 successor claims — see `analysis/prose-corpus-discoverability.md`.)

This document explains the automated workflows created for maintaining this repository.

## What Was Created

### New Files
```
.github/workflows/
├── claude-code.yml          (existing)
├── source-monitoring.yml    (NEW)
├── link-checker.yml         (NEW)
└── README.md                (NEW)

.github/
└── link-check-config.json   (NEW)
```

## Quick Start

### 1. Test the Workflows Locally

Before committing, verify the workflow syntax:

```bash
# Navigate to repository
cd "/Users/jeremy.wiley/Git projects/claude-code-project-best-practices"

# Check workflow files exist
ls -la .github/workflows/

# View a workflow
cat .github/workflows/source-monitoring.yml
```

### 2. Commit and Push

```bash
git add .github/
git commit -m "🔧 Add automated source monitoring and link checking workflows

- Add source-monitoring.yml: Monitor Anthropic releases, awesome lists, blog
- Add link-checker.yml: Validate markdown links and Tier A sources
- Add link-check-config.json: Configure link checker behavior
- Add workflows README: Document all workflows"

git push origin master
```

### 3. Enable Workflows

After pushing, the workflows will be automatically enabled on the repository.

Verify they're active:
```bash
# List workflows
gh workflow list

# You should see:
# - Claude Code Review
# - Source Monitoring
# - Link Checker
```

### 4. Test Manual Execution

```bash
# Trigger source monitoring manually
gh workflow run source-monitoring.yml

# Trigger link checker manually
gh workflow run link-checker.yml

# View recent runs
gh run list --limit 5
```

## What Each Workflow Does

### Source Monitoring (Runs Every Day 9am UTC)

**Jobs** (all run daily):

1. **check-anthropic-releases** - Monitors Claude Code releases
2. **check-awesome-lists** - Monitors community curated lists
3. **check-anthropic-blog** - Scrapes engineering blog
4. **check-practitioner-sources** - Monitors IndyDevDan, Fabric, frameworks
5. **self-compliance-audit** - Checks if we practice what we preach
6. **documentation-maintenance** - INDEX.md, PLAN.md, cross-references
7. **community-engagement** - PR and issue triage

**Output**: Creates GitHub issues with appropriate labels for follow-up

**Benefits**:
- Never miss important Anthropic updates
- Track community patterns and best practices
- Stay current in fast-moving AI coding sector
- Automated dogfooding compliance
- Keep documentation fresh and accurate
- Responsive community engagement

### Link Checker (Runs Every Day Midnight UTC)

**Checks**:
1. **All Markdown Links** - Validates every link in .md files
2. **Markdown Linting** - Ensures consistent formatting
3. **Tier A Source Accessibility** - Critical check for primary sources

**Output**:
- Creates issues for broken links (scheduled runs)
- Fails PR checks if new broken links introduced
- CRITICAL issues if Tier A sources are down

**Benefits**:
- Keep documentation healthy
- Catch dead links before users find them
- Monitor critical source availability

## Expected Issues Created

After the first runs, expect issues like:

1. **📚 Review Claude Code v2.X.X release**
   - Created when: New Claude Code release detected
   - Action: Review release notes, update SOURCES.md

2. **🔍 Review awesome-claude-code updates**
   - Created when: Recent commits in awesome lists
   - Action: Check for new community patterns

3. **📋 Daily source review - Date**
   - Created when: Every day (always)
   - Highlights: Activity in practitioner sources, framework updates
   - Action: Follow comprehensive checklist for all sources

4. **✅ Self-compliance audit - Date**
   - Created when: Pattern files modified OR dogfooding gaps exist
   - Action: Ensure repository practices documented patterns

5. **📊 Documentation maintenance - Date**
   - Created when: INDEX.md stale OR PLAN.md has completed items
   - Action: Update generated files, archive completed work

6. **🤝 Community engagement triage - Date**
   - Created when: Open PRs exist OR untriaged issues exist
   - Action: Review and respond to community contributions

7. **🔗 Broken links detected in documentation**
   - Created when: Links return 404/500/timeout
   - Action: Fix or update links

5. **🚨 CRITICAL: Tier A sources inaccessible**
   - Created when: Primary sources are down
   - Action: Immediate investigation required

## Workflow Schedule

| When | What Happens | Jobs |
|------|--------------|------|
| **Every day 9am UTC** | Complete source monitoring | 7 jobs run in parallel |
| | - check-anthropic-releases | New Claude Code releases |
| | - check-awesome-lists | Community curated lists |
| | - check-anthropic-blog | Engineering blog posts |
| | - check-practitioner-sources | Educators/frameworks |
| | - self-compliance-audit | Dogfooding check |
| | - documentation-maintenance | INDEX.md, PLAN.md |
| | - community-engagement | PR/issue triage |
| **Every day 12am UTC** | Link validation | 3 jobs: links, lint, Tier A sources |
| **On PR with .md changes** | Link checker validates new links | Prevents broken links |
| **When @.claude mentioned** | Claude Code review runs | AI-powered PR review |

**Philosophy**: All maintenance is now **daily** due to the fast-moving nature of AI coding tools. This project needs to stay current with rapid developments.

## Configuration

### Adjust Schedule

Edit the cron expressions in workflow files:

```yaml
# Current: Every Monday at 9am UTC
- cron: '0 9 * * 1'

# Change to: Every Tuesday at 2pm UTC
- cron: '0 14 * * 2'
```

**Cron format**: `minute hour day_of_month month day_of_week`

### Add More Sources to Monitor

Edit `source-monitoring.yml`, add new job:

```yaml
check-new-source:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - name: Check new source
      run: |
        # Your monitoring logic
```

### Ignore Certain Links

Edit `.github/link-check-config.json`:

```json
"ignorePatterns": [
  {
    "pattern": "^http://localhost"
  },
  {
    "pattern": "^https://example.com/temp"
  }
]
```

## Troubleshooting

### Workflow Not Running

**Problem**: Workflow doesn't trigger on schedule

**Solutions**:
1. Ensure workflows are on `master` branch (cron only runs on default)
2. Check repo settings: Settings → Actions → Allow all actions
3. Wait up to 1 hour after push for first scheduled run

### Too Many Issues Created

**Problem**: Issue spam from overly sensitive monitoring

**Solutions**:
1. Adjust check frequency in cron expressions
2. Add debouncing logic (only create issue if X hours since last)
3. Modify conditions in workflow (e.g., only alert on critical changes)

### Link Checker False Positives

**Problem**: Valid links marked as broken

**Solutions**:
1. Some sites block automation - add to ignorePatterns
2. Increase timeout in link-check-config.json
3. Add custom User-Agent headers for specific domains

### GitHub API Rate Limiting

**Problem**: "API rate limit exceeded" error

**Solutions**:
1. Current: 60 requests/hour (unauthenticated)
2. Workflows use built-in GITHUB_TOKEN automatically (5000 req/hour)
3. Should not hit limits with current frequency

## Integration with Existing Workflows

These workflows enhance your existing practices:

| Existing Practice | Old Cadence | New Automation | Frequency |
|-------------------|-------------|----------------|-----------|
| Anthropic blog check | Weekly | `check-anthropic-blog` job | Daily (9am UTC) |
| Awesome list review | Monthly | `check-awesome-lists` job | Daily (9am UTC) |
| Practitioner content | Bi-weekly | `check-practitioner-sources` job | Daily (9am UTC) |
| Framework updates | Quarterly | `check-practitioner-sources` job | Daily (9am UTC) |
| Self-compliance audit | After updates | Manual (triggered by issues) | As needed |
| Link maintenance | Manual | `link-checker` workflow | Daily (12am UTC) |

**Philosophy Change**: Given the fast pace of AI coding tools development, all external sources are now monitored **daily** instead of weekly/monthly/quarterly.

The workflows **create issues with pre-detected activity**, you still **do the review work**.

## Monitoring the Monitors

Check workflow health:

```bash
# View recent runs
gh run list --limit 20

# View specific workflow runs
gh run list --workflow=source-monitoring.yml

# View logs for a failed run
gh run view <run-id> --log

# Re-run failed workflows
gh run rerun <run-id>
```

## Cost Considerations

**GitHub Actions Free Tier**:
- Public repositories: Unlimited minutes
- Private repositories: 2,000 minutes/month

**Current Usage Estimate**:
- Source monitoring: ~3 minutes/week × 52 = ~156 min/year
- Link checker: ~5 minutes/week × 52 = ~260 min/year
- **Total**: ~416 minutes/year (well within free tier)

## Next Steps

1. **Commit and push** the new workflows
2. **Watch for first issues** (Monday 9am UTC for source monitoring)
3. **Triage and close** issues as you address them
4. **Tune sensitivity** if too many/few alerts
5. **Document learnings** in this file or PLAN.md

## Future Enhancements

Consider adding:

- [ ] Slack/Discord notifications for critical issues
- [ ] Dashboard visualization of source health metrics
- [ ] Automatic PR creation for simple fixes (version bumps)
- [ ] Trend analysis (star count growth, commit frequency)
- [ ] Integration with project board for automated triage

## Reference Documentation

- **Workflow Details**: `.github/workflows/README.md`
- **Review Cadence**: `PLAN.md:110-115`
- **Source Tiers**: `SOURCES.md:1207-1232`
- **Contributing Process**: `CONTRIBUTING.md:201-222`

## Questions?

If you encounter issues:
1. Check workflow logs: `gh run view <run-id> --log`
2. Review `.github/workflows/README.md` for troubleshooting
3. Validate YAML syntax online: https://www.yamllint.com/
4. Test locally with `act` (GitHub Actions local runner)

---

**Created**: February 13, 2026
**Purpose**: Automate source monitoring per SOURCES.md recommendations
**Replaces**: Manual weekly/monthly checks with automated issue creation
