# Memory System Project Archetypes

**Date**: 2026-04-27
**Status**: Research notes
**Purpose**: Common second-brain / KB project shapes. Used by `rethink-memory-stack-prompt.md` to drive per-archetype recommendations. Pair with `memory-systems-tools-inventory.md` and `memory-systems-architecture-axes.md`.

> A project's archetype tells you which axes matter. Get the archetype wrong and every tool choice downstream is suspect.

---

## A. Curated analytical knowledge base

**Examples**: This `claude-code-project-best-practices` repo. Domain-expertise wikis. Evidence-tiered frameworks. Research-synthesis vaults where each doc is hand-edited and cited.

**Characteristics**:
- ~tens to low-hundreds of carefully written markdown files.
- Each doc has provenance, evidence tier, cross-references.
- Correctness > recall.
- Stable concepts; few temporal facts.
- Single primary author/curator.

**Axis profile**:
- Write-time dominant; query-time light.
- Augments-wiki (prose carries argumentation).
- Topology + prose; embeddings unnecessary.
- Single-tool typical.
- Local egress preferred.
- Structural knowledge.
- Markdown.
- High determinism required for structural claims.

**Anti-fits**: Embedding-heavy tools (overkill); DB-substrate tools (lose portability); pure query-time tools (no compounding).

## B. Code monorepo / large codebase

**Examples**: 50k+ file repos. Polyrepo portfolios. Exploring an unfamiliar OSS codebase.

**Characteristics**:
- Code is the corpus.
- Structure exists but isn't documented.
- Recall matters as much as precision.
- Native Grep + Explore subagent breaks down past some scale threshold.

**Axis profile**:
- Both write-time (index) and query-time (lookup).
- Generates-wiki acceptable (code is canonical, not prose).
- Topology *or* embeddings, depending on scale.
- Often single-tool.
- Egress depends on proprietary status.
- Structural.
- Mixed substrate.

**Anti-fits**: LLM Wiki (wrong substrate — code is the canonical artifact, parallel wiki drifts); pure prose tools.

## C. Personal cross-domain second brain

**Examples**: Karpathy's actual target — reading queue + project notes + meeting transcripts + research papers + screenshots + media, queried across multiple AI tools.

**Characteristics**:
- Heterogeneous content (PDFs, code, images, video, prose).
- Written in personal voice.
- Vocabulary drifts over years.
- User switches between AI tools.
- Mostly stable concepts with some temporal layer.

**Axis profile**:
- Write-time + query-time both.
- Augments-wiki (personal interpretation matters).
- Topology + embeddings useful.
- Often cross-tool.
- Local strongly preferred (personal data).
- Mostly structural with temporal islands.
- Markdown for portability.
- Mixed determinism — reproducibility matters less than personal utility.

**Anti-fits**: Code-only tools (claude-context wastes capability); pure DB tools (lose portability of personal notes).

## D. Cross-project portfolio brain

**Examples**: User maintains N second-brain projects (analytical layers, code repos, research projects). Wants "what did I conclude about X across all projects?"

**Characteristics**:
- Each repo is its own wiki.
- Cross-project recall is the killer feature.
- Federation, not consolidation.

**Axis profile**:
- Both write-time (per-repo wikis) and query-time (federated lookup).
- Augments per repo.
- Topology + cross-repo communities.
- Cross-tool plausible.
- Mixed egress.
- Mostly structural.
- Per-repo markdown + optional federation index.
- High determinism per repo; cross-repo inferences flagged as such.

**Anti-fits**: Single-DB tools that flatten the per-repo structure.

## E. Work-state / project tracker

**Examples**: Tracking ongoing projects with deadlines, decisions, commitments, meetings, action items.

**Characteristics**:
- Temporal data dominant.
- Facts change frequently — yesterday's deadline is today's slipped date.
- Typed entities matter (Person, Decision, Deadline, Commitment).
- Wikis silently rot here.

**Axis profile**:
- Write-time at ingestion (extract typed entities) + query-time at briefing.
- Generates-wiki (events come from sources, not curation).
- Topology over typed entities; embeddings rarely needed.
- Single or cross-tool.
- Local strongly preferred (work-sensitive data).
- **Temporal dominant** — this is the differentiator.
- Markdown + typed-entity files (one MD per entity).
- High determinism on extraction; provenance per claim.

**Anti-fits**: Pure wiki (page-per-topic loses event granularity); pure vector DB (loses entity types).

## F. Session-history transcript archive

**Examples**: Transcripts from Claude Code, Codex, Cursor, Gemini, Copilot sessions. Mining them for patterns, decisions, reusable workflows.

**Characteristics**:
- Massive volume (every session adds files).
- Each transcript has a timestamp + agent + project context.
- Most sessions are trivial; few are gold.
- Need to extract durable knowledge from ephemeral chat.

**Axis profile**:
- Write-time heavy (extract durable knowledge from chatter) + query-time for retrospectives.
- Generates-wiki (transcripts → structured pages).
- Topology + LLM extraction.
- Single-tool typical (per agent) but cross-tool valuable.
- Local preferred.
- Mostly temporal at ingest; resolves to structural over time.
- Markdown.
- Provenance tagging essential — what came from which session.

**Anti-fits**: Tools that don't have agent-specific adapters.

## G. Multi-tool / team shared memory

**Examples**: Team uses Claude Code, Cursor, ChatGPT in parallel and wants shared project context. AI tools see same memory of the team and current work.

**Characteristics**:
- Concurrent writes from multiple clients.
- Multiple authors.
- Need access control / row-level security.
- Live state, not archived.

**Axis profile**:
- Both write-time and query-time.
- Mixed.
- Embeddings helpful for semantic retrieval across diverse content.
- **Cross-tool by definition**.
- Often hybrid egress (BYO model + self-hosted DB).
- Both structural and temporal.
- DB substrate justified (concurrency).
- Mixed determinism.

**Anti-fits**: Pure markdown-file tools (concurrent-write conflicts); single-user tools.

---

## Mapping archetypes to axis priorities

| Archetype | Top 3 axes that drive choice |
|---|---|
| A. Curated analytical KB | Write-time, augments-wiki, structural |
| B. Code monorepo | Query-time scale, embedding-vs-topology, egress |
| C. Personal cross-domain | Local-egress, augments-wiki, write-back loop |
| D. Cross-project portfolio | Federation, cross-tool, per-repo wiki |
| E. Work-state tracker | Temporal, typed-entities, provenance |
| F. Session archive | Adapter coverage, write-time mining, provenance |
| G. Multi-tool team | Cross-tool, concurrency, access control |

---

## Hybrid stacks worth evaluating per archetype

Not just one tool per archetype — explicit hybrids:

**A. Curated analytical KB**:
- Primary: LLM Wiki paradigm + graphify (augments)
- Hybrid alt 1: + Lum1104 for wiki-aware graph layer
- Hybrid alt 2: + MehmetGoekce L1/L2 split for context-budget management

**B. Code monorepo**:
- Primary: Graphify (topology, no embedding infra)
- Hybrid alt: + claude-context only when scale demands embedding-based retrieval
- Hybrid alt: + Pratiyush for session-history mining over the repo

**C. Personal cross-domain**:
- Primary: LLM Wiki + graphify
- Hybrid alt 1: + OpenBrain when multi-tool sync becomes necessary
- Hybrid alt 2: + Pratiyush adapters to mine session history into the wiki

**D. Cross-project portfolio**:
- Primary: Per-repo (LLM Wiki + graphify)
- Hybrid alt 1: + OpenBrain as the federation layer across repos
- Hybrid alt 2: + claude-context per code-heavy repo

**E. Work-state tracker**:
- Primary: Rowboat (typed entities, BYO model)
- Hybrid alt: + LLM Wiki for stable-knowledge layer alongside the temporal layer

**F. Session archive**:
- Primary: Pratiyush/llm-wiki (purpose-built for this)
- Hybrid alt: + graphify on the resulting wiki for cross-session topology

**G. Multi-tool team**:
- Primary: OpenBrain (post-compilation-agent ship)
- Hybrid alt: + per-user LLM Wiki for personal layer over shared OpenBrain

These are starting points for the prompt to evaluate, not final answers.
