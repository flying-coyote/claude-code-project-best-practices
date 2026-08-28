# TypeScript Library (Example)

> **ARCHIVED — but nothing live replaces it.** Archived in the v2.0 repositioning (March 2026, DECISIONS.md § Reposition as Analytical Layer) or a later reduction. **No successor — coverage gap.** This file was marked as superseded by `analysis/claude-md-progressive-disclosure.md`; it is not. That doc measures CLAUDE.md sizes across six repos and never exhibits a CLAUDE.md: it contains zero occurrences of "Current Focus", and "gotchas" appears only twice, as a bare section-name mention in a list and as a word in an ordering rule. Its Tier 1 skeleton (Project Name / Commands / Key Files / Git Workflow) shares one section of four with this file's (Purpose / Commands / Known Gotchas / Current Focus), and its smallest measured tier starts at 42 lines, so it has no bin for this 19-line minimal example. The distinctive material here — a complete copyable minimal CLAUDE.md, and gotchas written from bugs that actually occurred rather than generic advice — survives nowhere else in the repo. Retained until a real successor exists. This is a **coverage gap, not a currency gap** — the material is unreplaced, not merely out of date, so a reader who discards it is left with nothing. Its specifics are v1-era; its subject is still uncovered. (Marked 2026-08-28; successor determined by mapping plus adversarial verification, which overturned 35 of 39 successor claims — see `analysis/prose-corpus-discoverability.md`.)

## Purpose
Utility library for string manipulation, date formatting, and validation.

## Commands
- `npm test` - Run Jest tests (must pass before commits)
- `npm run test:coverage` - Check coverage (target 90%+)
- `npm run build` - TypeScript compilation to dist/
- `npm run lint` - ESLint (auto-fixes on save via hook)

## Known Gotchas
- Import paths must use .js extension (TypeScript module resolution)
- Test files must match *.test.ts pattern (not *.spec.ts)
- dist/ directory is gitignored but required for publishing
- Date utils use UTC by default (caused 3 timezone bugs in development)

## Current Focus
Adding validation helpers for v1.0 release
