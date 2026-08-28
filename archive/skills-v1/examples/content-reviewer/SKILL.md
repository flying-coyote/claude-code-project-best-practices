---
name: content-reviewer
description: Apply comprehensive quality review when user prepares content for publication (blog posts, articles, documentation, presentations). Trigger when user mentions "publish", "post", "article", "review this", "draft complete", "ready to share". Enforce evidence-based claims, intellectual honesty, professional voice, and balanced perspective.
allowed-tools: Read, Grep, Glob
---

# Content Reviewer

> **ARCHIVED — but nothing live replaces it.** Archived in the v2.0 repositioning (March 2026, DECISIONS.md § Reposition as Analytical Layer) or a later reduction. No live successor covers this file. `analysis/evidence-tiers.md` absorbs only the evidence dimension and re-expresses the confidence-language gradient on the Tier A-D / HIGH-MEDIUM-LOW axis (the archived Tier 1-5 table is superseded by owner ruling B-F7, 2026-07-12); it does not carry the four-dimension publication gate itself. The Voice and Balance dimensions have no home anywhere in `analysis/` — "active voice", "marketing hype", "professional voice", "intellectual honesty" and "balanced perspective" all return zero hits — and the trigger conditions, ❌/✅ hype-to-measurement rewrites, PASS/NEEDS WORK/FAIL output format and Don't list are unreplaced. The `publication-quality-checker` named in evidence-tiers.md § Integration with Skills does not exist as a skill file, so that section documents the gap rather than filling it. Retain this file as the reference for the editorial review gate until a real successor is written. This is a **coverage gap, not a currency gap** — the material is unreplaced, not merely out of date, so a reader who discards it is left with nothing. Its specifics are v1-era; its subject is still uncovered. (Marked 2026-08-28; successor determined by mapping plus adversarial verification, which overturned 35 of 39 successor claims — see `analysis/prose-corpus-discoverability.md`.)

Review content for publication readiness: evidence quality, intellectual honesty, professional voice, balanced perspective.

## Trigger Conditions

**Activate**: "ready to publish", "draft complete", "review this", "final review", quality check before sharing

**Skip**: Early brainstorming, internal notes, "skip review", code comments, research phase

## Review Dimensions

| Dimension | Pass Criteria |
|-----------|--------------|
| **Evidence** | Claims have sources, tier matches claim strength |
| **Honesty** | Uncertainty acknowledged, limitations stated |
| **Voice** | Active voice, specific, no marketing hype |
| **Balance** | Trade-offs discussed, context provided |

## Confidence Language

| Evidence Tier | Use |
|---------------|-----|
| Tier 1-2 | "demonstrates", "confirms", "production data shows" |
| Tier 3 | "suggests", "experts recommend" |
| Tier 4 | "vendor claims" (mark unvalidated) |
| Tier 5 | "I hypothesize", "speculation" |

## Common Fixes

```
❌ "This definitely solves the problem."
✅ "This approach solved the problem in our testing."

❌ "Revolutionary new technology transforms operations."
✅ "This technology reduced processing time from hours to minutes."

❌ "X is the best solution."
✅ "X addresses these challenges effectively, though alternatives exist."
```

## Output Format

```markdown
# Content Review

## Evidence Quality: [PASS/NEEDS WORK/FAIL]
- [Issue]: [Fix]

## Intellectual Honesty: [PASS/NEEDS WORK/FAIL]
- [Issue]: [Fix]

## Professional Voice: [PASS/NEEDS WORK/FAIL]
- [Issue]: [Fix]

## Balanced Perspective: [PASS/NEEDS WORK/FAIL]
- [Issue]: [Fix]

## Overall: [READY/REVISE/MAJOR REVISION]
Priority fixes:
1. [Fix]
```

## Don't

- Approve content with unsubstantiated claims
- Allow "best practice" without specifics
- Pass marketing language as professional
- Accept Tier 4-5 evidence for strong claims
- Approve content hiding uncertainty
