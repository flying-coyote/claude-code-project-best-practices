---
status: EMERGING
last-verified: "2026-04-28"
evidence-tier: C
applies-to-signals: [memory-systems, work-tracker, temporal]
revalidate-by: 2026-10-28
---

# Archetype E — Work-State / Project Tracker

**Evidence Tier**: C — Rowboat verified at [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) (Apache 2.0, 13.1k stars, desktop app, 2026-04-28).

## Purpose

Per-archetype recommendation for **temporal-dominant work tracking**: deadlines, commitments, decisions, people — content that mutates daily and would silently rot a topic-page wiki.

## E1. Primary stack

**Rowboat (typed entities, BYO-via-Composio) + a small LLM Wiki for the stable layer.**

| Layer       | Owner                                                                              | Why                                                                                                                  |
|-------------|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Temporal    | Rowboat-style typed-entity files (Decision/Commitment/Deadline/Person)             | Axis 6 — temporal-dominant; this is the differentiator                                                               |
| Stable      | Tiny Karpathy-style wiki for projects/people that don't change weekly               | Avoids "page becomes contradiction soup" failure                                                                     |
| Briefing    | Rowboat background agents                                                           | Daily briefing surfaces overnight changes                                                                            |

**Driving axes**: 6 (temporal), 8 (provenance per claim), 7 (markdown still — Rowboat README confirms "it's just Markdown"). **Tier**: C for the recommendation. Rowboat verified at [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) — Apache 2.0, 13.1k stars, desktop app for Mac/Windows/Linux.

## E2. Hybrid alternatives

| Hybrid                                                | Optimizes                                                          | Pick when                                                              |
|-------------------------------------------------------|---------------------------------------------------------------------|------------------------------------------------------------------------|
| Rowboat alone                                         | Simplicity                                                          | The "stable" sliver is genuinely small (early project)                 |
| Plain markdown + dated journal + Obsidian             | No new tooling                                                      | Rowboat install isn't justified; lose typed-entity queries, gain zero ops |
| Rowboat + Pratiyush ingestion                         | Pulling commitments out of meeting transcripts                      | Heavy meeting cadence                                                  |

## E3. Anti-patterns

- **Karpathy wiki on temporal data**: `Project X` page mutates daily; cross-refs go stale; wiki silently rots.
- **Graphify on a Rowboat vault**: graph rebuilds become the bottleneck because the corpus changes daily; Pass 2 LLM passes burn API on volatile content. Rowboat's typed entities make graphify redundant.

## E4. Adoption order

1. Pick three entity types (Decision, Commitment, Deadline). Hand-write 10 entity files. Reversible.
2. Add backlinks to existing project pages.
3. Install Rowboat (desktop app); point it at the vault. **Stop if** the daily briefing surfaces nothing you wouldn't have remembered.
4. Add Google services (Gmail/Calendar/Drive) or optional integrations only after step 3 earns its keep.

## E5. Constraint check

All met. Local-first holds for the markdown vault; Google services + optional Composio MCP / Deepgram / ElevenLabs / Exa add egress when enabled.

## Related Analysis

- [`memory-systems-archetype-recommendations.md`](memory-systems-archetype-recommendations.md) — index across all 7 archetypes + cross-cutting sections
- [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md) — framing and self-critique

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/memory-systems-archetype-recommendations.md`](analysis/memory-systems-archetype-recommendations.md) [EXTRACTED (1.00) ×2] — references
- [`INDEX.md`](INDEX.md) [EXTRACTED (1.00)] — references
- [`analysis/memory-systems-archetype-f-session-archive.md`](analysis/memory-systems-archetype-f-session-archive.md) [EXTRACTED (1.00) ×2] — references
- [`research/memory-systems-project-archetypes.md`](research/memory-systems-project-archetypes.md) [EXTRACTED (1.00)] — references
- [`research/memory-systems-tools-inventory.md`](research/memory-systems-tools-inventory.md) [EXTRACTED (1.00) ×2] — references
- [`research/memory-systems-architecture-axes.md`](research/memory-systems-architecture-axes.md) [EXTRACTED (1.00)] — references
- [`analysis/memory-systems-archetype-b-code-monorepo.md`](analysis/memory-systems-archetype-b-code-monorepo.md) [INFERRED (0.70)] — semantically_similar_to

<!-- graphify-footer:end -->
