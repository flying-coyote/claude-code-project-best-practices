---
evidence-tier: B
applies-to-signals: [contributing-new-analysis]
last-verified: 2026-04-22
revalidate-by: 2026-10-22
status: PRODUCTION
---

# Canonical Doc Template (Template)

**Evidence Tier**: B (self-referential methodology doc — captures the implicit template surfaced by a 2026-04-22 corpus audit, validated against 28 existing analysis docs)

## Purpose

This is the canonical structure for new analysis documents in `analysis/`. Copy this file, rename, and fill in. The template captures patterns already dominant in the corpus — not a new standard invented here.

Docs that exemplify each section well: [`behavioral-insights.md`](behavioral-insights.md) (diagnostic tables), [`model-migration-anti-patterns.md`](model-migration-anti-patterns.md) (counter-evidence + MUST-vs-positive tension), [`session-quality-tools.md`](session-quality-tools.md) (Gap statements).

---

## Required Frontmatter Schema

Every analysis doc must have a YAML frontmatter block with these fields:

```yaml
---
evidence-tier: A | B | C | Mixed
applies-to-signals: [list matching AUDIT-CONTEXT.md signal vocabulary]
last-verified: YYYY-MM-DD
revalidate-by: YYYY-MM-DD
status: PRODUCTION | EMERGING | ARCHIVED
measurement-claims:      # OPTIONAL — only if doc makes dated quantitative claims
  - claim: "..."
    source: "..."
    date: YYYY-MM-DD
    revalidate: YYYY-MM-DD
---
```

**Field reference**:

| Field | Purpose | Valid values |
|---|---|---|
| `evidence-tier` | Aggregate source quality of the doc's claims. Machine-readable. | `A` (Anthropic/primary observation), `B` (expert practitioner), `C` (community), `Mixed` |
| `applies-to-signals` | Which audit signals should route an agent to this doc. Must use vocabulary from `AUDIT-CONTEXT.md`. | e.g., `[claude-md-progressive-disclosure, model-version-4-7]` |
| `last-verified` | When the doc's core claims were last reviewed for current accuracy. | `YYYY-MM-DD` |
| `revalidate-by` | Expiry date after which claims need re-testing. Typically `last-verified + 6 months`. | `YYYY-MM-DD` |
| `status` | Lifecycle state. | `PRODUCTION` (validated, active), `EMERGING` (not yet validated), `ARCHIVED` (superseded, kept for history) |
| `measurement-claims` | Dated quantitative claims with their own revalidation cycles. Only include if doc makes such claims. | Array of objects |

**Rationale for split**: 19 of 28 existing docs include `measurement-claims` (production claims needing revalidation); 9 omit it (foundational methodology docs whose claims don't age the same way). The split is intentional — don't force `measurement-claims` onto methodology docs.

---

## Canonical Section Order

```markdown
# Doc Title

**Evidence Tier**: {tier} — {one-line justification}

## Purpose

{1-3 sentences stating what the doc answers and for whom.}

## {Core Problem / Context Section}

{Why this matters. Problem statement. Background needed to understand the rest.}

## {Diagnostic Framework / Comparison Matrix / Anti-Patterns}

{The analytical core. Prefer tables, decision trees, or explicit anti-pattern lists over prose.
Every claim carries an inline citation: (Tier X — source name).}

## Counter-Evidence / What This Does *Not* Mean

{Where the thesis breaks. Known exceptions. Alternative framings.
Axiom-framed docs without this section read as advocacy, not analysis.}

## Gaps

{Explicit statements of what would raise confidence. Format:
- **Gap: {topic}**. {Description}. **Needs**: {specific data or validation that would close the gap}.}

## Related Analysis

- [doc-name.md](doc-name.md) — one-line why it's related

## Sources

### Tier A (Primary / Vendor)
- ...

### Tier B (Validated / Expert Practitioner)
- ...

### Tier C (Community)
- ...

---

*Last updated: YYYY-MM-DD*
```

**Not every section is required in every doc**, but deviations should be deliberate:

- Pure methodology docs (e.g., `evidence-tiers.md`) may skip Counter-Evidence if the framework has no counter-position.
- Short diagnostic docs (e.g., `model-migration-anti-patterns.md` at ~180 lines) may merge Gaps into Sources.
- Case-study docs may add a "Case Study" section between Purpose and Diagnostic Framework.

---

## Citation Format Standard

Inline citations at the point of claim:

> Opus 4.7 interprets instructions literally (Tier A — Anthropic migration guide).

Not:

> Opus 4.7 interprets instructions literally. See sources.

Full source entries go in the Sources section with URL, date, and authority context. The inline form is for reader scanability; the Sources section is for verification.

**Acceptable variants**:

- `(Tier A — Anthropic migration guide)`
- `(Tier B — Vallentin, Tenzir, production data)`
- `(Tier Mixed A-B — 7-repo portfolio + Boris Cherny)`

**Not acceptable**:

- Unsourced claim followed only by a paragraph-end "see below"
- Citation without tier label
- Tier label without source attribution

Outlier docs getting retrofitted: `tool-ecosystem.md`, `mcp-daily-essentials.md`, `framework-selection-guide.md`.

---

## Gap Statement Standard

Used when a claim relies on an unvalidated threshold, arbitrary constant, or unmeasured correlation. Format:

> - **Gap: severity-weight calibration.** The 5/3/1 multipliers have no reported derivation. **Needs**: published study correlating score bands to independent outcome measures.

Template:

> - **Gap: {what's unvalidated}.** {Why this matters}. **Needs**: {specific study, data, or validation that would close it}.

**Adopt selectively.** Every doc that cites confidence scores or arbitrary thresholds should have a Gaps section. Foundational methodology docs and purely diagnostic matrices may not need one. Current exemplars: [`session-quality-tools.md`](session-quality-tools.md).

---

## Counter-Evidence Standard

Required for any doc presenting a thesis, set of principles, or opinionated framework. Not required for pure reference tables or cross-version matrices (they're already comparative).

The pattern comes from [`model-migration-anti-patterns.md`](model-migration-anti-patterns.md) — "What Literalism Does *Not* Mean":

> Literalism is **selective, not uniform**. Simon Willison's analysis of the leaked 4.7 system prompt surfaces a counter-signal...

Structure:

```markdown
## Counter-Evidence / What This Does Not Mean

{Lead sentence acknowledging a specific limit to the thesis.}

{Quote or cite the source of the counter-position, with tier.}

**Implication**: {How this changes the practical reading of the main thesis.}
```

---

## Integration Checklist (for new docs)

When adding a new analysis doc, update these files:

1. `analysis/{new-topic}.md` — created using this template
2. `SOURCES.md` — full source entries with tier attribution
3. `SOURCES-QUICK-REFERENCE.md` — only if cited source is Authority 3 or higher
4. `AUDIT-CONTEXT.md` — **mandatory** — add a signal → fetch row; otherwise the doc is unreachable by the audit prompt
5. `README.md` — add to "Core Analysis" table
6. `INDEX.md` — auto-regenerated; run the regenerator if configured
7. `PLAN.md` — add to "Recent Activity" (if you have maintainer access)

Full rationale and step-by-step guidance in [`CONTRIBUTING.md`](../CONTRIBUTING.md).

---

## Related Analysis

- [`evidence-tiers.md`](evidence-tiers.md) — Tier A/B/C definitions this template references
- [`confidence-scoring.md`](confidence-scoring.md) — HIGH/MEDIUM/LOW assessment that maps to Gap-statement usage
- [`model-migration-anti-patterns.md`](model-migration-anti-patterns.md) — counter-evidence exemplar
- [`session-quality-tools.md`](session-quality-tools.md) — Gap-statement exemplar
- [`behavioral-insights.md`](behavioral-insights.md) — diagnostic-framework exemplar

---

## Sources

### Tier A (Primary)

- Self-derived from corpus audit (2026-04-22) across 28 existing analysis docs; no external source.

### Tier B (Validated Methodology)

- [`evidence-tiers.md`](evidence-tiers.md) — tier schema
- [`confidence-scoring.md`](confidence-scoring.md) — gap/confidence schema

---

*Last updated: 2026-04-22*
