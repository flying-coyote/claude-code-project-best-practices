---
status: EMERGING
last-verified: "2026-08-28"
measurement-claims:
  - claim: "Single-curator hand-curated KBs hit the wiki+graph+contradiction-lint payoff threshold around ~500 documents"
    source: "Working-memory-vs-relation-count math; not measured studies. Left expired 2026-11-04 for the owner: this is a ruling or napkin estimate, not a measurement, so there is nothing to re-run; decide whether it belongs in measurement-claims at all."
    date: "2026-04-28"
    revalidate: "2026-10-28"
  - claim: "Three of four 'check repo' tools verified MIT (Pratiyush, MehmetGoekce, Egonex-AI/Understand-Anything - formerly Lum1104); Rowboat is Apache 2.0. Unchanged on re-verification."
    source: "Direct fetch of LICENSE files via raw.githubusercontent.com + GitHub API licence field, two independent channels, 2026-08-28"
    date: "2026-08-28"
    revalidate: "2027-02-28"
    tier: A  # direct primary observation of the LICENSE files; the doc-level `evidence-tier: C` scopes the tool *recommendations*, not these licence facts
  # Split 2026-08-28: the two halves of the original single claim no longer have the same truth value.
  - claim: "graphify 0.9.51 has zero LLM SDKs among its 29 required dependencies; anthropic/openai/tiktoken/boto3 appear only under optional provider extras"
    source: "Direct read of Graphify-Labs/graphify pyproject.toml, version 0.9.51, 2026-08-28 (org moved from safishamsi/graphify, which no longer resolves; default branch now v8)"
    date: "2026-08-28"
    revalidate: "2026-11-28"
    tier: A
  - claim: "Pass 2 LLM work routes through the invoking Claude Code session ONLY on the /graphify skill path; headless `graphify extract` makes direct provider API calls via --backend with its own credentials"
    source: "Direct read of Graphify-Labs/graphify skills/graphify/skill.md Part B (Agent-tool dispatch) + README backend chain, 2026-08-28"
    date: "2026-08-28"
    revalidate: "2026-11-28"
    tier: A
  - claim: "The unaugmented stack (CLAUDE.md + auto-memory + raw file navigation) achieved 89% DEFINITIVE answers (8/9) on a baseline measurement across the genealogy trio, measured 2026-04-29"
    source: "archive/memory-systems-genealogy-baseline.md — N=9, Sonnet, self-classified, single-arm, measurer-authored queries (~±10% binomial CI). Frozen snapshot: the measured corpora are private, and the baseline memory state was intentionally mutated by Experiment #1's 20 added files."
    date: "2026-04-29"
    revalidate: never  # cannot be re-measured — corpora private, baseline state destroyed. Marked so it stops re-entering the expiry queue as an unresolvable action item.
  - claim: "Understand-Anything (Egonex-AI, formerly Lum1104) via local Ollama as a Pass-2 substitute is untested in this repo"
    source: "Repo search 2026-08-28: grep -ri ollama across tree, no .ua/ or .understand-anything/ dir, no research artifact, zero commits under git log -S ollama"
    date: "2026-08-28"
    revalidate: "2026-11-28"
  # Merged 2026-11-07 from memory-systems-recommendation-methodology.md (fold-in, owner ruling 2026-07-16), carried intact including the entries left expired for the owner.
  - claim: "Understand-Anything v2.9.4 `/understand-knowledge` gates on `has_index and md_count >= 3` only, resolving `index.md` case-insensitively; uppercase `INDEX.md` detects, and `raw/`, `log.md` and the root schema are signals but not gate conditions"
    source: "Direct execution of upstream `parse-knowledge-base.py` (fetched at Egonex-AI/Understand-Anything main, plugin.json version 2.9.4) against this repo, 2026-08-29: detected=true, format=karpathy, has_log=false, has_raw=false, md_count=345"
    date: "2026-08-29"
    revalidate: "2026-11-29"
    tier: A
  - claim: "Karpathy's LLM Wiki paradigm rates Tier B by author authority, not Tier C, despite April 2026 publication date"
    source: "Author authority on par with Boris Cherny on Claude Code; user-stated criterion 2026-04-28. Left expired 2026-11-04 for the owner: this is a ruling or napkin estimate, not a measurement, so there is nothing to re-run; decide whether it belongs in measurement-claims at all."
    date: "2026-04-28"
    revalidate: "2026-10-28"
  - claim: "Wiki+graph+contradiction-lint discipline starts paying back at ~500 docs for single-curator hand-curated KBs (rough working-memory math, not measured)"
    source: "Working-memory ~50-100 docs × cross-ref density K=3-5 → ~1,500-2,500 relations beyond mental tracking at 500 docs. Left expired 2026-11-04 for the owner: this is a ruling or napkin estimate, not a measurement, so there is nothing to re-run; decide whether it belongs in measurement-claims at all."
    date: "2026-04-28"
    revalidate: "2026-10-28"
  - claim: "Under the `/graphify` skill path, Pass 2 LLM work runs on the invoking Claude Code session's model via its Agent tool — graphify v1 has no API-key or backend path of its own"
    source: "Direct read of safishamsi/graphify v1 skills/graphify/skill.md Part B (Agent-tool dispatch) + graphify/extract.py + pyproject.toml (zero LLM SDK deps, zero egress symbols), 2026-08-28"
    date: "2026-08-28"
    revalidate: "2026-11-28"
    tier: A
  - claim: "Owner-authorized egress is the deciding constraint, not data category — public-source genealogy data with placeholder discipline can be opted-in (Wiley projects, 2026-04-29); same data without owner authorization or with un-anonymized living persons cannot"
    source: "User's reframe 2026-04-29; saved in feedback_genealogy_data_classification memory. Left expired 2026-11-04 for the owner: this is a ruling or napkin estimate, not a measurement, so there is nothing to re-run; decide whether it belongs in measurement-claims at all."
    date: "2026-04-29"
    revalidate: "2026-10-29"
evidence-tier: C
convergence: emerging  # AI-PKM caveat (B-F1 seed): emerging WITH license risk — Obsidian Smart Connections ~786K downloads but Jan-2026 proprietary switch (DR-6 verified)
applies-to-signals: [memory-systems, methodology, evidence-tiering, knowledge-base, second-brain, wiki, graph, md-corpus-small, md-corpus-design-target, md-corpus-large, md-corpus-very-large, vault-obsidian, vault-karpathy, project-type-docs, project-type-research, typed-memory-no-registry, code-search, monorepo, cross-project-synchronization, federation, work-tracker, temporal, session-history, transcript-mining, team-shared-memory, multi-tool-concurrency, corpus-sensitive, pii, sensitive-content, healthcare-data, legal-data, journal-third-parties]
revalidate-by: 2026-10-28
---

# Memory & Knowledge System Recommendations

One consolidated doc (folded 2026-07-10; formerly a two-level index over seven per-archetype files): the per-archetype table routes to sections *in this document* for archetypes B through G, while **Archetype A keeps its own file** ([`memory-systems-archetype-a-curated-kb.md`](memory-systems-archetype-a-curated-kb.md)) as the heavily-routed primary. Cross-cutting sections (migration paths, never-combine list, license/cost gotchas, build-vs-borrow, evidence gaps) follow the archetype sections, and the methodology and self-critique section (merged in 2026-11-07) comes last before the sources.

Calibrated to **~500-document curated knowledge bases** as the single-curator design target. See § Methodology and self-critique (near the end of this document; merged in 2026-11-07) for the framing, threshold math, self-critique, and applied corrections behind these recommendations — including the **owner-authorized-egress deciding rule** that governs the C-EC archetype.

**Convergence status**: `emerging` (AI-PKM function, per the 2026-07-12 convergence review), so the binding rule applies: adopting infrastructure from these recommendations requires converged status or an explicit owner exception.

> **Source documents** (read first):
>
> - `archive/memory-systems-tools-inventory.md` (research note, archived 2026-07-10) — factual catalog of 8 tools/paradigms with capabilities and licenses
> - `archive/memory-systems-architecture-axes.md` (research note, archived 2026-07-10) — 8 architectural axes that distinguish the tools
> - `archive/memory-systems-project-archetypes.md` (research note, archived 2026-07-10) — 7 archetypes A–G with axis profiles
>
> **Citation note.** Paths under `project1/` name files on the author's machine, not in this repository. They are recorded as **provenance for a single-practitioner production deployment** — enough to identify what was inspected and when — and are deliberately not hyperlinks, because no reader of this repository can follow them. Treat every `project1/` claim at the Tier-B bar this repo gives uncorroborated single-project evidence.
>
> **Revalidated 2026-08-28.** All four expired claims were re-checked against primary sources, and each verdict was then adversarially re-checked. **Two of the four moved**, and one of those changes a recommendation in this document:
>
> - **Graphify dependencies — SUPERSEDED, claim split.** The original single claim bundled two facts that no longer share a truth value. The dependency half still reproduces (0.9.51: zero LLM SDKs among 29 required deps). The routing half does **not**: current graphify ships `--backend` provider support, so headless `graphify extract` egresses directly. The Claude-Code-session routing holds **only on the `/graphify` skill path**. The repo also moved (`safishamsi/graphify` no longer resolves → [`Graphify-Labs/graphify`](https://github.com/Graphify-Labs/graphify)) and relicensed. **This changes the C-EC guidance below** — see § Archetype C-EC.
> - **Licences — CONFIRMED, unchanged.** Three MIT, Rowboat Apache 2.0, verified through two independent channels. Marked Tier A (direct primary observation) inside this Tier C doc. Watch trigger recorded: Understand-Anything transferred to `Egonex-AI` and its LICENSE now co-asserts a corporate holder.
> - **Genealogy baseline — UNVERIFIABLE, frozen.** The 8/9 number is faithfully transcribed, but it can never be re-measured: the corpora are private and the baseline memory state was intentionally mutated by Experiment #1. Restamped as a dated snapshot with `revalidate: never` so it stops re-entering the expiry queue as an unresolvable item.
> - **Ollama substitute — CONFIRMED.** Still untested here. But upstream *now documents* an Ollama path (added 2026-06-19, after this repo's v2.3.2 check), so the experiment got cheaper while the evidence gap stayed exactly the same size. See § Gap 1.
>
> Per [`evidence-tiers.md`](evidence-tiers.md) § Expired but not invalid, this is what the expiry marker is for. Flagged rather than silently carried, because an expired claim presented without a marker is the exact currency failure [`prose-corpus-discoverability.md`](prose-corpus-discoverability.md) measures.

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
| A | Curated analytical knowledge base          | Understand-Anything below ~200 docs; Graphify + footer-injection at the ~500-doc design target                              | [`memory-systems-archetype-a-curated-kb.md`](memory-systems-archetype-a-curated-kb.md) (own file) |
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

A cross-domain personal vault drifts into `type:` sprawl faster than a single-curator analytical KB, because there is no editorial reviewer between "I'll just call this one `idea-fragment`" and a graph with 86 single-use types. So if your vault types its notes — and it should, since a `type:` is what turns a personal pile into something a [Tolaria](#c2-hybrid-alternatives)-style MCP or a generated index can query by kind — govern the vocabulary the same way [archetype-A §A1b](memory-systems-archetype-a-curated-kb.md#a1b-typed-frontmatter-hygiene--okf-as-the-km-leverage-pattern) does: one canonical type-registry doc as the source of truth, a pre-commit guard that *parses* that registry (so it can't disagree with it), and a coverage/drift health check. This is the Google **OKF** pattern (one required field, `type:`; [spec](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md), Apache-2.0, [announced 2026-06-12](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) — verified against primary sources). The exact deployment this is drawn from — the registry, the parsed guard, and the graph-derived next-work signal — is a real production second-brain (`project1`: `01-knowledge-base/_type-registry.md`, `automation/lib/okf.py`, `automation/orchestrator/quality_gates.py`, `automation/okf_health.py`, `automation/okf_signals.py`); **Tier B, one practitioner, not independently corroborated.**

The pairing worth carrying over to a personal vault: **OKF stores what you know; the RETHINK limb re-asks whether it is still worth keeping.** A second brain accretes — half-finished ideas, links you meant to read, "decided last Tuesday" notes — and a typed graph lets a periodic re-examination filter by type to what is most likely dead weight (stale captures, never-resolved threads) instead of re-reading the whole vault. project1's `okf_signals.py` is that re-examination made mechanical; for a personal vault the lighter version is a scheduled pass that lists, by type, the notes most overdue for a look. **The signal that should route you here is `typed-memory-no-registry`** — a vault that types its notes but has no registry and no guard, which is exactly the sprawl trap above.

## C2. Hybrid alternatives

| Hybrid                                              | Optimizes                                                          | Pick when                                                          |
|-----------------------------------------------------|---------------------------------------------------------------------|--------------------------------------------------------------------|
| + OpenBrain (post-compilation-agent ship)           | Cross-tool concurrency                                              | Switching frequently between Claude Code, Cursor, ChatGPT          |
| + Rowboat sliver                                    | Capturing the temporal layer (deadlines, commitments) without polluting the structural wiki | Wiki accumulating "decided last Tuesday" pages                     |
| + Understand-Anything plugin                        | Wiki-aware graph view that uses your `[[wikilinks]]`                | Once the wiki has dense cross-refs                                 |
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

Variant of Archetype C for projects where the **owner has chosen not to authorize vendor-LLM egress** of corpus content. The constraint is policy, not data category — the deciding rule and its provenance live in § Methodology and self-critique → The egress deciding rule, below. Tier C overall; Karpathy paradigm is **B by author authority**; the local-LLM-Pass-2 substitute is **D-leaning-C** (untested in this repo); the 89%-baseline finding is **B** (project-artifact-based; see [`archive/memory-systems-genealogy-baseline.md`](../archive/memory-systems-genealogy-baseline.md)).

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
| Understand-Anything wiki-aware graph — LLM agents discover implicit relationships | Same egress profile — but see the 2026-08-28 correction in C-EC.4: "goes through the invoking session" is a property of the skill path, not of the tool |
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
4. **Understand-Anything ([Egonex-AI](https://github.com/Egonex-AI/Understand-Anything), formerly Lum1104) + local Ollama** for the LLM-derived layer (the C-EC.2 hybrid; **untested** in this repo).
5. **graphify `extract --backend ollama`** (added 2026-08-28). Current graphify documents a fully-local Ollama backend and an `OPENAI_BASE_URL` path for llama.cpp / vLLM / LM Studio. This is a genuine change to this archetype: graphify's Pass 2 is **no longer categorically disqualified** under an egress constraint — conditional on the explicit backend flag and the environment audit in C-EC.4 step 2. Untested here; quality against a local model is unmeasured (Gap 1 covers the same question).

The Pass 1 line above keeps Graphify in the recommendation only because it does meaningful work on *mixed* corpora (some code + some prose). On pure-prose corpora, replace it with the wikilink-graph approach.

## C-EC.2 Hybrid alternatives (with caveats)

| Hybrid                                              | What it adds                                                          | What you trade                                                                                   |
|-----------------------------------------------------|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| + Understand-Anything ([Egonex-AI](https://github.com/Egonex-AI/Understand-Anything), formerly Lum1104) via local Ollama | LLM-derived implicit relationships without vendor egress              | Quality drops vs. Claude/GPT (Tier C inferred from inventory; **untested locally**); setup cost  |
| + graphify `extract --backend ollama` *(new 2026-08-28)* | Graphify's own Pass 2, kept local — no longer a vendor-egress path | Explicit flag is load-bearing (the default chain reaches Ollama **last**); quality against a local model unmeasured; **untested here** |
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
2. **Run graphify with Pass 2 explicitly disabled: `--code-only`, or `--backend ollama` if you want a local Pass 2.** Get the Pass 1 topology. Verify no LLM calls were made. Reversible.

   > **Corrected 2026-08-28 — the previous wording here was unsafe.** This step used to read "run it without an active Claude Code session (Pass 2 is invoked through the invoking session — no session, no Pass 2)." That was true of graphify v1 and is **false of current versions**. Headless `graphify extract` auto-detects a provider from the environment and walks a chain (Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama), so a host with any provider credential present **egresses silently** with no session involved. Worse, *absence of API keys is not sufficient either*: `--backend claude-cli` needs no key (it rides the Claude subscription) and Bedrock needs none (IAM via the ambient AWS provider chain). The precondition is an **explicit backend flag**, not an inferred one. Audit the environment as well, but do not rely on the audit alone.
3. **Hand-curate the wiki layer.** Accept the velocity drop; that's the price. **Stop if** the curation cost exceeds recall benefit at the current corpus size — for under ~200 docs the manual approach may not earn its keep yet (consult Archetype A's tier-2 fallback).
4. **Add auto-memory entries as you work.** Per [`memory-system-patterns.md`](memory-system-patterns.md).
5. **Reconsider a local-model Pass 2** — either Understand-Anything + Ollama, or graphify's own `--backend ollama` — only after you've maintained 50+ wiki pages by hand and want graph augmentation. **Run a measurement first** — see the evidence gaps below.
6. **Reconsider claude-video** only for the public sources subset (methodology talks, conference recordings). Maintain strict separation: a `sources/public/` subdir that the ingestion skill is allowed to touch, distinct from `sources/private/` that it never reads.

## C-EC.5 Constraint check

- **Local-first ✅ strict.** No tool in the primary stack egresses corpus content.
- **Markdown substrate ✅.** Same as Archetype C.
- **Augments-not-generates ✅.** No LLM authoring at all in the primary stack.
- **Graphify feeds wiki ✅** via Pass 1 only (topology only).
- **A/B/C evidence tiering preserved ✅.** Hand-curated wiki gives explicit control over claim provenance.
- **Wiki claims align with graph confidence ✅** trivially — graph is EXTRACTED-only since no Pass 2 means no INFERRED edges.

## C-EC.6 Evidence gaps and what we now know

**Gap 1 (still open): a local-model Pass 2 for the LLM-derived layer.** Untested in this repo. Highest-leverage experiment: take a 500-doc subset (synthetic clinical-note generator, or a redacted slice of a real journal corpus with permission); run Understand-Anything against it with local Ollama (gemma3, qwen2.5, or llama3.3 — pick one and document); compare graph quality (edge precision, missed relationships, node naming consistency) vs. the same corpus with Claude/GPT Pass 2; document the quality degradation. *This is the missing evidence behind any local-LLM Pass 2 recommendation* — without it the C-EC.2 row is Tier D speculation, not C.

> **Revalidated 2026-08-28: cheaper to run, exactly as unevidenced.** Upstream now documents an Ollama path in the README Quick Start — added by commit `7f5a717` on **2026-06-19** ("docs: note local-model option and token-usage expectations in install steps"), i.e. *after* this repo's 2026-04-28/30 verification against v2.3.2. Graphify has since added `--backend ollama` too. So the experiment is materially cheaper than when this gap was written. **The evidence gap is unchanged in size**: neither project publishes quality data for the local path, and this is provider delegation rather than first-party integration. The C-EC.2 rows stay at **D-leaning-C**. Note also that the version tested here (v2.3.2) is now six minor versions stale against v2.9.4, which stales the `/understand-knowledge` Karpathy-gate verification recorded in [`DECISIONS.md`](../DECISIONS.md) and every `.understand-anything/` path reference in this cluster (upstream default is now `.ua/`, with the legacy directory still honoured — so those references are stale, not broken).

**Gap 2 (resolved for this portfolio as of 2026-04-29, pending Gap 3's comparative arm): Is the unaugmented stack sufficient? Yes, when memory authorship is disciplined** — see [`archive/memory-systems-genealogy-baseline.md`](../archive/memory-systems-genealogy-baseline.md). The 9-query measurement scored 8/9 DEFINITIVE under the unaugmented stack alone; the PARTIAL was traced to a missing dedicated memory file for active brick walls, not to corpus size or augmentation absence.

> **Read this as a dated snapshot, not a live finding (restamped 2026-08-28).** The measurement is **N=9, Sonnet, self-classified, single-arm, with measurer-authored queries** — roughly ±10% binomial CI on 8/9. It also **cannot be re-measured**: the corpora are private, and the baseline memory state was intentionally mutated by Experiment #1's 20 added brick-wall files. The claim is therefore marked `revalidate: never` in this document's frontmatter — frozen rather than expiring, so it stops re-entering the quarterly queue as an item nobody can close. Calling it "resolved + validated", as this heading did until 2026-08-28, was stronger than a nine-query single-arm measurement supports. Experiment #1 validated the fix: authoring 5 dedicated brick-wall memory files (~6 min each) plus a flat-index entry per wall in `MEMORY.md` collapsed the failing query from 6-9 tool calls (PARTIAL) to **3 tool calls (DEFINITIVE)** — the validation subagent answered from `MEMORY.md`'s one-line index entries alone. Implications (Tier B from validated experiment):

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

For **mining AI-tool session history into durable knowledge**: extracting recurring rules, decisions, and conclusions from Claude Code / Codex / Cursor / Gemini transcripts. Tier C — Pratiyush verified MIT at [Pratiyush/llm-wiki](https://github.com/Pratiyush/llm-wiki) (re-verified 2026-08-28; the old `pratiyushpathak/` slug no longer resolves). Native session resume and `/rewind` cover part of this slice for single-session recovery; this archetype is for durable cross-session mining.

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
| Graphify + Understand-Anything on the same corpus *without designating one as authoritative*                       | Two topology layers with no defined merge; results disagree silently. Running both is fine if one explicitly drives the contradiction-lint and the other is read-only — pick which                      |
| `graphify --wiki` export + a hand-curated wiki on the same content                                     | Source-of-truth ambiguity; violates the graphify-feeds-wiki constraint                                                                                                                                 |
| claude-context + OpenBrain pgvector                                                                    | Two embedding indexes over similar content; doubled cost, drift, no defined merge strategy                                                                                                              |
| Rowboat + LLM Wiki on the same content scope                                                           | Page-per-topic vs typed-entity-per-event collide; backlinks point in conflicting directions                                                                                                            |
| OpenBrain Postgres + per-tool markdown vaults that diverge                                             | DB and files drift; neither is authoritative                                                                                                                                                            |

## License / cost gotchas

| Tool                                                                       | License                                                                  | Egress                                                                                                  | Commercial reuse                                                                                                                              |
|----------------------------------------------------------------------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Karpathy gist                                                              | None stated                                                              | n/a (paradigm)                                                                                          | Convention only, not redistributable code                                                                                                    |
| Graphify ([Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify), was `safishamsi/`) | **v1: MIT. Current (`v8` default): Apache-2.0**, MIT retained in `license-files` — not a clean swap (verified 2026-08-28) | **Depends on the invocation path.** `/graphify` skill path: Pass 2 runs on the invoking Claude Code session. Headless `graphify extract`: direct provider egress unless `--code-only` or an explicit `--backend ollama` | Free reuse under either licence; LLM cost via session *or* via your own provider key; sensitive content leaves the box unless the backend is pinned local |
| [Pratiyush/llm-wiki](https://github.com/Pratiyush/llm-wiki)                | MIT ✅ (re-verified 2026-08-28)                                           | Depends on LLM choice                                                                                   | Free reuse; redaction-by-default per inventory                                                                                               |
| MehmetGoekce/llm-wiki                                                      | MIT ✅ (re-verified 2026-08-28)                                           | Depends on LLM choice                                                                                   | Free reuse                                                                                                                                    |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) (formerly `Lum1104/`) | MIT ✅ (re-verified 2026-08-28) — LICENSE now co-asserts "Yuxiang Lin" **and** "Infinite Universe, Inc." | Depends on LLM choice                                                                                   | Free reuse. **Licence-change watch trigger**: org transfer + corporate copyright assignment is the Obsidian Smart Connections shape this doc's frontmatter already flags |
| claude-context                                                             | MIT ✅ on code                                                            | Code → embedding provider; chunks → Milvus/Zilliz                                                       | Free reuse of code; recurring infra + provider cost; egress disqualifies for proprietary code unless Ollama + self-hosted Milvus              |
| OpenBrain                                                                  | **FSL-1.1-MIT**                                                          | None if self-hosted + BYO model                                                                          | 2-year reciprocal restriction on competing managed services; converts to MIT after 2 years; internal commercial use fine                      |
| Rowboat ([rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat))    | **Apache 2.0** ✅ (re-verified 2026-08-28)                                | Google services (Gmail/Calendar/Drive) by default; optional Deepgram, ElevenLabs, Exa, Composio API keys | Free reuse with attribution; Google + optional-vendor egress; desktop app, not a library                                                      |
| InfraNodus ([infranodus/](https://github.com/infranodus))                  | Proprietary SaaS (€12–66/mo); MIT MCP server + n8n nodes are open-source clients | Full content + GPT egress to InfraNodus servers                                                          | Subscription required for core; no self-hosted option; methodology is well-established (Paranyushkin / Nodus Labs, 10+ years)                 |
| SiYuan                                                                     | AGPL-3.0                                                                 | None (local app); community MCP server only                                                              | AGPL copyleft applies; block-level local app                                                                                                  |

## Build-vs-borrow

| Archetype | Off-the-shelf gap                                                            | Build locally                                                              |
|-----------|------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| A         | Footer-injection script; contradiction lint                                   | ~50–100 lines Python; reads `graph.json` + walks `analysis/*.md`           |
| B         | CI step to enforce reindex-on-PR                                              | One GitHub Action with `graphify .` + cache key                             |
| C         | "Promote-to-wiki" agent (graphify finding → wiki page draft for human review) | Local script ~1 day                                                         |
| C-EC      | Egress-boundary lint (catch a tool config that would egress flagged paths); local-Ollama Pass-2 testbed (Understand-Anything or graphify `--backend ollama`); baseline measurement script | ~1 day for the lint; testbed is a measurement project (baseline already done — see [`archive/memory-systems-genealogy-baseline.md`](../archive/memory-systems-genealogy-baseline.md)) |
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
| 4 | Understand-Anything wiki-aware vs graphify-on-wiki quality                         | A/B on the same vault; have a human rate edge usefulness blind                                                            |
| 5 | OpenBrain compilation agent (not shipped)                              | Wait for release; until then this is Tier D speculation, not C                                                            |

---

# Methodology and self-critique

> **Merged 2026-11-07** from `memory-systems-recommendation-methodology.md` (fold-in approved by owner ruling 2026-07-16, batched to the 2026-09-30 session, executed 2026-11-07). The pre-merge snapshot is at [`archive/memory-systems-recommendation-methodology.md`](../archive/memory-systems-recommendation-methodology.md). This section explains *why* the recommendations above are calibrated to ~500-document curated KBs, which assumptions in the underlying constraints are weaker than they look, where the analysis is structurally weak, and what corrections were applied during iteration.
>
> **Revalidated 2026-08-28 (methodology claims) — the claim holds, but its *warrant* was unsound and one corollary is now false.** The conclusion (Pass 2 runs on the invoking session) is confirmed by direct mechanism evidence: `skills/graphify/skill.md` Part B dispatches Pass 2 through the invoking session's Agent tool — *"MANDATORY: You MUST use the Agent tool here"* — and there is no API-key or backend path in v1. But the reasoning recorded here was **"confirmed by zero LLM SDK deps"**, and absence of a dependency does not prove absence of egress: graphify's own current `claude-cli` backend is a zero-SDK-dependency direct-egress path. Cite the dispatch mechanism; use the dependency list only as corroboration.
>
> Two consequences, both applied below: the claim is now **scoped to the `/graphify` skill path** (headless `graphify extract` has its own provider chain), and assumption #5's corollary that *"pointing graphify at a local model is not a documented configuration"* is **retired as false** — see assumption #5 below.
>
> Per [`evidence-tiers.md`](evidence-tiers.md) § Expired but not invalid, this is what the expiry marker is for: it caught a reasoning defect that a silent re-date would have carried forward as a repo-wide proof pattern.

## What this analysis is FOR

The recommendations target **~500-document curated knowledge bases** — the scale at which the wiki + graph + contradiction-lint discipline starts paying back for a single curator without active automated ingestion. This is the design target, not the only valid scale.

**Convergence gate**: the function this analysis serves (AI-PKM) is rated `emerging` in this document's frontmatter, and because infrastructure adoption requires converged status or an explicit owner exception, the recommendations here calibrate the adoption decision without clearing that gate.

### Why ~500?

A single curator can hold ~50–100 docs in active mental review. With average cross-reference density K=3–5 per doc, 500 docs implies 1,500–2,500 relations to keep coherent — beyond mental tracking. The lint goes from "nice-to-have" at 28 to "load-bearing" at 500 over roughly an order of magnitude.

| Scale | Lint discipline | Recommendation |
|---|---|---|
| ≤ 50 docs | Excess | Plain markdown + manual cross-refs |
| 50–200 docs | Optional | Wikilinks + Understand-Anything plugin (if you want a graph view) |
| 200–500 docs (single curator) | Increasingly load-bearing | Add graphify + footer-injection + contradiction lint |
| ≥ 500 docs (single curator) | Load-bearing | Full design-target stack |
| Multi-author or active automated ingestion | Threshold compresses to ~100–200 | Adopt earlier |

**Caveat on the ~500 number**: this is rough working-memory-vs-relation-count math, not measured studies. Treat with ±50% confidence interval. An earlier draft of this methodology cited "200+ docs"; ~500 is more defensible as the *single-curator* threshold, while 200 is closer for multi-author or active-ingestion projects.

### Far-larger projects

Projects 12×–40× the design target (6k–20k+ markdown vaults with active ingestion and federation) run on heavily customized stacks tailored to their specifics. The archetype recommendations here are useful as upper-bound sanity checks but are not the calibration scale.

---

## Tier discipline

| Source class | Tier | Examples |
|---|---|---|
| Recognized thought leaders, paradigm-level claims | **B** by author authority | Karpathy LLM Wiki paradigm; Boris Cherny on Claude Code |
| Tool-specific quantitative benchmarks (vendor-reported) | **C** until reproduced | Graphify's 71.5× token claim; claude-context's ~40% reduction; OpenBrain's $0.10–0.30/month |
| Roadmap claims (not shipped) | **D** | OpenBrain's compilation agent |
| Verified factual claims (e.g., licenses) | **A** when directly verified | Pratiyush MIT, MehmetGoekce MIT, Understand-Anything MIT, Rowboat Apache 2.0 (dated 2026-04-28; all four re-verified unchanged 2026-08-28) |

**Important**: this corrects an earlier draft that downgraded Karpathy's paradigm to Tier C purely on recency. Recency does not auto-downgrade an author-authority source. The paradigm claim ("write-time wiki + ingest/query/lint workflows + bookkeeping-not-reading insight") is Tier B from publication; only the tool-specific implementations need independent reproduction to move from C to B.

---

## The egress deciding rule (owner authorization, not data category)

The constraint that routes a project to the C-EC archetype is **whether the owner has authorized vendor-LLM egress of the corpus**, not what category the data falls in. The proof case: the Wiley genealogy projects were originally framed as PII-constrained (the archetype was even named C-PII), but the owner reframed them on 2026-04-29 — living-person names use anonymized placeholders, the remaining content is public-source (FamilySearch, Ancestry, WikiTree, Find a Grave), so vendor-LLM egress is acceptable *at the owner's choice*. The same data without that authorization, or with un-anonymized living persons, cannot egress. Data category predicts where the constraint is likely; owner authorization is what actually decides it, so ask for the ruling rather than inferring it from content type.

The fine-grained sensitivity tags (`pii`, `sensitive-content`, `healthcare-data`, `legal-data`, `journal-third-parties`) refine the coarse `corpus-sensitive` signal *within* § Archetype C-EC above; the coarse row remains the top-level routing gate for the LLM-egress decision.

---

## Eight assumptions worth challenging before adopting

These are pushbacks on the user-stated constraints and on my own framing — surfaced upfront so a reader can apply judgment rather than treating the recommendations as decided.

### 1. "Graphify feeds wiki" is a feature you have to build, not one graphify ships

Graphify offers `--wiki` *export* (graph **generates** a wiki) and a hook system that fires on Glob/Grep. Neither of these is "feed findings into your existing markdown." The promotion path is custom glue (the footer-injection script in adoption step A4-3). If you don't write and maintain that script, you'll get the parallel-artifact failure your constraint is supposed to prevent.

**Implication**: scope the footer-injection script as load-bearing infrastructure. If you don't have appetite to maintain it, prefer Understand-Anything (which works *over* your existing wiki and wikilinks) over graphify (which assumes you'll write the bridge).

### 2. For prose-heavy corpora, graphify's "deterministic" pitch mostly evaporates

Tree-sitter Pass 1 (the deterministic, EXTRACTED-tag pass) returns ~nothing useful from `.md` files containing argumentation. The provenance discipline collapses to mostly INFERRED for an analytical-prose KB. The contradiction lint then has very little EXTRACTED bedrock to anchor against. **Determinism is for code corpora, not for prose corpora.** The inventory and axes docs don't make this distinction sharply enough.

### 3. The contradiction discipline scales sharply — calibrate to ~500 docs, not your local scale

At 28 docs (this repo's scale), a contradiction-lint is excess. At ~500 docs (the design target), the math flips: 1,500–2,500 relations, beyond mental tracking, silent drift inevitable. Multi-author or active automated ingestion compresses the threshold to ~100–200.

**Implication**: write recommendations for the ~500-doc design target, not for whatever scale you happen to be testing at. The lint is correct at 500 even where it's over-engineered at 28.

### 4. Karpathy's paradigm is Tier B by author authority

(See "Tier discipline" above.) An earlier draft downgraded it to Tier C on recency grounds. That was wrong — Karpathy is a recognized authority and his paradigm carries author-weight. Tool-specific quantitative claims still stay Tier C until independently reproduced; the paradigm itself does not.

### 5. "Local-first" for graphify is a half-truth on prose

Pass 1 (Tree-sitter) is local. Pass 2 (LLM concept extraction) is **not** — content goes to whatever LLM the invoking Claude Code session is using. On a prose KB, Pass 2 is *most of the signal*. So "graphify is local" reads as a privacy claim it doesn't make for prose.

**Sub-finding, re-sourced 2026-08-28.** The mechanism, stated correctly: `skills/graphify/skill.md` Part B dispatches Pass 2 through the **invoking session's Agent tool** ("MANDATORY: You MUST use the Agent tool here"), and graphify v1 carries no API-key or backend path of its own. The `pyproject.toml` dependency list (zero `anthropic`, `openai`, `litellm`) **corroborates** this; it does not establish it. That distinction matters beyond this doc — do not model absence-of-dependency as a proof of no-egress anywhere in this repository, because graphify's own current `claude-cli` backend is a zero-SDK-dependency path that egresses.

**Retired 2026-08-28 — this sub-finding used to end with a claim that is now false.** It read: *"Pointing graphify at a local model (e.g., Gemma 4) is not a documented configuration."* Current graphify documents `--backend ollama` as a fully-local path, ships an `ollama` extra, and documents `OPENAI_BASE_URL` for llama.cpp / vLLM / LM Studio. Local Pass 2 is now a **first-class documented configuration**, which *strengthens* rather than weakens the egress-constrained recommendation in § Archetype C-EC above.

> **But the local path is opt-in, and the default is not local.** `graphify extract` auto-detects a provider from the environment along a chain that reaches **Ollama last** (Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama), so a host with any provider credential present egresses silently. Absence of API keys is *not* a sufficient precondition either: `--backend claude-cli` needs no key (it rides the Claude subscription) and Bedrock needs none (IAM via the ambient AWS chain). State the finding as **"no longer categorically disqualified for egress-constrained prose corpora, conditional on an explicit `--backend ollama` and an environment audit"** — never as unconditional clearance.

### 6. Archetype purity is a useful frame but a misleading recommendation surface

Most real projects mix archetypes (e.g., A+F, C+E, A+D+F). Recommending one primary stack per archetype is useful for *framing*; real adoption needs to layer two archetypes' stacks selectively. Treat the per-archetype primaries above as orthogonal building blocks, not committed package deals.

### 7. Understand-Anything's "wiki-aware" framing requires Karpathy filename conventions, not just `[[wikilinks]]` (added 2026-04-28)

Verified 2026-04-28 against plugin v2.3.2: `/understand-knowledge`'s detector (`parse-knowledge-base.py`) gates on `index.md` (lowercase, at root or under `wiki/`) + ≥3 markdown files. `log.md`, `raw/`, and a root schema (`CLAUDE.md`/`AGENTS.md`) are detected but not required. Repos using `INDEX.md` uppercase, or routing schema to `.claude/CLAUDE.md` (this repo's case), fail detection. **No longer true upstream (re-verified 2026-08-29 against v2.9.4).** The detector now resolves `index.md` case-insensitively (`find_markdown_case_insensitive`, exact match wins), and the gate is `has_index and md_count >= 3` alone — `has_log`, `has_raw` and `has_schema` are collected as signals but not gated on, so the schema-location half was never load-bearing. Executed against this repo, which has only uppercase `INDEX.md`, v2.9.4 returns `detected: true, format: karpathy` (md_count 345). The v2.3.2 reading above stays as a dated record: its source could not be retrieved to re-check it (the tag 404s on raw.githubusercontent and the GitHub API is outside this session's repo scope), so whether it was accurate then is not decidable from here — only that it does not describe the current plugin.

**Implication**: the archetype-A "Understand-Anything alone over a hand-curated wiki" recommendation is conditional on Karpathy filename discipline, not just on having wikilinks. Renaming `INDEX.md` → `index.md` is a small change but breaks tooling that hardcodes the uppercase form (`automation/generate_index.py` here). **That rename is no longer needed** — v2.9.4 resolves the name case-insensitively, so the cost/benefit this sentence weighed has gone to zero on one side. The assumption's *substance* survives the correction and is why it is kept: a recommendation resting on an undocumented filename gate was fragile in exactly the way that mattered, and the gate moved. What changed is the direction of the failure, not whether recommend-time layout checks are worth doing. The general `/understand-anything:understand` skill is the fallback for repos that don't match — but that's a different code path with its own assumptions, not a drop-in. Document the layout requirement at recommend-time, not at adoption-time.

### 8. Graphify Pass 1 alone is not a topology layer for prose-heavy KBs (added 2026-04-28)

Empirical run, 2026-04-28, this repo at 38 analysis docs + supporting code, graphify v0.5.4. **Pass 1** (`graphify update .`, Tree-sitter only, zero LLM calls): 243 nodes / 427 edges / 73% EXTRACTED — but **0 of 38 `analysis/*.md` docs received nodes**. Pass 1's extraction model is code-only.

**Pass 2** run later the same day (8 parallel general-purpose subagents over 162 files, ~22 files/chunk): **1187 nodes / 1651 edges / 67 communities / 88% EXTRACTED / 24 hyperedges**. 251 nodes were anchored to `analysis/*.md` docs (≈6.6 concept nodes per analysis doc). Token-reduction benchmark on the resulting graph: **57.5× vs naive full-corpus** (graphify's marketing claim is 71×; this run hit 57.5× on the real corpus). Footer-injection re-run after Pass 2 found cross-file edges for **33 of 38 analysis docs** (file-level aggregation; node-level lookup returned zero — see implication below).

**Implications**:

1. **Pass-2-or-no-graphify is the primary decision**, not a footnote. Without Pass 2, graphify is a code-only AST tool with no awareness of prose; with it, graphify becomes a topology layer that captures explicit cross-references and surfaces non-obvious semantic similarities (e.g., the 24 hyperedges include a {memory-archetype-b, -d, -e, -f} grouping the prose itself never names as a set). Update archetype-A's adoption-order step 1 to make this decision explicit before any tooling install.

2. **Egress framing was correct**. Pass 2 ships document content to whatever LLM the invoking session uses. The earlier reversibility-except-egress framing applies in full and is the gate that determines whether graphify is even a viable topology layer for sensitive prose corpora.

3. **File-level aggregation matters for prose footers**. Each markdown file produces many concept nodes (mean 6.6, max 28 in this run), not one. Footer-injection scripts that look up edges by *file-path-as-node-id* return zero edges; they have to aggregate node-level edges by `source_file` to produce a "Related" footer. The script in `scripts/graphify_footer_inject.py` was updated 2026-04-28 to do this; the original node-keyed lookup was a code-corpus assumption that doesn't survive contact with prose.

4. **Subagent model selection is a real cost lever**. The 8 Pass 2 subagents each consumed 80k–190k tokens on the parent's Opus 4.7. Subagent extraction is mechanical structured output; pass `model: "sonnet"` to graphify-style fan-outs (or run graphify under a Sonnet-default Claude Code session) and the run is 4–8× cheaper with no quality difference observed.

---

## Three places the analysis is structurally weak

- **Reversibility framing on adoption-order step 1s**: deleting a graphify output folder undoes the local index, but Pass 2 has already shipped content to whatever LLM the invoking session uses, and that egress is not reversible. This document now distinguishes "reversible-local" from "reversible-except-egress" but the broader pattern — that any LLM-touching tool's first run is egress-irreversible — applies across many recommendations and is not consistently flagged.

- **The "never combine graphify + Understand-Anything" rule was overstated initially**. They're architecturally different: Understand-Anything uses your `[[wikilinks]]` as ground truth; graphify discovers structure via AST + LLM passes. Running both *can* be coherent if one is explicitly authoritative and the other is read-only. The never-combine entry (§ Never-combine list above) has been softened to reflect this; the absolute version was wrong.

- **Evidence-gap list misses the foundational experiment**. The deepest unknown isn't graphify's 71× token claim — it's whether wiki + graph beats plain markdown + good cross-refs at 30-doc scale, at 500-doc scale, and at 5,000-doc scale. That requires 3+ months of A/B on real query patterns at each scale. Without it, every recommendation is sophisticated guessing about the payoff curve.

---

## Two reframings worth considering

- **Archetype A's right answer splits by scale.** Below ~200 docs: "good wikilinks + Understand-Anything, defer everything else" — it respects existing wikilinks and is strictly downstream; manual cross-referencing is tractable. At ~500 docs: automated graphify becomes necessary, footer-injection glue is worth maintaining, contradiction-lint earns its keep. Don't over-generalize a small-scale recommendation to design-target projects, or vice versa.

- **OpenBrain as the archetype-G primary is contingent on a feature that hasn't shipped.** Recommending OpenBrain *now* treats Tier D speculation as Tier C evidence. The honest archetype-G primary today is "wait for the compilation agent to ship and reproduce its claims, OR roll a minimal Postgres + pgvector + tiny MCP shim yourself." OpenBrain's full stack is recorded in § Archetype G above as a forward-planning state, not a current adoption.

---

## Applied corrections during iteration

The recommendations above reflect these corrections from earlier drafts:

| Correction | What changed |
|---|---|
| Archetype A primary stack split by scale | Understand-Anything-only added as the explicit primary at <~200 docs; graphify+footer-injection remains the primary at ~500-doc design target |
| Archetype G flagged as roadmap-contingent | "Wait or roll your own Postgres+pgvector+MCP" is the recommendation today; full OpenBrain stack captured as future state |
| Adoption-order step 1s distinguish reversibility classes | Reversible-local vs reversible-except-egress; LLM Pass 2 = irreversible egress |
| Never-combine graphify+Understand-Anything softened | Allowed if one is explicitly authoritative |
| Karpathy paradigm Tier B by author authority | Corrected from prior Tier C downgrade |
| Threshold calibrated to ~500 docs | Earlier "200+" replaced with the more defensible single-curator threshold; 100–200 noted for multi-author or active-ingestion |
| All four "check repo" licenses verified 2026-04-28 | Pratiyush, MehmetGoekce, Understand-Anything = MIT; Rowboat = Apache 2.0 (rowboatlabs/rowboat). Re-verified unchanged 2026-08-28 |
| Rowboat description corrected | README lists Google Gmail/Calendar/Drive + optional Composio MCP (not Granola/Fireflies as the inventory had) |
| InfraNodus added to license/cost table | Acknowledged as paradigm alternative (text network analysis) but doesn't fit local-first + markdown-substrate constraints |

---

## What I shouldn't have shortcut

- "(analyses are public)" was used to justify graphify Pass 2 egress on this repo. Public-on-GitHub bounds external-disclosure harm; it does not address vendor retention, what bulk-indexers actually ship (the whole working tree, not just the public-by-intent subset), or future drift. The honest framing is: "the action is reversible-bounded-not-undoable; even public content's egress is one-way; verify what would ship before running."

- Treating every April-2026 tool as Tier C uniformly. Author authority distinguishes paradigm claims from tool implementations. Karpathy's paradigm carries weight; a specific implementation's benchmark does not, until reproduced.

---

## Sources

### Tier A

- Direct license verification (2026-04-28; **re-verified 2026-08-28** through two independent channels — raw LICENSE fetch plus the GitHub API licence field). Confirms, unchanged: Pratiyush/llm-wiki = MIT, MehmetGoekce/llm-wiki = MIT, Egonex-AI/Understand-Anything = MIT, Rowboat = Apache 2.0. **Tier A** (direct primary observation) despite this document's `evidence-tier: C`, which scopes the *tool recommendations*, not these licence facts.
- Direct read of `safishamsi/graphify` pyproject.toml (v1 branch, 2026-04-28) — zero LLM SDK dependencies confirmed; Pass 2 LLM work happens via the invoking Claude Code session. **Superseded 2026-08-28**, see below.
- Direct read of [`Graphify-Labs/graphify`](https://github.com/Graphify-Labs/graphify) pyproject.toml at 0.9.51 and `skills/graphify/skill.md` Part B (2026-08-28) — **Tier A**. Two findings, previously bundled as one claim: (a) zero LLM SDKs among the 29 *required* dependencies still holds (anthropic/openai/tiktoken/boto3 appear only under optional provider extras); (b) session routing is a property of the **skill path**, not of the package — `skill.md` Part B dispatches Pass 2 through the invoking session's Agent tool ("MANDATORY: You MUST use the Agent tool here"), while headless `graphify extract` has its own `--backend` provider chain. The old repo path no longer resolves; v1 is a frozen branch at 0.1.15.
  - **Method note.** Absence of a dependency is *corroboration*, not proof of no-egress, and should not be modelled as a proof pattern elsewhere in this repo — graphify's own `claude-cli` backend is a zero-SDK-dependency direct-egress path. Cite the dispatch mechanism; use the dependency list to support it.
- [archive/memory-systems-genealogy-baseline.md](../archive/memory-systems-genealogy-baseline.md) — Direct measurement across 3 genealogy projects, N=9 queries; 8/9 DEFINITIVE (89%) on the unaugmented stack; Tier B empirical evidence informing archetype C and C-EC. Archived 2026-07-10 as a dated measurement (claims dated 2026-04-29); the finding survives here and in §C-EC.6.
- *(from the merged methodology)* Direct read of `safishamsi/graphify` v1 `skills/graphify/skill.md` Part B + `graphify/extract.py` + `pyproject.toml` (2026-08-28) — Pass 2 is dispatched through the invoking session's Agent tool; zero LLM SDK dependencies and zero egress symbols corroborate. **This supersedes the 2026-04-28 entry, which cited only the dependency list** and therefore recorded corroboration as if it were proof. Source for assumption #5 sub-finding and assumption #8 egress framing. Scope: the `/graphify` skill path only.
- *(from the merged methodology)* Current graphify ([`Graphify-Labs/graphify`](https://github.com/Graphify-Labs/graphify), default branch `v8`, 2026-08-28) — documents `--backend ollama` and `OPENAI_BASE_URL`; provider auto-detection chain reaches Ollama last. Source for the retirement of assumption #5's local-model corollary. The old `safishamsi/graphify` path no longer resolves; v1 is a frozen branch at 0.1.15.
- *(from the merged methodology)* Understand-Anything v2.3.2 plugin detector verification (2026-04-28) — `parse-knowledge-base.py` gates on lowercase `index.md` at root or under `wiki/`; uppercase `INDEX.md` fails detection. Source for assumption #7. **Superseded 2026-08-29** (the 2026-08-28 stale-flag's re-verification, performed): v2.9.4 resolves the filename case-insensitively and gates on `has_index and md_count >= 3` only. Run against this repo it detects `karpathy`. Tier A, direct execution of upstream source fetched at `main`.
- *(from the merged methodology)* graphify v0.5.4 empirical run (2026-04-28) — Pass 1: 243 nodes / 427 edges / 0 analysis docs; Pass 2: 1187 nodes / 1651 edges / 67 communities / 251 nodes from analysis docs. Token benchmark: 57.5× vs naive full-corpus. Source for assumption #8 and the Pass-2-or-no-graphify decision.

### Tier B

- Andrej Karpathy — LLM Wiki paradigm (April 2026). Tier B by author authority. Write-time wiki + ingest/query/lint workflows + bookkeeping-not-reading insight. Source for the Karpathy-convention requirements across archetypes C, C-EC, and F.
- OKF typed-vault hygiene (§C1b) — single production second-brain (project1), firsthand: `01-knowledge-base/_type-registry.md`, `automation/lib/okf.py`, `automation/orchestrator/quality_gates.py:validate_okf_type`, `automation/okf_health.py`, `automation/okf_signals.py`. Full pattern + anti-patterns in archetype-A §A1b. **One practitioner, one project, not independently corroborated.**

### Tier C

- Graphify 71.5× token-savings claim. **Vendor-reported — not independently benchmarked.**
- claude-context ~40% reduction claim. **Vendor-reported — not independently benchmarked.**
- OpenBrain $0.10–0.30/month cost estimate. **Vendor-reported — not independently benchmarked.**
- InfraNodus subscription pricing (€12–66/mo) — Proprietary SaaS pricing as listed; not independently verified. **Vendor-reported — not independently benchmarked.**
- [Google Cloud — Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) — Apache-2.0; [announced 2026-06-12](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing). Sole required frontmatter field is `type:`. Date/license/required-field verified against primary spec + blog (2026-06-21).
- [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) — Apache 2.0, **~17.4k stars (2026-08-28**; the "13.1k" carried here since 2026-04-28 was stale by ~33% — star counts belong in their own dated clause, not inside a licence verification), desktop app for Mac/Windows/Linux, licence re-verified 2026-08-28. Typed-entity files, background briefing agents, Composio BYO integrations. **Community-reported star count and capability claims — not independently benchmarked.**
- [Pratiyush/llm-wiki](https://github.com/Pratiyush/llm-wiki) — MIT, re-verified 2026-08-28. *(Slug corrected: `pratiyushpathak/llm-wiki` no longer resolves. Default branch is `master`.)* Three-layer architecture (`raw/` → `wiki/` → `site/`), adapters for Claude Code, Codex, Cursor, Gemini, Obsidian, Copilot; redaction-by-default for keys/tokens. **Community-reported — not independently benchmarked.**
- [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) (formerly `Lum1104/Understand-Anything`; transfer complete, verified 2026-08-28) + local Ollama — cited as the C-EC.2 hybrid for LLM-derived relationships without vendor egress; explicitly labeled **untested in this repo** (Tier D leaning C). Upstream documented the Ollama path in commit `7f5a717`, 2026-06-19 — after this repo's v2.3.2 check.
- SiYuan — block-level local app (AGPL-3.0); cited as hybrid for atomic-note workflows; community MCP server only. **Community-reported — not independently benchmarked.**

---

## Related analyses

- [`memory-systems-archetype-a-curated-kb.md`](memory-systems-archetype-a-curated-kb.md) — archetype A, the heavily-routed primary (own file)
- [`archive/memory-systems-recommendation-methodology.md`](../archive/memory-systems-recommendation-methodology.md) — pre-merge snapshot of the methodology now in § Methodology and self-critique (folded in 2026-11-07)
- [`evidence-tiers.md`](evidence-tiers.md) — the evidence-tier framework the methodology applies; [`evidence-based-revalidation.md`](evidence-based-revalidation.md) — how to keep these recommendations current
- [`memory-system-patterns.md`](memory-system-patterns.md) — earlier pattern survey (precedes this archetype-driven view); the auto-memory layer used by C-EC
- [`archive/federated-query-architecture.md`](../archive/federated-query-architecture.md) — archived spoke case study relevant to archetype D (evicted 2026-07-10; canonical depth in the spoke repos)
- [`archive/local-cloud-llm-orchestration.md`](../archive/local-cloud-llm-orchestration.md) — archived spoke case study on routing deterministic work locally and Pass 2 to a vendor *only when corpus permits* (evicted 2026-07-10)
- [`archive/memory-systems-genealogy-baseline.md`](../archive/memory-systems-genealogy-baseline.md) — the archived empirical baseline behind §C-EC.6

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/memory-system-patterns.md`](memory-system-patterns.md) [EXTRACTED (1.00)] — references
- [`INDEX.md`](../INDEX.md) [EXTRACTED (1.00)] — references

<!-- graphify-footer:end -->
