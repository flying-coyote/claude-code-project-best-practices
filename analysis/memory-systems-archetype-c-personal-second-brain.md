---
status: EMERGING
last-verified: "2026-04-28"
evidence-tier: C
applies-to-signals: [memory-systems, second-brain, knowledge-base, wiki, vault-obsidian, md-corpus-small, md-corpus-design-target]
revalidate-by: 2026-10-28
---

# Archetype C — Personal Cross-Domain Second Brain

**Evidence Tier**: C overall (Karpathy paradigm is Tier B by author authority; tool-specific claims stay C).

## Purpose

Per-archetype recommendation for **personal, single-curator, cross-domain second brains**: a markdown vault that mixes notes, references, sketches, and the curator's own interpretation across many subjects.

## C1. Primary stack

**Karpathy LLM Wiki paradigm + Graphify (footer-injection) + Pratiyush adapters for session ingestion.** Local-first when the invoking session uses an Anthropic model and you accept that egress; otherwise skip Pass 2.

| Layer            | Owner                                                                  | Why                                                                       |
|------------------|------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Substrate        | Markdown vault                                                         | Axis 5 (local), 7 (portable)                                              |
| Wiki             | Karpathy convention (`sources/`, `wiki/`, `index.md`, `log.md`)        | Axis 2 — augments; personal interpretation matters                        |
| Topology         | Graphify (with `--watch` for live rebuild)                             | Axis 3 — topology over heterogeneous content                              |
| Session ingest   | Pratiyush adapter (Claude Code + Codex + Cursor + Gemini)              | Axis 4 — cross-tool source feeding single wiki                            |

**Driving axes**: 5 (local strongly preferred), 2 (augments-wiki), 6 (mostly structural with temporal islands). **Tier**: C overall (paradigm B; tools C).

## C2. Hybrid alternatives

| Hybrid                                              | Optimizes                                                          | Pick when                                                          |
|-----------------------------------------------------|---------------------------------------------------------------------|--------------------------------------------------------------------|
| + OpenBrain (post-compilation-agent ship)           | Cross-tool concurrency                                              | Switching frequently between Claude Code, Cursor, ChatGPT          |
| + Rowboat sliver                                    | Capturing the temporal layer (deadlines, commitments) without polluting the structural wiki | Wiki accumulating "decided last Tuesday" pages                     |
| + Lum1104 plugin                                    | Wiki-aware graph view that uses your `[[wikilinks]]`                | Once the wiki has dense cross-refs                                 |

## C3. Anti-patterns

- **Cloud-egress vector DB (Milvus/Zilliz Cloud, OpenAI embeddings) over personal notes**: privacy + recurring cost for a single user; embedding drift over years invalidates indexes.
- **LLM Wiki + Rowboat at full scope on the same content**: typed-entity files duplicate page-per-topic prose. Use Rowboat *only* for the temporal sliver.

## C4. Adoption order

1. Create the directory skeleton (`sources/`, `wiki/`, `index.md`, `log.md`, `CLAUDE.md`). Reversible.
2. Manually write 5 wiki pages from existing sources to learn the convention. **Stop if** bookkeeping load exceeds recall benefit at this scale.
3. Run `graphify .` once and add a footer-injection script.
4. Install Pratiyush; one-shot ingest of last month's sessions.
5. Reconsider OpenBrain only if juggling >2 AI tools daily.

## C5. Constraint check

All six met when graphify Pass 2 stays on a model you accept egress to (or is skipped). Pratiyush has redaction-by-default per inventory.

## Related Analysis

- [`memory-systems-archetype-recommendations.md`](memory-systems-archetype-recommendations.md) — index across all 7 archetypes + cross-cutting sections
- [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md) — framing and self-critique
