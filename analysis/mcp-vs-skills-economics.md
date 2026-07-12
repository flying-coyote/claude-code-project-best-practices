---
version-requirements:
  claude-code: "v2.0.0+"
version-last-verified: "2026-02-27"
measurement-claims:
  - claim: "Skills are 50% cheaper than MCP ($10.27 vs $20.78 per task) (stale-pending-remeasure: MCP tool search v2.1.121 changed token economics)"
    source: "Tenzir production data"
    date: "2026-01-15"
    revalidate: "2026-10-10"
  - claim: "MCP is 38% faster than Skills (6.2 min vs 8.6 min) (stale-pending-remeasure: MCP tool search v2.1.121 changed token economics)"
    source: "Tenzir production data"
    date: "2026-01-15"
    revalidate: "2026-10-10"
  - claim: "Skills use 55% less cached tokens (4.0M vs 8.8M) (stale-pending-remeasure: MCP tool search v2.1.121 changed token economics)"
    source: "Tenzir production data"
    date: "2026-01-15"
    revalidate: "2026-10-10"
status: PRODUCTION
last-verified: "2026-07-10"
evidence-tier: B
convergence: single-source  # cost-delta function is one Tenzir dataset; the CLI+Skill section documents its own multi-source support for the pattern claim only
applies-to-signals: [harness-skills, harness-mcp]
revalidate-by: 2026-07-15
---

# MCP vs Skills Economics

> **Collapsed 2026-07-10 (Reduction Phase 4).** The choice guidance went native (official features-overview decision table). Kept delta: the measured cost economics (Tenzir $10.27 vs $20.78/task), flagged stale-pending-remeasure since tool search (v2.1.121) changed MCP's token economics.

**Source**: [Tenzir Blog - "We Did MCP Wrong"](https://tenzir.com/blog/we-did-mcp-wrong) (Matthias Vallentin, January 2026)
**Evidence Tier**: B (Production data from active project)

MCP (Model Context Protocol) and Skills are two different approaches to extending Claude Code's capabilities. Production data showed Skills at roughly 50% cheaper than an equivalent MCP implementation, though MCP finished faster. For live choice guidance between the two, see the official features-overview decision table; this doc keeps only the measured cost delta behind that comparison.

> "When you're paying per token, 'slower but half price' wins."
> — Matthias Vallentin, Tenzir

---

## The Production Data

Tenzir compared identical workflows delivered via MCP server vs Claude Code Skills. Every figure below is a pre-tool-search measurement: (stale-pending-remeasure: MCP tool search v2.1.121 changed token economics).

| Metric | MCP | Skills | Winner |
|--------|-----|--------|--------|
| **Duration** | 6.2 min | 8.6 min | MCP (38% faster) |
| **Tool calls** | 61 | 52 | Skills (15% fewer) |
| **Cost** | $20.78 | $10.27 | **Skills (50% cheaper)** |
| **Cached tokens** | 8.8M | 4.0M | Skills (55% less) |

**Key finding**: Skills produced working output at half the cost of MCP — $10.27 vs $20.78 per task — measured before MCP tool search shipped.

---

## Why the Cost Difference

The MCP run relied on three custom tools (`run_pipeline`, `docs_read`, `run_test`) built as purpose-built infrastructure, each call a round-trip to the MCP server — 61 calls total. The Skills run used mostly generic tools (Bash, Read, Write, Task), with the domain knowledge loaded as context rather than infrastructure — 52 calls total. That infrastructure-vs-context split produced the cached-token gap (8.8M vs 4.0M), which is also the gap MCP tool search now targets directly: deferring tool definitions instead of loading the full MCP surface up front cuts into that cached-token cost. Until the comparison is re-run against a tool-search-enabled MCP server, the relative size of that gap is stale-pending-remeasure.

---

## The CLI + Skill Pattern (When the Vendor MCP Falls Short)

Vallentin's March 2026 [LinkedIn post](https://lnkd.in/dqHjgHc6) extends the original "We Did MCP Wrong" thesis to a concrete situation that recurs across SaaS tools: **the official MCP server is read-only, but the agent needs write access.**

The worked example is Attio (a CRM). Attio's official MCP server lets an agent browse records but not create, update, or annotate them — a fundamental gap for a tool meant to let agents act. Rather than wait for the vendor to ship write endpoints, Vallentin built a CLI for the Attio API and paired it with a skill that teaches the agent when and how to invoke it.

### Four-Step Recipe to CLI-ify Any REST API

| Step | Action | Tool |
|------|--------|------|
| 1 | Take the published OpenAPI spec | Vendor docs |
| 2 | Generate a typed SDK | `@hey-api/openapi-ts` |
| 3 | Wire the SDK into a CLI | `commander` |
| 4 | Write a skill that documents *when* and *how* the agent should reach for the CLI | Markdown skill file |

Reference implementation: [`mavam/clattio`](https://lnkd.in/dqHjgHc6) — installable as `npx skills add mavam/clattio`, delivers complete read-write access to Attio without an MCP transport.

### When This Pattern Wins

- The vendor's MCP server is missing write or admin operations you need.
- The vendor publishes a usable OpenAPI spec (the recipe is mechanical from there).
- The team is comfortable maintaining a thin CLI wrapper as a Unix-style binary (no transport layer, no server lifecycle).
- The skill that accompanies the CLI is what minimizes time-to-value for the agent — without it, the agent must discover the CLI by reading `--help`.

### Convergence: Independent Practitioners Reaching the Same Conclusion (Q1–Q2 2026)

Vallentin's framing isn't a one-off. By Q2 2026 multiple independent practitioners — and at least two database/data-tool vendors — had publicly described the same conclusion: for many integrations, a CLI shipped to the agent beats an MCP server, especially when the agent is already comfortable shelling out.

| Practitioner / vendor | Date | Source | What they shipped or argued |
|---|---|---|---|
| Matthias Vallentin (Tenzir) | 2026-03-17 | [LinkedIn post + `mavam/clattio`](https://lnkd.in/dqHjgHc6) | OpenAPI → typed SDK → CLI → skill recipe for Attio |
| Hoyt Emerson | 2026-04-07 | LinkedIn post about Fletch CLI for ADBC data transfers | "A local CLI tool allows you to simply run commands and functions you normally would in the terminal, with the added support of using your agent to do this... if the CLI already handles auth locally... then why use an MCP server?" |
| Hex (referenced in Hoyt's post) | April 2026 | Product release | Shipped a CLI **alongside** their existing MCP server — same vendor offering both, with the CLI explicitly aimed at agent use |
| ClickHouse | 2026 | [Futurum coverage](https://futurumgroup.com/insights/clickhouse-builds-a-cli-to-make-its-databases-agent-native/) | Built a CLI to make ClickHouse databases agent-native — vendor decision, not third-party wrapper |
| Jannik Reinhard | 2026-02-22 | [Independent blog](https://jannikreinhard.com/2026/02/22/why-cli-tools-are-beating-mcp-for-ai-agents/) | Practitioner essay titled "Why CLI Tools Are Beating MCP for AI Agents" |
| OSS Insight | 2026-05 | ["Agent-Native CLI Wave"](https://ossinsight.io/blog/agent-native-cli-wave-2026) | Trend piece: counts ≥6 major repos that launched in Q1 2026 with the premise "take existing software, give it a structured CLI for agents" |

**Implication**: The recipe and the underlying observation are not a Tenzir-specific commercial framing — they are reproducible enough that independent practitioners and at least two database/data-tool vendors arrive at the same conclusion. This strengthens the *pattern* claim (CLI + Skill works) without strengthening the *categorical* claim (MCP is bad). Multiple shops shipping the same pattern is evidence the pattern works; it is not evidence the alternative is wrong — note that Hex chose to ship **both** a CLI and an MCP server, treating them as complementary rather than as substitutes.

A second framing from Hoyt's same post — "agents should build their tools for themselves first" (agent self-tooling) — remains a single-practitioner observation with one emerging-tool data point (Browser Harness) and is not yet corroborated. Track separately.

### Caveat: Vendor Incentive

Vallentin's company (Tenzir) builds agent-friendly data tooling, so the **categorical** claim that "MCP is a solution in search of a problem Unix solved decades ago" reflects commercial framing. Two parts deserve separate treatment:

| Claim | Status |
|-------|--------|
| "Attio's MCP server is read-only" | Verifiable observation about one vendor's implementation |
| "CLI + Skill > MCP for SaaS tools where OpenAPI exists" | Defensible pattern; reproducible recipe |
| "MCP is a solution in search of a problem" | Opinion — discount accordingly |

Import the recipe; don't import the categorical conclusion. Under the repo's convergence rule this doc is classed single-source (the measured cost delta rests on one Tenzir dataset), so adopting the recipe as standing infrastructure requires converged status or an explicit owner exception.

This pattern is **complementary to** the MCP-vs-Skills cost comparison above, not a replacement. The cost data (`$10.27` vs `$20.78`) addresses workflows where both options exist; the CLI+Skill recipe addresses the case where the vendor MCP doesn't expose what you need at all.

---

## Sources

**Primary (Tier B)**: [Tenzir Blog - "We Did MCP Wrong"](https://tenzir.com/blog/we-did-mcp-wrong) — Matthias Vallentin, January 2026. Cost economics (50% cheaper, 38% slower, 55% less cached tokens) — stale-pending-remeasure: MCP tool search v2.1.121 changed token economics; revalidate 2026-10-10.

**Secondary (Tier C)**: [Matthias Vallentin LinkedIn — "CLI + Skill > MCP"](https://lnkd.in/dqHjgHc6) — March 17, 2026. Four-step CLI-ification recipe; reference implementation `mavam/clattio`. Vendor-incentive caveat applies (see above).

*Last updated: 2026-07-10*

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/behavioral-insights.md`](analysis/behavioral-insights.md) [EXTRACTED (1.00)] — references
- [`AUDIT-CONTEXT.md`](AUDIT-CONTEXT.md) [EXTRACTED (1.00)] — references
- [`INDEX.md`](INDEX.md) [EXTRACTED (1.00)] — references

<!-- graphify-footer:end -->
