# Source Authority Matrix

Unified weighting system for evaluating the credibility and relevance of any source.
Two dimensions: **authority** (how credible is the source?) and **recency** (how current?).

## Authority Tiers (0-5)

| Tier | Label | Weight | Description | Examples |
|------|-------|--------|-------------|----------|
| 5 | Foundational | 1.0 | Built the thing; wrote the spec; authoritative regardless of age | Boris Cherny (Claude Code), Ryan Blue (Iceberg), Matthias Vallentin (Tenzir), Anthropic engineering blog |
| 4 | Authoritative | 0.85 | Core engineering team, framework maintainers, peer-reviewed research | Anthropic engineers, Apache PMC members, Andrej Karpathy, OWASP standards bodies |
| 3 | Practitioner | 0.65 | Named practitioners with documented production experience and metrics | Engineers with public deployment data, conference speakers with real-world case studies |
| 2 | Commentator | 0.35 | Third-tier thought leaders, YouTubers, bloggers without production evidence | YouTube content creators, Medium bloggers, newsletter authors without deployment data |
| 1 | Unverified | 0.15 | Vendor marketing claims, theoretical speculation, unattributed assertions | Product demos without metrics, "X is dead" proclamations, anonymous forum posts |
| 0 | Rejected | 0.0 | Actively debunked, retracted, or deliberately misleading | Retracted claims, proven vendor misrepresentations, debunked benchmarks |

## Recency Dimension

| Age | Factor | Tier 5 Override |
|-----|--------|-----------------|
| <30 days | 1.0 | 1.0 |
| 30-90 days | 0.9 | 0.9 |
| 90-180 days | 0.75 | 0.7 (floor) |
| 180-365 days | 0.5 | 0.7 (floor) |
| >365 days | 0.3 | 0.7 (floor) |

**Tier 5 floor rule**: Foundational sources maintain a minimum recency factor of 0.7.
Boris Cherny's January 2026 interview remains highly relevant even as it ages
because he built the system. The same applies to Ryan Blue on Iceberg, Anthropic
on their own engineering patterns, etc.

## Composite Score

```
Effective Weight = Authority Weight × Recency Factor
```

**Examples:**

| Source | Authority | Recency | Effective Weight |
|--------|-----------|---------|-----------------|
| Boris Cherny interview (Jan 2026, now 3 months old) | 5 (1.0) | 0.7 floor | **0.70** |
| Anthropic engineering blog (2 months old) | 4 (0.85) | 0.9 | **0.77** |
| Named practitioner case study (1 month old) | 3 (0.65) | 1.0 | **0.65** |
| Fresh YouTube clickbait ("This KILLS Claude Code!") | 2 (0.35) | 1.0 | **0.35** |
| Vendor marketing claim (last week) | 1 (0.15) | 1.0 | **0.15** |
| Debunked benchmark | 0 (0.0) | any | **0.00** |

**Key insight**: A 6-month-old Foundational source (0.70) outweighs a brand-new
Commentator (0.35) by 2x. This matches the principle that the person who built
the thing knows more than the person who made a video about it.

## Mapping to Existing Evidence Tiers

The hypothesis-validator skill uses an inverted 1-5 scale (1 = highest, 5 = lowest).
This matrix uses 0-5 (5 = highest, 0 = rejected). The mapping:

| Authority Tier | Evidence Tier | Label |
|----------------|---------------|-------|
| 5 (Foundational) | 1 (Production) | Built/deployed the system |
| 4 (Authoritative) | 2 (Peer-reviewed) | Validated by peers |
| 3 (Practitioner) | 3 (Expert) | Documented experience |
| 2 (Commentator) | 4 (Vendor/theoretical) | Claims without production data |
| 1 (Unverified) | 5 (Speculation) | No supporting data |
| 0 (Rejected) | N/A | Actively debunked |

When recording evidence in hypotheses, use the existing 1-5 evidence tier scale.
Use the 0-5 authority scale when evaluating whether to accept claims into
the knowledge base in the first place.

## Decision Rules

- **Effective Weight >= 0.65**: Accept provisionally; note source for future validation
- **Effective Weight 0.35-0.64**: Investigate further before incorporating into hypotheses
- **Effective Weight 0.15-0.34**: Flag for Karen evaluation; do not use as sole evidence
- **Effective Weight < 0.15**: Do not incorporate; document only if contradicts existing evidence
- **Effective Weight 0.0**: Reject; flag as debunked if previously accepted
