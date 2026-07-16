---
evidence-tier: B
convergence: single-source
applies-to-signals: [audit-always-fetch, contributing-new-analysis, revalidation-trigger, project-type-research]
last-verified: 2026-07-16
revalidate-by: 2026-10-22
status: PRODUCTION
---

# Evidence Tier System

> **Merged 2026-07-16 (Absorption Scan 2026-07 §1).** confidence-scoring.md folded in — one evidence-methodology doc instead of two. No external absorber exists for evidence-grading of AI-tooling claims; this consolidation is a reduction move, not an absorption.

**Evidence Tier**: B (methodology document — adapted from established research methodology, validated in production use across this repository; self-referential scheme)

A classification framework for source quality and claim confidence.

## Overview

This document describes the **Tier A-D** system for evaluating source quality and outputs, which is the only tier system in use, plus the HIGH/MEDIUM/LOW confidence-assessment framework merged in from confidence-scoring.md on 2026-07-16.

It previously also described a second axis, **Tier 1-5** for research evidence strength. That axis was RETIRED by owner ruling 2026-07-12 (ruling B-F7; it was never ratified); the retired-axis record was extracted 2026-07-16 to [evidence-tiers-1-5-axis-record.md](../archive/evidence-tiers-1-5-axis-record.md).

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
- **Confidence levels**: assessed HIGH/MEDIUM/LOW — see the Confidence Assessment section below for the canonical tier → confidence mapping

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

## Research Evidence Tiers (1-5) — RETIRED

> **Retired 2026-07-12 (owner ruling B-F7)**: the 1-5 claim-strength axis was never ratified; Tier A-D is the only tier system. The full retired-axis record (tier definitions and the "Using Both Systems Together" practice) was extracted 2026-07-16 to [evidence-tiers-1-5-axis-record.md](../archive/evidence-tiers-1-5-axis-record.md).

---

## Confidence Assessment (HIGH/MEDIUM/LOW) — merged 2026-07-16

Merged from confidence-scoring.md (pre-merge snapshot: [archive/confidence-scoring.md](../archive/confidence-scoring.md)). Systematic confidence assessment for hypotheses, research claims, and technical assertions — use it when formulating hypotheses, evaluating technical or vendor claims, making architectural decisions, or running publication quality checks.

### Confidence Levels

**HIGH (>80%)** — multiple independent confirmations, production validation with measured outcomes, peer-reviewed support, no significant contradictions, replicable results. Evidence floor: 2+ Tier A sources (ideal: 3+ independent sources across Tier A/B). Suitable for definitive statements ("demonstrates").

**MEDIUM (50-80%)** — sound reasoning with some empirical evidence, minor contradictions or gaps, expert opinion in support, further validation still needed. Evidence floor: 1+ Tier B source (a single strong source or several weaker ones). Use hedge words ("suggests", "indicates", "may"), acknowledge limitations, and note what validation is missing.

**LOW (<50%)** — theoretical reasoning only, limited evidence, significant contradictions, or unvalidated vendor claims; Tier C-D sources only. Label explicitly as speculation ("hypothesize", "theorize"); never present as established fact.

### Tier → Confidence Mapping (canonical)

| Evidence Tier       | Typical Confidence     | Notes                          |
|---------------------|------------------------|--------------------------------|
| **Multiple Tier A** | HIGH (>80%)            | Strongest possible evidence    |
| **Single Tier A**   | MEDIUM-HIGH (65-85%)   | Strong but needs corroboration |
| **Multiple Tier B** | MEDIUM (60-75%)        | Solid evidence, some validation |
| **Single Tier B**   | MEDIUM (50-65%)        | Adequate for cautious claims   |
| **Tier C**          | MEDIUM-LOW (40-60%)    | Supportive but not conclusive  |
| **Tier D**          | LOW (<50%)             | Speculation or unverified      |

Adjust upward when multiple independent sources agree, production validation exists, peer review confirms, no significant contradictions surface, and the methodology is replicable; adjust downward when sources conflict, only vendor claims are available, the reasoning is theoretical without empirical validation, known contradictions exist, or the methodology is not replicable.

### Documentation Format

For hypotheses:

```markdown
**Hypothesis**: [Clear, testable statement]
**Evidence**:
- [Tier X]: [Source and key finding]
**Contradictions**: [Any conflicting evidence]
**Confidence**: [HIGH/MEDIUM/LOW] ([percentage])
**Validation Status**: [What's needed to increase confidence]
```

For technical claims, state the claim, its source-quality tier (A-D), the supporting evidence, the confidence assessment, and what that confidence level is suitable for.

### Decision Thresholds

- **Architecture decisions**: require HIGH confidence (Tier A/B evidence); accept MEDIUM only when validated with a POC
- **Tool selection**: require MEDIUM minimum, verified with proof-of-concept testing
- **Best practices**: MEDIUM-LOW acceptable where industry consensus exists, validated through team experience

### Confidence Evolution

Confidence should evolve as evidence accumulates: LOW (theoretical only) → MEDIUM (after POC or early validation) → HIGH (after production deployment with measured outcomes) → HIGH, independently verified (after peer review). Match the language to the band at every stage — definitive only at HIGH, hedged at MEDIUM, labeled speculation at LOW.

### Calibration Gaps (the framework applied to itself)

- **Threshold calibration.** The HIGH >80% / MEDIUM 50-80% / LOW <50% bands are cognitive anchors, not empirically derived. **Needs**: a study correlating band assignment to outcome accuracy across a corpus of labeled claims. Without this, "HIGH" and "MEDIUM" measure reviewer calibration more than reality.
- **Tier → confidence mapping.** Mapping Tier A source quality to HIGH confidence assumes primary sources are consistently correct; Anthropic's own disclosed "eval awareness" and "self-evaluation rationalization" failure modes (see [agent-evaluation.md](agent-evaluation.md)) show that even Tier A sources can carry systematic errors. **Needs**: explicit Tier A source-reliability audit before promoting claims to HIGH.
- **Confidence inflation over time.** As a claim accumulates citations, confidence scores drift upward (citation cascades), and this framework has no mechanism to detect or correct the inflation. **Needs**: periodic downward-revalidation where highly-confident claims are deliberately stress-tested against counter-evidence.

These gaps don't invalidate the framework — they are the framework applied to itself. See [session-quality-tools.md](../archive/session-quality-tools.md) (archived 2026-07-10) for an exemplar of full gap-statement usage.

---

## Integration with Skills

### academic-citation-manager
- Validates evidence tiers in claims
- Flags unsupported assertions
- Suggests appropriate tier for sources
- Maps evidence tiers to confidence levels and suggests appropriate confidence language

### publication-quality-checker
- Requires Tier A-B for strong claims
- Warns on Tier C without corroboration
- Blocks Tier D presented as fact
- Validates confidence levels match evidence; ensures hedge words on MEDIUM/LOW claims

### hypothesis-validator
- Tracks evidence tier per hypothesis
- Requires higher tier for validation
- Distinguishes speculation from evidence
- Assigns HIGH/MEDIUM/LOW confidence and tracks its evolution over time

### research-extractor
- Classifies extracted claims by confidence
- Links evidence to confidence assessment
- Documents validation gaps

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
**Problem**: Accepting vendor whitepapers (Tier C) at face value
**Symptom**: Overstated benefits, surprise limitations in production
**Solution**: Treat vendor claims as hypotheses; validate with POC or independent benchmark

### ❌ Confidence Exceeding Evidence
**Problem**: Claiming HIGH confidence on Tier C-D sources, or using definitive language on MEDIUM-confidence claims
**Symptom**: Hedge-free assertions that later reverse under scrutiny
**Solution**: Match language to the confidence band — definitive only at HIGH, hedged at MEDIUM, labeled speculation at LOW; update the band as evidence evolves

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
| **Model capabilities** | 6 months (after new model release) | Test with new model | "Opus 4.6 handles X well" — re-test on 4.7 given literal-interpretation shift |
| **Prompt-interpretation behavior** | Any new model release | Side-by-side output diff on new model | "Agent infers edge cases from 'handle corner cases'" — 4.7 changed this (see [model-migration-anti-patterns.md](model-migration-anti-patterns.md)) |

#### Expiry Date Citation Format

```markdown
**Claim with Expiry**
- Measurement: "Memory Tool + Context Editing: 39% improvement in agent search"
- Source: Anthropic internal testing (Tier A)
- Date: November 24, 2025
- Revalidate: November 24, 2026
- Context: Tested with Opus 4.6. Opus 4.7 (April 2026) shifted prompt interpretation toward literalism — re-test before citing on 4.7+.
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
- Status: Chrome extension deprecated 2026-01-10 (historical ledger: archive/docs-v1/DEPRECATIONS.md)
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

**Track via the `emerging-pattern-monitor` skill**, which reviews EMERGING docs against these promotion criteria quarterly (the docs-v1 TOOLS-TRACKER.md that held the re-evaluation schedule was removed in the 2026-07 reduction).

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
| **Breaking change** | "Deprecated in v3.0.0" | Banner in the affected doc (historical ledger: `archive/docs-v1/DEPRECATIONS.md`) |
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

This enables automated expiry checking via `scripts/check-measurement-expiry.py`, which scans `analysis/` frontmatter and exits non-zero on any claim past its `revalidate:` date.

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

**Record the deprecation in the affected doc (banner) and log the decision in DECISIONS.md** — the standalone DEPRECATIONS.md ledger was retired with docs-v1 in the 2026-07 reduction (historical record: `archive/docs-v1/DEPRECATIONS.md`). Each record needs:
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

**Automated Tracking** (via `scripts/check-measurement-expiry.py`, run locally or wired into CI):
- Scans `analysis/` doc frontmatter for `measurement-claims` entries with `revalidate:` dates
- Fails (exit 1) on expired claims and warns on claims expiring within 30 days
- `--create-issue` emits an issue body a GitHub workflow can post
- (The former `tools-evolution-tracker.yml` daily workflow served the archived docs-v1 TOOLS-TRACKER and was removed in the 2026-07 reduction)

**Manual Editorial Control**:
- Promotion decisions (EMERGING → RECOMMENDED)
- Evidence tier assignment for new sources
- Deprecation decisions and grace periods
- Measurement re-validation interpretation

**Key Principle**: Automation structures information; humans make decisions.

---

### Quarterly Audit Checklist

**Review Rapid Evolution Tracking**:
- [ ] Review all EMERGING patterns for promotion eligibility
- [ ] Run `scripts/check-measurement-expiry.py` — no measurement claims past expiry without re-validation
- [ ] Check DECISIONS.md for deprecation decisions whose grace periods have lapsed (docs pending archival)
- [ ] Audit version-requirements in patterns vs current Claude Code version
- [ ] Review any expiry issues emitted by `check-measurement-expiry.py --create-issue` last quarter
- [ ] Update SOURCES.md with any missed Anthropic blog posts

---

## Related Patterns

- [Context Engineering](./behavioral-insights.md) - Correctness over compression
- [Documentation Maintenance](../archive/patterns-v1/documentation-maintenance.md) - Keeping docs current in fast-moving projects

---

## Sources

- Framework adapted from established research methodology (literature review best practices)
- Tier 1-5 system based on evidence-based medicine hierarchies (axis retired 2026-07-12; record at [evidence-tiers-1-5-axis-record.md](../archive/evidence-tiers-1-5-axis-record.md))
- Production validation across 12+ documentation projects
- Confidence framework (merged 2026-07-16 from confidence-scoring.md): synthesis methodology validated in cybersecurity research projects; internal evidence cross-refs [agent-evaluation.md](agent-evaluation.md) (Tier A — eval-awareness failure modes cited in the calibration gaps) and [session-quality-tools.md](../archive/session-quality-tools.md) (archived gap-statement exemplar)

**Evidence Tier**: B (Adapted from peer-reviewed methodology frameworks)

*Last updated: 2026-07-16 (confidence-scoring merge + retired-axis extraction + dead-reference prune)*

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/model-migration-anti-patterns.md`](analysis/model-migration-anti-patterns.md) [EXTRACTED (1.00)] — references
- [`analysis/CANONICAL-DOC-TEMPLATE.md`](analysis/CANONICAL-DOC-TEMPLATE.md) [EXTRACTED (1.00)] — references
- [`analysis/agent-evaluation.md`](analysis/agent-evaluation.md) [EXTRACTED (1.00)] — references

<!-- graphify-footer:end -->
