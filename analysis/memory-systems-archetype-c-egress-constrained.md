---
status: EMERGING
last-verified: "2026-04-30"
measurement-claims:
  - claim: "Owner-authorized egress is the deciding constraint, not data category — public-source genealogy data with placeholder discipline can be opted-in (Wiley projects, 2026-04-29); same data without owner authorization or with un-anonymized living persons cannot"
    source: "User's reframe 2026-04-29; saved in feedback_genealogy_data_classification memory"
    date: "2026-04-29"
    revalidate: "2026-10-29"
  - claim: "The unaugmented stack (CLAUDE.md + auto-memory + raw file navigation) achieved 89% DEFINITIVE answers (8/9) on a baseline measurement across the genealogy trio"
    source: "memory-systems-genealogy-baseline.md (2026-04-29 measurement)"
    date: "2026-04-29"
    revalidate: "2026-07-29"
  - claim: "Lum1104/Understand-Anything via local Ollama as a Pass-2 substitute is untested in this repo"
    source: "Repo search; no testbed evidence found"
    date: "2026-04-30"
    revalidate: "2026-07-30"
evidence-tier: C
applies-to-signals: [memory-systems, second-brain, knowledge-base, wiki, md-corpus-large, md-corpus-very-large, pii, sensitive-content, healthcare-data, legal-data, journal-third-parties, vault-obsidian, project-type-research]
revalidate-by: 2026-10-30
---

# Archetype C-Egress-Constrained — Cross-Domain Second Brain Without Vendor-LLM Egress

**Evidence Tier**: C overall. Karpathy paradigm is **B by author authority**; tool-specific claims stay C; the local-LLM-Pass-2 substitute is **D-leaning-C** (untested in this repo, plausible from inventory documentation). The 89%-baseline finding from the genealogy measurement is **B** (project-artifact-based; see [`memory-systems-genealogy-baseline.md`](memory-systems-genealogy-baseline.md)).

> **Naming note**: this doc was originally `archetype-c-pii.md` with genealogy as the canonical example. Renamed 2026-04-30 to reflect the actual constraint axis (owner-authorized vendor egress, not data-category PII) after the user reframed the Wiley-genealogy projects' egress posture on 2026-04-29 with placeholder discipline + public-source content. Genealogy now sits as an *opt-out* example below, not the canonical case.

## Purpose

Variant of Archetype C for projects where the **owner has chosen not to authorize vendor-LLM egress** of corpus content. The constraint is policy, not data category. Reasons vary:

- **Hard category constraints**: medical records, attorney-client legal correspondence, HR / employee performance notes, journals naming third parties without their consent
- **Soft category constraints**: published-but-aggregated personal data the owner wants to control (e.g. comprehensive profiles aggregating public records that no public source provides as a unit)
- **Vendor-policy mismatches**: corpus subject to data-residency, GDPR-Article-9, HIPAA, or contractual non-disclosure that prevents API egress
- **Research / threat-modeling reasons**: owner wants to characterize the unaugmented stack first, before committing to a vendor-egress dependency

Same shape as Archetype C: single-curator markdown vault with structural and (optionally) temporal layers. The difference is what's allowed to leave the box.

## The constraint conflict

The Archetype C primary stack (Karpathy LLM Wiki + Graphify Pass 2 + Pratiyush adapters) all egress content to a vendor LLM during ingest. PII corpora typically can't allow that. Concretely:

| Required by Archetype C primary stack                                | Blocked by PII constraint                                                                  |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Graphify Pass 2 — LLM extracts concepts from each file                | Bulk content egress to Anthropic/OpenAI API on every changed file                          |
| Pratiyush adapter — ingests session `.jsonl` to wiki                  | Sessions contain quoted PII from the corpus; egress at ingest                              |
| Lum1104 wiki-aware graph — LLM agents discover implicit relationships | Same egress profile (Pass 2 calls go through invoking session)                              |
| `claude-context` semantic search                                      | Code/text goes to embedding provider; chunks to Milvus/Zilliz                               |
| Cloud embedding APIs (OpenAI, VoyageAI, Gemini)                        | Same                                                                                        |
| claude-video skill (Whisper API + frame analysis)                      | Audio to Groq/OpenAI; frames + transcript to Claude — fine for public, not for private     |

What's left: pure topology (Pass 1), prose curation (manual), deterministic structure extraction (AST, wikilinks), local-only LLM passes if you accept the quality drop, and the auto-memory layer that already exists in `~/.claude/projects/<project>/memory/`.

## Canonical examples

This archetype fits cleanly when the owner has hard or soft constraints on egress. Examples:

- **Medical / clinical-notes corpora** — HIPAA, BAA constraints, PHI by definition.
- **Legal-correspondence vaults** — attorney-client privilege, work-product, opposing-party protected info.
- **Personal journals naming living third parties** — friends, family members, colleagues described in detail.
- **Performance / personnel files** — even on the owner's own employees.
- **Pre-publication research drafts** with embargoed source material.

The shared trait: the *content* might be entirely on the owner's local disk, but the owner has determined that vendor LLMs should not retain a copy of it.

### Genealogy as opt-out, not canonical example (2026-04-29 reframe)

The Wiley genealogy projects (`/home/jerem/genealogy/`, `/home/jerem/genealogy-kindred/`, `/home/jerem/genealogy-dry-cross/`) — ~17k md, 3.3k md, 396 md files respectively — were originally framed as the canonical case for this archetype. The owner has since reframed:

- Living-person names use anonymized placeholders in `tree.json` and journals.
- Remaining content (deceased ancestors, dates, ARK URLs, citations) is publicly available on FamilySearch, Ancestry, WikiTree, Find a Grave.
- Vendor-LLM egress is therefore acceptable for these projects at owner's choice.

The genealogy `CLAUDE.md` files still contain the original "Do NOT bulk-feed these paths to vendor-LLM tools..." rule. **That rule predates the reframe and should be updated when the owner authorizes a specific tool to run.** Don't unilaterally relax it in code.

The empirical finding from running this archetype's primary stack against the genealogy corpus *anyway* (see [`memory-systems-genealogy-baseline.md`](memory-systems-genealogy-baseline.md)): the unaugmented stack scored 8/9 DEFINITIVE on a 9-query measurement. The archetype-C-egress-constrained primary stack is **good enough** for genealogy regardless of whether the egress constraint is enforced — which means the original C-PII framing was slightly misleading. The PII concern was load-bearing for "must we use the unaugmented stack" but turned out not to be load-bearing for "is the unaugmented stack sufficient."

That finding informs the archetype's broader applicability: **for actual hard-egress-constraint projects (medical, legal, journals with third parties), expect the unaugmented stack to be similarly sufficient if memory authorship is disciplined.** Augmentation is not the bottleneck for retrieval quality — authorship discipline is.

## C-EC.1 Primary stack (PII-constrained)

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

1. **Wikilink graph extraction** — a deterministic ~50-line script that walks `*.md` files, parses `[[wikilink]]` references, and builds an adjacency list. No LLM. Works on any prose corpus that uses wikilinks. Output is a JSON edge list that footer-injection scripts can consume.
2. **Frontmatter index** — extract `type:`, `tags:`, `subject:` fields from YAML frontmatter into a SQLite or JSON index. Also deterministic.
3. **Heading-graph** — sibling/parent relationships across files based on heading-text matches. Brittle but local.
4. **Lum1104 + local Ollama** for the LLM-derived layer (this is the C-EC.2 hybrid; **untested** in this repo).

The Pass 1 line above keeps Graphify in the recommendation only because it does meaningful work on *mixed* corpora (some code + some prose). On pure-prose corpora, replace it with the wikilink-graph approach.

## C-EC.2 Hybrid alternatives (with caveats)

| Hybrid                                              | What it adds                                                          | What you trade                                                                                   |
|-----------------------------------------------------|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| + Lum1104/Understand-Anything via local Ollama       | LLM-derived implicit relationships without vendor egress              | Quality drops vs. Claude/GPT (Tier C inferred from inventory; **untested locally**); setup cost  |
| + Pre-redaction filter for selective Pass 2          | Some Pass 2 benefit on non-PII subset                                  | Brittle in practice; misses ~95% of corpus for genealogy; risk of leak from incomplete redaction |
| + Local-only Whisper for audio sources               | Audio ingest of family interviews, recorded methodology               | Setup of `whisper.cpp` or `faster-whisper`; quality drop vs Groq Whisper                          |
| + Block-level layer (SiYuan) running entirely local  | Block IDs + transclusion for atomic-note workflows                     | Heavier app; community MCP server only; AGPL-3.0                                                  |
| + claude-video for **public** sources only           | Watch-later YouTube ingest of public methodology, not private material | Strict separation discipline required; one slip = egress event                                    |

## C-EC.3 Anti-patterns

- **Run graphify Pass 2 on a "redacted" subset and pretend the rest will catch up.** Redaction is incomplete in practice (names show up in unexpected fields, addresses leak through filenames). Risk of leak; the unredacted parts go uninstrumented anyway, defeating the point.
- **Wire claude-context with Ollama "to be safe."** Ollama keeps the embedding generation local, but chunks still go to Milvus/Zilliz unless self-hosted. Self-host Milvus too or skip.
- **Use Pratiyush on session logs that touched the PII corpus.** Those sessions contain quoted PII; ingestion egresses on the next sync.
- **Use claude-video on family interview recordings.** Whisper API call alone violates the constraint, never mind the frame analysis.
- **Treat "local LLM via Ollama" as automatically PII-safe.** It is *vendor-egress-safe*, but the local model still produces outputs that may end up in shared logs, telemetry, or downstream commits. The local-only constraint extends to where the *outputs* are stored, not just where the inference happens.

## C-EC.4 Adoption order

1. **Inventory the egress boundary.** List the paths whose content cannot egress. Document in `CLAUDE.md` (paths + tools-not-to-run + cross-project egress confirmation rule). Reversible.
2. **Run `graphify .` configured to skip Pass 2.** Either via a flag or by running it without an active Claude Code session (Pass 2 is invoked through the invoking session per the inventory entry — no session, no Pass 2). Get the Pass 1 topology. Verify no LLM calls were made. Reversible.
3. **Hand-curate the wiki layer.** Accept the velocity drop; that's the price. **Stop if** the curation cost exceeds recall benefit at the current corpus size — for under ~200 docs the manual approach may not earn its keep yet (consult Archetype A's tier-2 fallback).
4. **Add auto-memory entries as you work.** This is the substrate this conversation lives in. Per [`memory-system-patterns.md`](memory-system-patterns.md).
5. **Reconsider Lum1104 + local Ollama** only after you've maintained 50+ wiki pages by hand and want graph augmentation. **Run a measurement first** — see Evidence gap below.
6. **Reconsider claude-video** only for the public sources subset (methodology talks, conference recordings). Maintain strict separation: a `sources/public/` subdir that the ingestion skill is allowed to touch, distinct from `sources/private/` that it never reads.

## C-EC.5 Constraint check

- **Local-first ✅ strict.** No tool in the primary stack egresses corpus content.
- **Markdown substrate ✅.** Same as Archetype C.
- **Augments-not-generates ✅.** No LLM authoring at all in the primary stack.
- **Graphify feeds wiki ✅** via Pass 1 only (topology only).
- **A/B/C evidence tiering preserved ✅.** Hand-curated wiki gives explicit control over claim provenance.
- **Wiki claims align with graph confidence ✅** trivially — graph is EXTRACTED-only since no Pass 2 means no INFERRED edges.

## C-EC.6 Evidence gaps and what we now know

### Gap 1 (still open): Lum1104 + local Ollama for the LLM-derived layer

The "Lum1104 + local Ollama for egress-constrained corpora" hybrid remains **untested in this repo**. Highest-leverage experiment:

1. Take a 500-doc subset (synthetic clinical-note generator, or a redacted slice of a real journal corpus with permission).
2. Run Lum1104 against it with local Ollama (gemma3, qwen2.5, or llama3.3 — pick one and document).
3. Compare graph quality (edge precision, missed relationships, node naming consistency) vs. running the same against a non-constrained corpus with Claude/GPT Pass 2.
4. Document the quality degradation. *This is the missing evidence behind any local-LLM Pass 2 recommendation* — without it the C-EC.2 row is Tier D speculation, not C.

### Gap 2 (resolved 2026-04-29): Is the unaugmented stack sufficient?

**Result: largely yes** — see [`memory-systems-genealogy-baseline.md`](memory-systems-genealogy-baseline.md). 9-query measurement across the 3-project genealogy trio scored 8/9 DEFINITIVE under the unaugmented stack alone. The PARTIAL was traced to a missing dedicated memory file for active brick walls, not to corpus size or augmentation absence.

Implications:

- **Disciplined memory authoring** (`CLAUDE.md` routing + dedicated memory files for resolved issues + `MEMORY.md` as flat index) is what makes the unaugmented stack work, not augmentation per se.
- The cheapest improvement is more dedicated memory files, not graph infrastructure. Estimated cost: ~10 min per file. Estimated tool-call reduction: 5–9 reads → 1–2 reads on synthesis queries.
- For projects with disciplined authoring, the marginal value of vendor-LLM Pass 2 augmentation is small enough that the egress constraint rarely makes augmentation worth fighting for.
- This shifts the archetype's narrative: **hard egress constraints are less of a recall handicap than originally framed.** The graph augmentation case strengthens specifically when authoring is undisciplined, the corpus is too large for any single curator to maintain memory files for active topics, or there are multiple curators with inconsistent discipline.

### Gap 3 (still open): Comparative arm

The genealogy baseline is a one-arm measurement. To rigorously claim "augmentation isn't needed" we need a second arm running Graphify Pass 2 + wiki + footer-injection against the same project + same query set, and a delta. The 2026-04-29 reframe of the genealogy projects' egress posture means that arm is now feasible to run (vendor-LLM authorization granted by owner). Recommended next step.

## Related Analysis

- [`memory-systems-archetype-c-personal-second-brain.md`](memory-systems-archetype-c-personal-second-brain.md) — egress-permissive variant
- [`memory-systems-genealogy-baseline.md`](memory-systems-genealogy-baseline.md) — empirical measurement of the unaugmented stack across the 3-project genealogy trio (89% DEFINITIVE rate)
- [`memory-systems-archetype-recommendations.md`](memory-systems-archetype-recommendations.md) — index across all 7 archetypes + cross-cutting
- [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md) — framing and self-critique
- [`local-cloud-llm-orchestration.md`](local-cloud-llm-orchestration.md) — how to route deterministic work locally and Pass 2 to a vendor *only when corpus permits*
- [`memory-system-patterns.md`](memory-system-patterns.md) — the auto-memory layer used here as the cross-session substrate
