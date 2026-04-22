# Claude Code Best Practices — Analytical Layer

Evidence-based analysis of Claude Code patterns, not implementation guides. We evaluate claims, compare approaches, and surface quantified behavioral insights.

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
- `analysis/` - 28 evidence-based analysis documents (the core content)
- `archive/` - Prior v1 patterns, skills, templates (preserved for reference)
- `SOURCES.md` - Comprehensive source database with evidence tiers

## Adding New Analysis
1. Identify authoritative source (Tier A or B required per SOURCES.md)
2. Document in analysis/ with source attribution and evidence tier
3. Update SOURCES.md with new reference
4. Focus on evaluation and comparison, not implementation how-to

## Known Gotchas
- Settings schema uses `permissions.allow`, not `allowedTools`
- Always update cross-references when adding new analysis
- PLAN.md stays in git as canonical plan

## Current Focus
v2.1 — 28 analysis documents with production evidence from 7-repo portfolio, complementing ECC (tooling) and superpowers (methodology)

Note: This project uses emoji prefixes (documentation project). Code repos in the portfolio use conventional commits (`feat:`, `fix:`, `docs:`).
