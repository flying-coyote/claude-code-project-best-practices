# Best Practices Project

## Commands
- `npm run lint` - Lint all markdown files
- `npm run lint:fix` - Auto-fix markdown issues
- No build/test commands - documentation-only project

## Git Workflow
Commit prefixes:
- 📚 Documentation and patterns
- 🔧 Configuration and infrastructure
- ✅ Validation and testing
- 📊 Research and analysis

## Adding New Patterns
1. Identify authoritative source (Tier A or B required per SOURCES.md)
2. Document in patterns/ with source attribution
3. Update SOURCES.md with new reference
4. Update related patterns' "Related Patterns" sections
5. Run dogfooding audit if documenting something we should implement ourselves

## Known Gotchas
- Check `DOGFOODING-GAPS.md` before adding patterns we should implement
- Settings schema uses `permissions.allow`, not `allowedTools`
- Always update cross-references when adding new patterns
- Run self-compliance audit after documenting new patterns
- Completed work records: Use git history (commits), not active files
- Archive only reference docs (decision records, summaries) not completed work
- PLAN.md stays in git as canonical plan; move completed items to ARCHIVE.md monthly

## Current Focus
Post-v1.0 maintenance. Aligning with SDD methodology (see patterns/spec-driven-development.md)

## Recent Learnings (2026-03-06)

### Removed Tier Language from Infrastructure
**Old**: Tier 1/2/3/4 system with numbered progression
**New**: Single recommended setup (CLAUDE.md + hooks + permissions) + optional advanced features (GitHub Actions, Version Tracking)
**Reason**: Tier numbers created false hierarchy and decision paralysis. 95% of projects need the same setup (what was Tier 2).
**Impact**: Simpler mental model, reduced decision fatigue, clearer that one path works for most projects
**Files changed**: README.md, patterns/project-infrastructure.md, QUICKSTART.md, prompts/MAKE-PROJECT-RECOMMENDATIONS.md, cross-references
**Note**: Evidence tiers (A-D), confidence scoring (1-5), and skill tiers (1-3) still use tier language - only infrastructure tiers removed
