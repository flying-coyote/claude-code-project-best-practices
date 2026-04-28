---
name: emerging-pattern-monitor
version: 2.0.0
description: Monitors EMERGING analysis topics and evaluates for PRODUCTION promotion
triggers:
  - "review emerging patterns"
  - "check pattern promotion"
  - "evaluate emerging"
  - "promote pattern"
auto_load: false
---

# Emerging Pattern Monitor Skill

**Purpose**: Monitor EMERGING patterns in analysis documents, track promotion criteria, and recommend when patterns are ready for PRODUCTION status.

**When to Use**:
- Weekly automated checks (recommended)
- Before quarterly audits
- When Anthropic blog post validates approach
- When production case study published
- User says "review emerging patterns" or similar

**What This Skill Does**:
1. Identifies analysis topics marked as EMERGING in analysis/ docs and SOURCES.md
2. Evaluates against promotion criteria
3. Tracks evidence accumulation over time
4. Recommends promotion when criteria met
5. Creates promotion proposals

---

## Promotion Criteria

To promote from EMERGING to PRODUCTION, a pattern must achieve **all three**:

### 1. Tier A Source Validation

**Requirement**: Approach validated by authoritative source

**Acceptable sources**:
- Anthropic engineering blog post
- Anthropic official documentation endorsement
- Peer-reviewed research (published in ACM, USENIX, IEEE)
- OWASP or NIST standard

**Verification**:
- Check SOURCES.md for Tier A attribution
- Verify URL is from anthropic.com/engineering or code.claude.com/docs
- Confirm publication date (within 2 years for relevance)

### 2. Production Validation

**Requirement**: Pattern used successfully in production

**Acceptable evidence**:
- **2+ independent case studies** from different organizations, OR
- **1 Tier A case study** (Anthropic, Fortune 500, named enterprise)

**Case study quality criteria**:
- Named organization or practitioner
- Quantified outcomes (measurements, time savings, etc.)
- Duration: 30+ days production use
- Publicly verifiable (blog post, conference talk, etc.)

**Verification**:
- Search SOURCES.md for case study citations
- Check evidence tier (B or higher)
- Verify measurements are specific and dated

### 3. Community Maturity

**Requirement**: Pattern or framework shows stability

**For frameworks/tools**:
- Version 1.0+ released
- Active maintenance (commits/releases within 3 months)
- 100+ GitHub stars OR 10+ contributors
- Documentation exists (README with examples)

**For methodology patterns** (non-code):
- Referenced by 2+ independent sources
- Stable definition (not rapidly changing)
- Clear usage examples in SOURCES.md

---

## Workflow

### Phase 1: Identify EMERGING Topics

**Search strategy**:
1. Grep analysis/ docs for `EMERGING` status markers
2. Review SOURCES.md for "EMERGING PATTERN" markers
3. Check analysis docs with confidence scores below production threshold

**Expected output**:
```
EMERGING Topics Found:
1. Reinforcement Learning from Memory (RLM)
   - File: SOURCES.md:430-454
   - Status: EMERGING since 2025-10-15

2. Claude-Flow multi-agent framework
   - File: analysis/framework-selection-guide.md
   - Status: EMERGING since 2025-11-20
```

### Phase 2: Evaluate Each Topic

**For each EMERGING topic, create evaluation scorecard**:

```markdown
## Topic: [Name]

**Status**: EMERGING
**First Mentioned**: [date]

### Promotion Criteria Evaluation

#### 1. Tier A Source Validation
- Status: [ACHIEVED / IN PROGRESS / NOT MET]
- Source: [name]
- Evidence Tier: [A/B/C]

#### 2. Production Validation
- Status: [ACHIEVED / IN PROGRESS / NOT MET]
- Case studies: [count] of 2 required

#### 3. Community Maturity
- Status: [ACHIEVED / IN PROGRESS / NOT MET]
- Framework version: [version]

### Overall Assessment
**Promotion Ready?**: [YES/NO] ([count] of 3 criteria met)
**Recommendation**: [Promote / Keep as EMERGING / Downgrade]
```

### Phase 3: Take Action

**If promotion ready (all 3 criteria met)**:
1. Update analysis document status to PRODUCTION
2. Remove EMERGING markers from documentation
3. Update cross-references in related analysis docs
4. Document promotion in DECISIONS.md

**If blockers exist**:
1. Document blockers clearly
2. Set next review date (1-3 months)
3. Monitor for triggering events

---

## Related Analysis

- [Evidence Tiers](../../analysis/evidence-tiers.md) - Tier A source criteria
- [Pattern Version Updater](../pattern-version-updater/SKILL.md) - Coordinates on version requirements

---

## Skill Maintenance

**Update this skill when**:
- Promotion criteria change
- New evidence tier definitions added
- Anthropic guidance on pattern validation changes

**Last Updated**: April 2026
**Skill Version**: 2.0.0
