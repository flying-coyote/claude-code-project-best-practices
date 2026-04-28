---
status: EMERGING
last-verified: "2026-04-28"
evidence-tier: C
applies-to-signals: [memory-systems, session-history, transcript-mining]
revalidate-by: 2026-10-28
---

# Archetype F — Session-History Transcript Archive

**Evidence Tier**: C — Pratiyush verified MIT at [pratiyushpathak/llm-wiki](https://github.com/pratiyushpathak/llm-wiki) (2026-04-28).

## Purpose

Per-archetype recommendation for **mining AI-tool session history into durable knowledge**: extracting recurring rules, decisions, and conclusions from Claude Code / Codex / Cursor / Gemini transcripts.

## F1. Primary stack

**Pratiyush/llm-wiki (purpose-built) + Graphify on the resulting wiki for cross-session topology.**

| Layer        | Owner                                                                                     | Why                                                       |
|--------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| Ingestion    | Pratiyush adapters (Claude Code, Codex, Cursor, Gemini, Obsidian, Copilot)                 | Axis 4 — multi-agent coverage                             |
| Wiki         | Pratiyush three-layer (`raw/` → `wiki/` → `site/`)                                         | Provenance per session preserved in `raw/`                |
| Topology     | Graphify on the resulting wiki                                                              | Cross-session communities                                 |

**Driving axes**: 1 (write-time mining heavy), 8 (provenance per session essential), 4 (cross-tool adapters). **Tier**: C.

## F2. Hybrid alternatives

| Hybrid                                       | Optimizes                                                  | Pick when                                                                |
|----------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------|
| Pratiyush alone                              | Lower complexity                                            | Small archive (under a few hundred sessions)                             |
| Pratiyush + MehmetGoekce L1/L2               | Pinning crystallized rules in always-loaded layer            | You keep re-discovering the same gotcha across sessions                   |
| Plain `.jsonl` parsing scripts               | Zero install                                                 | Single-agent archive; multi-adapter selling point doesn't apply           |

## F3. Anti-patterns

- **claude-context over raw transcripts**: encourages re-deriving conclusions every query rather than promoting durable knowledge. The whole point is write-time extraction.
- **Skipping redaction**: Pratiyush has redaction-by-default for keys/tokens; the others on this list don't. Indexing `~/.claude/projects/` without redaction risks publishing API keys to a static HTML site.

## F4. Adoption order

1. `./setup.sh` Pratiyush against last week of sessions only.
2. Inspect what gets promoted to `wiki/`. **Stop if** wiki entries are 90% noise.
3. Add `llmwiki sync` SessionStart hook (auto-trigger) once the noise floor is acceptable.
4. Run `graphify` over the produced `wiki/` only after a few weeks of accumulation.

## F5. Constraint check

All met. Provenance per session aligns with the wiki↔graph confidence constraint.

## Related Analysis

- [`memory-systems-archetype-recommendations.md`](memory-systems-archetype-recommendations.md) — index across all 7 archetypes + cross-cutting sections
- [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md) — framing and self-critique
- [`session-quality-tools.md`](session-quality-tools.md) — adjacent: session-quality assessment
