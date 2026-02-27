# Quarterly Review Process

**Purpose**: Systematic maintenance to prevent outdated claims, expired revalidation dates, and documentation drift.

**Schedule**: Q1 (Mar 31), Q2 (Jun 30), Q3 (Sep 30), Q4 (Dec 31)

**Owner**: Maintenance team (see CONTRIBUTING.md)

---

## Review Checklist

### 1. Revalidation Dates (30 minutes)

**Check for expiring or expired measurement claims:**

```bash
# Find all revalidation dates
grep -r "revalidate:" patterns/*.md

# Find claims expiring in next 90 days (manual review)
# Flag any past due dates
```

**Actions**:
- [ ] Review all claims with revalidation dates within 90 days
- [ ] For expired claims: revalidate with original source or update
- [ ] Update `revalidate:` date if claim still valid
- [ ] Remove or update claim if no longer accurate
- [ ] Document any significant changes in CHANGES.md

**Current critical dates** (as of 2026-02-27):
- ⚠️ **2026-03-20**: OWASP MCP security claims (43% vuln rate, ~10 trustworthy)
- 2026-10-15: MCP baseline latency claims
- 2026-11-24: Advanced tool use measurement claims

---

### 2. Version Requirements (20 minutes)

**Update VERSION-TRACKING.md with current releases:**

```bash
# Check Anthropic changelog for new releases
open https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md

# Check model releases
open https://www.anthropic.com/changelog
```

**Actions**:
- [ ] Update "Current Versions" in VERSION-TRACKING.md
- [ ] Check beta header status (advanced-tool-use, 1M context)
- [ ] Document any graduated features
- [ ] Flag patterns with outdated version requirements
- [ ] Add `version-last-verified` to patterns if missing

**Files to update**:
- VERSION-TRACKING.md
- patterns/ (frontmatter `version-requirements` and `version-last-verified`)

---

### 3. Source Freshness (30 minutes)

**Refresh GitHub star counts and check source validity:**

```bash
# Find star count references
grep -r "Stars.*as of" SOURCES.md

# Check for broken links (use link checker or manual spot check)
```

**Actions**:
- [ ] Update star counts for repositories in SOURCES.md
- [ ] Flag star counts older than 3 months
- [ ] Spot-check 10-15 source URLs for accessibility
- [ ] Remove or flag broken/deprecated sources
- [ ] Document source changes in CHANGES.md

**Star count refresh targets**:
- shanraisshan/claude-code-best-practice (currently 5.6k+ as of Feb 2026)
- obra/superpowers
- Other Tier B/C sources with documented star counts

---

### 4. EMERGING Pattern Promotion (40 minutes)

**Evaluate EMERGING patterns for promotion to PRODUCTION:**

**Current EMERGING patterns**:
1. mcp-daily-essentials.md (90-day review: May 27, 2026)
2. productivity-tooling.md (90-day review: May 27, 2026)

**Actions for each EMERGING pattern**:
- [ ] Check if 90-day review milestone reached
- [ ] Count independent validations (need 3-5 depending on pattern)
- [ ] Review for negative reports in issues/discussions
- [ ] Verify measurement claims still accurate
- [ ] Check if ecosystem has shifted significantly

**Promotion decision**:
- **Promote to PRODUCTION** if criteria met: Update status, remove maturity notice
- **Keep EMERGING** if needs more validation: Extend 90-day milestone
- **Mark DEPRECATED** if superseded: Add to DEPRECATIONS.md, migrate

---

### 5. Deprecation Cross-Check (20 minutes)

**Ensure deprecated tools/patterns aren't still recommended:**

```bash
# Get list of deprecated items
grep "Status: ❌ DEPRECATED" DEPRECATIONS.md

# Check if they appear in pattern recommendations
# (Manual search for each deprecated item)
```

**Actions**:
- [ ] Review DEPRECATIONS.md active deprecations
- [ ] Search patterns/ for references to deprecated items
- [ ] Ensure deprecation notices appear where referenced
- [ ] Verify migration paths documented
- [ ] Check if grace periods expired (remove references)

**Current deprecations** (as of 2026-02-27):
- `/commit-push-pr` slash command (deprecated 2026-01-31)
- Claude in Chrome (deprecated 2026-01-10, grace period ends 2026-04-10)

---

### 6. Beta Header Status (15 minutes)

**Check if beta features graduated or have updated headers:**

```bash
# Find beta header references
grep -r "beta-header\|Beta Header" patterns/*.md
```

**Actions**:
- [ ] Review VERSION-TRACKING.md beta header table
- [ ] Check Anthropic changelog for graduation announcements
- [ ] Update pattern status if feature graduated from beta
- [ ] Update beta header if newer version available
- [ ] Flag beta headers older than 6 months for investigation

**Current beta headers to check**:
- `advanced-tool-use-2025-11-20` (3+ months old)
- `context-1m-2025-08-07` (6+ months old)

---

### 7. DOGFOODING-GAPS Audit (30 minutes)

**Check if we're following our own recommendations:**

```bash
# Review current gaps
cat DOGFOODING-GAPS.md
```

**Actions**:
- [ ] Review documented gaps in DOGFOODING-GAPS.md
- [ ] Check if any gaps have been resolved
- [ ] Add new gaps identified during review
- [ ] Flag patterns we document but don't implement
- [ ] Prioritize top 3 gaps for next quarter

---

### 8. Pattern Verification Dates (10 minutes)

**Update last-verified dates on reviewed patterns:**

```bash
# Patterns should have last-verified within 3 months
grep -r "last-verified:" patterns/*.md | sort
```

**Actions**:
- [ ] Update `last-verified` date on all reviewed patterns
- [ ] Flag patterns not reviewed in 6+ months
- [ ] Prioritize old patterns for deep review next quarter

---

## Post-Review Actions

### 1. Update Documentation (15 minutes)

**Files to update after review**:
- [ ] VERSION-TRACKING.md (versions, beta headers)
- [ ] SOURCES.md (star counts, source changes)
- [ ] DOGFOODING-GAPS.md (new gaps, resolved gaps)
- [ ] DEPRECATIONS.md (new deprecations if any)
- [ ] This file (QUARTERLY-REVIEW.md) - update next review date

### 2. Create Summary Report (20 minutes)

**Document review findings**:

```bash
# Create quarterly review report
cp AUDIT-2026-02-27.md QUARTERLY-REVIEW-2026-Q1.md
# Edit to summarize findings
```

**Report sections**:
1. **Summary**: Findings overview (critical, high, medium, low)
2. **Actions Taken**: What was updated/fixed
3. **Deferred Items**: What needs follow-up
4. **Next Quarter Priorities**: Focus areas for next review

### 3. Commit and Push (5 minutes)

```bash
# Stage all changes
git add -A

# Commit with clear message
git commit -m "📊 Q[N] 202[Y] quarterly review: [brief summary]

- Updated VERSION-TRACKING.md (current: v2.X.Y)
- Refreshed source star counts
- [other key updates]

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

# Push to repository
git push origin master
```

---

## Time Budget

**Total time**: ~3.5 hours per quarter

| Task | Time | Priority |
|------|------|----------|
| Revalidation dates | 30 min | 🔴 Critical |
| Version requirements | 20 min | 🔴 Critical |
| Source freshness | 30 min | 🟡 High |
| EMERGING promotion | 40 min | 🟡 High |
| Deprecation check | 20 min | 🟡 High |
| Beta header status | 15 min | 🟠 Medium |
| Dogfooding audit | 30 min | 🟠 Medium |
| Pattern verification | 10 min | 🟠 Medium |
| Documentation update | 15 min | — |
| Summary report | 20 min | — |
| Commit/push | 5 min | — |

**Optimization**: Can parallelize source freshness and version checks.

---

## Review Schedule

### 2026 Schedule

| Quarter | Due Date | Status | Completed |
|---------|----------|--------|-----------|
| **Q1** | Mar 31, 2026 | ⏰ Upcoming | — |
| **Q2** | Jun 30, 2026 | Scheduled | — |
| **Q3** | Sep 30, 2026 | Scheduled | — |
| **Q4** | Dec 31, 2026 | Scheduled | — |

### Calendar Integration

**Add to calendar**:
- Q1 review: March 25-31, 2026
- Q2 review: June 24-30, 2026
- Q3 review: September 24-30, 2026
- Q4 review: December 24-31, 2026

**Reminder**: Set calendar reminder 7 days before each deadline.

---

## Ad-Hoc Reviews

**Trigger ad-hoc review for**:
1. **Major Claude Code release** (e.g., v2.2.0, v3.0.0)
2. **New model release** (e.g., Opus 4.7)
3. **Security advisory** affecting MCP or Claude Code
4. **Community-reported outdated claims** (via issues/discussions)
5. **Deprecation announcement** from Anthropic

**Process**: Run relevant sections of this checklist, not full review.

---

## Automation Opportunities

**Future improvements**:
1. **Revalidation date monitoring**: GitHub Action to flag expiring claims (30-day warning)
2. **Star count refresh**: Automated via GitHub API
3. **Link validation**: Weekly CI check for broken URLs
4. **Version tracking**: Alert on new Anthropic releases
5. **Beta header detection**: Scrape changelog for graduation announcements

**Tracked in**: ARCHITECTURE.md under "Future Enhancements"

---

## Related Documentation

- [VERSION-TRACKING.md](VERSION-TRACKING.md) - Current versions and beta headers
- [DOGFOODING-GAPS.md](DOGFOODING-GAPS.md) - Self-compliance tracking
- [DEPRECATIONS.md](DEPRECATIONS.md) - Deprecated patterns and migration paths
- [AUDIT-2026-02-27.md](AUDIT-2026-02-27.md) - Initial audit that prompted this process
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines

---

*Process established: February 27, 2026*
*Next review: March 31, 2026 (Q1 2026)*
