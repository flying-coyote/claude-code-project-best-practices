---
evidence-tier: B
convergence: single-source
applies-to-signals: [audit-always-fetch, revalidation-trigger]
last-verified: 2026-04-22
revalidate-by: 2026-10-22
status: ARCHIVED
---

# Confidence Scoring for Research and Hypotheses

> **MERGED INTO evidence-tiers.md (2026-07-16, Absorption wave Phase 3).** One evidence-methodology doc instead of two. This copy is the pre-merge snapshot, kept for history.

**Source**: Production-validated pattern from research projects
**Evidence Tier**: B (Validated in cybersecurity research projects)

## Purpose

Systematically assess confidence levels for hypotheses, research claims, and technical assertions using evidence-based scoring.

## When to Use

- Formulating research hypotheses
- Evaluating technical claims
- Making architectural decisions
- Assessing vendor assertions
- Publication quality checks

---

## Confidence Levels

### High Confidence (>80%)

**Criteria**:
- Multiple independent confirmations
- Production validation with measured outcomes
- Peer-reviewed research supporting claim
- No significant contradictions
- Replicable results

**Evidence Requirements**:
- Minimum: 2+ Tier A sources
- Ideal: 3+ independent sources across Tier A/B

**Example**:
```markdown
**Hypothesis**: DuckDB outperforms Spark for sub-1GB datasets

**Evidence**:
- Tier A: Production deployment (45s → 2s query time)
- Tier A: Independent benchmark run (10x faster for small datasets)
- Tier B: Published VLDB paper confirming architecture advantage
- Tier B: Creator (DuckDB team) confirms design intent

**Contradictions**: None found
**Confidence**: HIGH (>80%)
```

### Medium Confidence (50-80%)

**Criteria**:
- Sound logical reasoning
- Some empirical evidence
- Minor contradictions or gaps
- Expert opinion supports claim
- Needs additional validation

**Evidence Requirements**:
- Minimum: 1+ Tier B sources
- Acceptable: Single strong source or multiple weaker sources

**Example**:
```markdown
**Hypothesis**: Iceberg table format reduces storage costs 30-50%

**Evidence**:
- Tier B: Conference talk from Netflix (claims 40% reduction)
- Tier C: Vendor whitepaper (claims 30-50% range)
- Tier C: Community blog posts (anecdotal reports)

**Contradictions**: Vendor claims vary (30-70% range)
**Confidence**: MEDIUM (50-80%)
**Needs**: Independent benchmark or production case study
```

### Low Confidence (<50%)

**Criteria**:
- Theoretical reasoning only
- Limited supporting evidence
- Significant contradictions exist
- Vendor claims without validation
- Substantial validation needed

**Evidence Requirements**:
- Tier C-D sources only
- Speculation or unverified assertions

**Example**:
```markdown
**Hypothesis**: AI-based SIEM will replace rule-based detection

**Evidence**:
- Tier C: Vendor marketing claims
- Tier D: Industry speculation and unattributed blog posts
- Tier D: Social media discussions

**Contradictions**:
- Experts warn against "AI washing"
- Production deployments still use rules
- False positive rates problematic

**Confidence**: LOW (<50%)
**Status**: Speculative - requires production validation
```

---

## Integration with Evidence Tiers

**Retired axis (owner ruling 2026-07-12)**: earlier revisions of this doc scored evidence on two axes, source quality (Tier A-D) and a separate 1-5 research-evidence scale. The 1-5 axis is retired because it was never ratified; Tier A-D is the only tier system, and the mappings and examples in this doc now read on A-D alone.

### Mapping Evidence to Confidence

| Evidence Tier | Typical Confidence | Notes |
|---------------|-------------------|-------|
| **Multiple Tier A** | HIGH (>80%) | Strongest possible evidence |
| **Single Tier A** | MEDIUM-HIGH (65-85%) | Strong but needs corroboration |
| **Multiple Tier B** | MEDIUM (60-75%) | Solid evidence, some validation |
| **Single Tier B** | MEDIUM (50-65%) | Adequate for cautious claims |
| **Tier C** | MEDIUM-LOW (40-60%) | Supportive but not conclusive |
| **Tier D** | LOW (<50%) | Speculation or unverified |

### Confidence Adjustment Factors

**Increase confidence** when:
- ✅ Multiple independent sources agree
- ✅ Production validation exists
- ✅ Peer-reviewed research confirms
- ✅ No significant contradictions found
- ✅ Replicable methodology

**Decrease confidence** when:
- ⚠️ Sources conflict or contradict
- ⚠️ Only vendor claims available
- ⚠️ Theoretical without empirical validation
- ⚠️ Known contradictions exist
- ⚠️ Methodology not replicable

---

## Documentation Format

### For Hypotheses

```markdown
**Hypothesis**: [Clear, testable statement]

**Evidence**:
- [Tier X]: [Source and key finding]
- [Tier Y]: [Source and key finding]

**Contradictions**: [Any conflicting evidence]

**Confidence**: [HIGH/MEDIUM/LOW] ([percentage])

**Validation Status**: [What's needed to increase confidence]
```

### For Technical Claims

```markdown
**Claim**: [Specific assertion]

**Source Quality**: [Tier A-D]

**Supporting Evidence**:
1. [Evidence item 1]
2. [Evidence item 2]

**Confidence Assessment**: [HIGH/MEDIUM/LOW]
**Suitable for**: [What this confidence level allows]
```

---

## Usage Guidelines

### For Publication

**HIGH confidence claims**:
- ✅ Suitable for definitive statements
- ✅ Can claim "demonstrates" or "proves"
- ✅ Acceptable for peer review

**MEDIUM confidence claims**:
- ✅ Use hedge words: "suggests", "indicates", "may"
- ✅ Acknowledge limitations
- ⚠️ Note areas needing validation

**LOW confidence claims**:
- ⚠️ Clearly label as speculation
- ⚠️ Use "hypothesize", "theorize", "speculate"
- ❌ Never present as established fact

### For Decision Making

**Architecture decisions**:
- Require: HIGH confidence (Tier A/B evidence)
- Accept: MEDIUM if validated with POC

**Tool selection**:
- Require: MEDIUM confidence minimum
- Verify: With proof-of-concept testing

**Best practices**:
- Accept: MEDIUM-LOW if industry consensus
- Validate: Through team experience

---

## Confidence Evolution

Confidence should evolve as evidence accumulates:

```
Initial: LOW (theoretical only)
    ↓
After POC: MEDIUM (early validation)
    ↓
After Production: HIGH (measured outcomes)
    ↓
After Peer Review: HIGH (independently verified)
```

**Example Evolution**:
```markdown
**2024-Q1**: Hypothesis formulated (LOW - Tier C vendor claims)
**2024-Q2**: POC completed (MEDIUM - internal validation)
**2024-Q3**: Production deployment (HIGH - measured 10x improvement)
**2024-Q4**: Published study (HIGH - peer-reviewed confirmation)
```

---

## Integration with Skills

### hypothesis-validator
- Assigns confidence levels to all hypotheses
- Tracks confidence evolution over time
- Flags claims exceeding evidence

### publication-quality-checker
- Validates confidence levels match evidence
- Ensures hedge words for MEDIUM/LOW claims
- Blocks LOW confidence presented as fact

### research-extractor
- Classifies extracted claims by confidence
- Links evidence to confidence assessment
- Documents validation gaps

### academic-citation-manager
- Maps evidence tiers to confidence levels
- Suggests appropriate confidence language
- Validates citation quality supports claims

---

## Anti-Patterns

**DON'T**:
- ❌ Claim HIGH confidence with only Tier C-D sources
- ❌ Present LOW confidence speculation as fact
- ❌ Ignore contradictions when assessing confidence
- ❌ Use definitive language with MEDIUM confidence
- ❌ Mix confidence levels without clear boundaries

**DO**:
- ✅ Explicitly state confidence level
- ✅ Document evidence supporting assessment
- ✅ Acknowledge contradictions and gaps
- ✅ Use appropriate hedge language
- ✅ Update confidence as evidence evolves

---

## Gaps

The confidence-scoring framework itself carries unvalidated thresholds — applying its own medicine:

- **Gap: threshold calibration.** The HIGH >80% / MEDIUM 50–80% / LOW <50% bands are cognitive anchors, not empirically derived. **Needs**: a study correlating band assignment to outcome accuracy across a corpus of labeled claims. Without this, "HIGH" and "MEDIUM" are more about reviewer calibration than about reality.
- **Gap: tier → confidence mapping.** The mapping of Tier A source quality to HIGH confidence assumes primary sources are consistently correct. Anthropic's own disclosed "eval awareness" and "self-evaluation rationalization" failure modes (see [agent-evaluation.md](agent-evaluation.md)) show that even Tier A sources can have systematic errors. **Needs**: explicit Tier A source-reliability audit before promoting claims to HIGH.
- **Gap: confidence inflation over time.** As a claim accumulates citations, confidence scores tend to drift upward (citation cascades). This framework has no mechanism to detect or correct inflation. **Needs**: periodic downward-revalidation where highly-confident claims are deliberately stress-tested against counter-evidence.

These gaps don't invalidate the framework — they are the framework applied to itself. See [session-quality-tools.md](../archive/session-quality-tools.md) (archived 2026-07-10, retirement complete) for an exemplar of full gap-statement usage.

---

## Sources

This document is a synthesis methodology piece. It has no external citations beyond cross-references to other analysis docs in this repo. Internal cross-references that supply evidence:

### Tier A

- [agent-evaluation.md](agent-evaluation.md) — Documents Anthropic's disclosed "eval awareness" and "self-evaluation rationalization" failure modes, cited in the Gap section to challenge the assumption that Tier A sources are consistently correct.
- [session-quality-tools.md](../archive/session-quality-tools.md) — archived exemplar of the full Gap-statement format this doc defines (retirement completed 2026-07-10).

---

## Related Patterns

- [Evidence Tiers](./evidence-tiers.md) - Classification of source quality (Tier A-D)
- [Context Engineering](./behavioral-insights.md) - Correctness over compression

---

**Version**: 1.0
**Created**: 2025-12-13
**Source**: Production validation in cybersecurity research projects
**Applies to**: Research projects, technical analysis, hypothesis-driven work

*Last updated: January 2026*

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/behavioral-insights.md`](analysis/behavioral-insights.md) [EXTRACTED (1.00)] — references
- [`AUDIT-CONTEXT.md`](AUDIT-CONTEXT.md) [EXTRACTED (1.00)] — references
- [`INDEX.md`](INDEX.md) [EXTRACTED (1.00)] — references

<!-- graphify-footer:end -->
