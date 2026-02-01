---
name: Content Reviewer
description: Apply comprehensive quality review when user prepares content for publication (blog posts, articles, documentation, presentations). Trigger when user mentions "publish", "post", "article", "review this", "draft complete", "ready to share". Enforce evidence-based claims, intellectual honesty, professional voice, and balanced perspective.
allowed-tools: Read, Grep, Glob
---

# Content Reviewer

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
