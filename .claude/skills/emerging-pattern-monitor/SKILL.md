---
name: emerging-pattern-monitor
version: 1.0.0
description: Monitors EMERGING patterns and evaluates for PRODUCTION promotion
triggers:
  - "review emerging patterns"
  - "check pattern promotion"
  - "evaluate emerging"
  - "promote pattern"
auto_load: false
---

# Emerging Pattern Monitor Skill

**Purpose**: Monitor EMERGING patterns, track promotion criteria, and recommend when patterns are ready for PRODUCTION status.

**When to Use**:
- Weekly automated checks (recommended)
- Before quarterly audits
- When Anthropic blog post validates approach
- When production case study published
- User says "review emerging patterns" or similar

**What This Skill Does**:
1. Identifies all patterns marked as EMERGING
2. Evaluates against promotion criteria
3. Tracks evidence accumulation over time
4. Recommends promotion when criteria met
5. Updates TOOLS-TRACKER.md tracking
6. Creates promotion proposals

---

## Promotion Criteria

To promote from 🔬 EMERGING to ✅ PRODUCTION, pattern must achieve **all three**:

### 1. Tier A Source Validation ✅

**Requirement**: Pattern approach validated by authoritative source

**Acceptable sources**:
- ✅ Anthropic engineering blog post
- ✅ Anthropic official documentation endorsement
- ✅ Peer-reviewed research (published in ACM, USENIX, IEEE)
- ✅ OWASP or NIST standard

**Not acceptable**:
- ❌ Tier B sources alone (expert practitioners)
- ❌ Vendor whitepapers (Tier C)
- ❌ Social media discussions (Tier D)

**Verification**:
- Check SOURCES.md for Tier A attribution
- Verify URL is from anthropic.com/engineering or code.claude.com/docs
- Confirm publication date (within 2 years for relevance)

### 2. Production Validation 📊

**Requirement**: Pattern used successfully in production

**Acceptable evidence**:
- ✅ **2+ independent case studies** from different organizations, OR
- ✅ **1 Tier A case study** (Anthropic, Fortune 500, named enterprise)

**Case study quality criteria**:
- Named organization or practitioner
- Quantified outcomes (measurements, time savings, etc.)
- Duration: 30+ days production use
- Publicly verifiable (blog post, conference talk, etc.)

**Not acceptable**:
- ❌ Anonymous "I tried this and it worked" comments
- ❌ Toy projects or demos
- ❌ Single-session experiments
- ❌ Unverifiable claims

**Verification**:
- Search SOURCES.md for case study citations
- Check evidence tier (B or higher)
- Verify measurements are specific and dated

### 3. Community Maturity 🌱

**Requirement**: Pattern or framework shows stability

**For frameworks/tools**:
- ✅ Version 1.0+ released
- ✅ Active maintenance (commits/releases within 3 months)
- ✅ 100+ GitHub stars OR 10+ contributors
- ✅ Documentation exists (README with examples)

**For methodology patterns** (non-code):
- ✅ Referenced by 2+ independent sources
- ✅ Stable definition (not rapidly changing)
- ✅ Clear usage examples in SOURCES.md

**Not acceptable**:
- ❌ Pre-1.0 / beta frameworks
- ❌ Abandoned projects (no updates >6 months)
- ❌ Single-maintainer with no community
- ❌ Undocumented or example-only code

**Verification**:
- Check GitHub: stars, last commit date, contributor count
- Verify version number (>=1.0.0)
- Review documentation quality

---

## Workflow

### Phase 1: Identify EMERGING Patterns

**Search strategy**:
1. Grep patterns/ for `status: "EMERGING"`
2. Check TOOLS-TRACKER.md Re-evaluation Schedule
3. Review SOURCES.md for "EMERGING PATTERN" markers

**Expected output**:
```
EMERGING Patterns Found:
1. Reinforcement Learning from Memory (RLM)
   - File: SOURCES.md:430-454
   - Status: EMERGING since 2025-10-15
   - Next review: 2026-03-01

2. Claude-Flow multi-agent framework
   - File: patterns/framework-selection-guide.md
   - Status: EMERGING since 2025-11-20
   - Next review: 2026-02-28
```

### Phase 2: Evaluate Each Pattern

**For each EMERGING pattern, create evaluation scorecard**:

```markdown
## Pattern: Reinforcement Learning from Memory (RLM)

**Status**: 🔬 EMERGING
**First Mentioned**: 2025-10-15
**Next Review**: 2026-03-01

### Promotion Criteria Evaluation

#### 1. Tier A Source Validation
- [ ] Status: ✅ ACHIEVED
- Source: Anthropic Engineering Blog
- URL: https://www.anthropic.com/engineering/rlm-approach
- Date: 2025-11-24
- Evidence Tier: A (Primary vendor documentation)

#### 2. Production Validation
- [ ] Status: ⏸️ IN PROGRESS (1 of 2 required)
- Case Study 1:
  - Organization: ACME Corp (named in blog post)
  - Outcome: 15% reduction in repetitive errors
  - Duration: 45 days production use
  - Evidence Tier: B (Expert practitioner with public validation)
- Case Study 2: NEEDED
  - Requirement: 1 more independent case study OR 1 Tier A case study

#### 3. Community Maturity
- [ ] Status: ⏸️ IN PROGRESS
- Framework: rlm-framework v0.8.0 (pre-1.0)
- GitHub: 87 stars, 3 contributors
- Last commit: 7 days ago (active)
- Documentation: Exists, good quality
- Issue: Version not yet 1.0

### Overall Assessment

**Promotion Ready?**: ❌ NO (2 of 3 criteria met)

**Blockers**:
- Missing 1 production case study OR need Tier A case study
- Framework not yet v1.0.0

**Estimated Time to Promotion**: 1-2 months
- v1.0.0 release expected in March 2026 (per roadmap)
- 1 additional case study likely within 6 weeks (framework adoption growing)

**Recommendation**: Keep as EMERGING, review again 2026-03-15
```

### Phase 3: Update Tracking

**In TOOLS-TRACKER.md Re-evaluation Schedule**:

```markdown
| Pattern | Tier A | Production | Community | Next Review | Promotion Likely? |
|---------|--------|------------|-----------|-------------|-------------------|
| RLM | ✅ Yes | ⏸️ 1/2 | ⏸️ v0.8.0 | 2026-03-15 | Medium (waiting for v1.0) |
```

**In pattern frontmatter** (if exists):

```yaml
---
status: "EMERGING"
promotion-criteria:
  tier-a-source: true
  production-validation: 1-of-2
  community-maturity: false  # v0.8.0, need v1.0+
next-review: "2026-03-15"
blockers:
  - "Need 1 more case study OR 1 Tier A case study"
  - "Framework must reach v1.0.0"
---
```

### Phase 4: Take Action

**If promotion ready (all 3 criteria met)**:
1. Create promotion proposal (see template below)
2. Update pattern status to PRODUCTION
3. Remove EMERGING markers from documentation
4. Update TOOLS-TRACKER.md status
5. Update cross-references in related patterns
6. Document promotion in DEPRECATIONS.md (Historical Evolution section)

**If blockers exist**:
1. Document blockers clearly
2. Set next review date (1-3 months depending on blocker type)
3. Add to quarterly audit checklist
4. Monitor for triggering events (Anthropic blog post, v1.0 release, etc.)

### Phase 5: Create Report

**Generate summary for user or automation**:

```markdown
## Emerging Pattern Monitor Report

**Date**: 2026-02-16
**Patterns Evaluated**: 3
**Promoted to PRODUCTION**: 0
**Still EMERGING**: 3

### Summary

#### Reinforcement Learning from Memory (RLM)
- **Status**: Still EMERGING
- **Criteria Met**: 2 of 3 (Tier A ✅, Production ⏸️, Community ⏸️)
- **Blockers**: Need 1 more case study, framework must reach v1.0
- **Next Review**: 2026-03-15
- **Promotion Likely**: Medium (1-2 months)

#### Claude-Flow Multi-Agent Framework
- **Status**: Still EMERGING
- **Criteria Met**: 2 of 3 (Tier A ❌, Production ✅, Community ✅)
- **Blockers**: No Tier A source (only Tier B)
- **Next Review**: 2026-02-28
- **Promotion Likely**: Low (needs Anthropic validation)

#### Adaptive Swarm Topologies
- **Status**: Still EMERGING
- **Criteria Met**: 0 of 3 (all in research phase)
- **Blockers**: No production use, research-only
- **Next Review**: 2026-04-01
- **Promotion Likely**: Low (6+ months)

### Actions Taken
- Updated TOOLS-TRACKER.md re-evaluation schedule
- Set next review dates for all patterns
- Flagged Claude-Flow for Anthropic blog monitoring

### Recommendations
1. Monitor for RLM framework v1.0 release (expected March 2026)
2. Search for additional RLM case studies in March
3. Check Anthropic blog for Claude-Flow mention
4. Delay Adaptive Swarm review until production evidence exists
```

---

## Promotion Proposal Template

**When pattern meets all 3 criteria, use this template**:

```markdown
## Promotion Proposal: [Pattern Name]

**Current Status**: 🔬 EMERGING
**Proposed Status**: ✅ PRODUCTION
**Date**: [Today's date]

### Criteria Verification

#### 1. Tier A Source Validation ✅
- **Source**: [Anthropic blog post / official docs]
- **URL**: [Link]
- **Date**: [Publication date]
- **Evidence Tier**: A
- **Validation**: Pattern approach explicitly endorsed

#### 2. Production Validation ✅
- **Case Study 1**:
  - Organization: [Name]
  - Outcome: [Quantified result]
  - Duration: [Days in production]
  - Source: [URL or citation]
  - Evidence Tier: [A or B]

- **Case Study 2** (if applicable):
  - [Same format]

**Total**: 2+ case studies OR 1 Tier A case study ✅

#### 3. Community Maturity ✅
- **Framework**: [name] v[1.0+]
- **GitHub**: [stars] stars, [contributors] contributors
- **Last Commit**: [date] (within 3 months)
- **Documentation**: [Good/Excellent]
- **Status**: Stable, production-ready

### Pattern Quality Check

- [ ] Pattern file exists with clear documentation
- [ ] Examples provided
- [ ] Related patterns cross-referenced
- [ ] Evidence sources cited in SOURCES.md
- [ ] No conflicting guidance with existing PRODUCTION patterns

### Impact Analysis

**Patterns Affected**: [List related patterns]
**Documentation Updates Needed**: [List files]
**Breaking Changes**: [None / List if any]

### Proposed Changes

1. Update pattern file:
   ```yaml
   status: "PRODUCTION"  # Changed from EMERGING
   promoted-date: "2026-02-16"
   ```

2. Update TOOLS-TRACKER.md:
   - Move from EMERGING section to RECOMMENDED section
   - Update status column: 🔬 EMERGING → ✅ RECOMMENDED

3. Remove EMERGING markers from:
   - Pattern file content
   - Cross-references in related patterns
   - SOURCES.md mentions

4. Document in DEPRECATIONS.md Historical Evolution:
   ```markdown
   ### Case Study: [Pattern Name]
   **Status**: 🔬 EMERGING → ✅ RECOMMENDED
   **Timeline**: [First mention] → [Promotion date]
   **Promotion Trigger**: [What achieved final criterion]
   ```

### Approval

**Recommended by**: emerging-pattern-monitor skill
**Review Required**: Yes (human approval before promotion)

**Approver Comments**:
[Space for human reviewer to add notes]

**Decision**: [ ] APPROVE [ ] REJECT [ ] DEFER

**If DEFER, reason**:
[Explain why deferring despite criteria being met]
```

---

## Special Cases

### Rapid Promotion (Fast-Track)

**When Anthropic explicitly endorses in blog post**:
- If blog post says "we recommend X approach"
- AND provides production data from Anthropic's own use
- **Then**: Tier A source + Tier A case study = 2 of 3 criteria immediately

**Example**:
```
Anthropic blog: "We've been using RLM in production for 3 months, seeing 25% error reduction"

Result:
- Tier A source: ✅ (blog post)
- Production validation: ✅ (Tier A case study from Anthropic)
- Community maturity: Still need v1.0 framework

Promotion timeline: As soon as v1.0 releases
```

### Pattern Without Framework

**For methodology patterns (no code/framework)**:
- Community maturity criterion changes to:
  - ✅ Referenced by 2+ independent sources (Tier B or higher)
  - ✅ Stable definition (same approach in all sources)
  - ✅ Usage examples documented

**Example**: Johari Window for Ambiguity Resolution
- No framework needed (methodology pattern)
- Tier A: Anthropic blog validates approach
- Production: 2 practitioner case studies (Tier B)
- Community: Referenced in 3 articles, stable definition
- **Result**: Promote to PRODUCTION

### Downgrade from EMERGING

**If pattern becomes obsolete before promotion**:
- New approach supersedes it (e.g., native feature replaces workaround)
- Security vulnerability discovered
- Evidence disproven (benchmarks not reproducible)

**Action**:
- Change status: 🔬 EMERGING → ❌ DEPRECATED
- Document in DEPRECATIONS.md
- Remove from TOOLS-TRACKER.md active tracking
- Add historical note in pattern file

---

## Automation Integration

### Weekly Automated Check

**GitHub Actions can run this skill weekly**:

```yaml
# .github/workflows/emerging-pattern-monitor.yml
name: Emerging Pattern Monitor
on:
  schedule:
    - cron: '0 8 * * 1'  # Monday 8am UTC
  workflow_dispatch:

jobs:
  monitor:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run emerging pattern monitor
        run: |
          # Invoke skill via Claude Code CLI
          claude code --skill emerging-pattern-monitor
```

**Output**: Issue created if any pattern ready for promotion

### Anthropic Blog Integration

**When anthropic-blog-rss.yml detects new post**:
1. analyze-blog-post.py extracts pattern validation
2. If blog validates EMERGING pattern → trigger this skill
3. Update promotion criteria automatically
4. Create promotion proposal if criteria now met

---

## Related Patterns

- [Evidence Tiers](../../patterns/evidence-tiers.md) - Tier A source criteria
- [Pattern Version Updater](../pattern-version-updater/SKILL.md) - Coordinates on version requirements
- [Documentation Maintenance](../../patterns/documentation-maintenance.md) - Quarterly audit cadence

---

## Testing Checklist

**Before promoting a pattern**:
- [ ] All 3 criteria independently verified
- [ ] Source URLs accessible and correct
- [ ] GitHub metrics current (not cached)
- [ ] Pattern file quality meets standards
- [ ] Cross-references updated
- [ ] TOOLS-TRACKER.md updated
- [ ] No conflicts with existing PRODUCTION patterns
- [ ] Human reviewer approval obtained

---

## Skill Maintenance

**Update this skill when**:
- Promotion criteria change
- New evidence tier definitions added
- TOOLS-TRACKER.md structure changes
- Anthropic guidance on pattern validation changes

**Last Updated**: 2026-02-16
**Skill Version**: 1.0.0
