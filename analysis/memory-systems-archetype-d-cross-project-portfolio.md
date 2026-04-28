---
status: EMERGING
last-verified: "2026-04-28"
evidence-tier: C
applies-to-signals: [memory-systems, cross-project-synchronization, federation]
revalidate-by: 2026-10-28
---

# Archetype D — Cross-Project Portfolio Brain

**Evidence Tier**: C — federation is hand-rolled today; the OpenBrain compilation-agent path is **Tier D** (not shipped).

## Purpose

Per-archetype recommendation for managing **multiple knowledge-bearing repos as a portfolio** — preserving per-repo evidence and provenance while still surfacing cross-repo connections.

## D1. Primary stack

**Per-repo (LLM Wiki + Graphify) + a thin federation index.** Federation today is hand-rolled. OpenBrain's compilation agent is roadmap, not shipping.

| Layer                  | Owner                                                                                              | Why                                                                                          |
|------------------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Per-repo               | Karpathy wiki + Graphify (as in archetype A)                                                        | Preserves per-repo evidence tier and provenance                                              |
| Federation             | Small `~/portfolio/INDEX.md` + nightly cron merging per-repo `index.md` files                       | Axis 4 — federation, not consolidation                                                       |
| Cross-repo topology    | Second graphify run over all repos → cross-repo communities tagged INFERRED                         | Axis 8 — separates within-repo (EXTRACTED) from cross-repo (INFERRED)                        |

**Driving axes**: 4 (cross-tool/cross-repo), 2 (augments per repo), 8 (provenance discipline survives federation). **Tier**: C; OpenBrain compilation-agent path is Tier D (not shipped).

## D2. Hybrid alternatives

| Hybrid                                                            | Optimizes                                                                | Pick when                                                          |
|-------------------------------------------------------------------|---------------------------------------------------------------------------|--------------------------------------------------------------------|
| Per-repo + OpenBrain federation (when compilation agent ships)    | Live cross-repo recall                                                    | FSL-1.1-MIT terms acceptable; want concurrent multi-tool reads     |
| Per-repo + claude-context only on code-heavy repos                | Semantic recall in code without forcing every repo into vectors           | Some repos are code, some are prose                                |
| Single mega-repo with tagged subfolders                           | Drops federation complexity                                               | Repos are small and you're really managing one knowledge body      |

## D3. Anti-patterns

- **Single-DB consolidation across all repos** (OpenBrain Postgres, claude-context Milvus): flattens per-repo evidence tiers; one repo's schema decisions infect another's. A single Milvus collection with vectors from prose + AST chunks produces nonsense neighbors.
- **Shared cross-repo graph as the *only* graph**: communities bleed across project boundaries. The cross-repo graph must be a *secondary* INFERRED-only view.

## D4. Adoption order

1. Each repo independently passes archetype-A adoption first.
2. Write a 50-line script concatenating per-repo `index.md` files into a portfolio INDEX.
3. Run `graphify ~/portfolio` over all repos to see what cross-repo edges emerge. **Stop if** edges are mostly noise.
4. Re-evaluate OpenBrain only after the compilation agent ships and you've reproduced its claims.

## D5. Constraint check

All six met when run as per-repo + thin federation. OpenBrain path defers local-first to self-hosted Postgres setup; FSL terms must be accepted.

## Related Analysis

- [`memory-systems-archetype-recommendations.md`](memory-systems-archetype-recommendations.md) — index across all 7 archetypes + cross-cutting sections
- [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md) — framing and self-critique
- [`federated-query-architecture.md`](federated-query-architecture.md) — federation patterns relevant here
- [`cross-project-synchronization.md`](cross-project-synchronization.md) — cross-project sync patterns
