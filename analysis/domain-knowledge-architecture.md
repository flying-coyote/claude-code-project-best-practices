---
version-requirements:
  claude-code: "v2.1.0+"
version-last-verified: "2026-03-30"
measurement-claims:
  - claim: "Skills consume ~2% of context budget each"
    source: "Anthropic documentation"
    date: "2026-03-19"
    revalidate: "2026-09-19"
  - claim: "Quality degrades at 60% context capacity"
    source: "Boris Cherny (March 2026)"
    date: "2026-03-01"
    revalidate: "2026-09-01"
  - claim: "MCP servers add 300-800ms baseline latency"
    source: "MCP patterns analysis"
    date: "2026-03-01"
    revalidate: "2026-09-01"
status: PRODUCTION
last-verified: "2026-07-10"
evidence-tier: Mixed
convergence: emerging  # AI-PKM caveat (B-F1 seed): emerging WITH license risk — Obsidian Smart Connections ~786K downloads but Jan-2026 proprietary switch (DR-6 verified)
applies-to-signals: [project-type-domain-heavy, typed-memory-no-registry]
revalidate-by: 2026-09-30
---

# Domain Knowledge Architecture: Making Expertise Findable Without Overwhelming Context

> **Collapsed 2026-07-10 (Reduction Phase 4).** The core recommendation (skills for domain knowledge, CLAUDE.md for what applies broadly) is now the documented first-party default. Kept delta: the domain-heavy findability patterns that go beyond it.

This is the companion document to [Harness Engineering](./harness-engineering.md), focused on the domain knowledge layer of the harness stack.

---

## The Problem, In Brief

Domain-heavy projects — security rule ecosystems, infrastructure-as-code, regulatory compliance — fail in three ways: the LLM can't find resources that already exist and reinvents them; loading enough domain knowledge to be useful pushes context past the ~60% capacity threshold where quality degrades ([Behavioral Insights](./behavioral-insights.md)); and different sessions produce different approaches to the same problem absent an enforced methodology. Skills and CLAUDE.md now solve the top-level split (methodology vs. always-on context) by default. What's left unsolved is *findability inside a domain* — pointing an agent at the right rule file, typed note, or live lookup without loading the domain into context up front. That's what the rest of this document covers.

---

## The Progressive Disclosure Stack

| Layer | Mechanism | What It Contains | When It Loads | Context Cost |
|-------|-----------|-----------------|---------------|-------------|
| **Always-on** | CLAUDE.md | Project purpose, key commands, resource map | Every session | ~60 lines (minimal) |
| **Path-triggered** | `.claude/rules/` | Domain-specific conventions per file type | When working with matching files | Per-file, on demand |
| **On-demand** | Skills | Methodology for specific task types | When task matches skill description | ~2% context each |
| **Lookup** | MCP servers | Live access to databases, APIs, registries | When explicitly called | Per-query |
| **External memory** | File system | Reference docs, catalogs, prior decisions | When agent reads specific files | Per-read |
| **Deep dive** | Subagents | Specialized investigation in fresh context | When delegated | Zero main context cost |

This mirrors the pattern Manus discovered independently — file system as external memory — and it's why Claude Code's 4-tool design (read, write, edit, bash) works: the tools let the LLM *pull* context on demand instead of having it pushed into the window (Vercel's text-to-SQL experiment found this swap alone moved accuracy from 80% to 100% — see Sources). The two sections below — resource maps and typed knowledge — are the domain-heavy-specific patterns built on top of this stack; skills and CLAUDE.md are now covered by the official docs.

---

## The Resource Map Pattern

The core delta pattern for domain-heavy projects: instead of loading domain knowledge into CLAUDE.md or skills, maintain a **resource map** — a lightweight index that tells the LLM *where to look*, not *what the answer is*.

### What a Resource Map Contains

```markdown
## Project Resources

### Detection Rules
- **Location**: rules/ (organized by protocol)
- **Lookup**: grep rules/ for existing coverage before creating new rules
- **Conventions**: see .claude/rules/detection-rules.md (auto-loads when editing rule files)
- **Validation**: run `make validate-rules` before committing

### External Resources
- **Threat intel**: accessible via MCP (threat-intel-server)
- **Rule database**: query via MCP (rule-db-server) for coverage gaps
- **Team decisions**: docs/decisions/ (ADR format)
```

### Why Resource Maps Work

1. **Small footprint**: fits in CLAUDE.md's ~60-line budget or a referenced file
2. **Points, doesn't contain**: tells the LLM where to find knowledge, not what the knowledge is
3. **Enables pull, not push**: the LLM uses Read, Grep, or MCP to fetch only what it needs

### Where to Put the Resource Map

| Approach | When to Use |
|----------|------------|
| Inline in CLAUDE.md | Small projects, <10 resource categories |
| Referenced file (`@docs/resource-map.md`) | Resource map would otherwise bloat CLAUDE.md |

---

## Typed Knowledge as the Queryable Substrate (OKF)

A resource map points the LLM at *where* knowledge lives; typed frontmatter changes *how* it can be retrieved once it gets there. The external-memory layer in the progressive-disclosure stack (the "File system / Per-read" row) defaults to grep — fine for "find the string," weak for "find every decision that is still open." Give each knowledge file a `type:` in YAML frontmatter and the directory becomes a typed graph an agent or script can query by kind: every `Assumption`, every `MDR`, every `contradiction`. That's the difference between an external memory the agent re-reads and one it (or a cron) interrogates.

The vendor-neutral spec is Google Cloud's **Open Knowledge Format (OKF) v0.1** ([SPEC.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md), Apache-2.0; [announced 2026-06-12](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) — date/license verified against primary sources): a directory of markdown files whose one required frontmatter field is `type:`, everything else left to the producer. It formalizes the file-as-external-memory pattern above and adds the one field that makes the corpus queryable. Convergence status for this function (AI-PKM) is *emerging*, not converged, so under the repo's convergence rule this stays a documented pattern rather than a default — adopting it as infrastructure requires converged status or an explicit owner exception.

The pairing that matters: **OKF stores what we know; the RETHINK limb of the loop re-asks whether it's still the right thing to know.** Domain expertise rots — a coverage note, a validated approach, a control mapping all age — and a presence-based resource map can't tell you *which* target has gone stale. A typed graph can: the loop's RETHINK pass (the intent-alignment "why" dimension; see [harness-engineering.md](./harness-engineering.md)) filters by type to what's most likely to need re-validation instead of re-reading everything.

### Worked case study (Tier B, single practitioner — FLAGGED)

A firsthand implementation in a ~500-doc cross-repo security-research vault (project1, "Second Brain"). **Value seen recently; one practitioner, one project, not independently corroborated** — treat the mechanism as transferable, the magnitude as one data point.

- Canonical type registry: [`01-knowledge-base/_type-registry.md`](file:///home/jerem/project1/01-knowledge-base/_type-registry.md) holds 30 canonical types + 9 singletons + a merge map, and records two real consolidations (127 distinct types, 86 used once → ~30 on 2026-06-09; then a 51-value drift → canonical on 2026-06-18). [`AGENTS.md`](file:///home/jerem/project1/AGENTS.md) owns per-type field conventions; the registry owns the list.
- Pre-commit drift guard: [`quality_gates.py`](file:///home/jerem/project1/automation/orchestrator/quality_gates.py)'s `validate_okf_type` *parses* the registry (via [`okf.py`](file:///home/jerem/project1/automation/lib/okf.py)'s `load_canonical_types()`) rather than hard-coding the list, so the gate can never disagree with the human-readable registry.
- RETHINK operationalization: [`okf_signals.py`](file:///home/jerem/project1/automation/okf_signals.py) reads the typed graph and emits next-work from the types themselves — overdue `Assumption` reviews, undecided `Proposed` MDRs, unresolved `contradiction`s, weak `hypothesis` notes, thin-coverage components — with no separate backlog to keep in sync. The graph is the backlog. [`okf_health.py`](file:///home/jerem/project1/automation/okf_health.py) tracks coverage/drift and is federation-ready (`--federated` across the hub's spoke repos).

Transferable lesson: a resource map tells the agent where to look; a `type:` plus a parsed registry tells the *loop* what to re-examine, which is what lets RETHINK run on a cadence without re-loading the domain. Detailed in [archetype-A](./memory-systems-archetype-a-curated-kb.md) §A1b.

---

## Path-Scoped Rules for Domain Conventions

For ecosystems with distinct file types or directories, `.claude/rules/` with path frontmatter provides zero-cost context until the LLM actually touches matching files.

```markdown
<!-- .claude/rules/suricata-rules.md -->
---
paths:
  - "rules/**/*.rules"
  - "**/*.sid"
---

When working with Suricata rules:
- Check existing rules in rules/ before creating new ones
- Follow the SID allocation scheme in docs/sid-ranges.md
- Validate with `suricata -T -c suricata.yaml -S <rulefile>`
```

The same shape applies to any file-type-scoped convention — a Zeek rule keyed on `scripts/**/*.zeek`, a YARA rule keyed on `yara/**/*.yar` — each pointing at its own naming scheme and validation command. Rules load only when the LLM touches matching files: for a project with 6 domain areas, only the relevant rule loads, not all 6 — progressive disclosure applied to conventions.

---

## MCP for Live Domain Lookups

When domain knowledge lives in external systems, MCP servers provide live lookup without pre-loading.

### When to Use MCP vs File-Based

| Data Characteristic | Use MCP | Use File-Based |
|--------------------|---------|---------------|
| Changes frequently (daily/weekly) | Yes | No |
| Too large to maintain locally | Yes | No |
| Requires authentication/API access | Yes | No |
| Stable, manageable size | No | Yes (much faster) |
| Needs to work offline | No | Yes |

**Decision principle**: MCP for data that's dynamic or authoritative-at-source, file-based for stable reference material. MCP adds 300-800ms latency per call — fine for lookups, not for high-frequency access.

---

## Generalization: Applying to Any Complex Domain

The examples above use security engineering, but the findability patterns generalize:

| Domain | Resource Map Contents | Path-Scoped Rules | MCP |
|--------|----------------------|-------------------|-----|
| **Security (Suricata/Zeek/YARA)** | Rule directories, coverage matrix, threat intel | Per-rule-language conventions | Threat intel API, rule database |
| **Infrastructure (Terraform/K8s)** | Module registry, state locations, environment map | Per-provider conventions | Cloud provider APIs, state backends |
| **Compliance (SOX/HIPAA/PCI)** | Control catalog, evidence locations, audit schedule | Per-regulation requirements | Audit system API, evidence repository |

The pattern holds regardless of domain: a resource map tells the LLM where to look, path-scoped rules teach conventions when touching relevant files, and MCP provides live access to dynamic external data. Skills carry the task methodology on top — see the official skills docs for that layer.

---

## Sources

### Tier A (Primary Vendor / Expert Practitioner)

- Boris Cherny: context capacity threshold (~60%) — March 2026
- Anthropic: skills documentation (~2% context budget per skill); ["Effective harnesses for long-running agents"](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) (November 2025)

### Tier B (Validated / Production)

- Manus: file system as external memory pattern — context engineering lessons (2025-2026)
- Vercel: text-to-SQL experiment — general-purpose (pull) tools outperformed specialized (push) tools, 80% → 100% accuracy
- **OKF typed-substrate case study** (§Typed Knowledge as the Queryable Substrate) — single production vault (project1), firsthand: `_type-registry.md`, `okf.py`, `quality_gates.py:validate_okf_type`, `okf_health.py`, `okf_signals.py`. **One practitioner, one project, not independently corroborated.**

### Tier C (Vendor-Published Standard)

- [Google Cloud — Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) — Apache-2.0; [announced 2026-06-12](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing). Sole required frontmatter field is `type:`. Date/license/required-field verified against the primary spec + blog (2026-06-21).

### Related Analysis

- [Harness Engineering](./harness-engineering.md) — Umbrella concept, diagnostic framework, philosophy comparison
- [Behavioral Insights](./behavioral-insights.md) — Context thresholds, CLAUDE.md adherence, instruction processing
- [Plugins & Extensions](./plugins-and-extensions.md) — Extension mechanism selection (skills vs MCP vs hooks vs rules)
- [MCP vs Skills Economics](./mcp-vs-skills-economics.md) — Cost analysis for mechanism selection
- [Safety & Sandboxing](./safety-and-sandboxing.md) — Security constraints as domain knowledge

---

*Last updated: March 2026 (collapsed 2026-07-10)*

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/behavioral-insights.md`](analysis/behavioral-insights.md) [EXTRACTED (1.00)] — references
- [`analysis/mcp-vs-skills-economics.md`](analysis/mcp-vs-skills-economics.md) [EXTRACTED (1.00)] — references
- [`AUDIT-CONTEXT.md`](AUDIT-CONTEXT.md) [EXTRACTED (1.00)] — references
- [`INDEX.md`](INDEX.md) [EXTRACTED (1.00)] — references

<!-- graphify-footer:end -->
