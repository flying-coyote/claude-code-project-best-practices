# GitHub Actions Workflows

This directory contains automated workflows for maintaining the repository and monitoring external sources.

## Workflows

### 1. claude-code.yml
**Purpose**: Claude Code review for pull requests

**Triggers**:
- Pull requests (opened, synchronized, reopened)
- Issue comments containing `@.claude`

**What it does**:
- Runs Claude Code review on PR changes
- Uses context from CLAUDE.md, ARCHITECTURE.md, SOURCES.md
- Posts review comments

**Manual trigger**: Not available (PR/comment triggered only)

---

### 2. source-monitoring.yml
**Purpose**: Monitor external sources for updates

**Triggers**:
- Scheduled: Every Monday at 9am UTC
- Manual: Via workflow_dispatch

**Jobs**:

#### check-anthropic-releases
Monitors Claude Code releases on GitHub:
- Fetches latest release from anthropics/claude-code
- Checks if documented in SOURCES.md
- Creates issue if new release detected

#### check-awesome-lists
Monitors community curated lists:
- Checks hesreallyhim/awesome-claude-code for recent commits
- Creates issue if updates detected in last 7 days
- Tracks star count

#### check-anthropic-blog
Monitors Anthropic Engineering Blog:
- Scrapes latest blog post URL
- Checks if documented in SOURCES.md
- Creates issue for potential new posts

#### monthly-review-reminder
Creates monthly checklist:
- Runs first Monday of each month (day ≤ 7)
- Creates comprehensive review checklist
- Covers all source tiers and maintenance tasks

**Manual trigger**:
```bash
# Via GitHub UI: Actions → Source Monitoring → Run workflow
# Or via gh CLI:
gh workflow run source-monitoring.yml
```

**Configuration**:
- Requires `issues: write` permission (already configured)
- No secrets needed for public repository monitoring
- Uses GitHub API without authentication (60 req/hour limit)

---

### 3. link-checker.yml
**Purpose**: Validate all markdown links

**Triggers**:
- Scheduled: Every Sunday at midnight UTC
- Manual: Via workflow_dispatch
- Pull requests that modify .md files

**Jobs**:

#### check-links
Validates all markdown links:
- Uses `markdown-link-check` to scan all .md files
- Follows config in `.github/link-check-config.json`
- Creates issue if broken links found (scheduled runs only)
- For PRs: Fails check but doesn't create issue

#### markdown-lint
Runs markdownlint:
- Checks markdown formatting
- Uses config from `.markdownlint.jsonc`
- Comments on PR if lint fails

#### check-source-accessibility
Monitors critical Tier A sources:
- Tests HTTP accessibility of primary sources
- Focuses on Anthropic docs, GitHub Spec Kit, agentskills.io
- Creates CRITICAL issue if Tier A sources are down

**Manual trigger**:
```bash
# Via GitHub UI: Actions → Link Checker → Run workflow
# Or via gh CLI:
gh workflow run link-checker.yml
```

**Configuration**:
- Requires `issues: write` permission (already configured)
- Uses link-check-config.json for retry/timeout settings

---

## Configuration Files

### link-check-config.json
Configuration for markdown-link-check:

```json
{
  "ignorePatterns": [localhost URLs],
  "timeout": "10s",
  "retryOn429": true,
  "retryCount": 3,
  "aliveStatusCodes": [200, 203, ...]
}
```

**Key settings**:
- 10 second timeout per link
- Retries 3 times on failure
- Accepts 200-level, 300-level, and some 400-level codes (401/403 for auth-required)
- Custom User-Agent for Anthropic domains

---

## Monitoring Schedule

| Workflow | Frequency | Day/Time | Purpose |
|----------|-----------|----------|---------|
| claude-code | On-demand | PR/comment | Code review |
| source-monitoring | Weekly | Mon 9am UTC | Check updates |
| source-monitoring (monthly) | Monthly | 1st Mon | Full checklist |
| link-checker | Weekly | Sun 12am UTC | Validate links |
| link-checker (PR) | On-demand | PR with .md | Prevent broken links |

---

## Issue Labels

Workflows automatically create issues with these labels:

| Label | Meaning |
|-------|---------|
| `documentation` | Documentation-related issue |
| `source-update` | External source has updates |
| `community` | Community source (awesome lists) |
| `tier-a` | Primary authoritative source |
| `maintenance` | Routine maintenance task |
| `bug` | Something broken (links, accessibility) |
| `critical` | Urgent - affects primary sources |

---

## Manual Workflow Execution

### Via GitHub UI
1. Navigate to **Actions** tab
2. Select workflow from left sidebar
3. Click **Run workflow** button
4. Choose branch (usually `master`)
5. Click **Run workflow**

### Via GitHub CLI
```bash
# List all workflows
gh workflow list

# Run source monitoring
gh workflow run source-monitoring.yml

# Run link checker
gh workflow run link-checker.yml

# View recent runs
gh run list --workflow=source-monitoring.yml
```

---

## Troubleshooting

### Rate Limiting
If GitHub API rate limiting occurs:
- Unauthenticated: 60 requests/hour
- Authenticated: 5,000 requests/hour

**Solution**: Add `GITHUB_TOKEN` secret (already available in Actions)

### Link Checker False Positives
Some sites block automated requests:
- Add to `ignorePatterns` in link-check-config.json
- Or add custom headers in `httpHeaders` section

### Workflow Not Running
Check:
1. Workflow file syntax (YAML validation)
2. Branch is `master` (cron only runs on default branch)
3. Repository settings → Actions → Allow all actions

---

## Maintenance

### Updating Source Monitoring
To monitor additional repositories:
1. Edit `source-monitoring.yml`
2. Add new job following `check-awesome-lists` pattern
3. Use GitHub API: `https://api.github.com/repos/{owner}/{repo}`

### Updating Link Checker
To ignore additional patterns:
1. Edit `.github/link-check-config.json`
2. Add to `ignorePatterns` array
3. Use regex patterns for flexible matching

### Adding New Workflows
1. Create `.github/workflows/your-workflow.yml`
2. Follow existing patterns for issue creation
3. Use appropriate labels
4. Document in this README

---

## Integration with PLAN.md

Workflows align with review cadence in PLAN.md:110-115:

| Source Type | PLAN.md Frequency | Workflow |
|-------------|-------------------|----------|
| Anthropic Blog | Weekly | `check-anthropic-blog` (Mon) |
| awesome-claude-code | Monthly | `monthly-review-reminder` (1st Mon) |
| SDD frameworks | Quarterly | Manual review (reminder in monthly) |

---

## Security Considerations

### Secrets Required
- None currently (public repository monitoring only)

### Permissions
- `issues: write` - Create/update issues
- `contents: read` - Read repository files
- `pull-requests: write` - Comment on PRs

### External APIs Used
- GitHub API (api.github.com) - No auth for public repos
- Anthropic website (www.anthropic.com) - Public HTTP access

### Sensitive Data
- No secrets or credentials in workflows
- All monitored sources are public
- Issue creation uses public data only

---

## Future Enhancements

Potential additions (from workflow recommendations):

- [ ] Parse changelog for specific feature categories
- [ ] Track star count trends over time
- [ ] Summarize multiple new releases in single issue
- [ ] Integrate with project board for triage
- [ ] Add Slack/email notifications for critical issues
- [ ] Dashboard visualization of source health

---

**Last Updated**: February 2026
**Reference**: SOURCES.md:1119-1127 for review cadence
