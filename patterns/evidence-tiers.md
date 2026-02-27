# Evidence Tier System

A classification framework for source quality and claim confidence.

## Overview

This document describes two complementary classification systems:
- **Tier A-D**: For evaluating source quality and outputs
- **Tier 1-5**: For evaluating research evidence strength

Use both systems together for comprehensive evidence assessment.

---

## Source Quality Tiers (A-D)

### Tier A: Primary Sources
- **What**: Direct observation, production data, official documentation
- **Examples**:
  - Anthropic's own engineering blog posts
  - Your own production implementation results
  - Official vendor documentation
  - Published specifications (RFC, IEEE, NIST)
- **Weight**: Strongest evidence - suitable for definitive claims

### Tier B: Peer-Reviewed & Expert
- **What**: Academic publications, expert interviews, validated analyses
- **Examples**:
  - Peer-reviewed academic papers
  - Expert interviews with named sources
  - Conference proceedings (USENIX, IEEE S&P)
  - Industry certifications and audits
- **Weight**: Strong evidence - suitable for confident claims

### Tier C: Industry & Analysis
- **What**: Industry reports, vendor documentation, analysis pieces
- **Examples**:
  - Gartner/Forrester reports
  - Vendor whitepapers (treated with skepticism)
  - Industry blog posts from practitioners
  - Community best practices
- **Weight**: Supporting evidence - should be corroborated

### Tier D: Opinions & Speculation
- **What**: Personal opinions, speculative analysis, unverified claims
- **Examples**:
  - Social media discussions
  - Unattributed claims
  - Theoretical projections
  - Your own speculation
- **Weight**: Context only - not suitable for definitive claims

## Usage Guidelines

### For Publication
- **Strong claims**: Require Tier A or B evidence
- **Opinions**: Can use Tier C with attribution
- **Speculation**: Must be clearly labeled as such
- **Never**: Present Tier D as fact

### For Research
- **Hypothesis formation**: Any tier can inspire hypotheses
- **Hypothesis validation**: Requires Tier A or B
- **Confidence levels**:
  - High (5): Multiple Tier A sources
  - Medium (3-4): Tier B sources
  - Low (1-2): Tier C or single source

### For Decision Making
- **Architectural decisions**: Tier A or B required
- **Tool selection**: Tier B acceptable, verify with POC
- **Best practices**: Tier C acceptable if consensus exists

## Citation Format

```markdown
**Claim** (Tier X - Source Type)
Source: [Name/Title]
URL: [if applicable]
Date: [when published/accessed]
```

Example:
```markdown
**Tool Search Tool reduces context by 85%** (Tier A - Primary Source)
Source: Anthropic Developer Blog
URL: https://www.anthropic.com/engineering/...
Date: November 24, 2025
```

## Contradiction Handling

When sources conflict:
1. **Note the contradiction** - Document both positions
2. **Evaluate tier quality** - Higher tier takes precedence
3. **Seek resolution** - Look for additional sources
4. **Be transparent** - Acknowledge uncertainty in your claims

Example:
> "Vendor X claims 10x performance improvement (Tier C), while independent benchmark shows 3x (Tier B). The conservative estimate is more reliable."

---

## Research Evidence Tiers (1-5)

Used for hypothesis validation and research claim assessment. Complements the A-D system with focus on empirical validation.

### Tier 1: Production Deployments with Measured Outcomes
- **What**: Real-world deployments with quantified results
- **Examples**:
  - "DuckDB reduced query time from 45s to 2s in our SOC"
  - "Iceberg table format handles 500M events/day in production"
  - Published case studies with named organizations and metrics
- **Confidence**: Highest - suitable for strong claims
- **Validation**: Independently verifiable, replicable

### Tier 2: Peer-Reviewed Research with Replication
- **What**: Academic research validated through peer review
- **Examples**:
  - Published papers in USENIX, IEEE S&P, ACM conferences
  - Studies with reproducible methodology and datasets
  - Meta-analyses synthesizing multiple studies
- **Confidence**: High - suitable for confident claims
- **Validation**: Peer-reviewed, methodology documented

### Tier 3: Expert Consensus with Documented Reasoning
- **What**: Agreement among recognized domain experts
- **Examples**:
  - Technical talks at industry conferences (e.g., DataBricks Summit)
  - Expert interviews with transparent reasoning
  - Industry standards bodies (NIST, ISO) recommendations
- **Confidence**: Medium - requires corroboration
- **Validation**: Expert credentials verifiable, reasoning documented

### Tier 4: Vendor Claims or Theoretical Assertions
- **What**: Vendor marketing, theoretical models without validation
- **Examples**:
  - Vendor whitepapers claiming performance improvements
  - Theoretical projections without production data
  - Blog posts from vendors promoting their products
- **Confidence**: Low - treat with skepticism
- **Validation**: Requires independent verification

### Tier 5: Speculation Without Supporting Data
- **What**: Opinions, predictions, unverified claims
- **Examples**:
  - Social media discussions and hot takes
  - Unattributed claims ("many users report...")
  - Personal speculation without evidence
- **Confidence**: Minimal - context only, never cite as fact
- **Validation**: Not suitable for validation

---

## Using Both Systems Together

### For Academic/Research Content
Use **Tier 1-5** for hypothesis validation and research claims:

```markdown
**Hypothesis**: DuckDB outperforms Spark for sub-1GB security datasets

**Evidence**:
- Tier 1: Production deployment at ACME Corp (2s vs 45s query time)
- Tier 2: Benchmark study published at VLDB 2024
- Tier 3: Jake Thomas (DuckDB creator) confirms architecture advantages

**Confidence**: High (multiple Tier 1-2 sources)
```

### For Project Documentation and Outputs
Use **Tier A-D** for source citations:

```markdown
**Tool Search reduces context usage by 85%** (Tier A - Primary Source)
Source: Anthropic Engineering Blog
Date: November 24, 2024
```

### Combined Assessment Example

```markdown
**Claim**: Iceberg table format is superior for security data lakes

**Source Quality** (A-D):
- Tier A: Apache Iceberg official documentation
- Tier B: Ryan Blue (creator) technical talks

**Research Evidence** (1-5):
- Tier 1: Netflix production deployment (500M events/day)
- Tier 2: Benchmark comparison study (IEEE 2024)
- Tier 3: Industry consensus at Data+AI Summit

**Overall Assessment**: Strong claim with Tier A sources and Tier 1-2 evidence
```

---

## Integration with Skills

### academic-citation-manager
- Validates evidence tiers in claims
- Flags unsupported assertions
- Suggests appropriate tier for sources

### publication-quality-checker
- Requires Tier A-B for strong claims
- Warns on Tier C without corroboration
- Blocks Tier D presented as fact

### hypothesis-validator
- Tracks evidence tier per hypothesis
- Requires higher tier for validation
- Distinguishes speculation from evidence

---

## Anti-Patterns

### ❌ Tier D Presented as Fact
**Problem**: Citing speculation, social media, or personal opinions as authoritative
**Symptom**: Unfounded claims in publications, damaged credibility
**Solution**: Always label Tier D as speculation; never present as established fact

### ❌ Single-Source Strong Claims
**Problem**: Making definitive assertions based on one source
**Symptom**: Claims that fail under scrutiny, cherry-picked evidence
**Solution**: Require Tier A-B evidence for strong claims; corroborate Tier C

### ❌ Ignoring Contradictions
**Problem**: Dismissing conflicting evidence that challenges preferred conclusion
**Symptom**: Biased analysis, missed nuance, intellectual dishonesty
**Solution**: Document contradictions explicitly; favor higher tier when sources conflict

### ❌ Vendor Claims Without Validation
**Problem**: Accepting vendor whitepapers (Tier C/4) at face value
**Symptom**: Overstated benefits, surprise limitations in production
**Solution**: Treat vendor claims as hypotheses; validate with POC or independent benchmark

---

## Evidence Tiers for Rapidly Evolving Topics

AI tooling, model capabilities, and ecosystem tools evolve rapidly. This section extends the evidence tier system with temporal considerations for fast-moving technology domains.

### The Challenge: Time-Bound Truth

In rapidly evolving fields, yesterday's Tier A truth becomes today's outdated claim:
- Model improvements change performance benchmarks every 6 months
- Tool recommendations become obsolete with new releases
- Security vulnerabilities emerge in previously-trusted dependencies
- Feature availability depends on specific version requirements

**Core Principle**: Evidence tiers remain, but claims acquire expiry dates based on category.

---

### Tier A with Expiry Dates

Even primary sources require re-validation for time-sensitive claims.

#### Measurement Expiry Guidelines

| Claim Type | Expiry Period | Re-validation Method | Example |
|------------|---------------|----------------------|---------|
| **Performance benchmarks** | 1 year | Re-run with current version | "85% token reduction" |
| **Feature availability** | Until next major version | Verify in latest release notes | "Requires v2.1.30+" |
| **Security audit results** | 6 months | Check for new CVEs/advisories | "43% of MCP servers vulnerable" |
| **Cost comparisons** | 6 months | Verify current pricing | "4x more cost-effective" |
| **Model capabilities** | 6 months (after new model release) | Test with new model | "Opus 4.6 handles X well" |

#### Expiry Date Citation Format

```markdown
**Claim with Expiry**
- Measurement: "Memory Tool + Context Editing: 39% improvement in agent search"
- Source: Anthropic internal testing (Tier A)
- Date: November 24, 2025
- Revalidate: November 24, 2026
- Context: Tested with Opus 4.6, may change with Opus 5.0
```

#### When Measurements Expire

**Expired but not invalid**: Claims past expiry date should be:
1. **Flagged**: Mark with ⚠️ NEEDS REVALIDATION
2. **Preserved**: Keep historical measurement with date
3. **Updated**: Add new measurement when available
4. **Contextualized**: Explain if/how result changed

Example:
```markdown
**Historical Measurement** (⚠️ NEEDS REVALIDATION - Expired 2026-01-15):
- Original claim: "Playwright 4x more token-efficient than Chrome extension"
- Tested: December 2025 with Opus 4.5
- Status: Chrome extension deprecated 2026-01-10 (see DEPRECATIONS.md)
- Current: Playwright now sole recommendation (no comparison needed)
```

---

### EMERGING PATTERN Status

For patterns without Tier A/B validation, use EMERGING status with explicit promotion criteria.

#### When to Mark as EMERGING

Use 🔬 EMERGING status when:
- No Tier A source validates approach (yet)
- No production case studies exist (yet)
- Community/framework still in development (<1.0 version)
- Pattern shows promise but requires validation

**Critical**: EMERGING ≠ RECOMMENDED. Don't adopt EMERGING patterns in production without explicit risk acceptance.

#### Promotion Criteria

To promote from 🔬 EMERGING to ✅ RECOMMENDED, pattern must achieve:

1. **Tier A Source Validation**
   - Anthropic blog post validates approach, OR
   - Official documentation endorses pattern, OR
   - Peer-reviewed research confirms effectiveness

2. **Production Validation**
   - 2+ independent case studies, OR
   - 1 Tier A case study (Anthropic, major enterprise), OR
   - 6+ months production use with documented outcomes

3. **Community Maturity** (for frameworks/tools)
   - Version 1.0+ released
   - Active maintenance (commits within 3 months)
   - 100+ GitHub stars (or equivalent community signal)

#### EMERGING Pattern Tracking

**Document in pattern file**:
```yaml
---
status: EMERGING
promotion-criteria:
  tier-a-source: false  # Waiting for Anthropic blog post
  production-validation: 1-of-2  # Have 1 case study, need 1 more
  community-maturity: true  # Framework v1.2.0, active maintenance
next-review: 2026-03-01
---
```

**Track in TOOLS-TRACKER.md**:
- EMERGING patterns appear in Re-evaluation Schedule section
- Quarterly review against promotion criteria
- Automated monitoring via `emerging-pattern-monitor` skill

#### Example: Reinforcement Learning from Memory (RLM)

**Current Status** (2026-02-16): 🔬 EMERGING

**Promotion Tracking**:
- ✅ Tier A Source: Anthropic blog validated concept (2025-11-01)
- ⏸️ Production Validation: 1 of 2 required case studies
- ⏸️ Community Maturity: Framework in development, no 1.0 release
- **Next Review**: 2026-03-01
- **Promotion Likely?**: Medium (needs 1 more case study OR 1.0 release)

---

### Version-Aware Citations

Technical claims often depend on specific versions. Include version context in citations.

#### Version Citation Format

```markdown
**Feature: Session Memory across projects**
- Availability: Claude Code v2.1.30+
- Model: Any (not model-specific)
- Source: Anthropic release notes (Tier A)
- Date: January 15, 2026
- Breaking changes: None
```

#### Version Dependency Types

| Dependency Type | Example | Tracking Method |
|-----------------|---------|-----------------|
| **Minimum version** | "Requires v2.1.30+" | List in pattern frontmatter |
| **Model-specific** | "Opus 4.6+ only" | Document model requirement |
| **Breaking change** | "Deprecated in v3.0.0" | See DEPRECATIONS.md |
| **Feature flag** | "Enable with --flag" | Document in usage section |

#### Pattern Frontmatter for Version Tracking

**Every pattern should include**:
```yaml
---
version-requirements:
  claude-code: "v2.1.30+"  # Optional: only if version-specific
  model: "Opus 4.6+"       # Optional: only if model-specific
version-last-verified: "2026-02-27"
measurement-claims:
  - claim: "39% improvement in agent search"
    source: "Anthropic internal testing"
    date: "2025-11-24"
    revalidate: "2026-11-24"
status: "PRODUCTION"  # or EMERGING, DEPRECATED
last-verified: "2026-02-16"
---
```

This enables automated tracking via `scripts/generate-tools-tracker.py`.

---

### Handling Rapid Deprecation

Fast-moving ecosystems require explicit deprecation processes.

#### Deprecation Triggers

**Immediate deprecation** (0-day grace period):
- Critical security vulnerability discovered
- Official vendor deprecation notice
- Data integrity or safety issue

**Standard deprecation** (90-day grace period):
- Better alternative available (>2x performance improvement)
- Official guidance contradicts current pattern
- Tool/framework abandoned (no updates >1 year)

#### Deprecation Documentation

**Required in DEPRECATIONS.md**:
1. What was deprecated and when
2. Why it was deprecated (with evidence tier)
3. Migration path to recommended alternative
4. Affected pattern files
5. Grace period and removal date

Example:
```markdown
### `/commit-push-pr` Slash Command

**Status**: ❌ DEPRECATED
**Deprecated Date**: 2026-01-31
**Reason**: Natural language git operations in Opus 4.6 handle complex git workflows
**Evidence**: Anthropic guidance (Tier A) - "Avoid complex slash command lists"
**Migration**: Use natural language: "commit and push my changes, then create a PR"
**Grace Period**: 90 days (removal: 2026-05-01)
```

---

### Integration with Automation

**Automated Tracking** (via `.github/workflows/tools-evolution-tracker.yml`):
- Daily parsing of patterns for version requirements
- Extraction of measurement claims with expiry dates
- Flagging expired claims for re-validation
- Monitoring EMERGING patterns for promotion

**Manual Editorial Control**:
- Promotion decisions (EMERGING → RECOMMENDED)
- Evidence tier assignment for new sources
- Deprecation decisions and grace periods
- Measurement re-validation interpretation

**Key Principle**: Automation structures information; humans make decisions.

---

### Quarterly Audit Checklist

**Review Rapid Evolution Tracking** (see DOGFOODING-GAPS.md):
- [ ] Review all EMERGING patterns for promotion eligibility
- [ ] Verify no measurement claims past expiry without re-validation
- [ ] Check DEPRECATIONS.md for patterns to archive
- [ ] Audit version-requirements in patterns vs current Claude Code version
- [ ] Review automation-generated issues from last quarter
- [ ] Update SOURCES.md with any missed Anthropic blog posts
- [ ] Verify TOOLS-TRACKER.md accuracy against manual review

---

## Related Patterns

- [Agent Principles](./agent-principles.md) - Production AI reliability principles
- [Context Engineering](./context-engineering.md) - Correctness over compression
- [Documentation Maintenance](./documentation-maintenance.md) - Keeping docs current in fast-moving projects

---

## Sources

- Framework adapted from established research methodology (literature review best practices)
- Tier 1-5 system based on evidence-based medicine hierarchies
- Production validation across 12+ documentation projects

**Evidence Tier**: B (Adapted from peer-reviewed methodology frameworks)

*Last updated: January 2026*
