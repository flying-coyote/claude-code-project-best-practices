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
| + claude-video for "watch later" YouTube ingest     | Converts the dormant YouTube pile (conference talks, tutorials, podcasts) into searchable transcripts + frame summaries that feed `sources/` | Significant fraction of intake is video; "watch later" backlog has effectively become a write-only graveyard |
| + Tolaria as the editor surface                     | Native UX over the markdown vault without Obsidian plugin sprawl    | You want a desktop app and AGENTS-file convention rather than rolling your own `CLAUDE.md` from scratch |
| + SiYuan if block-level recombination dominates     | Block IDs and transclusion for atomic-note workflows                | Knowledge is heavily recombined across pages (Zettelkasten style)  |

### C2.1 Watch-later YouTube ingest pattern

The "watch later" YouTube pile is a common Archetype C failure mode: source-rich, intake-zero. Most users accumulate hundreds of unwatched links that contain the very expert interviews, conference talks, and walkthroughs the second brain exists to capture.

**Recommended pattern**:
1. Maintain a `sources/queue/watchlist.md` with one URL per line (paste from YouTube's "Watch later" export or browser bookmarks).
2. Process N at a time via `claude-video`: `<url> + "summarize key claims, vendors named, methodology described, contradictions with my existing notes"`.
3. The skill's output (frames + timestamped transcript + Claude analysis) becomes a new `sources/<slug>.md` file with a `type: video` frontmatter.
4. Wiki ingest workflow runs as normal — same as for any text source.
5. Original video URL stays in the source file for re-derivation.

**Egress profile** (Axis 5): Whisper API call goes to Groq or OpenAI; frames + transcript go to Claude during analysis. Both are at parity with graphify Pass 2 in egress class. **Fine for public videos; not fine for private content.** If a video contains private material, drop it from this pipeline — see [`memory-systems-archetype-c-egress-constrained.md`](memory-systems-archetype-c-egress-constrained.md) for the constrained variant.

**Skip when**: Watch-later pile is small enough to actually watch; video content is mostly entertainment (no second-brain value); content is private.

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

- [`memory-systems-archetype-c-egress-constrained.md`](memory-systems-archetype-c-egress-constrained.md) — **egress-constrained variant** when owner has decided corpus content cannot egress to vendor LLMs (medical, legal, journals naming third parties); previously titled "C-PII"
- [`memory-systems-genealogy-baseline.md`](memory-systems-genealogy-baseline.md) — empirical measurement of the unaugmented stack across the 3-project genealogy trio
- [`memory-systems-archetype-recommendations.md`](memory-systems-archetype-recommendations.md) — index across all 7 archetypes + cross-cutting sections
- [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md) — framing and self-critique
