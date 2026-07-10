# Memory System Architecture — Comparison Axes

**Date**: 2026-04-27
**Status**: Research notes
**Purpose**: The architectural dimensions that distinguish memory/knowledge systems. Used by `rethink-memory-stack-prompt.md` to drive per-archetype recommendations. Pair with `memory-systems-tools-inventory.md` and `memory-systems-project-archetypes.md`.

> Most "which tool is best" debates collapse when you separate these axes. Two tools that look like substitutes often sit on different axes entirely.

---

## Axis 1: Write-time vs query-time

**The core economic axis.** When does the synthesis cost get paid?

| | Write-time | Query-time |
|---|---|---|
| Cost paid when | At ingest | At retrieval |
| Per-query cost | Cheap (read pre-synthesized) | Expensive (search + retrieve + synthesize) |
| Per-ingest cost | Heavy (LLM touches many files) | Light (chunk + embed + insert) |
| Preserves | The *interpretation* — named entities, resolved contradictions | The *raw substrate* — every fact stays queryable |
| Failure alone | Vocabulary lock-in; silent staleness | Embedding drift; no compounding insight; re-derives every time |

**Tools by lean**: Wiki (write), graphify (write-dominant), Pratiyush/MehmetGoekce/Lum1104 (write), claude-context (query), OpenBrain (query, becoming hybrid), Rowboat (write).

**Hybrid principle**: Most production systems need *both halves*. Write-time bakes synthesized structure; query-time provides flexibility for novel angles.

## Axis 2: Augments vs generates the wiki

When you have both a wiki and a graph layer, who's authoritative?

| | Augments-wiki | Generates-wiki |
|---|---|---|
| Authoritative source | Human-curated wiki pages | Graph output |
| Direction of work | Graph appends as footer; wiki body is curated prose | Graph writes pages; human curates on top |
| Wiki survives if graph removed? | Yes | No |
| Best when | Prose carries argumentation graph can't represent | Most value is in connections, not prose |
| Example pattern | Jsong's footer-injection in `analysis/*.md` | `graphify --wiki` direct export |

## Axis 3: Topology-based vs embedding-based vs prose-based

How are connections discovered?

| Method | Mechanism | Strength | Weakness |
|---|---|---|---|
| **Topology** (graphify, Lum1104) | AST + wikilinks + Leiden communities | Deterministic, no hallucination, no infra | Can't find semantic similarity that isn't structurally linked |
| **Embeddings** (claude-context, OpenBrain) | Dense vectors + similarity search | Catches semantic similarity even without explicit links | Needs vector DB; embedding drift; opaque why X matched |
| **Prose** (LLM Wiki, Pratiyush, MehmetGoekce) | LLM reads + writes synthesis | Captures argumentation, hedging, narrative | Vocabulary lock-in; silent staleness |

**Hybrid principle**: GraphRAG (Microsoft) showed topology + embeddings beat either alone. None of the 2026 tools fully implement this; Lum1104 and graphify are closest on the topology side.

## Axis 4: Single-tool vs cross-tool memory

Who reads the memory?

| | Single-tool | Cross-tool |
|---|---|---|
| Substrate constraint | Whatever Claude can read (markdown best) | Must be queryable from N clients (DB or MCP) |
| Concurrency | None needed | Multi-client read/write |
| Lock-in | None — markdown survives | Schema/wire format |
| Tools | LLM Wiki, graphify, MehmetGoekce, Lum1104 | OpenBrain (purpose-built), claude-context (incidentally) |

**Hybrid principle**: Markdown-on-disk *can* be cross-tool if all tools read files. The DB layer is only required when concurrent writes from multiple clients matter.

## Axis 5: Local vs cloud egress

Where does content go?

| Tool | Code stays local? | Docs/images stay local? | Notes |
|---|---|---|---|
| LLM Wiki | depends on which LLM you use | same | Convention only |
| Graphify | ✅ AST is local | ❌ Pass 2 sends content to Claude/GPT API | faster-whisper for audio is local |
| Pratiyush/MehmetGoekce | depends | depends | Redaction-by-default in Pratiyush |
| Lum1104 | depends | depends | Plugin |
| Claude-context | ❌ Code → embedding provider; chunks → Milvus/Zilliz | n/a (code-only) | Cloud DB by default |
| OpenBrain | ✅ self-hosted Postgres | ✅ if BYO model | FSL license |
| Rowboat | ✅ self-hosted, BYO model | ✅ | Local-first design |

**Decision filter**: Proprietary code or sensitive content → eliminate cloud-egress tools or wire local-only providers (Ollama).

## Axis 6: Structural vs temporal knowledge

What kind of knowledge is being captured?

| | Structural (concepts) | Temporal (events) |
|---|---|---|
| Examples | "What is attention?" "How does auth flow connect to payments?" | "What did we decide last week?" "Has the deadline shifted?" |
| Stability | Stable — concepts and their relationships persist | Volatile — facts change over time |
| Best fit | Wiki + graphify | Rowboat-style typed entities |
| Failure of wrong fit | Graphify on temporal data: stale graph immediately | Wiki on temporal data: page becomes contradiction soup |

**This is the gap most current tools miss**. Avi Chawla's critique: Karpathy's wiki *breaks* on temporal data because a wiki page about "Project X" can't represent "every decision made, who made it, when, whether anything has shifted."

## Axis 7: Markdown substrate vs database substrate

Where does knowledge live on disk?

| | Markdown | Database |
|---|---|---|
| Portability | ✅ Survives decades, every tool reads it | Bound to schema + engine |
| Grep-ability | ✅ | Requires SQL |
| Concurrent writes | Poor (file conflicts) | ✅ |
| Backup | Trivial (git) | Requires DB dump |
| LLM-readable | ✅ Native | Requires query layer |
| Lock-in | None | High |

**Decision filter**: For long-lived knowledge you'd want to read in 10 years, prefer markdown. For high-concurrency multi-user, prefer DB.

## Axis 8: Deterministic vs LLM-derived structure

How much of the structure is reproducible?

| Method | Reproducible? | Example |
|---|---|---|
| **Deterministic** | ✅ Yes — same input gives same output | AST parsing, wikilink extraction, file-tree walking |
| **LLM-derived** | ❌ No — varies by model + temperature + prompt | Concept extraction, semantic similarity, summary writing |

**Provenance tagging** (graphify's EXTRACTED/INFERRED/AMBIGUOUS) is the bridge: the system declares which edges are reproducible and which are model-derived. This enables auditing.

**Hybrid principle**: Run deterministic passes first (cheap, reliable, source-of-truth). Run LLM passes second (expensive, fallible, augmenting). Tag provenance on every output.

## Axis 9: Block-level vs page-level granularity

How fine-grained is the addressable unit of knowledge?

| | Block-level | Page-level |
|---|---|---|
| Atomic unit | Paragraph, list item, code block | File or section |
| Reference style | `((block-id))` or backlinks to specific blocks | `[[page-name]]` |
| Refactor cost | Low — move blocks between pages without breaking refs | High — file moves break wikilinks unless renamed atomically |
| Best for | Knowledge that's frequently recombined (atomic notes, Zettelkasten, code snippets) | Knowledge that lives as cohesive arguments (analyses, methodology, longform) |
| Examples | SiYuan, Logseq, Roam | Karpathy LLM Wiki, Pratiyush, Tolaria, Obsidian (default) |

**Trade-off**: Block-level enables recombination workflows but creates more dangling references when the underlying app dies — block IDs are app-specific even when files are markdown. Page-level survives any markdown reader but constrains refactoring.

## Axis 10: Agent contract — convention vs MCP server vs CLI

How does an AI agent learn the vault's structure, schema, and rules?

| | Convention file | MCP server | CLI subprocess |
|---|---|---|---|
| Where it lives | A file in the vault (`CLAUDE.md`, `AGENTS.md`, `.cursorrules`) | A separate process the agent connects to | Binary the agent shells out to |
| Who reads | Any LLM-aware tool that loads the file | MCP client (Claude Code, Codex, Cursor) | Any agent that can shell out |
| Discovery | Filename convention | Tool listing via MCP | `--help` text |
| Updates propagate by | Editing the file in git | Restarting the server | Patching the binary |
| Survives the originating tool's death | ✅ — file is plain text | ❌ — server process dies with the tool | ✅ — CLI is reusable |
| Examples | Karpathy paradigm, Tolaria's `AGENTS` file, Codex `.codex/` convention | SiYuan MCP, Pratiyush MCP, Graphify MCP, OpenBrain | Graphify CLI, claude-context (indirectly via npx) |

**Convention wins on portability** (any agent that respects the convention works), **MCP wins on capability** (typed tools, structured I/O), **CLI wins on simplicity** (no protocol). Tolaria's `AGENTS` file pattern is interesting because it's tool-agnostic by design — same vault, multiple agents, no per-tool fork. MCP locks the integration to MCP-aware clients.

---

## Cross-cutting: the contradiction question

When you combine a wiki and a graph, the architecture must decide:

1. **Who's authoritative?** (Axis 2)
2. **What confidence does each claim carry?** (Axis 8)
3. **What happens when wiki and graph disagree?**

Three valid answers:

- **Wiki yields** — graph is read-only structural truth; wiki is reconciled interpretation. Lint enforces.
- **Graph yields** — wiki is human prose; graph is best-effort approximation. No enforcement.
- **Neither** — both are derived views of `sources/`; differences are reported but not resolved.

The answer drives whether you need a contradiction lint, and how strict it is.

---

## Use these axes to drive recommendations

For any project archetype, walk the axes:

1. Write-time / query-time / both?
2. Augments or generates?
3. What method discovers connections?
4. Single-tool or cross-tool?
5. Local or cloud egress acceptable?
6. Structural, temporal, or both?
7. Markdown or DB?
8. How much determinism is needed?

Two archetypes that disagree on even one axis often need different stacks.
