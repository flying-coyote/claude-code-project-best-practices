---
status: EMERGING
last-verified: "2026-04-28"
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
evidence-tier: C
applies-to-signals: [memory-systems, knowledge-base, second-brain, wiki, graph]
revalidate-by: 2026-10-28
---

# Memory & Knowledge System Recommendations by Archetype

Per-archetype primary stacks, hybrids, anti-patterns, and adoption order for memory and knowledge tools across seven common project shapes (A–G). Calibrated to **~500-document curated knowledge bases** as the single-curator design target. See `memory-systems-recommendation-methodology.md` for the framing, threshold math, self-critique, and applied corrections behind these recommendations.

> **Source documents** (read first):
> - `research/memory-systems-tools-inventory.md` — factual catalog of 8 tools/paradigms with capabilities and licenses
> - `research/memory-systems-architecture-axes.md` — 8 architectural axes that distinguish the tools
> - `research/memory-systems-project-archetypes.md` — 7 archetypes A–G with axis profiles

**Constraints honored on every recommendation**:

1. Graphify-style graph output feeds the wiki (promotes findings into pages); does not sit as a parallel artifact.
2. Wiki claims align with graph confidence (EXTRACTED / INFERRED / AMBIGUOUS).
3. A/B/C evidence tiering preserved through the stack.
4. Augments-not-generates for prose-rich projects.
5. Local-first preferred over cloud egress.
6. Markdown substrate preferred for long-lived knowledge.

**Tier note**: Tool-specific quantitative claims are Tier C. Karpathy's paradigm is **Tier B by author authority** (Karpathy is treated as a thought leader on par with Boris Cherny on Claude Code).

---

## A. Curated analytical knowledge base

**Examples**: domain-expertise wikis, evidence-tiered frameworks, research-synthesis vaults where each doc is hand-edited and cited.

### A1. Primary stack — splits by scale

- **At the ~500-doc design target**: **Graphify (write-time topology) → footer-injected into a Karpathy-pattern wiki convention.**
- **Below ~200 docs**: **Lum1104 alone over a hand-curated wiki with `[[wikilinks]]`.** Lum1104 uses existing wikilinks as ground truth (deterministic on *your* structure) and is strictly downstream — no glue work to maintain, no Pass-2 egress on prose. Promote to graphify+footer when growing past ~200.

| Layer | Owner (design-target stack) | Why |
|---|---|---|
| Substrate | Markdown files in `analysis/` | Axis 7 — long-lived, grep-able, git-backed |
| Topology | Graphify (`graphify-out/graph.json`) | Axis 8 — Tree-sitter + Leiden are deterministic; provenance tags auditable. Note: for prose corpora most edges are INFERRED, not EXTRACTED |
| Synthesis | Hand-edited prose, augmented by graph footer | Axis 2 — augments-wiki; prose carries argumentation graph can't represent |
| Lint | Local script reading `graph.json` + each `analysis/*.md`, flagging wiki claims that conflict with EXTRACTED edges | Axis 8 — bridges deterministic vs LLM-derived |

**Driving axes**: 1 (write-time dominant), 2 (augments-wiki), 7 (markdown), 8 (provenance discipline). **Evidence tier**: B for the Karpathy paradigm, C for graphify's specific 71.5× token claim ([safishamsi/graphify](https://github.com/safishamsi/graphify)).

### A2. Hybrid alternatives

| Hybrid | Optimizes | Pick when |
|---|---|---|
| + MehmetGoekce L1/L2 split | Context budget at scale | KB exceeds ~100 docs and CLAUDE.md routinely loses important rules |
| + Lum1104 plugin | Wiki-aware graph (uses your wikilinks as ground truth) | Rich `[[wikilinks]]` already exist and you want a graph that respects them |
| + Pratiyush adapters | Mining historical Claude Code sessions back into the analytical layer | Session archive (archetype F) is worth promoting findings into A |

### A3. Anti-patterns

- **Claude-context (Milvus + embeddings) against a 30-doc analytical KB**: pays vector-DB ops cost and embedding-provider egress for recall benefit Grep already provides; embedding drift later forces reindex.
- **OpenBrain Postgres substrate for ~30 markdown analyses**: flattens per-doc evidence-tier metadata; loses git diff as the audit log; converts a portable artifact into a DB dump.
- **`graphify --wiki` direct export *alongside* a hand-curated `analysis/`**: produces two parallel "wikis" with no defined source-of-truth — violates the graphify-feeds-wiki constraint.

### A4. Adoption order

1. `pipx install graphifyy` (PyPI name; CLI is `graphify`); run `graphify .` once. **Reversibility caveat**: deleting `graphify-out/` undoes the local index, but Pass 2 ships content to the LLM (whatever the invoking Claude Code session uses) and that egress is *not* reversible. For sensitive content, skip Pass 2 or run on a public-only subset. **Stop if** `GRAPH_REPORT.md` surfaces no relationships you didn't already know.
2. Inspect `graph.html` and EXTRACTED/INFERRED/AMBIGUOUS counts. Read-only.
3. Write a 30–50 line footer-injection script (per `analysis/*.md`, append "Related (from graph)" with INFERRED edges marked). Commit on a branch. **Stop if** edges look noisy and require manual filtering — that's a signal to evaluate Lum1104 instead.
4. Add `graphify hook install` (git hooks: rebuild on commit/branch).
5. Only then evaluate L1/L2 split or Lum1104.

### A5. Constraint check

| Constraint | Met? |
|---|---|
| Graphify feeds wiki | ✅ via footer injection |
| No wiki/graph contradiction | ✅ lint enforces, provenance tags carry through |
| A/B/C tiering preserved | ✅ markdown substrate keeps tier metadata in front-matter |
| Augments not generates | ✅ prose stays hand-edited |
| Local-first | ⚠️ graphify Pass 2 ships content to the Claude Code session's LLM. Bound the egress by skipping Pass 2 on sensitive content. |
| Markdown substrate | ✅ |

---

## B. Code monorepo / large codebase

### B1. Primary stack

**Graphify alone** for repos under ~10k files. **Graphify + claude-context** above that threshold.

| Layer | Owner | Why |
|---|---|---|
| Topology | Graphify Tree-sitter (~16 languages per pyproject) | Axis 3 — deterministic, no embedding drift |
| Semantic recall (large only) | claude-context (BM25 + dense vectors over Milvus) | Axis 3 — when AST topology misses semantic similarity at scale |
| Wiki layer | `graphify --wiki` is acceptable here (code is canonical, not prose) | Axis 2 — generates-wiki is fine when the wiki is a derived view |

**Driving axes**: 1 + query-time at scale, 3 (topology vs embeddings tradeoff), 5 (egress matters for proprietary code). **Tier**: C — both token-savings claims are vendor-reported only.

### B2. Hybrid alternatives

| Hybrid | Optimizes | Pick when |
|---|---|---|
| Graphify + claude-context (Ollama embeddings, self-hosted Milvus) | Local-first semantic recall | Proprietary code that can't egress to OpenAI/VoyageAI |
| Graphify + Pratiyush adapters | Mining session history *over* the repo | Postmortem culture; multiple devs leaving good context in transcripts |
| Plain Grep + Explore subagent | Zero-infra | Repos under ~5k files where graphify install cost exceeds the benefit |

### B3. Anti-patterns

- **LLM Wiki paradigm on a 50k-file repo**: code is the canonical artifact; a parallel hand-curated wiki rots within weeks of refactors. Use graphify's generated wiki view instead.
- **claude-context on a 2k-file repo**: pays Milvus ops + embedding-provider egress for recall Grep already covers.
- **`graphify --wiki` *and* a separate hand-curated docs site over the same code**: source-of-truth ambiguity; the docs site contradicts AST-derived claims as code changes.

### B4. Adoption order

1. `graphify .` from the repo root with `--cache`. Reversible-local; egress applies.
2. `graphify hook install` for branch-switch rebuilds. Reversible.
3. Inspect token-savings on three real queries vs Grep+Explore. **Stop if** savings are under 3×.
4. Only at scale (>10k files) and only after step 3 shows benefit, evaluate claude-context with **Ollama embeddings** to keep code local.

### B5. Constraint check

- Graphify feeds wiki: ✅ via `--wiki` export.
- No contradiction: ⚠️ generated wiki has no human prose to contradict; discipline simplifies to "wiki = graph view."
- Tiering: N/A (code corpus, not evidence claims).
- Augments: deviates intentionally — generates-wiki is correct here.
- Local-first: ✅ for Pass 1 + Ollama-backed claude-context. ❌ if OpenAI embeddings.
- Markdown: ✅ for the wiki view.

---

## C. Personal cross-domain second brain

### C1. Primary stack

**Karpathy LLM Wiki paradigm + Graphify (footer-injection) + Pratiyush adapters for session ingestion.** Local-first when the invoking session uses an Anthropic model and you accept that egress; otherwise skip Pass 2.

| Layer | Owner | Why |
|---|---|---|
| Substrate | Markdown vault | Axis 5 (local), 7 (portable) |
| Wiki | Karpathy convention (`sources/`, `wiki/`, `index.md`, `log.md`) | Axis 2 — augments; personal interpretation matters |
| Topology | Graphify (with `--watch` for live rebuild) | Axis 3 — topology over heterogeneous content |
| Session ingest | Pratiyush adapter (Claude Code + Codex + Cursor + Gemini) | Axis 4 — cross-tool source feeding single wiki |

**Driving axes**: 5 (local strongly preferred), 2 (augments-wiki), 6 (mostly structural with temporal islands). **Tier**: C overall (paradigm B; tools C).

### C2. Hybrid alternatives

| Hybrid | Optimizes | Pick when |
|---|---|---|
| + OpenBrain (post-compilation-agent ship) | Cross-tool concurrency | Switching frequently between Claude Code, Cursor, ChatGPT |
| + Rowboat sliver | Capturing the temporal layer (deadlines, commitments) without polluting the structural wiki | Wiki accumulating "decided last Tuesday" pages |
| + Lum1104 plugin | Wiki-aware graph view that uses your `[[wikilinks]]` | Once the wiki has dense cross-refs |

### C3. Anti-patterns

- **Cloud-egress vector DB (Milvus/Zilliz Cloud, OpenAI embeddings) over personal notes**: privacy + recurring cost for a single user; embedding drift over years invalidates indexes.
- **LLM Wiki + Rowboat at full scope on the same content**: typed-entity files duplicate page-per-topic prose. Use Rowboat *only* for the temporal sliver.

### C4. Adoption order

1. Create the directory skeleton (`sources/`, `wiki/`, `index.md`, `log.md`, `CLAUDE.md`). Reversible.
2. Manually write 5 wiki pages from existing sources to learn the convention. **Stop if** bookkeeping load exceeds recall benefit at this scale.
3. Run `graphify .` once and add a footer-injection script.
4. Install Pratiyush; one-shot ingest of last month's sessions.
5. Reconsider OpenBrain only if juggling >2 AI tools daily.

### C5. Constraint check

All six met when graphify Pass 2 stays on a model you accept egress to (or is skipped). Pratiyush has redaction-by-default per inventory.

---

## D. Cross-project portfolio brain

### D1. Primary stack

**Per-repo (LLM Wiki + Graphify) + a thin federation index.** Federation today is hand-rolled. OpenBrain's compilation agent is roadmap, not shipping.

| Layer | Owner | Why |
|---|---|---|
| Per-repo | Karpathy wiki + Graphify (as in archetype A) | Preserves per-repo evidence tier and provenance |
| Federation | Small `~/portfolio/INDEX.md` + nightly cron merging per-repo `index.md` files | Axis 4 — federation, not consolidation |
| Cross-repo topology | Second graphify run over all repos → cross-repo communities tagged INFERRED | Axis 8 — separates within-repo (EXTRACTED) from cross-repo (INFERRED) |

**Driving axes**: 4 (cross-tool/cross-repo), 2 (augments per repo), 8 (provenance discipline survives federation). **Tier**: C; OpenBrain compilation-agent path is Tier D (not shipped).

### D2. Hybrid alternatives

| Hybrid | Optimizes | Pick when |
|---|---|---|
| Per-repo + OpenBrain federation (when compilation agent ships) | Live cross-repo recall | FSL-1.1-MIT terms acceptable; want concurrent multi-tool reads |
| Per-repo + claude-context only on code-heavy repos | Semantic recall in code without forcing every repo into vectors | Some repos are code, some are prose |
| Single mega-repo with tagged subfolders | Drops federation complexity | Repos are small and you're really managing one knowledge body |

### D3. Anti-patterns

- **Single-DB consolidation across all repos** (OpenBrain Postgres, claude-context Milvus): flattens per-repo evidence tiers; one repo's schema decisions infect another's. A single Milvus collection with vectors from prose + AST chunks produces nonsense neighbors.
- **Shared cross-repo graph as the *only* graph**: communities bleed across project boundaries. The cross-repo graph must be a *secondary* INFERRED-only view.

### D4. Adoption order

1. Each repo independently passes archetype-A adoption first.
2. Write a 50-line script concatenating per-repo `index.md` files into a portfolio INDEX.
3. Run `graphify ~/portfolio` over all repos to see what cross-repo edges emerge. **Stop if** edges are mostly noise.
4. Re-evaluate OpenBrain only after the compilation agent ships and you've reproduced its claims.

### D5. Constraint check

All six met when run as per-repo + thin federation. OpenBrain path defers local-first to self-hosted Postgres setup; FSL terms must be accepted.

---

## E. Work-state / project tracker

### E1. Primary stack

**Rowboat (typed entities, BYO-via-Composio) + a small LLM Wiki for the stable layer.**

| Layer | Owner | Why |
|---|---|---|
| Temporal | Rowboat-style typed-entity files (Decision/Commitment/Deadline/Person) | Axis 6 — temporal-dominant; this is the differentiator |
| Stable | Tiny Karpathy-style wiki for projects/people that don't change weekly | Avoids "page becomes contradiction soup" failure |
| Briefing | Rowboat background agents | Daily briefing surfaces overnight changes |

**Driving axes**: 6 (temporal), 8 (provenance per claim), 7 (markdown still — Rowboat README confirms "it's just Markdown"). **Tier**: C for the recommendation. Rowboat verified at [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) — Apache 2.0, 13.1k stars, desktop app for Mac/Windows/Linux.

### E2. Hybrid alternatives

| Hybrid | Optimizes | Pick when |
|---|---|---|
| Rowboat alone | Simplicity | The "stable" sliver is genuinely small (early project) |
| Plain markdown + dated journal + Obsidian | No new tooling | Rowboat install isn't justified; lose typed-entity queries, gain zero ops |
| Rowboat + Pratiyush ingestion | Pulling commitments out of meeting transcripts | Heavy meeting cadence |

### E3. Anti-patterns

- **Karpathy wiki on temporal data**: `Project X` page mutates daily; cross-refs go stale; wiki silently rots.
- **Graphify on a Rowboat vault**: graph rebuilds become the bottleneck because the corpus changes daily; Pass 2 LLM passes burn API on volatile content. Rowboat's typed entities make graphify redundant.

### E4. Adoption order

1. Pick three entity types (Decision, Commitment, Deadline). Hand-write 10 entity files. Reversible.
2. Add backlinks to existing project pages.
3. Install Rowboat (desktop app); point it at the vault. **Stop if** the daily briefing surfaces nothing you wouldn't have remembered.
4. Add Google services (Gmail/Calendar/Drive) or optional integrations only after step 3 earns its keep.

### E5. Constraint check

All met. Local-first holds for the markdown vault; Google services + optional Composio MCP / Deepgram / ElevenLabs / Exa add egress when enabled.

---

## F. Session-history transcript archive

### F1. Primary stack

**Pratiyush/llm-wiki (purpose-built) + Graphify on the resulting wiki for cross-session topology.**

| Layer | Owner | Why |
|---|---|---|
| Ingestion | Pratiyush adapters (Claude Code, Codex, Cursor, Gemini, Obsidian, Copilot) | Axis 4 — multi-agent coverage |
| Wiki | Pratiyush three-layer (`raw/` → `wiki/` → `site/`) | Provenance per session preserved in `raw/` |
| Topology | Graphify on the resulting wiki | Cross-session communities |

**Driving axes**: 1 (write-time mining heavy), 8 (provenance per session essential), 4 (cross-tool adapters). **Tier**: C.

### F2. Hybrid alternatives

| Hybrid | Optimizes | Pick when |
|---|---|---|
| Pratiyush alone | Lower complexity | Small archive (under a few hundred sessions) |
| Pratiyush + MehmetGoekce L1/L2 | Pinning crystallized rules in always-loaded layer | You keep re-discovering the same gotcha across sessions |
| Plain `.jsonl` parsing scripts | Zero install | Single-agent archive; multi-adapter selling point doesn't apply |

### F3. Anti-patterns

- **claude-context over raw transcripts**: encourages re-deriving conclusions every query rather than promoting durable knowledge. The whole point is write-time extraction.
- **Skipping redaction**: Pratiyush has redaction-by-default for keys/tokens; the others on this list don't. Indexing `~/.claude/projects/` without redaction risks publishing API keys to a static HTML site.

### F4. Adoption order

1. `./setup.sh` Pratiyush against last week of sessions only.
2. Inspect what gets promoted to `wiki/`. **Stop if** wiki entries are 90% noise.
3. Add `llmwiki sync` SessionStart hook (auto-trigger) once the noise floor is acceptable.
4. Run `graphify` over the produced `wiki/` only after a few weeks of accumulation.

### F5. Constraint check

All met. Provenance per session aligns with the wiki↔graph confidence constraint.

---

## G. Multi-tool team shared memory

### G1. Primary stack — roadmap-contingent

**Today's honest recommendation: wait, or roll your own.** OpenBrain's write-time/compilation-agent half is roadmap, not shipped — recommending it as primary now would treat Tier D speculation as Tier C evidence.

- **Wait** for OpenBrain's compilation agent to ship and reproduce its claims.
- **Roll a minimal Postgres + pgvector + tiny MCP shim** with per-user wiki overlay. Boring, well-understood components; avoids FSL-1.1-MIT terms entirely.

**Once OpenBrain ships** (hypothetical future state): OpenBrain (Postgres + pgvector + AI gateway, Postgres RLS) + per-user Karpathy wiki overlay would be the stack.

| Layer | Owner | Why |
|---|---|---|
| Shared | OpenBrain (Postgres + pgvector + AI gateway, Postgres RLS) | Axis 4 — cross-tool by definition; concurrency requires DB |
| Per-user | Personal Karpathy wiki overlay | Axis 2 — augments shared layer |
| Code (optional) | claude-context with self-hosted Milvus + Ollama embeddings | If team needs code-specific semantic search and can host the infra |

**Driving axes**: 4 (cross-tool concurrency), 7 leans DB here, 5 (self-hosted = local-first if BYO model). **Tier**: C for OpenBrain query-time; **D** for the compilation agent.

### G2. Hybrid alternatives

| Hybrid | Optimizes | Pick when |
|---|---|---|
| OpenBrain + claude-context (self-hosted) | Code-heavy team workflows | Significant fraction of team work is in code |
| OpenBrain + Pratiyush per-team snapshot | Retrospectives over team sessions | Heavy AI-tool adoption per-developer |
| Roll your own (Postgres + pgvector + tiny MCP) | Avoiding FSL terms | FSL-1.1-MIT 2-year reciprocal unacceptable for commercial reuse |

### G3. Anti-patterns

- **File-only markdown vault for a concurrent-write team**: file-conflict hell. Concurrent writes on file substrate fail.
- **OpenBrain for a single user**: MCP context tax + Postgres ops cost without the concurrency benefit. Use archetype C instead.

### G4. Adoption order

1. Two-person pilot with self-hosted Postgres+pgvector+MCP shim (or OpenBrain on Supabase).
2. Wire one MCP client (Claude Code) and one capture point (Slack or shared inbox). **Stop if** after two weeks no one queries the shared memory.
3. Add a second MCP client. Re-evaluate.
4. Defer compilation-agent integration until upstream ships and reproduces.

### G5. Constraint check

- Graphify feeds wiki: deferred until graph layer exists.
- No contradiction: ✅ via Postgres RLS + provenance columns.
- Tiering: ✅ as a column.
- Augments: ✅ at the per-user overlay.
- Local-first: ✅ self-hosted; ⚠️ only if BYO model.
- Markdown: ❌ — DB substrate justified by concurrency. Mitigate with periodic markdown export.

---

# Cross-cutting

## Migration paths

| From → To | What migrates | What gets rebuilt |
|---|---|---|
| A → D | Wiki convention; per-repo graphify configs; evidence-tier metadata | Federation index; cross-repo graph as INFERRED-only view |
| C → G | Markdown content (one-time export); wiki structure | Concurrency layer (Postgres); access control; per-user overlay re-pointed |
| F → A | Promoted findings (durable rules, recurring decisions) | Hand-curated analyses with evidence tiers; raw transcripts to cold storage |
| E → A | Typed-entity content about completed projects becomes summary pages | Temporal-lint cron dropped; structural lint takes over |
| B → D | Per-repo graphify outputs federate | Cross-repo graph; portfolio INDEX |
| C → E | Stable wiki pages stay; events split out into typed entities | Rowboat overlay; daily briefing |
| F → G | Pratiyush-produced wiki | Concurrency, RLS, redaction policy review |

## Never-combine list

| Combination | Failure |
|---|---|
| Pratiyush + MehmetGoekce on the same vault | Both want to author/organize the same wiki pages with different conventions; ingest passes overwrite each other's structure |
| Graphify + Lum1104 on the same corpus *without designating one as authoritative* | Two topology layers with no defined merge; results disagree silently. Running both is fine if one explicitly drives the contradiction-lint and the other is read-only — pick which |
| `graphify --wiki` export + a hand-curated wiki on the same content | Source-of-truth ambiguity; violates the graphify-feeds-wiki constraint |
| claude-context + OpenBrain pgvector | Two embedding indexes over similar content; doubled cost, drift, no defined merge strategy |
| Rowboat + LLM Wiki on the same content scope | Page-per-topic vs typed-entity-per-event collide; backlinks point in conflicting directions |
| OpenBrain Postgres + per-tool markdown vaults that diverge | DB and files drift; neither is authoritative |

## License / cost gotchas

| Tool | License | Egress | Commercial reuse |
|---|---|---|---|
| Karpathy gist | None stated | n/a (paradigm) | Convention only, not redistributable code |
| Graphify | MIT ✅ | Pass 2 LLM calls go through invoking Claude Code session | Free reuse; LLM cost via session; sensitive content leaves the box |
| Pratiyush/llm-wiki | MIT ✅ (verified 2026-04-28) | Depends on LLM choice | Free reuse; redaction-by-default per inventory |
| MehmetGoekce/llm-wiki | MIT ✅ (verified 2026-04-28) | Depends on LLM choice | Free reuse |
| Lum1104/Understand-Anything | MIT ✅ (verified 2026-04-28) | Depends on LLM choice | Free reuse |
| claude-context | MIT ✅ on code | Code → embedding provider; chunks → Milvus/Zilliz | Free reuse of code; recurring infra + provider cost; egress disqualifies for proprietary code unless Ollama + self-hosted Milvus |
| OpenBrain | **FSL-1.1-MIT** | None if self-hosted + BYO model | 2-year reciprocal restriction on competing managed services; converts to MIT after 2 years; internal commercial use fine |
| Rowboat ([rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat)) | **Apache 2.0** ✅ (verified 2026-04-28) | Google services (Gmail/Calendar/Drive) by default; optional Deepgram, ElevenLabs, Exa, Composio API keys | Free reuse with attribution; Google + optional-vendor egress; desktop app, not a library |
| InfraNodus ([infranodus/](https://github.com/infranodus)) | Proprietary SaaS (€12–66/mo); MIT MCP server + n8n nodes are open-source clients | Full content + GPT egress to InfraNodus servers | Subscription required for core; no self-hosted option; methodology is well-established (Paranyushkin / Nodus Labs, 10+ years) |

## Build-vs-borrow

| Archetype | Off-the-shelf gap | Build locally |
|---|---|---|
| A | Footer-injection script; contradiction lint | ~50–100 lines Python; reads `graph.json` + walks `analysis/*.md` |
| B | CI step to enforce reindex-on-PR | One GitHub Action with `graphify .` + cache key |
| C | "Promote-to-wiki" agent (graphify finding → wiki page draft for human review) | Local script ~1 day |
| D | Federation index across per-repo `index.md` files | 50-line script |
| E | Temporal lint ("deadline shifted past today") | Cron + small Python |
| F | Multi-agent dedup (same conclusion across 3 agents → single page) | Pratiyush partially does this; verify and extend |
| G | RBAC policies on top of Postgres RLS | Per-team policies; non-trivial |

## Evidence gaps — top 5 Tier C → Tier B

| # | Claim | Experiment to move to Tier B |
|---|---|---|
| 1 | Graphify's 71.5× token-savings claim | Reproduce on three corpora (pure code, pure prose, mixed); require ≥10× on at least two |
| 2 | Claude-context ~40% reduction | Reproduce on a real proprietary repo at 5k / 20k / 50k file sizes with a fixed query set |
| 3 | Karpathy paradigm "compounding insight" benefit | Run a 6-month retention study on a real ~500-doc KB: does query latency on novel questions actually drop? |
| 4 | Lum1104 wiki-aware vs graphify-on-wiki quality | A/B on the same vault; have a human rate edge usefulness blind |
| 5 | OpenBrain compilation agent (not shipped) | Wait for release; until then this is Tier D speculation, not C |

---

## Related analyses

- `analysis/memory-systems-recommendation-methodology.md` — framing, threshold math, self-critique behind these recommendations
- `analysis/memory-system-patterns.md` — earlier pattern survey (precedes this archetype-driven view)
- `analysis/federated-query-architecture.md` — relevant to archetype D
- `analysis/local-cloud-llm-orchestration.md` — relevant to the local-first constraint
