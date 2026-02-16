# Technical Blog (Example)

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
