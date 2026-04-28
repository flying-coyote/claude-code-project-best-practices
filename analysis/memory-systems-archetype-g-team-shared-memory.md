---
status: EMERGING
last-verified: "2026-04-28"
evidence-tier: C
applies-to-signals: [memory-systems, team-shared-memory, multi-tool-concurrency]
revalidate-by: 2026-10-28
---

# Archetype G — Multi-Tool Team Shared Memory

**Evidence Tier**: C for query-time; **D** for the OpenBrain compilation agent (not shipped). Today's honest primary is "wait or roll your own."

## Purpose

Per-archetype recommendation for **concurrent-write team shared memory** across multiple AI tools — where file substrate fails to concurrency and a database becomes structurally necessary.

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

**Driving axes**: 4 (cross-tool concurrency), 7 leans DB here, 5 (self-hosted = local-first if BYO model). **Tier**: C for OpenBrain query-time; **D** for the compilation agent.

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

## Related Analysis

- [`memory-systems-archetype-recommendations.md`](memory-systems-archetype-recommendations.md) — index across all 7 archetypes + cross-cutting sections
- [`memory-systems-recommendation-methodology.md`](memory-systems-recommendation-methodology.md) — framing and self-critique
