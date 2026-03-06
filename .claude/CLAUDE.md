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

## Current Focus
Post-v1.0 maintenance. Aligning with SDD methodology (see patterns/spec-driven-development.md)

## Recent Learnings (2026-03-06)

### Rename: SETUP-PROJECT.md → MAKE-PROJECT-RECOMMENDATIONS.md
**Reason**: Better reflects the file's purpose (analyze + recommend, not just setup)
**Update**: All references changed, old name deprecated

### Tier Language Change
**Old**: Tier 1 "Baseline" / Tier 2 "Active"
**New**: Tier 1 "Minimal (optional)" / Tier 2 "Active (Recommended Baseline)"
**Reason**: Users thought Tier 1 was the standard, missing CLAUDE.md benefits
