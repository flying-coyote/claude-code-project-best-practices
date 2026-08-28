# Technical Blog (Example)

> **ARCHIVED — but nothing live replaces it.** Archived in the v2.0 repositioning (March 2026, DECISIONS.md § Reposition as Analytical Layer) or a later reduction. No live successor covers this file. evidence-tiers.md carries only its A/B/C/D claim-grading block; claude-md-progressive-disclosure.md does not reach it at all, since its measured band starts at 42 lines (this file is 28) and its six-repo dataset contains no content/writing project. The voice rules stated as a repeat-violation list, the markdown-project gotchas (assets in images/, case-sensitive links, drafts/ excluded from lint), and the file's role as a worked example CLAUDE.md for a non-code writing project have no counterpart anywhere in analysis/. Retained in archive/ as the only record of these. This is a **coverage gap, not a currency gap** — the material is unreplaced, not merely out of date, so a reader who discards it is left with nothing. Its specifics are v1-era; its subject is still uncovered. (Marked 2026-08-28; successor determined by mapping plus adversarial verification, which overturned 35 of 39 successor claims — see `analysis/prose-corpus-discoverability.md`.)

## Purpose
Blog on software architecture and system design. Target: senior developers/tech leads.

## Commands
- `npm run lint` - Check markdown formatting
- `git log --oneline` - Review recent posts
- See publication checklist in docs/PUBLISHING.md before finalizing

## Voice Rules (Repeatedly Violated)
- Use first person "I" for personal experience, "you" for guidance
- Specific tools with versions ("PostgreSQL 15") not generic ("database")
- Acknowledge tradeoffs - no silver bullets

## Evidence Tiers (Required)
- **Strong claims** require Tier A/B (official docs, production data, benchmarks)
- **Tier C** (industry blogs) must be labeled as such
- **Opinions** clearly marked as Tier D

## Known Gotchas
- Images must be in images/ subdirectory, not root (broke 4 posts)
- Markdown links are case-sensitive (GitHub != local filesystem)
- Draft files in drafts/ won't be linted (caused 2 publishing errors)
- Internal links use relative paths from published/ directory

## Current Focus
Drafting "Context Engineering in Practice" post (target: March 15)
