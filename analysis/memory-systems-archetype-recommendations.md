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
applies-to-signals: [memory-systems, knowledge-base, second-brain, wiki, graph, md-corpus-small, md-corpus-design-target, md-corpus-large, md-corpus-very-large, vault-obsidian, vault-karpathy, project-type-docs]
revalidate-by: 2026-10-28
---

# Memory & Knowledge System Recommendations — Index

Per-archetype primary stacks live in their own files (split 2026-04-28 to match this repo's "one pattern per file" convention). This doc is the index plus cross-cutting sections (migration paths, never-combine list, license/cost gotchas, build-vs-borrow, evidence gaps).

Calibrated to **~500-document curated knowledge bases** as the single-curator design target. See [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md) for the framing, threshold math, self-critique, and applied corrections behind these recommendations.

> **Source documents** (read first):
>
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

## Per-archetype recommendations

| # | Archetype                                  | Primary stack (one-line)                                                                                       | Doc                                                                                                                              |
|---|--------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| A | Curated analytical knowledge base          | Lum1104 below ~200 docs; Graphify + footer-injection at the ~500-doc design target                              | [`memory-systems-archetype-a-curated-kb.md`](memory-systems-archetype-a-curated-kb.md)                                            |
| B | Code monorepo / large codebase             | Graphify alone under ~10k files; + claude-context above                                                          | [`memory-systems-archetype-b-code-monorepo.md`](memory-systems-archetype-b-code-monorepo.md)                                      |
| C | Personal cross-domain second brain         | Karpathy LLM Wiki + Graphify (footer-injection) + Pratiyush adapters                                             | [`memory-systems-archetype-c-personal-second-brain.md`](memory-systems-archetype-c-personal-second-brain.md)                      |
| D | Cross-project portfolio brain              | Per-repo (LLM Wiki + Graphify) + thin federation index                                                           | [`memory-systems-archetype-d-cross-project-portfolio.md`](memory-systems-archetype-d-cross-project-portfolio.md)                  |
| E | Work-state / project tracker               | Rowboat (typed entities) + small LLM Wiki for stable layer                                                       | [`memory-systems-archetype-e-work-state-tracker.md`](memory-systems-archetype-e-work-state-tracker.md)                            |
| F | Session-history transcript archive         | Pratiyush/llm-wiki + Graphify on the resulting wiki                                                              | [`memory-systems-archetype-f-session-archive.md`](memory-systems-archetype-f-session-archive.md)                                  |
| G | Multi-tool team shared memory              | Wait or roll your own (Postgres + pgvector + MCP); OpenBrain stack contingent on roadmap                          | [`memory-systems-archetype-g-team-shared-memory.md`](memory-systems-archetype-g-team-shared-memory.md)                            |

---

# Cross-cutting

## Migration paths

| From → To | What migrates                                                                  | What gets rebuilt                                                                |
|-----------|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| A → D     | Wiki convention; per-repo graphify configs; evidence-tier metadata              | Federation index; cross-repo graph as INFERRED-only view                         |
| C → G     | Markdown content (one-time export); wiki structure                              | Concurrency layer (Postgres); access control; per-user overlay re-pointed        |
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

## Build-vs-borrow

| Archetype | Off-the-shelf gap                                                            | Build locally                                                              |
|-----------|------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| A         | Footer-injection script; contradiction lint                                   | ~50–100 lines Python; reads `graph.json` + walks `analysis/*.md`           |
| B         | CI step to enforce reindex-on-PR                                              | One GitHub Action with `graphify .` + cache key                             |
| C         | "Promote-to-wiki" agent (graphify finding → wiki page draft for human review) | Local script ~1 day                                                         |
| D         | Federation index across per-repo `index.md` files                              | 50-line script                                                             |
| E         | Temporal lint ("deadline shifted past today")                                  | Cron + small Python                                                         |
| F         | Multi-agent dedup (same conclusion across 3 agents → single page)              | Pratiyush partially does this; verify and extend                            |
| G         | RBAC policies on top of Postgres RLS                                           | Per-team policies; non-trivial                                              |

## Evidence gaps — top 5 Tier C → Tier B

| # | Claim                                                                | Experiment to move to Tier B                                                                                            |
|---|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| 1 | Graphify's 71.5× token-savings claim                                  | Reproduce on three corpora (pure code, pure prose, mixed); require ≥10× on at least two                                  |
| 2 | Claude-context ~40% reduction                                          | Reproduce on a real proprietary repo at 5k / 20k / 50k file sizes with a fixed query set                                  |
| 3 | Karpathy paradigm "compounding insight" benefit                        | Run a 6-month retention study on a real ~500-doc KB: does query latency on novel questions actually drop?                |
| 4 | Lum1104 wiki-aware vs graphify-on-wiki quality                         | A/B on the same vault; have a human rate edge usefulness blind                                                            |
| 5 | OpenBrain compilation agent (not shipped)                              | Wait for release; until then this is Tier D speculation, not C                                                            |

---

## Related analyses

- [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md) — framing, threshold math, self-critique behind these recommendations
- [`memory-system-patterns.md`](memory-system-patterns.md) — earlier pattern survey (precedes this archetype-driven view)
- [`federated-query-architecture.md`](federated-query-architecture.md) — relevant to archetype D
- [`local-cloud-llm-orchestration.md`](local-cloud-llm-orchestration.md) — relevant to the local-first constraint
