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

## Related Patterns

- [Agent Principles](./agent-principles.md) - Production AI reliability principles
- [Context Engineering](./context-engineering.md) - Correctness over compression

*Last updated: January 2026*
