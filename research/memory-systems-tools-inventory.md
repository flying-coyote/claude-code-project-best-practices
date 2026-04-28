# Memory & Knowledge System Tools — Inventory

**Date**: 2026-04-27 (license verifications + InfraNodus added 2026-04-28)
**Status**: Research notes
**Purpose**: Factual catalog of memory/knowledge tools for second-brain and KB projects. Read alongside `memory-systems-architecture-axes.md` and `memory-systems-project-archetypes.md`. Driven by `rethink-memory-stack-prompt.md`.

> **Evidence note**: Tool-specific quantitative claims (token-savings numbers, costs) come from each project's own benchmarks unless otherwise noted — Tier C until independently reproduced. **Karpathy's paradigm** (entry 1 below) is **Tier B by author authority**, not C; recency does not auto-downgrade an author-authority source.

---

## Comparison matrix

| Tool | Substrate | Write-time | Query-time | Integration | License | Authoritative source |
|---|---|---|---|---|---|---|
| Karpathy LLM Wiki (paradigm) | Markdown files | ✅ heavy | indirect (via Claude reading files) | None — convention only | n/a (gist) | [karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) |
| Graphify (safishamsi) | NetworkX graph + JSON + HTML | ✅ AST + LLM passes | ✅ CLI `graphify query` + MCP server | Skill + PreToolUse hook + CLI + MCP | MIT | [github](https://github.com/safishamsi/graphify) |
| Pratiyush/llm-wiki | Markdown vault + static HTML + JSON-LD | ✅ adapter-based ingestion | ✅ MCP server (12 tools) | CLI + MCP + SessionStart hook | MIT ✅ (verified 2026-04-28) | [github](https://github.com/Pratiyush/llm-wiki) |
| MehmetGoekce/llm-wiki | Markdown (Logseq/Obsidian) | ✅ ingest scans + cross-links | ✅ `/wiki query` | Slash commands + L1/L2 split | MIT ✅ (verified 2026-04-28) | [github](https://github.com/MehmetGoekce/llm-wiki) |
| Lum1104/Understand-Anything | Force-directed graph (JSON) | ✅ deterministic + LLM agents | ✅ `/understand-knowledge` | Claude Code plugin | MIT ✅ (verified 2026-04-28) | [github](https://github.com/Lum1104/Understand-Anything) |
| zilliztech/claude-context | Milvus + pgvector index | partial (chunk + embed at index) | ✅ heavy — semantic search | MCP server only | MIT | [github](https://github.com/zilliztech/claude-context) |
| OpenBrain (justSteve) | Postgres + pgvector + Supabase | partial (capture + dedup); compilation agent on roadmap | ✅ MCP-driven retrieval | MCP server | FSL-1.1-MIT | [github](https://github.com/justSteve/OpenBrain) |
| Rowboat (rowboatlabs/rowboat) | Markdown vault + desktop app (Mac/Windows/Linux) | ✅ extracts decisions/commitments/deadlines from Google services | indirect (via background agents) | Desktop app + optional Composio MCP | Apache 2.0 ✅ (verified 2026-04-28) | [github](https://github.com/rowboatlabs/rowboat) |
| InfraNodus (infranodus.com) | Vendor backend (proprietary SaaS) | ✅ text network analysis (words as nodes, co-occurrence as edges) | ✅ via official MCP server (MIT) + n8n nodes (MIT) | SaaS + browser extensions + Obsidian plugin + MCP | Proprietary (€12–66/mo); MCP/n8n clients are MIT | [github org](https://github.com/infranodus) |

---

## 1. Karpathy's LLM Wiki (paradigm, not a tool)

**Tier**: **B by author authority** (Karpathy is treated as a thought leader on par with Boris Cherny on Claude Code). Recency does not auto-downgrade. Tool-specific implementations of this paradigm (entries 2–5 below) are still Tier C until independently reproduced.
**Origin**: April 2026 gist by Andrej Karpathy.
**What it is**: A *convention* for organizing knowledge so an LLM can maintain it. Not software.
**Structure**: `sources/` (immutable) + `wiki/` (LLM-generated markdown) + `CLAUDE.md` (schema) + `index.md` (catalog) + `log.md` (append-only ledger).
**Three workflows**: Ingest (source → summary + cross-refs + index update + log append), Query (read wiki), Lint (contradictions / orphans / staleness).
**Core insight**: The bottleneck in knowledge bases is bookkeeping, not reading. LLMs don't get bored.
**Position**: Pure write-time. Persistent compounding artifact. The opposite of RAG.
**Failure mode alone**: Vocabulary lock-in (queries phrased differently than wiki was written miss content); silent staleness when sources change.
**Use when**: Stable concepts; single primary AI tool; depth over breadth.

## 2. Graphify (safishamsi/graphify)

**License**: MIT. **Stars**: ~36.3k as of April 2026.
**What it is**: Build-time tool that converts a folder of code/docs/papers/images/video into a queryable knowledge graph.
**Architecture**:
- Pass 1: Tree-sitter AST extraction (deterministic, no LLM, local).
- Pass 2: Parallel LLM agents extract concepts/relationships from unstructured content.
- Clustering: **Leiden community detection** on graph topology — *no embeddings, no vector DB*.
- Caching: SHA256-keyed; only changed files re-process.

**Provenance tags on every edge**:
- `EXTRACTED` (100% confidence, source-direct)
- `INFERRED` (confidence-scored)
- `AMBIGUOUS` (needs review)

**Outputs**: `graph.html`, `GRAPH_REPORT.md`, `graph.json`, `cache/`.
**Interfaces**:
- Slash command: `/graphify .` in Claude Code/Codex/Cursor/etc.
- CLI: `graphify query "..." --budget N`, `graphify path X Y`, `graphify explain X`.
- Hook install: `graphify claude install` adds CLAUDE.md directive + PreToolUse hook (fires before Glob/Grep).
- `--watch`: live AST rebuild on code edits; flags doc/image edits for `--update`.
- `graphify hook install`: git hooks rebuild on commit / branch switch.
- `--wiki` export: produces a wiki-style markdown with `index.md` per god-node and per community.
- MCP server: `python -m graphify.serve graphify-out/graph.json` exposes `query_graph`, `get_node`, `get_neighbors`, `shortest_path`.

**File support**: 20 programming languages; PDF, Markdown, .txt, .rst, images (Claude Vision), audio/video (faster-whisper), Office (with `[office]` extra).
**Export formats**: SVG, GraphML (Gephi/yEd), Cypher (Neo4j).
**Token claim**: 71.5× fewer tokens per query vs raw files on a 52-file mixed corpus (Karpathy benchmark). Tier C until reproduced.
**LLM provider**: graphify has **zero LLM SDK dependencies** in `pyproject.toml` (no `anthropic`, `openai`, `litellm`) — verified 2026-04-28 on the v1 branch. Pass 2 LLM work happens *via the invoking Claude Code session*, using whatever model that session is configured with. Implication: there's no documented "BYO local model" config (e.g., point at Ollama/Gemma); local-only usage requires either skipping Pass 2 entirely (Tree-sitter Pass 1 only) or forking graphify to replace Claude-Code-skill calls with direct local-LLM calls.
**PyPI name**: temporarily `graphifyy` while the `graphify` name is reclaimed; CLI is still `graphify`.
**Position**: Write-time topology builder + query-time graph navigator. No embeddings.
**Use when**: Mixed-content corpus; explicit cross-references exist or can be inferred; want structure-aware retrieval without vector infra.

## 3. Pratiyush/llm-wiki

**What it is**: Production-grade Karpathy-pattern wiki. Converts agent session `.jsonl` transcripts into a structured wiki with static HTML.
**Adapters**: Claude Code (`~/.claude/projects/`), Codex CLI (`~/.codex/sessions/`), Cursor, Gemini, Obsidian, Copilot.
**Three layers**: `raw/` (immutable markdown from `.jsonl`) → `wiki/` (LLM-organized: sources / entities / concepts / syntheses / comparisons / questions, interlinked via `[[wikilinks]]`) → `site/` (HTML + dual `.txt`/`.json` siblings per page for AI consumption).
**Extras**: `llms.txt`, JSON-LD graph (`graph.jsonld`), sitemaps, RSS, command-palette search.
**Commands**: `./setup.sh`, `llmwiki sync`, `llmwiki build`, `llmwiki serve`, `llmwiki graph`.
**MCP server**: 12 tools for remote queries.
**Auto-trigger**: SessionStart hook syncs on agent launch.
**Stack**: Python stdlib + `markdown` only. No npm. No DB. Redaction-by-default for keys/tokens.
**Position**: Write-time wiki with built-in graph layer; ingestion-focused (transforms session history into knowledge).
**Use when**: You want to mine value from existing AI session logs across multiple agents.

## 4. MehmetGoekce/llm-wiki — L1/L2 cache architecture

**What it is**: Karpathy-pattern wiki with **CPU-cache-hierarchy split** for context budget management.
**L1 (always-loaded)**: ~10–20 files. Rules, gotchas, identity, credentials. Auto-loaded every session.
**L2 (on-demand)**: ~50–200 wiki pages. Loaded selectively via `/wiki query`.
**Routing principle**: *"Would the LLM making a mistake without this knowledge be dangerous or embarrassing? Then it belongs in L1."*
**Compatibility**: Logseq + Obsidian.
**Commands**: `/wiki ingest`, `/wiki query`, `/wiki lint`. Ingest scans for affected pages and auto-creates cross-links.
**Position**: Write-time wiki with explicit context-budget tiering.
**Use when**: Long-running projects with growing wiki; need to keep critical rules always-on without context bloat.

## 5. Lum1104/Understand-Anything

**What it is**: Claude Code plugin that produces a force-directed knowledge graph with community clustering from a Karpathy-pattern wiki.
**Key capability**: **Deterministic parser reads `index.md` to extract wikilinks and categories** *before* any LLM pass. Then LLM agents discover implicit relationships.
**Why this is architecturally different from graphify**: Graphify treats the corpus as opaque files (re-discovers structure via AST + concept extraction). Understand-Anything *uses the wiki's existing link structure as ground truth*, then augments.
**Install**:
```
/plugin marketplace add Lum1104/Understand-Anything
/plugin install understand-anything
```
**Command**: `/understand-knowledge ~/path/to/wiki`
**Output**: Force-directed JSON graph with community clustering, navigable nodes.
**Position**: Wiki-aware graph layer. Strictly downstream of an existing wiki.
**Use when**: You already maintain a Karpathy-pattern wiki with explicit cross-references and want a graph view that respects your hand-curated links.

## 6. zilliztech/claude-context

**License**: MIT. **Stars**: 9.8k. **Stack**: Node ≥20 monorepo (core / VS Code ext / MCP server).
**What it is**: Specialized MCP server for semantic code search via hybrid BM25 + dense vectors over Milvus/Zilliz.
**Architecture**:
- AST-based code chunking
- Merkle-tree incremental indexing
- Embedding providers: OpenAI / VoyageAI / Ollama / Gemini
- Vector DB: Milvus / Zilliz Cloud
- 14+ programming languages

**Tools**: `index_codebase`, `search_code`, `clear_index`, `get_indexing_status`.
**Install**: `claude mcp add claude-context -e OPENAI_API_KEY=... -e MILVUS_ADDRESS=... -e MILVUS_TOKEN=... -- npx @zilliz/claude-context-mcp@latest`
**Token claim**: ~40% reduction vs full directory loading.
**Position**: Pure query-time, code-specific, embedding-based, vector-DB-required.
**Egress**: Source code goes to embedding provider; chunks + vectors go to Milvus/Zilliz.
**Use when**: Code corpus exceeds what Grep + Explore subagent can scale to (>~10k files).
**Skip when**: Small/medium repos; proprietary code without provider approval; documentation-heavy projects (it's code-only).

## 7. OpenBrain (justSteve/OpenBrain)

**License**: FSL-1.1-MIT (Functional Source License — 2-year reciprocal, then converts to MIT). **Author**: Nate B. Jones. **Stars**: low (newly seeded).
**What it is**: Self-hosted "infrastructure layer for thinking" — one DB, one AI gateway, MCP — so any AI client shares persistent memory.
**Stack**: Postgres + pgvector (Supabase) + AI gateway with schema-aware LLM routing + content fingerprinting + Postgres row-level security + SvelteKit/Next.js dashboard + Slack/Discord capture + optional K8s.
**Cost**: ~$0.10–0.30/month. **Setup**: ~45 minutes (no-code or AI-assisted).
**Position**: Currently pure query-time; **scheduled compilation agent on roadmap** (per Nate Jones) — would add write-time graph layer over the memory store.
**Use when**: Multiple AI tools (Claude Code + Cursor + ChatGPT) need shared persistent memory; cross-tool concurrency.
**Skip when**: Single-tool workflow; the MCP context tax + DB ops aren't earning their keep.

## 8. Rowboat ([rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat))

**License**: Apache 2.0 (verified 2026-04-28). **Stars**: ~13.1k. **Stack**: TypeScript desktop app (Mac/Windows/Linux). **Origin**: Rowboat Labs, Y Combinator S24.
**What it is**: "Open-source AI coworker that turns work into a knowledge graph and acts on it" — desktop app that connects to email and meeting notes, builds a long-lived knowledge graph, and uses that context for tasks like prep briefs and document generation. Markdown is the substrate ("it's just Markdown" per README).
**Ingests from**: **Google services (Gmail, Calendar, Drive)** by default — *not* Granola/Fireflies as an earlier draft of this inventory stated. The inventory entry was originally drawn from the [Avi Chawla post](https://blog.dailydoseofds.com/p/the-next-step-after-karpathys-wiki); the README is authoritative.
**Optional integrations** (require API keys in `~/.rowboat/config/`): Deepgram (voice input), ElevenLabs (voice output), Exa (web search), Composio MCP (external tools).
**Background agents**: Built into the desktop app; produce briefings from graph state.
**Position**: Fills the gap that Karpathy's wiki and graphify don't address — *knowledge that changes over time*. Distinct from a typed-entity-files-on-disk pattern; it's an integrated app with its own data model atop markdown.
**Use when**: Tracking ongoing work (projects with deadlines, commitments across people, decisions that may shift) and you accept Google + optional-vendor egress.
**Skip when**: Stable conceptual knowledge (use wiki + graphify instead); air-gapped requirement (Google services egress is the default).

## 9. InfraNodus (infranodus.com)

**License**: Proprietary SaaS (€12–66/mo; 14-day free trial). Open-source clients in [github.com/infranodus](https://github.com/infranodus): MCP server (MIT, 86 stars), n8n nodes/workflows (MIT), VSCode extension (NOASSERTION), datasets (MIT). The core platform is *not* open-source; no self-hosted option.
**Tier**: **B by author authority** for the methodology (Dmitry Paranyushkin / Nodus Labs, ~10+ years, published text-network-analysis research). C for any specific quantitative product claim.
**What it is**: Established platform for **text network analysis** — words are nodes, co-occurrences are edges, graph-theory algorithms identify topic clusters and structural gaps. GPT generates narrative insights atop the graph. Different paradigm from graphify (AST + Leiden) and Karpathy wiki (LLM-curated prose).
**Inputs**: PDFs, markdown, CSVs, plain text, Google search results, YouTube transcripts, websites, Amazon reviews, RSS feeds.
**Outputs**: Interactive network visualizations, topic clusters, sentiment analysis, AI-generated insights.
**Deployment**: Web SaaS + browser extensions (Chrome/Firefox/Safari) + Obsidian plugin + MCP server + REST API.
**Architecture vs constraints in this project**:

| Constraint | InfraNodus fit |
|---|---|
| Local-first | ❌ proprietary SaaS; full content + GPT egress |
| Markdown substrate | ❌ vendor backend; markdown is input only |
| Open-source / no lock-in | ❌ subscription required; only MCP/n8n clients are MIT |
| Author authority | ✅ established researcher with published methodology |

**Position**: Paradigm alternative to graphify, but doesn't fit local-first + markdown constraints. The MIT MCP server makes an InfraNodus account queryable from Claude Code if the methodology is independently valuable — that's the cleanest integration path.
**Use when**: Text network analysis is the primary need (gap-finding in a body of writing, topic-cluster visualization) and SaaS is acceptable.
**Skip when**: Local-first or markdown-substrate is required; or when graphify's AST+Leiden is a better fit for the corpus.
