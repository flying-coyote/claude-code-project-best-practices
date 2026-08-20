---
version-requirements:
  claude-code: "v2.1.0+"
version-last-verified: "2026-04-06"
measurement-claims:
  - claim: "CLAUDE.md sizes range from 42-209 lines across 6 repos, correlating with project complexity and domain sensitivity"
    source: "Direct analysis — 6 repository CLAUDE.md files"
    date: "2026-04-06"
    revalidate: "2026-10-06"
  - claim: "~150 instruction cap for CLAUDE.md validated by Boris Cherny; excessive instructions degrade adherence below 80%"
    source: "Boris Cherny interviews (March 2026) + behavioral-insights.md"
    date: "2026-04-06"
    revalidate: "2026-10-06"
status: PRODUCTION
last-verified: "2026-08-13"
evidence-tier: A
convergence: converged
applies-to-signals: [claude-md-size, claude-md-references, claude-md-missing, claude-md-vague-descriptors, session-edit-thrashing, session-repeated-instructions, repo-has-agents-md]
revalidate-by: 2026-10-22
---

# CLAUDE.md Progressive Disclosure: How Project Context Scales

> **Collapsed 2026-07-10 (Reduction Phase 4).** The prescription is now first-party (official CLAUDE.md guidance: include/exclude table, imports, child files, "prune ruthlessly"; /init). Kept delta: the portfolio's measured 42–209-line data and the ~150-line boundary evidence.

**Evidence Tier**: Mixed (A-B) — Direct observation across 6 repos (Tier A), validated by Boris Cherny ~150 instruction cap (Tier B)

## Purpose

This document tracks how CLAUDE.md size scales with project complexity, based on direct observation across 6 repositories. What remains here is the measured portfolio: the 42-209 line size range across six repos, and the ~150-instruction adherence boundary reported by Boris Cherny.

---

## Three Maturity Tiers

### Tier 1: Minimal (42-57 lines)

**Examples**: zeek-iceberg-demo (55 lines), network-visualization-services (42 lines), third-brain (57 lines)

**Sections**: Project overview, quick reference commands, key files, git workflow

**When appropriate**: Demos, reference implementations, lightweight services, knowledge management. The project has clear boundaries and the agent doesn't need extensive guardrails.

**Typical structure**:

```markdown
# Project Name
One-paragraph description.

## Commands
- `npm run build` — Build project
- `pytest tests/` — Run tests

## Key Files
- `src/main.py` — Entry point
- `config/settings.yaml` — Configuration

## Git Workflow
Commit prefixes: feat:, fix:, docs:
```

### Tier 2: Resource Map (99-112 lines)

**Examples**: health-inventory (112 lines)

**Sections**: Commands, critical query parameters, resource map (organized by directory: scripts/, lib/, config/, data/, tests/, docs/), environment variables, known gotchas, workflow

**When appropriate**: Data pipelines, monitoring systems, projects with multiple entry points and domain-specific conventions. The agent needs to know where things are and what conventions to follow, but doesn't handle sensitive data.

**Key addition over Tier 1**: The **resource map** — a structured directory of what's where, organized by function rather than alphabetically. This prevents the agent from spending tokens exploring the filesystem.

### Tier 3: Rules + Security (166-209 lines)

**Examples**: mndr-review-automation (166 lines), Splunk-db-connect-benchmark (209 lines)

**Sections**: Security boundaries (FIRST), architecture (pipeline steps, intake workflow, escalation triggers), key paths (extensive file list), relationship to other repos, rules, tests inventory

**When appropriate**: Production pipelines with sensitive data, complex multi-step architectures, projects with compliance requirements. The agent needs both domain context and hard constraints.

**Critical pattern**: mndr-review-automation opens with **"Security Boundaries — READ THIS FIRST"** before any other content. This front-loading ensures the agent encounters data isolation rules before it encounters any instructions that might tempt it to read raw customer data.

---

## Comparison Across 6 Repos

| Repository | Lines | Tier | First Section | Rules | Commands | Agents |
|-----------|-------|------|---------------|-------|----------|--------|
| network-visualization-services | 42 | 1 | Status + service framework | 0 | 1 | 0 |
| zeek-iceberg-demo | 55 | 1 | Project overview + OCSF pipeline | 0 | 4 | 0 |
| third-brain | 57 | 1 | Knowledge management lifecycle | 5 | 0 | 0 |
| health-inventory | 112 | 2 | Commands + critical parameters | 4 | 0 | 0 |
| mndr-review-automation | 166 | 3 | **Security Boundaries** | 4 | 0 | 1 |
| Splunk-db-connect-benchmark | 209 | 3 | Purpose + architecture | 0 | 4 | 0 |

### Disclosure Hierarchy Within Each File

Regardless of tier, a consistent ordering emerges:

1. **Lines 1-10**: Project identity + immediate action items (or security boundaries for sensitive projects)
2. **Lines 10-30**: Quick reference commands and critical parameters
3. **Lines 30-60**: Resource map (file organization, key modules)
4. **Lines 60+**: Specialized concerns (architecture detail, tests, integrations, gotchas)

---

## The ~150-Instruction Boundary

Boris Cherny's guidance (March 2026): Keep CLAUDE.md under ~150 instructions. Beyond this, adherence drops below the already-imperfect ~80% baseline.

---

## AGENTS.md Interop

AGENTS.md (agents.md) is the emerging cross-tool agent-config standard, stewarded by the Agentic AI Foundation under the Linux Foundation as of 2026, adopted across tens of thousands of repos and read by 20+ agents; Claude Code reads it, with CLAUDE.md remaining the richer native format (Tier B, verified 2026-07-16). This doc's sizing/disclosure evidence applies to either file. Trigger to watch: the AGENTS.md ecosystem publishing data-backed sizing guidance would flip this doc's absorption row.

Update (2026-08-19): the split-brain audit this doc's `repo-has-agents-md` signal feeds now covers files consumed by two runtimes in fact, because DeepSeek Harness (dsh v0.1, released 2026-08-13) natively discovers both AGENTS.md and CLAUDE.md, plus their `.local.md` overlays, from home and root-to-cwd, injecting them under a maxBytes budget that drops whole broader files before truncating the single most-specific one (Tier A, `packages/context/agent-instructions/README.md` in [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness), verified 2026-08-19). That budget mechanic is a second independent data point that instruction-file loading is budget-bounded, beside Claude Code's own memory-loading budget, and it is a reason split-brain drift between the two files now carries cross-runtime consequences, since a divergent pair is consumed by two harnesses rather than one.

---

## Currency (2026-08-13) — First-Party Adopts "Progressive Disclosure" by Name

Anthropic's ["The new rules of context engineering for Claude 5 generation models"](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) (2026-07-24, Thariq Shihipar, Claude Code team) is a **first-party endorsement of this doc's core thesis**. Progressive disclosure is now a named, recommended shift in official guidance rather than an observed portfolio pattern.

**Source caveat — read the tier carefully.** This is a Tier A source (first-party, Anthropic-authored) but it is **mirror-verified 2026-08-13; direct fetch blocked** (claude.com/blog serves a login-wall redirect to our fetcher, so content was verified through an independent mirror rather than the primary URL). Quoted text below is verbatim via that mirror. Re-verify against the primary URL when it becomes fetchable before citing the quotes as settled.

**The headline claim**: "We removed over 80% of Claude Code's system prompt" for Opus 5 and Fable 5 "with no measurable loss on coding evals." Note the scope — that is Anthropic pruning *its own* system prompt for the Claude 5 generation, not a measured claim about user-authored CLAUDE.md files. It is directionally consistent with the ~150-instruction boundary above (less instruction text, no adherence penalty) but it does not re-measure it, and it does not license deleting 80% of a CLAUDE.md.

**The six named shifts** (paraphrased from the post):

| Shift | From | To |
|---|---|---|
| 1 | Rules | Judgment |
| 2 | Examples | Interface design |
| 3 | Upfront context | **Progressive disclosure** |
| 4 | Repetition | Single source of truth |
| 5 | Manual CLAUDE.md | Auto-memory |
| 6 | Simple specs | Rich references |

The post also recommends **`/doctor`** to audit and rightsize agent context — a first-party instrument for the sizing question this doc answers with measurement.

**Absorption reading (partial-absorption signal — flagged, not acted on).** Per this project's absorption discipline, first-party guidance that names and recommends the concept is exactly the trigger shape for a lane change: the *concept* half of this doc (why progressive disclosure, and shifts 3/4/6 in particular) is now carried first-party. What remains as this doc's delta is the part first-party does not carry: the **measured 42–209-line 6-repo dataset**, the three-tier sizing rationale derived from it, and the ~150-instruction adherence boundary. **Flagged for the next absorption sweep** — status, `follows:`, and lane frontmatter are deliberately left unchanged here; that call belongs to the sweep, not to a currency note.

### Model-side interaction — the reference-enforcement warning gains a counterpoint

Shifts 3 and 5 (progressive disclosure, auto-memory) presuppose a model that **follows references reliably** — a CLAUDE.md that points at `rules/data-isolation.md` is only progressive disclosure if the pointer actually gets followed. That assumption is in direct tension with the Opus 4.7-era "references without read-enforcement" failure mode (Tier A, Anthropic migration guide — the row that cites this doc in [`model-migration-anti-patterns.md`](model-migration-anti-patterns.md)), where referenced files were frequently not read and mechanical enforcement was the remediation. Opus 4.8 softened it ("less likely to skip a tool call the task required") without eliminating it.

**Keep the mechanical-enforcement remediation** (PreToolUse hook or an explicit Read step) for any 100%-adherence requirement until re-measured on a Claude 5-family model. The strongest evidence in the other direction is still weak: the Fable-era probe found the reference-only arm read the fixture **4/4 without enforcement**, but that is recorded as **descriptive only** — the explicit-Read control was also 4/4 (saturated pair, zero within-study contrast), and it measures Fable, not Opus 5 or the Sonnet 5 default. Nothing in the Claude 5-generation guidance is a measurement of reference-following. Treat the first-party shift as a design direction, not as permission to drop enforcement on sensitive rules.

---

## Sources

### Tier A (Direct Production Observation)

- 6-repository CLAUDE.md comparison (April 2026) — Line counts, section structures, tier classification across zeek-iceberg-demo, third-brain, mndr-review-automation, health-inventory, network-visualization-services, Splunk-db-connect-benchmark
- Anthropic / Thariq Shihipar (Claude Code team), ["The new rules of context engineering for Claude 5 generation models"](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) (2026-07-24) — first-party guidance naming progressive disclosure as a recommended shift; the "removed over 80% of Claude Code's system prompt … with no measurable loss on coding evals" claim; six shifts; `/doctor` for context rightsizing. **Tier A source, mirror-verified 2026-08-13 (direct fetch blocked — claude.com/blog login-wall redirect).** Re-verify quotes against the primary URL when fetchable.

### Tier B (Validated / Expert Practitioner)

- Boris Cherny (March 2026) — ~150 instruction cap, CLAUDE.md as advisory (~80% adherence), hooks for enforcement

### Related Analysis

- [Behavioral Insights](./behavioral-insights.md) — ~80% CLAUDE.md adherence rate, 60% context degradation threshold, ~150 instruction cap

---

*Last updated: 2026-08-19 (AGENTS.md interop extended — DeepSeek Harness reads both files natively with a maxBytes budget, a second budget-bounded-loading data point). Prior: 2026-08-13 (currency section on Anthropic's Claude 5-generation context-engineering post — first-party adoption of "progressive disclosure" by name, the 80%-system-prompt-reduction claim, the six shifts, `/doctor`; mirror-verified with direct-fetch-blocked caveat; partial-absorption signal flagged for the next sweep without touching status/lane frontmatter; model-side counterpoint on reference-following enforcement; `last-verified` → 2026-08-13). Prior: 2026-07-16 (added AGENTS.md interop note; `repo-has-agents-md` added to applies-to-signals). Prior: July 2026.*
<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/model-migration-anti-patterns.md`](analysis/model-migration-anti-patterns.md) [EXTRACTED (1.00)] — references

<!-- graphify-footer:end -->
