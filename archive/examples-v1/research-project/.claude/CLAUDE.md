# AI Impact Research (Example)

> **ARCHIVED — but nothing live replaces it.** Archived in the v2.0 repositioning (March 2026, DECISIONS.md § Reposition as Analytical Layer) or a later reduction. No live successor covers this file. `analysis/evidence-tiers.md` carries the A-D tier vocabulary (with A/B defined inversely to this file) and a hypothesis documentation block, but the HYP-NNN file-naming convention, the `rationale` field, the sources/-to-BIBLIOGRAPHY.md consistency rule, the `contradictions/` directory convention, the DOI-or-permanent-URL requirement for Tier A sources, and the expert-quote date/context/consent-flag rule appear nowhere in `analysis/` — `grep -rn 'HYP-\|BIBLIOGRAPHY\|DOI' analysis/` returns zero hits. The correlation/causation integrity violation is likewise absent from both named successors. `analysis/claude-md-progressive-disclosure.md` measures CLAUDE.md line counts and offers only a generic Tier 1 skeleton; no live doc provides a worked research-project example CLAUDE.md. Retained for reference as an uncovered gap. This is a **coverage gap, not a currency gap** — the material is unreplaced, not merely out of date, so a reader who discards it is left with nothing. Its specifics are v1-era; its subject is still uncovered. (Marked 2026-08-28; successor determined by mapping plus adversarial verification, which overturned 35 of 39 successor claims — see `analysis/prose-corpus-discoverability.md`.)

## Purpose
Systematic literature review: AI coding tools' impact on productivity/quality.

## Commands
- See hypotheses/README.md for tracking format
- `git log --oneline` to review research timeline
- BIBLIOGRAPHY.md tracks all sources with evidence tiers

## Evidence Tiers (Required for All Claims)
- **Tier A**: Peer-reviewed studies, official reports (strong claims only)
- **Tier B**: Expert analysis, production data (supporting evidence)
- **Tier C**: Vendor docs, surveys (note limitations)
- **Tier D**: Anecdotal, personal (mark as speculation)

## Hypothesis Tracking Format
Each hypothesis file must include:
- Statement, rationale, confidence level (HIGH/MEDIUM/LOW)
- Supporting evidence (with tiers), contradicting evidence
- This format was violated 5 times → standardize

## Known Gotchas
- Sources in sources/ must match BIBLIOGRAPHY.md entries (broke 3 citations)
- Hypothesis files named HYP-NNN-description.md (not arbitrary names)
- Contradictions directory tracks unresolved conflicts (don't hide them)
- All Tier A sources require DOI or permanent URL (2 papers became inaccessible)
- Expert quotes require date, context, and consent flag

## Research Integrity Violations to Avoid
- Repeatedly mixed correlation/causation (6 instances in draft)
- Used "definitely" instead of "may indicate" (4 corrections needed)
- Omitted contradicting evidence (caught in peer review twice)

## Current Focus
Synthesizing 23 sources on productivity metrics (target: hypothesis validation by March 1)
