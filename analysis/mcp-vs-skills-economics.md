---
version-requirements:
  claude-code: "v2.0.0+"
version-last-verified: "2026-02-27"
measurement-claims:
  - claim: "Skills were 50% cheaper than MCP ($10.27 vs $20.78 per task) — HISTORICAL pre-tool-search measurement (2026-01), deferred to first-party /usage per-category 2026-07-16; kept as the controlled A/B record, not live guidance"
    source: "Tenzir production data"
    date: "2026-01-15"
  - claim: "MCP was 38% faster than Skills (6.2 min vs 8.6 min) — HISTORICAL pre-tool-search measurement (2026-01), deferred 2026-07-16; kept as the controlled A/B record, not live guidance"
    source: "Tenzir production data"
    date: "2026-01-15"
  - claim: "Skills used 55% less cached tokens (4.0M vs 8.8M) — HISTORICAL pre-tool-search measurement (2026-01), deferred 2026-07-16; kept as the controlled A/B record, not live guidance"
    source: "Tenzir production data"
    date: "2026-01-15"
status: RETIRING
replacement-by: "Anthropic /usage per-category breakdown (first-party, GA — code.claude.com/docs/en/costs, Pro/Max/Team/Enterprise) — live cost attribution to skills, subagents, plugins, and per-MCP-server as % of plan usage (24h/7d, local-machine, approximate). Bar PARTIAL: first-party + GA + citeable clear; covers-slice only partly — supersedes the stale absolute Tenzir cost figures as the live cost signal. Retained here: the controlled same-workflow A/B instrument (identical task via MCP vs Skills, incl. duration and cached-token dimensions) that /usage cannot produce from your own usage mix. Relocated 2026-07-16: the multi-source CLI+Skill pattern → mcp-patterns.md (not a /usage concern)."
last-verified: "2026-07-16"
evidence-tier: B
convergence: single-source  # the retained cost-delta record is one Tenzir dataset; live cost signal deferred to first-party /usage (see replacement-by); the CLI+Skill pattern and its multi-source support relocated to mcp-patterns.md 2026-07-16
applies-to-signals: [harness-skills, harness-mcp]
revalidate-by: 2026-09-30
---

# MCP vs Skills Economics

> **Replacement status: RETIRING (2026-07-16, Absorption Scan 2026-07 §2.1).** The live cost-signal function is first-party now: `/usage` attributes recent usage to skills, subagents, plugins, and individual MCP servers as a percentage of the total ([code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs)). Use `/usage` for current numbers — every figure below is a pre-tool-search January-2026 snapshot kept as a historical record. The one thing this doc still uniquely carries is methodological: the controlled same-workflow A/B instrument (see below), which an observational monitor cannot produce. The CLI+Skill pattern moved to [`mcp-patterns.md`](mcp-patterns.md). Expected completion: RETIRED + archived at the 2026-09-30 review.

**Source**: [Tenzir Blog - "We Did MCP Wrong"](https://tenzir.com/blog/we-did-mcp-wrong) (Matthias Vallentin, January 2026)
**Evidence Tier**: B (Production data from active project; historical record)

MCP and Skills are two approaches to extending Claude Code's capabilities. Tenzir's January-2026 production comparison showed Skills at roughly 50% cheaper than an equivalent MCP implementation, though MCP finished faster — measured before MCP tool search (v2.1.121) changed MCP's token economics, so the absolute figures are a dated snapshot, not live guidance. For live choice guidance see the official features-overview decision table; for your own live cost mix, `/usage`.

> "When you're paying per token, 'slower but half price' wins."
> — Matthias Vallentin, Tenzir

---

## The Production Data (historical record, 2026-01)

Tenzir compared identical workflows delivered via MCP server vs Claude Code Skills. Every figure below is a pre-tool-search measurement, preserved as recorded:

| Metric | MCP | Skills | Winner |
|--------|-----|--------|--------|
| **Duration** | 6.2 min | 8.6 min | MCP (38% faster) |
| **Tool calls** | 61 | 52 | Skills (15% fewer) |
| **Cost** | $20.78 | $10.27 | **Skills (50% cheaper)** |
| **Cached tokens** | 8.8M | 4.0M | Skills (55% less) |

---

## Why the Cost Difference

The MCP run relied on three custom tools (`run_pipeline`, `docs_read`, `run_test`) built as purpose-built infrastructure, each call a round-trip to the MCP server — 61 calls total. The Skills run used mostly generic tools (Bash, Read, Write, Task), with the domain knowledge loaded as context rather than infrastructure — 52 calls total. That infrastructure-vs-context split produced the cached-token gap (8.8M vs 4.0M), which is also the gap MCP tool search now targets directly by deferring tool definitions instead of loading the full MCP surface up front.

---

## What the First-Party Replacement Does Not Cover (the retained instrument)

`/usage` attributes your live usage mix to categories — skills, subagents, plugins, per-MCP-server, each as a share of plan usage — and that makes it the right live cost signal. It structurally cannot produce a controlled comparison, because if you built a workflow one way there is no counterfactual to report: it will never tell you what the identical task would have cost implemented the other way, and it reports no per-implementation duration or cached-token comparison. When a build-vs-borrow decision needs the comparative number, the instrument is a Tenzir-style A/B — the same task built both ways, measured head-to-head. That instrument, not the January-2026 figures, is what this doc retains until retirement completes.

---

## Sources

**Primary (Tier B)**: [Tenzir Blog - "We Did MCP Wrong"](https://tenzir.com/blog/we-did-mcp-wrong) — Matthias Vallentin, January 2026. Historical cost economics (50% cheaper, 38% slower, 55% less cached tokens), pre-tool-search snapshot.

**First-party replacement (Tier A)**: [Manage costs effectively — /usage per-category breakdown](https://code.claude.com/docs/en/costs) — verified 2026-07-16.

*Last updated: 2026-07-16 (RETIRING — live cost signal deferred to /usage; CLI+Skill pattern relocated to mcp-patterns.md; Tenzir figures marked historical).*

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/behavioral-insights.md`](analysis/behavioral-insights.md) [EXTRACTED (1.00)] — references
- [`AUDIT-CONTEXT.md`](AUDIT-CONTEXT.md) [EXTRACTED (1.00)] — references
- [`INDEX.md`](INDEX.md) [EXTRACTED (1.00)] — references

<!-- graphify-footer:end -->
