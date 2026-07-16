---
status: ARCHIVED
evidence-tier: B
extracted-from: analysis/evidence-tiers.md
extracted: 2026-07-16
---

# Evidence Tiers — Retired 1-5 Axis (Record)

> **Extracted 2026-07-16 from `analysis/evidence-tiers.md`.** The 1-5 claim-strength axis was RETIRED by owner ruling 2026-07-12 (ruling B-F7; it was never ratified) — Tier A-D is the only tier system in use. These sections are preserved verbatim as a historical record and moved here because evidence-tiers.md is an Always-Fetch doc, where every retired line taxed every audit.

---

## Research Evidence Tiers (1-5)

> **RETIRED** (owner ruling 2026-07-12): this 1-5 evidence axis was never ratified and is retired. Tier A-D is the only tier system. The description below is preserved as a record.

Formerly used for hypothesis validation and research claim assessment; it complemented the A-D system with a focus on empirical validation.

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

> **RETIRED with the 1-5 axis** (owner ruling 2026-07-12): the combined-assessment practice below is preserved as a record. Use Tier A-D alone.

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
