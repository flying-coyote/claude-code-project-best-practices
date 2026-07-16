# Claude Code Best Practices — Analytical Layer

A portable, evidence-based audit you can run against any Claude Code project to get recommendations specific to *that project*. Every claim carries an evidence tier (A/B/C); the one-prompt audit routes observed project signals to the 4–8 of 24 routable analysis docs that apply. This is the evidence-graded-audit lane in a seven-lane ecosystem (README § Where This Sits): first-party docs carry the baseline, ECC the tooling, superpowers the methodology, ClaudeLog the mechanics, standards bodies the specs, thought-leader canons the commentary — this repo carries the measurements and instruments, and prunes itself into the other lanes as they mature (per-doc ledger: ABSORPTION-MAP.md).

## Commands
- `npm run lint` - Lint all markdown files
- `npm run lint:fix` - Auto-fix markdown issues
- No build/test commands - documentation-only project

## Git Workflow
Commit prefixes:
- 📊 Analysis and evaluation
- 📚 Documentation updates
- 🔧 Configuration and infrastructure

## Project Structure
- `analysis/` - 25 files: 24 routable evidence-based analysis docs + the canonical template (the core content)
- `archive/` - Prior v1 patterns, skills, templates (preserved for reference)
- `SOURCES.md` - Comprehensive source database with evidence tiers

## Adding New Analysis
1. Identify authoritative source (Tier A or B required per SOURCES.md)
2. Document in analysis/ with source attribution and evidence tier
3. Update SOURCES.md with new reference
4. Wire into routing — add a row to `AUDIT-CONTEXT.md` and matching `applies-to-signals` frontmatter, or the audit cannot reach the doc (the Dapr doc was missed here once)
5. Focus on evaluation and comparison, not implementation how-to

## Resource Map
- Analysis documents: `analysis/` (24 routable evidence-based evaluations)
- Absorption ledger: `ABSORPTION-MAP.md` (per-doc external absorbers, lanes, deltas, triggers — derived; frontmatter is canonical)
- Source database: `SOURCES.md` + `SOURCES-QUICK-REFERENCE.md`
- Architecture decisions: `DECISIONS.md`
- v1 archive: `archive/` (patterns, skills, templates — reference only)

## Known Gotchas
- Settings schema uses `permissions.allow`, not `allowedTools`
- Always update cross-references when adding new analysis
- PLAN.md stays in git as canonical plan

## Current Focus
v2.1 — 24 routable analysis docs (44→27 in the 2026-07 reduction, Decision 11; 27→25 files in the 2026-07-16 absorption wave — the first THIRD-PARTY sweep: absorption instrument built (ABSORPTION-MAP.md + `follows:` lane), five docs follow external canons, mcp-vs-skills-economics RETIRING toward `/usage`, framework-selection merged into orchestration-comparison, confidence-scoring merged into evidence-tiers; see drafts/ABSORPTION-SCAN-2026-07.md + DECISIONS.md Decision 12). Production evidence from 7-repo portfolio + memory-system archetype recommendations with empirical Pass-2 testbed evidence. Project intent: a temporary analytical layer designed to prune itself as robust community/vendor replacements mature (applied 2026-06-04: session-quality-tools → first-party `/insights`; at scale 2026-07-10 vs first-party; third-party 2026-07-16).

Note: This project uses emoji prefixes (documentation project). Code repos in the portfolio use conventional commits (`feat:`, `fix:`, `docs:`).

Portfolio-review program (2026-07): see `.claude/review-protocol.md` before any review-program session.
