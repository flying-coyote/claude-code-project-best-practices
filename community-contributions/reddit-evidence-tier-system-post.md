# Reddit Post Draft: Evidence Tier System for Claude Code Patterns

**Target**: r/ClaudeCode

**Type**: Discussion / Community Resource

**Flair**: Discussion or Resources

---

## Post Title

[Discussion] Evidence Tier System for Assessing Claude Code Pattern Quality

## Post Body

### TL;DR

I created a dual-tier system for assessing the quality of Claude Code patterns, tips, and recommendations. Looking for feedback and wondering if this would be useful to standardize across the community.

**GitHub**: https://github.com/flying-coyote/claude-code-project-best-practices/blob/master/patterns/evidence-tiers.md

---

### The Problem

When learning Claude Code, you encounter advice from many sources:
- Anthropic's official blog (authoritative but limited)
- Community GitHub repos (helpful but varying quality)
- Reddit posts and Discord tips (practical but unverified)
- Random blog posts (hit or miss)

**How do you know what to trust?**

I kept asking: "Is this claim validated? Should I bet my production workflow on it?"

---

### The Solution: Dual-Tier Evidence System

I developed a two-layer assessment framework:

#### Layer 1: Document Evidence Tiers (A-D)

| Tier | Source | Trustworthiness |
|------|--------|-----------------|
| **A** | Anthropic official (blog, docs) | Authoritative |
| **B** | Production-validated (real projects) | Tested |
| **C** | Community consensus (obra, shanraisshan) | Validated |
| **D** | Unverified (single claims, theories) | Experimental |

#### Layer 2: Measurement Claims (with expiry dates)

For specific claims like "Tool Search reduces tokens by 85%":
- **Source**: Anthropic Engineering Blog
- **Date**: 2025-11-24
- **Revalidate**: 2026-11-24

Why expiry dates? Because:
- Claude Code evolves (what's true today may change)
- Better to revalidate than assume
- Explicit about when claims need verification

---

### Real Examples

**High-confidence pattern** (Tier A + measurement):
```yaml
Pattern: Advanced Tool Use
Evidence Tier: A (Anthropic blog)
Claim: "Tool Search: 85% token reduction (77K → 8.7K)"
Source: Anthropic Engineering Blog (2025-11-24)
Revalidate: 2026-11-24
Status: PRODUCTION
```

**Emerging pattern** (Tier B + community validation):
```yaml
Pattern: MCP Daily Essentials
Evidence Tier: B (Community + production measurement)
Claim: "Context7 + Sequential Thinking: 25K tokens (12.5% budget)"
Source: valgard analysis (2026-01)
Status: EMERGING (90-day validation period)
Revalidate: 2027-01-01
```

---

### Maturity Status Workflow

Patterns progress through maturity stages:

1. **EMERGING** (90-day validation period)
   - Community consensus exists
   - Requires independent validation
   - Use cautiously in production

2. **PRODUCTION** (promotion criteria met)
   - 3+ independent validations
   - Measurements stable across Claude Code versions
   - No significant negative reports

3. **DEPRECATED** (tracked with grace periods)
   - Better alternatives exist
   - Breaking changes occurred
   - Migration path documented

---

### Why This Matters

**For users**:
- Quickly assess if advice is trustworthy
- Understand risk when adopting patterns
- Know when to revalidate claims

**For contributors**:
- Clear standard for documentation quality
- Framework for tracking pattern maturity
- Systematic deprecation tracking

**For the community**:
- Raise documentation quality bar
- Reduce "works on my machine" syndrome
- Track evolution of best practices

---

### Examples in Production

I've applied this to 36+ patterns in my repo:
- 18 patterns at PRODUCTION status (Tier A/B, validated)
- 15 patterns at EMERGING status (90-day validation)
- 3 patterns DEPRECATED (with migration paths)

Real impact: Caught "Claude in Chrome" deprecation early, documented migration to Playwright (4x token efficiency improvement).

---

### Questions for Community

1. **Would standardizing evidence tiers help you?**
   - When evaluating tools/patterns/MCPs?
   - When deciding what to adopt in production?

2. **What would you change?**
   - Too complex? Too simple?
   - Different tier labels?
   - Other criteria?

3. **Should this be community-wide?**
   - Tag patterns in shanraisshan's repo?
   - Label Reddit posts/comments?
   - Discord resource channel?

4. **What about measurement claims?**
   - Too much overhead to track expiry dates?
   - Valuable for knowing when to revalidate?

---

### Resources

- **Full framework**: [evidence-tiers.md](https://github.com/flying-coyote/claude-code-project-best-practices/blob/master/patterns/evidence-tiers.md)
- **Example patterns**: See any `.md` in [patterns/](https://github.com/flying-coyote/claude-code-project-best-practices/tree/master/patterns)
- **Deprecation tracking**: [DEPRECATIONS.md](https://github.com/flying-coyote/claude-code-project-best-practices/blob/master/DEPRECATIONS.md)

---

### Open Question

Should we create a "Claude Code Evidence Standard" that the community can adopt? Or is this overkill?

I'm open to feedback—this is a framework I built for myself that seems useful, but happy to hear it's overcomplicated if that's the case!

---

## Posting Strategy

### Before Posting
- [ ] Check r/ClaudeCode rules (character limits, link policies)
- [ ] Verify all GitHub links are accessible
- [ ] Read recent posts to match community tone
- [ ] Prepare to engage with comments promptly

### Engagement Plan
If reception is positive:
1. Answer questions about implementation
2. Offer to collaborate on standardization
3. Share templates/tools
4. Connect with mods about potential wiki entry

If reception is negative:
1. Listen to concerns
2. Understand what feels like overkill
3. Simplify based on feedback
4. Pivot to "just sharing what works for me"

### Success Metrics
- Upvotes > 20: Community finds it useful
- 10+ comments: Generates discussion
- Other repos adopt: Real validation
- Requests for tools/templates: Actionable interest

---

## Alternative: Shorter Version

If full post feels too long:

---

**Title**: Quick tip: I use an "evidence tier" system to assess Claude Code advice quality

**Body**:

When I see Claude Code tips/patterns/tools, I categorize them:

- **Tier A**: Anthropic official (blog, docs) - Trust fully
- **Tier B**: Production-validated (tested in real projects) - Trust with caution
- **Tier C**: Community consensus (obra, shanraisshan, Reddit) - Experimental
- **Tier D**: Unverified (single claims) - Verify before using

For specific claims ("Tool X reduces tokens by Y%"), I track:
- Source + date
- Revalidation date (because Claude Code evolves)

This helped me catch "Claude in Chrome" deprecation early and migrate to Playwright (4x token efficiency).

Full framework: [GitHub link]

Anyone else do something similar? Overkill or useful?

---

## Tone Notes

- Curious, not authoritative ("I created" not "You should use")
- Seeking feedback, not promoting
- Credit community projects prominently
- Open to criticism ("is this overkill?")
- Share benefits without overselling
