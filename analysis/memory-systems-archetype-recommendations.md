---
status: EMERGING
last-verified: "2026-04-30"
measurement-claims:
  - claim: "Single-curator hand-curated KBs hit the wiki+graph+contradiction-lint payoff threshold around ~500 documents"
    source: "Working-memory-vs-relation-count math; not measured studies"
    date: "2026-04-28"
    revalidate: "2026-10-28"
  - claim: "Three of four 'check repo' tools verified MIT (Pratiyush, MehmetGoekce, Lum1104); Rowboat is Apache 2.0"
    source: "Direct fetch of LICENSE files via raw.githubusercontent.com"
    date: "2026-04-28"
    revalidate: "2026-07-28"
  - claim: "Graphify has zero LLM SDK dependencies in pyproject.toml — Pass 2 LLM work happens via the invoking Claude Code session, not graphify-internal API calls"
    source: "Direct read of safishamsi/graphify pyproject.toml on v1 branch"
    date: "2026-04-28"
    revalidate: "2026-07-28"
  - claim: "The unaugmented stack (CLAUDE.md + auto-memory + raw file navigation) achieved 89% DEFINITIVE answers (8/9) on a baseline measurement across the genealogy trio"
    source: "archive/memory-systems-genealogy-baseline.md (2026-04-29 measurement; archived 2026-07-10 as a dated measurement)"
    date: "2026-04-29"
    revalidate: "2026-07-29"
  - claim: "Lum1104/Understand-Anything via local Ollama as a Pass-2 substitute is untested in this repo"
    source: "Repo search; no testbed evidence found"
    date: "2026-04-30"
    revalidate: "2026-07-30"
evidence-tier: C
convergence: emerging  # AI-PKM caveat (B-F1 seed): emerging WITH license risk — Obsidian Smart Connections ~786K downloads but Jan-2026 proprietary switch (DR-6 verified)
applies-to-signals: [memory-systems, knowledge-base, second-brain, wiki, graph, md-corpus-small, md-corpus-design-target, md-corpus-large, md-corpus-very-large, vault-obsidian, vault-karpathy, project-type-docs, project-type-research, typed-memory-no-registry, code-search, monorepo, cross-project-synchronization, federation, work-tracker, temporal, session-history, transcript-mining, team-shared-memory, multi-tool-concurrency, corpus-sensitive, pii, sensitive-content, healthcare-data, legal-data, journal-third-parties]
revalidate-by: 2026-10-28
---

# Memory & Knowledge System Recommendations

One consolidated doc (folded 2026-07-10; formerly a two-level index over seven per-archetype files): the per-archetype table routes to sections *in this document* for archetypes B through G, while **Archetype A keeps its own file** ([`memory-systems-archetype-a-curated-kb.md`](memory-systems-archetype-a-curated-kb.md)) as the heavily-routed primary. Cross-cutting sections (migration paths, never-combine list, license/cost gotchas, build-vs-borrow, evidence gaps) follow the archetype sections.

Calibrated to **~500-document curated knowledge bases** as the single-curator design target. See [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md) for the framing, threshold math, self-critique, and applied corrections behind these recommendations — including the **owner-authorized-egress deciding rule** that governs the C-EC archetype.

**Convergence status**: `emerging` (AI-PKM function, per the 2026-07-12 convergence review), so the binding rule applies: adopting infrastructure from these recommendations requires converged status or an explicit owner exception.

> **Source documents** (read first):
>
> - `archive/memory-systems-tools-inventory.md` (research note, archived 2026-07-10) — factual catalog of 8 tools/paradigms with capabilities and licenses
> - `archive/memory-systems-architecture-axes.md` (research note, archived 2026-07-10) — 8 architectural axes that distinguish the tools
> - `archive/memory-systems-project-archetypes.md` (research note, archived 2026-07-10) — 7 archetypes A–G with axis profiles

**Constraints honored on every recommendation**:

1. Graphify-style graph output feeds the wiki (promotes findings into pages); does not sit as a parallel artifact.
2. Wiki claims align with graph confidence (EXTRACTED / INFERRED / AMBIGUOUS).
3. A/B/C evidence tiering preserved through the stack.
4. Augments-not-generates for prose-rich projects.
5. Local-first preferred over cloud egress.
6. Markdown substrate preferred for long-lived knowledge.

**Tier note**: Tool-specific quantitative claims are Tier C. Karpathy's paradigm is **Tier B by author authority** (Karpathy is treated as a thought leader on par with Boris Cherny on Claude Code). The genealogy-baseline finding cited in the C-EC section is **Tier B** (project-artifact measurement, archived 2026-07-10).

## Per-archetype recommendations

| # | Archetype                                  | Primary stack (one-line)                                                                                       | Where |
|---|--------------------------------------------|----------------------------------------------------------------------------------------------------------------|--------|
| A | Curated analytical knowledge base          | Lum1104 below ~200 docs; Graphify + footer-injection at the ~500-doc design target                              | [`memory-systems-archetype-a-curated-kb.md`](memory-systems-archetype-a-curated-kb.md) (own file) |
| B | Code monorepo / large codebase             | Graphify alone under ~10k files; + claude-context above                                                          | [§ Archetype B](#archetype-b-code-monorepo) below |
| C | Personal cross-domain second brain         | Karpathy LLM Wiki + Graphify (footer-injection) + Pratiyush adapters                                             | [§ Archetype C](#archetype-c-personal-cross-domain-second-brain) below |
| **C-EC** | **Second brain — egress-constrained**       | **Karpathy convention + hand-curated wiki + wikilink graph + auto-memory; no vendor LLM egress**              | [§ Archetype C-EC](#archetype-c-ec-egress-constrained-second-brain) below |
| D | Cross-project portfolio brain              | Per-repo (LLM Wiki + Graphify) + thin federation index                                                           | [§ Archetype D](#archetype-d-cross-project-portfolio) below |
| E | Work-state / project tracker               | Rowboat (typed entities) + small LLM Wiki for stable layer                                                       | [§ Archetype E](#archetype-e-work-state-tracker) below |
| F | Session-history transcript archive         | Pratiyush/llm-wiki + Graphify on the resulting wiki                                                              | [§ Archetype F](#archetype-f-session-history-archive) below |
| G | Multi-tool team shared memory              | Wait or roll your own (Postgres + pgvector + MCP); OpenBrain stack contingent on roadmap                          | [§ Archetype G](#archetype-g-team-shared-memory) below |

---

# Archetype B (code monorepo)

For **code repositories**, especially monorepos and large codebases where AST topology and (at scale) semantic search add value over plain Grep + Explore. Tier C — both token-savings claims (graphify 71.5×, claude-context ~40%) are vendor-reported, not independently reproduced.

## B1. Primary stack

**Graphify alone** for repos under ~10k files. **Graphify + claude-context** above that threshold.

| Layer                       | Owner                                                                | Why                                                                          |
|-----------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------|
| Topology                    | Graphify Tree-sitter (~16 languages per pyproject)                   | Axis 3 — deterministic, no embedding drift                                   |
| Semantic recall (large only)| claude-context (BM25 + dense vectors over Milvus)                    | Axis 3 — when AST topology misses semantic similarity at scale               |
| Wiki layer                  | `graphify --wiki` is acceptable here (code is canonical, not prose)  | Axis 2 — generates-wiki is fine when the wiki is a derived view              |

**Driving axes**: 1 + query-time at scale, 3 (topology vs embeddings tradeoff), 5 (egress matters for proprietary code).

## B2. Hybrid alternatives

| Hybrid                                                       | Optimizes                       | Pick when                                                                |
|--------------------------------------------------------------|----------------------------------|--------------------------------------------------------------------------|
| Graphify + claude-context (Ollama embeddings, self-hosted Milvus) | Local-first semantic recall     | Proprietary code that can't egress to OpenAI/VoyageAI                    |
| Graphify + Pratiyush adapters                                | Mining session history *over* the repo | Postmortem culture; multiple devs leaving good context in transcripts    |
| Plain Grep + Explore subagent                                | Zero-infra                       | Repos under ~5k files where graphify install cost exceeds the benefit    |

## B3. Anti-patterns

- **LLM Wiki paradigm on a 50k-file repo**: code is the canonical artifact; a parallel hand-curated wiki rots within weeks of refactors. Use graphify's generated wiki view instead.
- **claude-context on a 2k-file repo**: pays Milvus ops + embedding-provider egress for recall Grep already covers.
- **`graphify --wiki` *and* a separate hand-curated docs site over the same code**: source-of-truth ambiguity; the docs site contradicts AST-derived claims as code changes.

## B4. Adoption order

1. `graphify .` from the repo root with `--cache`. Reversible-local; egress applies.
2. `graphify hook install` for branch-switch rebuilds. Reversible.
3. Inspect token-savings on three real queries vs Grep+Explore. **Stop if** savings are under 3×.
4. Only at scale (>10k files) and only after step 3 shows benefit, evaluate claude-context with **Ollama embeddings** to keep code local.

## B5. Constraint check

- Graphify feeds wiki: ✅ via `--wiki` export.
- No contradiction: ⚠️ generated wiki has no human prose to contradict; discipline simplifies to "wiki = graph view."
- Tiering: N/A (code corpus, not evidence claims).
- Augments: deviates intentionally — generates-wiki is correct here.
- Local-first: ✅ for Pass 1 + Ollama-backed claude-context. ❌ if OpenAI embeddings.
- Markdown: ✅ for the wiki view.

---

# Archetype C (personal cross-domain second brain)

For **personal, single-curator, cross-domain second brains**: a markdown vault that mixes notes, references, sketches, and the curator's own interpretation across many subjects. Tier C overall (Karpathy paradigm is Tier B by author authority; tool-specific claims stay C).

## C1. Primary stack

**Karpathy LLM Wiki paradigm + Graphify (footer-injection) + Pratiyush adapters for session ingestion.** Local-first when the invoking session uses an Anthropic model and you accept that egress; otherwise skip Pass 2.

| Layer            | Owner                                                                  | Why                                                                       |
|------------------|------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Substrate        | Markdown vault                                                         | Axis 5 (local), 7 (portable)                                              |
| Wiki             | Karpathy convention (`sources/`, `wiki/`, `index.md`, `log.md`)        | Axis 2 — augments; personal interpretation matters                        |
| Topology         | Graphify (with `--watch` for live rebuild)                             | Axis 3 — topology over heterogeneous content                              |
| Session ingest   | Pratiyush adapter (Claude Code + Codex + Cursor + Gemini)              | Axis 4 — cross-tool source feeding single wiki                            |

**Driving axes**: 5 (local strongly preferred), 2 (augments-wiki), 6 (mostly structural with temporal islands).

### C1b. Type your vault (OKF) — a personal vault sprawls fastest

A cross-domain personal vault drifts into `type:` sprawl faster than a single-curator analytical KB, because there is no editorial reviewer between "I'll just call this one `idea-fragment`" and a graph with 86 single-use types. So if your vault types its notes — and it should, since a `type:` is what turns a personal pile into something a [Tolaria](#c2-hybrid-alternatives)-style MCP or a generated index can query by kind — govern the vocabulary the same way [archetype-A §A1b](memory-systems-archetype-a-curated-kb.md#a1b-typed-frontmatter-hygiene--okf-as-the-km-leverage-pattern) does: one canonical type-registry doc as the source of truth, a pre-commit guard that *parses* that registry (so it can't disagree with it), and a coverage/drift health check. This is the Google **OKF** pattern (one required field, `type:`; [spec](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md), Apache-2.0, [announced 2026-06-12](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) — verified against primary sources). The exact deployment this is drawn from — the registry, the parsed guard, and the graph-derived next-work signal — is a real production second-brain ([project1](file:///home/jerem/project1): `01-knowledge-base/_type-registry.md`, `automation/lib/okf.py`, `automation/orchestrator/quality_gates.py`, `automation/okf_health.py`, `automation/okf_signals.py`); **Tier B, one practitioner, not independently corroborated.**

The pairing worth carrying over to a personal vault: **OKF stores what you know; the RETHINK limb re-asks whether it is still worth keeping.** A second brain accretes — half-finished ideas, links you meant to read, "decided last Tuesday" notes — and a typed graph lets a periodic re-examination filter by type to what is most likely dead weight (stale captures, never-resolved threads) instead of re-reading the whole vault. project1's [`okf_signals.py`](file:///home/jerem/project1/automation/okf_signals.py) is that re-examination made mechanical; for a personal vault the lighter version is a scheduled pass that lists, by type, the notes most overdue for a look. **The signal that should route you here is `typed-memory-no-registry`** — a vault that types its notes but has no registry and no guard, which is exactly the sprawl trap above.

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

**Egress profile** (Axis 5): Whisper API call goes to Groq or OpenAI; frames + transcript go to Claude during analysis. Both are at parity with graphify Pass 2 in egress class. **Fine for public videos; not fine for private content.** If a video contains private material, drop it from this pipeline — see [§ Archetype C-EC](#archetype-c-ec-egress-constrained-second-brain) for the constrained variant.

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

---

# Archetype C-EC (egress-constrained second brain)

Variant of Archetype C for projects where the **owner has chosen not to authorize vendor-LLM egress** of corpus content. The constraint is policy, not data category — the deciding rule and its provenance live in [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md). Tier C overall; Karpathy paradigm is **B by author authority**; the local-LLM-Pass-2 substitute is **D-leaning-C** (untested in this repo); the 89%-baseline finding is **B** (project-artifact-based; see [`archive/memory-systems-genealogy-baseline.md`](../archive/memory-systems-genealogy-baseline.md)).

> **Naming note**: originally `archetype-c-pii.md` with genealogy as the canonical example; renamed 2026-04-30 to reflect the actual constraint axis (owner-authorized vendor egress, not data-category PII) after the owner reframed the Wiley-genealogy projects' egress posture on 2026-04-29.

Reasons owners adopt this constraint vary:

- **Hard category constraints**: medical records, attorney-client legal correspondence, HR / employee performance notes, journals naming third parties without their consent
- **Soft category constraints**: published-but-aggregated personal data the owner wants to control (e.g. comprehensive profiles aggregating public records that no public source provides as a unit)
- **Vendor-policy mismatches**: corpus subject to data-residency, GDPR-Article-9, HIPAA, or contractual non-disclosure that prevents API egress
- **Research / threat-modeling reasons**: owner wants to characterize the unaugmented stack first, before committing to a vendor-egress dependency

Same shape as Archetype C: single-curator markdown vault with structural and (optionally) temporal layers. The difference is what's allowed to leave the box.

## The constraint conflict

The Archetype C primary stack (Karpathy LLM Wiki + Graphify Pass 2 + Pratiyush adapters) all egress content to a vendor LLM during ingest. Constrained corpora can't allow that. Concretely:

| Required by Archetype C primary stack                                | Blocked by the egress constraint                                                            |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Graphify Pass 2 — LLM extracts concepts from each file                | Bulk content egress to Anthropic/OpenAI API on every changed file                          |
| Pratiyush adapter — ingests session `.jsonl` to wiki                  | Sessions contain quoted sensitive content from the corpus; egress at ingest                |
| Lum1104 wiki-aware graph — LLM agents discover implicit relationships | Same egress profile (Pass 2 calls go through invoking session)                              |
| `claude-context` semantic search                                      | Code/text goes to embedding provider; chunks to Milvus/Zilliz                               |
| Cloud embedding APIs (OpenAI, VoyageAI, Gemini)                        | Same                                                                                        |
| claude-video skill (Whisper API + frame analysis)                      | Audio to Groq/OpenAI; frames + transcript to Claude — fine for public, not for private     |

What's left: pure topology (Pass 1), prose curation (manual), deterministic structure extraction (AST, wikilinks), local-only LLM passes if you accept the quality drop, and the auto-memory layer that already exists in `~/.claude/projects/<project>/memory/`.

## Canonical examples

Medical / clinical-notes corpora (HIPAA, BAA, PHI by definition); legal-correspondence vaults (attorney-client privilege, work-product); personal journals naming living third parties; performance / personnel files; pre-publication research drafts with embargoed source material. The shared trait: the *content* might be entirely on the owner's local disk, but the owner has determined that vendor LLMs should not retain a copy of it.

### Genealogy as opt-out, not canonical example (2026-04-29 reframe)

The Wiley genealogy projects (~17k / 3.3k / 396 md files) were originally framed as the canonical case. The owner has since reframed: living-person names use anonymized placeholders, the remaining content is publicly available (FamilySearch, Ancestry, WikiTree, Find a Grave), so vendor-LLM egress is acceptable for these projects at owner's choice. The genealogy `CLAUDE.md` files still contain the original "Do NOT bulk-feed these paths to vendor-LLM tools..." rule — **that rule predates the reframe and should be updated only when the owner authorizes a specific tool to run. Don't unilaterally relax it in code.**

The empirical finding from running this archetype's primary stack against the genealogy corpus anyway ([`archive/memory-systems-genealogy-baseline.md`](../archive/memory-systems-genealogy-baseline.md)): the unaugmented stack scored 8/9 DEFINITIVE on a 9-query measurement, which means the original C-PII framing was slightly misleading — the PII concern determined "must we use the unaugmented stack" but turned out not to matter for "is the unaugmented stack sufficient." For actual hard-egress-constraint projects (medical, legal, journals with third parties), expect the unaugmented stack to be similarly sufficient if memory authorship is disciplined; augmentation is not the bottleneck for retrieval quality — authorship discipline is.

## C-EC.1 Primary stack

**Karpathy LLM Wiki paradigm + hand-curated wiki + Graphify Pass 1 only + auto-memory layer.** No Pass 2. No Pratiyush. No vendor embeddings. No cloud-Whisper ingest of private audio.

| Layer            | Owner                                                                  | Why                                                                                  |
|------------------|------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Substrate        | Markdown vault                                                         | Axis 5 (local strict), Axis 7 (portable)                                             |
| Wiki             | Karpathy convention, **hand-curated only** (no LLM authoring)           | Axis 8 — only deterministic / human-derived structure leaves the box                 |
| Topology         | Wikilink graph (deterministic) + Graphify Pass 1 *only if corpus has code* | Axis 5 strict; Axis 8 — deterministic only. **See empirical caveat below.** |
| Session memory   | Auto-memory only (`~/.claude/projects/*/memory/`)                       | Stays in invoking session; doesn't bulk-feed corpus through an ingestion pipeline    |
| Cross-tool       | None — single-curator, single-tool stays simple                         | Axis 4                                                                               |
| Editor surface   | Tolaria *or* plain editor + git                                         | Axis 10 — AGENTS file convention is local-only by default                            |

**Driving axes**: 5 strict (no egress), 6 (mostly structural; volatile facts go to typed entities), 8 (deterministic-only at the corpus boundary), 10 (convention-based agent contract preferred over MCP servers that might egress).

### Empirical caveat: Tree-sitter doesn't help on pure prose

The 2026-04-28 graphify testbed against this repo (38 prose analysis docs at the time) found that **graphify Pass 1 indexed 0 of 38 docs** — Tree-sitter produces an AST for code, not for prose markdown. For a corpus that's almost entirely prose (clinical notes, legal correspondence, journals, longform analyses), the "Pass 1 only" recommendation produces ~zero useful topology in practice.

What works on prose under egress constraint:

1. **Wikilink graph extraction** — a deterministic ~50-line script that walks `*.md` files, parses `[[wikilink]]` references, and builds an adjacency list. No LLM. Output is a JSON edge list that footer-injection scripts can consume.
2. **Frontmatter index** — extract `type:`, `tags:`, `subject:` fields from YAML frontmatter into a SQLite or JSON index. Also deterministic.
3. **Heading-graph** — sibling/parent relationships across files based on heading-text matches. Brittle but local.
4. **Lum1104 + local Ollama** for the LLM-derived layer (the C-EC.2 hybrid; **untested** in this repo).

The Pass 1 line above keeps Graphify in the recommendation only because it does meaningful work on *mixed* corpora (some code + some prose). On pure-prose corpora, replace it with the wikilink-graph approach.

## C-EC.2 Hybrid alternatives (with caveats)

| Hybrid                                              | What it adds                                                          | What you trade                                                                                   |
|-----------------------------------------------------|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| + Lum1104/Understand-Anything via local Ollama       | LLM-derived implicit relationships without vendor egress              | Quality drops vs. Claude/GPT (Tier C inferred from inventory; **untested locally**); setup cost  |
| + Pre-redaction filter for selective Pass 2          | Some Pass 2 benefit on non-sensitive subset                            | Brittle in practice; misses ~95% of corpus for genealogy; risk of leak from incomplete redaction |
| + Local-only Whisper for audio sources               | Audio ingest of family interviews, recorded methodology               | Setup of `whisper.cpp` or `faster-whisper`; quality drop vs Groq Whisper                          |
| + Block-level layer (SiYuan) running entirely local  | Block IDs + transclusion for atomic-note workflows                     | Heavier app; community MCP server only; AGPL-3.0                                                  |
| + claude-video for **public** sources only           | Watch-later YouTube ingest of public methodology, not private material | Strict separation discipline required; one slip = egress event                                    |

## C-EC.3 Anti-patterns

- **Run graphify Pass 2 on a "redacted" subset and pretend the rest will catch up.** Redaction is incomplete in practice (names show up in unexpected fields, addresses leak through filenames). Risk of leak; the unredacted parts go uninstrumented anyway, defeating the point.
- **Wire claude-context with Ollama "to be safe."** Ollama keeps the embedding generation local, but chunks still go to Milvus/Zilliz unless self-hosted. Self-host Milvus too or skip.
- **Use Pratiyush on session logs that touched the sensitive corpus.** Those sessions contain quoted sensitive content; ingestion egresses on the next sync.
- **Use claude-video on family interview recordings.** Whisper API call alone violates the constraint, never mind the frame analysis.
- **Treat "local LLM via Ollama" as automatically safe.** It is *vendor-egress-safe*, but the local model still produces outputs that may end up in shared logs, telemetry, or downstream commits. The local-only constraint extends to where the *outputs* are stored, not just where the inference happens.

## C-EC.4 Adoption order

1. **Inventory the egress boundary.** List the paths whose content cannot egress. Document in `CLAUDE.md` (paths + tools-not-to-run + cross-project egress confirmation rule). Reversible.
2. **Run `graphify .` configured to skip Pass 2.** Either via a flag or by running it without an active Claude Code session (Pass 2 is invoked through the invoking session — no session, no Pass 2). Get the Pass 1 topology. Verify no LLM calls were made. Reversible.
3. **Hand-curate the wiki layer.** Accept the velocity drop; that's the price. **Stop if** the curation cost exceeds recall benefit at the current corpus size — for under ~200 docs the manual approach may not earn its keep yet (consult Archetype A's tier-2 fallback).
4. **Add auto-memory entries as you work.** Per [`memory-system-patterns.md`](memory-system-patterns.md).
5. **Reconsider Lum1104 + local Ollama** only after you've maintained 50+ wiki pages by hand and want graph augmentation. **Run a measurement first** — see the evidence gaps below.
6. **Reconsider claude-video** only for the public sources subset (methodology talks, conference recordings). Maintain strict separation: a `sources/public/` subdir that the ingestion skill is allowed to touch, distinct from `sources/private/` that it never reads.

## C-EC.5 Constraint check

- **Local-first ✅ strict.** No tool in the primary stack egresses corpus content.
- **Markdown substrate ✅.** Same as Archetype C.
- **Augments-not-generates ✅.** No LLM authoring at all in the primary stack.
- **Graphify feeds wiki ✅** via Pass 1 only (topology only).
- **A/B/C evidence tiering preserved ✅.** Hand-curated wiki gives explicit control over claim provenance.
- **Wiki claims align with graph confidence ✅** trivially — graph is EXTRACTED-only since no Pass 2 means no INFERRED edges.

## C-EC.6 Evidence gaps and what we now know

**Gap 1 (still open): Lum1104 + local Ollama for the LLM-derived layer.** Untested in this repo. Highest-leverage experiment: take a 500-doc subset (synthetic clinical-note generator, or a redacted slice of a real journal corpus with permission); run Lum1104 against it with local Ollama (gemma3, qwen2.5, or llama3.3 — pick one and document); compare graph quality (edge precision, missed relationships, node naming consistency) vs. the same corpus with Claude/GPT Pass 2; document the quality degradation. *This is the missing evidence behind any local-LLM Pass 2 recommendation* — without it the C-EC.2 row is Tier D speculation, not C.

**Gap 2 (resolved + validated 2026-04-29): Is the unaugmented stack sufficient? Yes, when memory authorship is disciplined** — see [`archive/memory-systems-genealogy-baseline.md`](../archive/memory-systems-genealogy-baseline.md). The 9-query measurement scored 8/9 DEFINITIVE under the unaugmented stack alone; the PARTIAL was traced to a missing dedicated memory file for active brick walls, not to corpus size or augmentation absence. Experiment #1 validated the fix: authoring 5 dedicated brick-wall memory files (~6 min each) plus a flat-index entry per wall in `MEMORY.md` collapsed the failing query from 6-9 tool calls (PARTIAL) to **3 tool calls (DEFINITIVE)** — the validation subagent answered from `MEMORY.md`'s one-line index entries alone. Implications (Tier B from validated experiment):

- **Disciplined memory authoring** is what makes the unaugmented stack work, not augmentation per se. The pattern: `CLAUDE.md` routes; dedicated memory files behind a flat `MEMORY.md` index hold resolved-but-complex knowledge; rich one-line index summaries are answer-sufficient for list/synthesis queries.
- The cheapest improvement is more dedicated memory files, not graph infrastructure. ~6-10 min per file. Tool-call reduction: 5-9 reads → 1-3 reads on synthesis queries; classification typically upgrades by a tier.
- For projects with disciplined authoring, the marginal value of vendor-LLM Pass 2 augmentation is small enough that the egress constraint rarely makes augmentation worth fighting for.
- **Hard egress constraints are less of a recall handicap than originally framed.** The graph-augmentation case strengthens specifically when authoring is undisciplined, the corpus is too large for any single curator to maintain memory files for active topics, or there are multiple curators with inconsistent discipline.

**Gap 3 (still open): Comparative arm.** The genealogy baseline is a one-arm measurement. To rigorously claim "augmentation isn't needed" we need a second arm running Graphify Pass 2 + wiki + footer-injection against the same project + same query set, and a delta. The 2026-04-29 egress reframe means that arm is now feasible (vendor-LLM authorization granted by owner). Recommended next step.

---

# Archetype D (cross-project portfolio)

For managing **multiple knowledge-bearing repos as a portfolio** — preserving per-repo evidence and provenance while still surfacing cross-repo connections. Tier C — federation is hand-rolled today; the OpenBrain compilation-agent path is **Tier D** (not shipped).

## D1. Primary stack

**Per-repo (LLM Wiki + Graphify) + a thin federation index.**

| Layer                  | Owner                                                                                              | Why                                                                                          |
|------------------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Per-repo               | Karpathy wiki + Graphify (as in archetype A)                                                        | Preserves per-repo evidence tier and provenance                                              |
| Federation             | Small `~/portfolio/INDEX.md` + nightly cron merging per-repo `index.md` files                       | Axis 4 — federation, not consolidation                                                       |
| Cross-repo topology    | Second graphify run over all repos → cross-repo communities tagged INFERRED                         | Axis 8 — separates within-repo (EXTRACTED) from cross-repo (INFERRED)                        |

**Driving axes**: 4 (cross-tool/cross-repo), 2 (augments per repo), 8 (provenance discipline survives federation).

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

---

# Archetype E (work-state tracker)

For **temporal-dominant work tracking**: deadlines, commitments, decisions, people — content that mutates daily and would silently rot a topic-page wiki. Tier C — Rowboat verified at [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) (Apache 2.0, 13.1k stars, desktop app, 2026-04-28).

## E1. Primary stack

**Rowboat (typed entities, BYO-via-Composio) + a small LLM Wiki for the stable layer.**

| Layer       | Owner                                                                              | Why                                                                                                                  |
|-------------|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Temporal    | Rowboat-style typed-entity files (Decision/Commitment/Deadline/Person)             | Axis 6 — temporal-dominant; this is the differentiator                                                               |
| Stable      | Tiny Karpathy-style wiki for projects/people that don't change weekly               | Avoids "page becomes contradiction soup" failure                                                                     |
| Briefing    | Rowboat background agents                                                           | Daily briefing surfaces overnight changes                                                                            |

**Driving axes**: 6 (temporal), 8 (provenance per claim), 7 (markdown still — Rowboat README confirms "it's just Markdown").

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

---

# Archetype F (session-history archive)

For **mining AI-tool session history into durable knowledge**: extracting recurring rules, decisions, and conclusions from Claude Code / Codex / Cursor / Gemini transcripts. Tier C — Pratiyush verified MIT at [pratiyushpathak/llm-wiki](https://github.com/pratiyushpathak/llm-wiki) (2026-04-28). Native session resume and `/rewind` cover part of this slice for single-session recovery; this archetype is for durable cross-session mining.

## F1. Primary stack

**Pratiyush/llm-wiki (purpose-built) + Graphify on the resulting wiki for cross-session topology.**

| Layer        | Owner                                                                                     | Why                                                       |
|--------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| Ingestion    | Pratiyush adapters (Claude Code, Codex, Cursor, Gemini, Obsidian, Copilot)                 | Axis 4 — multi-agent coverage                             |
| Wiki         | Pratiyush three-layer (`raw/` → `wiki/` → `site/`)                                         | Provenance per session preserved in `raw/`                |
| Topology     | Graphify on the resulting wiki                                                              | Cross-session communities                                 |

**Driving axes**: 1 (write-time mining heavy), 8 (provenance per session essential), 4 (cross-tool adapters).

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

---

# Archetype G (team shared memory)

For **concurrent-write team shared memory** across multiple AI tools — where file substrate fails to concurrency and a database becomes structurally necessary. Tier C for query-time; **D** for the OpenBrain compilation agent (not shipped).

## G1. Primary stack — roadmap-contingent

**Today's honest recommendation: wait, or roll your own.** OpenBrain's write-time/compilation-agent half is roadmap, not shipped — recommending it as primary now would treat Tier D speculation as Tier C evidence.

- **Wait** for OpenBrain's compilation agent to ship and reproduce its claims.
- **Roll a minimal Postgres + pgvector + tiny MCP shim** with per-user wiki overlay. Boring, well-understood components; avoids FSL-1.1-MIT terms entirely.

**Once OpenBrain ships** (hypothetical future state): OpenBrain (Postgres + pgvector + AI gateway, Postgres RLS) + per-user Karpathy wiki overlay would be the stack.

| Layer            | Owner                                                                          | Why                                                          |
|------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------|
| Shared           | OpenBrain (Postgres + pgvector + AI gateway, Postgres RLS)                     | Axis 4 — cross-tool by definition; concurrency requires DB   |
| Per-user         | Personal Karpathy wiki overlay                                                  | Axis 2 — augments shared layer                               |
| Code (optional)  | claude-context with self-hosted Milvus + Ollama embeddings                     | If team needs code-specific semantic search and can host the infra |

**Driving axes**: 4 (cross-tool concurrency), 7 leans DB here, 5 (self-hosted = local-first if BYO model).

## G2. Hybrid alternatives

| Hybrid                                                 | Optimizes                                                        | Pick when                                                                |
|--------------------------------------------------------|-------------------------------------------------------------------|--------------------------------------------------------------------------|
| OpenBrain + claude-context (self-hosted)               | Code-heavy team workflows                                         | Significant fraction of team work is in code                             |
| OpenBrain + Pratiyush per-team snapshot                | Retrospectives over team sessions                                 | Heavy AI-tool adoption per-developer                                     |
| Roll your own (Postgres + pgvector + tiny MCP)         | Avoiding FSL terms                                                | FSL-1.1-MIT 2-year reciprocal unacceptable for commercial reuse          |

## G3. Anti-patterns

- **File-only markdown vault for a concurrent-write team**: file-conflict hell. Concurrent writes on file substrate fail.
- **OpenBrain for a single user**: MCP context tax + Postgres ops cost without the concurrency benefit. Use archetype C instead.

## G4. Adoption order

1. Two-person pilot with self-hosted Postgres+pgvector+MCP shim (or OpenBrain on Supabase).
2. Wire one MCP client (Claude Code) and one capture point (Slack or shared inbox). **Stop if** after two weeks no one queries the shared memory.
3. Add a second MCP client. Re-evaluate.
4. Defer compilation-agent integration until upstream ships and reproduces.

## G5. Constraint check

- Graphify feeds wiki: deferred until graph layer exists.
- No contradiction: ✅ via Postgres RLS + provenance columns.
- Tiering: ✅ as a column.
- Augments: ✅ at the per-user overlay.
- Local-first: ✅ self-hosted; ⚠️ only if BYO model.
- Markdown: ❌ — DB substrate justified by concurrency. Mitigate with periodic markdown export.

---

# Cross-cutting

## Migration paths

| From → To | What migrates                                                                  | What gets rebuilt                                                                |
|-----------|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| A → D     | Wiki convention; per-repo graphify configs; evidence-tier metadata              | Federation index; cross-repo graph as INFERRED-only view                         |
| C → G     | Markdown content (one-time export); wiki structure                              | Concurrency layer (Postgres); access control; per-user overlay re-pointed        |
| C → C-EC  | Wiki structure; conventions; wikilink-graph outputs                              | Drop Pass 2 / Pratiyush adapters / vendor embeddings; add egress-boundary CLAUDE.md rule; switch to hand-curation for wiki authoring |
| C-EC → C  | Wiki structure; conventions; the trust to run Pass 2                             | Decide explicitly which corpus paths can egress; restore Pass 2; test with a small slice first |
| F → A     | Promoted findings (durable rules, recurring decisions)                          | Hand-curated analyses with evidence tiers; raw transcripts to cold storage       |
| E → A     | Typed-entity content about completed projects becomes summary pages             | Temporal-lint cron dropped; structural lint takes over                           |
| B → D     | Per-repo graphify outputs federate                                              | Cross-repo graph; portfolio INDEX                                                |
| C → E     | Stable wiki pages stay; events split out into typed entities                     | Rowboat overlay; daily briefing                                                  |
| F → G     | Pratiyush-produced wiki                                                          | Concurrency, RLS, redaction policy review                                        |

## Never-combine list

| Combination                                                                                          | Failure                                                                                                                                                                                                |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pratiyush + MehmetGoekce on the same vault                                                            | Both want to author/organize the same wiki pages with different conventions; ingest passes overwrite each other's structure                                                                            |
| Graphify + Lum1104 on the same corpus *without designating one as authoritative*                       | Two topology layers with no defined merge; results disagree silently. Running both is fine if one explicitly drives the contradiction-lint and the other is read-only — pick which                      |
| `graphify --wiki` export + a hand-curated wiki on the same content                                     | Source-of-truth ambiguity; violates the graphify-feeds-wiki constraint                                                                                                                                 |
| claude-context + OpenBrain pgvector                                                                    | Two embedding indexes over similar content; doubled cost, drift, no defined merge strategy                                                                                                              |
| Rowboat + LLM Wiki on the same content scope                                                           | Page-per-topic vs typed-entity-per-event collide; backlinks point in conflicting directions                                                                                                            |
| OpenBrain Postgres + per-tool markdown vaults that diverge                                             | DB and files drift; neither is authoritative                                                                                                                                                            |

## License / cost gotchas

| Tool                                                                       | License                                                                  | Egress                                                                                                  | Commercial reuse                                                                                                                              |
|----------------------------------------------------------------------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Karpathy gist                                                              | None stated                                                              | n/a (paradigm)                                                                                          | Convention only, not redistributable code                                                                                                    |
| Graphify                                                                   | MIT ✅                                                                   | Pass 2 LLM calls go through invoking Claude Code session                                                | Free reuse; LLM cost via session; sensitive content leaves the box                                                                            |
| Pratiyush/llm-wiki                                                         | MIT ✅ (verified 2026-04-28)                                              | Depends on LLM choice                                                                                   | Free reuse; redaction-by-default per inventory                                                                                               |
| MehmetGoekce/llm-wiki                                                      | MIT ✅ (verified 2026-04-28)                                              | Depends on LLM choice                                                                                   | Free reuse                                                                                                                                    |
| Lum1104/Understand-Anything                                                | MIT ✅ (verified 2026-04-28)                                              | Depends on LLM choice                                                                                   | Free reuse                                                                                                                                    |
| claude-context                                                             | MIT ✅ on code                                                            | Code → embedding provider; chunks → Milvus/Zilliz                                                       | Free reuse of code; recurring infra + provider cost; egress disqualifies for proprietary code unless Ollama + self-hosted Milvus              |
| OpenBrain                                                                  | **FSL-1.1-MIT**                                                          | None if self-hosted + BYO model                                                                          | 2-year reciprocal restriction on competing managed services; converts to MIT after 2 years; internal commercial use fine                      |
| Rowboat ([rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat))    | **Apache 2.0** ✅ (verified 2026-04-28)                                   | Google services (Gmail/Calendar/Drive) by default; optional Deepgram, ElevenLabs, Exa, Composio API keys | Free reuse with attribution; Google + optional-vendor egress; desktop app, not a library                                                      |
| InfraNodus ([infranodus/](https://github.com/infranodus))                  | Proprietary SaaS (€12–66/mo); MIT MCP server + n8n nodes are open-source clients | Full content + GPT egress to InfraNodus servers                                                          | Subscription required for core; no self-hosted option; methodology is well-established (Paranyushkin / Nodus Labs, 10+ years)                 |
| SiYuan                                                                     | AGPL-3.0                                                                 | None (local app); community MCP server only                                                              | AGPL copyleft applies; block-level local app                                                                                                  |

## Build-vs-borrow

| Archetype | Off-the-shelf gap                                                            | Build locally                                                              |
|-----------|------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| A         | Footer-injection script; contradiction lint                                   | ~50–100 lines Python; reads `graph.json` + walks `analysis/*.md`           |
| B         | CI step to enforce reindex-on-PR                                              | One GitHub Action with `graphify .` + cache key                             |
| C         | "Promote-to-wiki" agent (graphify finding → wiki page draft for human review) | Local script ~1 day                                                         |
| C-EC      | Egress-boundary lint (catch a tool config that would egress flagged paths); Lum1104 + local Ollama testbed; baseline measurement script | ~1 day for the lint; testbed is a measurement project (baseline already done — see [`archive/memory-systems-genealogy-baseline.md`](../archive/memory-systems-genealogy-baseline.md)) |
| D         | Federation index across per-repo `index.md` files                              | 50-line script                                                             |
| E         | Temporal lint ("deadline shifted past today")                                  | Cron + small Python                                                         |
| F         | Multi-agent dedup (same conclusion across 3 agents → single page)              | Pratiyush partially does this; verify and extend                            |
| G         | RBAC policies on top of Postgres RLS                                           | Per-team policies; non-trivial                                              |

## Evidence gaps — top 5 Tier C → Tier B

| # | Claim                                                                | Experiment to move to Tier B                                                                                            |
|---|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| 1 | Graphify's 71.5× token-savings claim *(Tier C — vendor-reported, not independently benchmarked)*  | Reproduce on three corpora (pure code, pure prose, mixed); require ≥10× on at least two                                  |
| 2 | Claude-context ~40% reduction *(Tier C — vendor-reported, not independently benchmarked)*          | Reproduce on a real proprietary repo at 5k / 20k / 50k file sizes with a fixed query set                                  |
| 3 | Karpathy paradigm "compounding insight" benefit                        | Run a 6-month retention study on a real ~500-doc KB: does query latency on novel questions actually drop?                |
| 4 | Lum1104 wiki-aware vs graphify-on-wiki quality                         | A/B on the same vault; have a human rate edge usefulness blind                                                            |
| 5 | OpenBrain compilation agent (not shipped)                              | Wait for release; until then this is Tier D speculation, not C                                                            |

---

## Sources

### Tier A

- Direct license verification (2026-04-28) — Raw fetch of LICENSE files from raw.githubusercontent.com. Confirms: Pratiyush/llm-wiki = MIT, MehmetGoekce/llm-wiki = MIT, Lum1104/Understand-Anything = MIT, Rowboat = Apache 2.0.
- Direct read of safishamsi/graphify pyproject.toml (v1 branch, 2026-04-28) — Zero LLM SDK dependencies confirmed; Pass 2 LLM work happens via invoking Claude Code session.
- [archive/memory-systems-genealogy-baseline.md](../archive/memory-systems-genealogy-baseline.md) — Direct measurement across 3 genealogy projects, N=9 queries; 8/9 DEFINITIVE (89%) on the unaugmented stack; Tier B empirical evidence informing archetype C and C-EC. Archived 2026-07-10 as a dated measurement (claims dated 2026-04-29); the finding survives here and in §C-EC.6.
- [memory-systems-recommendation-methodology.md](memory-systems-recommendation-methodology.md) — Methodology, threshold math, assumption challenges, applied corrections, and the owner-authorized-egress deciding rule that underpin all per-archetype recommendations.

### Tier B

- Andrej Karpathy — LLM Wiki paradigm (April 2026). Tier B by author authority. Write-time wiki + ingest/query/lint workflows + bookkeeping-not-reading insight. Source for the Karpathy-convention requirements across archetypes C, C-EC, and F.
- OKF typed-vault hygiene (§C1b) — single production second-brain (project1), firsthand: `01-knowledge-base/_type-registry.md`, `automation/lib/okf.py`, `automation/orchestrator/quality_gates.py:validate_okf_type`, `automation/okf_health.py`, `automation/okf_signals.py`. Full pattern + anti-patterns in archetype-A §A1b. **One practitioner, one project, not independently corroborated.**

### Tier C

- Graphify 71.5× token-savings claim. **Vendor-reported — not independently benchmarked.**
- claude-context ~40% reduction claim. **Vendor-reported — not independently benchmarked.**
- OpenBrain $0.10–0.30/month cost estimate. **Vendor-reported — not independently benchmarked.**
- InfraNodus subscription pricing (€12–66/mo) — Proprietary SaaS pricing as listed; not independently verified. **Vendor-reported — not independently benchmarked.**
- [Google Cloud — Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) — Apache-2.0; [announced 2026-06-12](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing). Sole required frontmatter field is `type:`. Date/license/required-field verified against primary spec + blog (2026-06-21).
- [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) — Apache 2.0, 13.1k stars, desktop app for Mac/Windows/Linux, verified 2026-04-28. Typed-entity files, background briefing agents, Composio BYO integrations. **Community-reported star count and capability claims — not independently benchmarked.**
- [pratiyushpathak/llm-wiki](https://github.com/pratiyushpathak/llm-wiki) — MIT, verified 2026-04-28. Three-layer architecture (`raw/` → `wiki/` → `site/`), adapters for Claude Code, Codex, Cursor, Gemini, Obsidian, Copilot; redaction-by-default for keys/tokens. **Community-reported — not independently benchmarked.**
- Lum1104/understand-anything + local Ollama — cited as the C-EC.2 hybrid for LLM-derived relationships without vendor egress; explicitly labeled **untested in this repo** (Tier D leaning C).
- SiYuan — block-level local app (AGPL-3.0); cited as hybrid for atomic-note workflows; community MCP server only. **Community-reported — not independently benchmarked.**

---

## Related analyses

- [`memory-systems-archetype-a-curated-kb.md`](memory-systems-archetype-a-curated-kb.md) — archetype A, the heavily-routed primary (own file)
- [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md) — framing, threshold math, self-critique, and the owner-authorized-egress deciding rule
- [`memory-system-patterns.md`](memory-system-patterns.md) — earlier pattern survey (precedes this archetype-driven view); the auto-memory layer used by C-EC
- [`archive/federated-query-architecture.md`](../archive/federated-query-architecture.md) — archived spoke case study relevant to archetype D (evicted 2026-07-10; canonical depth in the spoke repos)
- [`archive/local-cloud-llm-orchestration.md`](../archive/local-cloud-llm-orchestration.md) — archived spoke case study on routing deterministic work locally and Pass 2 to a vendor *only when corpus permits* (evicted 2026-07-10)
- [`archive/memory-systems-genealogy-baseline.md`](../archive/memory-systems-genealogy-baseline.md) — the archived empirical baseline behind §C-EC.6

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/memory-system-patterns.md`](analysis/memory-system-patterns.md) [EXTRACTED (1.00)] — references
- [`INDEX.md`](INDEX.md) [EXTRACTED (1.00)] — references

<!-- graphify-footer:end -->
