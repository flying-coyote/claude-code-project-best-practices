# Confidence Scoring for Research and Hypotheses

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
- Minimum: 2+ Tier A or Tier 1 sources
- Ideal: 3+ independent sources across Tier A/B and Tier 1-2

**Example**:
```markdown
**Hypothesis**: DuckDB outperforms Spark for sub-1GB datasets

**Evidence**:
- Tier 1: Production deployment (45s → 2s query time)
- Tier 1: Independent benchmark (10x faster for small datasets)
- Tier 2: Published VLDB paper confirming architecture advantage
- Tier 3: Creator (DuckDB team) confirms design intent

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
- Minimum: 1+ Tier B or Tier 2-3 sources
- Acceptable: Single strong source or multiple weaker sources

**Example**:
```markdown
**Hypothesis**: Iceberg table format reduces storage costs 30-50%

**Evidence**:
- Tier 3: Conference talk from Netflix (claims 40% reduction)
- Tier 4: Vendor whitepaper (claims 30-50% range)
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
- Tier C-D or Tier 4-5 sources only
- Speculation or unverified assertions

**Example**:
```markdown
**Hypothesis**: AI-based SIEM will replace rule-based detection

**Evidence**:
- Tier 4: Vendor marketing claims
- Tier 5: Industry speculation and blog posts
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

### Mapping Evidence to Confidence

| Evidence Tier | Typical Confidence | Notes |
|---------------|-------------------|-------|
| **Multiple Tier A or Tier 1** | HIGH (>80%) | Strongest possible evidence |
| **Single Tier A or Tier 1** | MEDIUM-HIGH (65-85%) | Strong but needs corroboration |
| **Multiple Tier B or Tier 2** | MEDIUM (60-75%) | Solid evidence, some validation |
| **Single Tier B or Tier 2** | MEDIUM (50-65%) | Adequate for cautious claims |
| **Tier C or Tier 3** | MEDIUM-LOW (40-60%) | Supportive but not conclusive |
| **Tier D or Tier 4-5** | LOW (<50%) | Speculation or unverified |

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
**Research Evidence**: [Tier 1-5]

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
- Require: HIGH confidence (Tier A/B, Tier 1-2 evidence)
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
**2024-Q1**: Hypothesis formulated (LOW - Tier 4 vendor claims)
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

## Related Patterns

- [Evidence Tiers](./evidence-tiers.md) - Classification of source quality and research evidence
- [Agent Principles](./agent-principles.md) - Accuracy and intellectual honesty
- [Context Engineering](./context-engineering.md) - Correctness over compression

---

**Version**: 1.0
**Created**: 2025-12-13
**Source**: Production validation in cybersecurity research projects
**Applies to**: Research projects, technical analysis, hypothesis-driven work
