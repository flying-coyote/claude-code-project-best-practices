# Best Practices Project

Curated patterns and templates for Claude Code projects — reference implementation that practices what it preaches.

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
