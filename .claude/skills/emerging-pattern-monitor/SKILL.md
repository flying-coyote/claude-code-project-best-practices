---
name: emerging-pattern-monitor
version: 2.2.0
description: Monitors analysis-doc lifecycle in all three lanes — EMERGING→PRODUCTION promotion, PRODUCTION→RETIRING/RETIRED retirement (replacement-readiness as robust community/vendor elements mature), and follow-lane upkeep (followed canons' advance triggers + liveness, per ABSORPTION-MAP.md)
triggers:
  - "review emerging patterns"
  - "check pattern promotion"
  - "evaluate emerging"
  - "promote pattern"
  - "review retirement candidates"
  - "replacement readiness"
  - "what can we retire"
  - "follow-lane check"
  - "absorption sweep"
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
   - File: analysis/orchestration-comparison.md (Framework Selection section, merged 2026-07-16)
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

## Retirement Monitoring (PRODUCTION → RETIRING → RETIRED)

The inverse lane. This project is designed to prune itself as the ecosystem matures (see [CONTRIBUTING.md](../../CONTRIBUTING.md) § Retiring a doc) — coverage shrinking is success, not decay — so PRODUCTION docs are also monitored for whether a robust community/vendor element has caught up enough to take over a slice.

### Phase R1: Scan PRODUCTION docs for replacement candidates

Triggers to check:
- A new Anthropic first-party feature/command that overlaps a doc's slice (changelog, engineering blog, a new `/`-command)
- A community tool reaching GA + real adoption that covers a doc's slice
- A periodic obsolescence sweep — "what did the market just ship that we no longer need to carry?"

### Phase R2: Apply the robustness bar (retire only when ALL four clear)

1. **Supported** — first-party (Anthropic) or robustly community-maintained (active, 1.0+, real adoption)
2. **GA, not preview** — generally available, not a research preview/beta
3. **Covers the slice's substance** — does the actual work the doc covered, not a superficial overlap
4. **Citeable** — a stable source to cite (vendor doc, changelog, named feature)

All four clear → recommend `RETIRING` (defer the slice; keep only what the replacement does not cover). Replacement fully carries the load → `RETIRED` (tombstone pointer).

### Phase R3: Take action (per CONTRIBUTING.md § Retiring a doc)

1. Set `status: RETIRING/RETIRED` + `replacement-by:` frontmatter
2. Add the Replacement-status banner; register the replacement in SOURCES.md with its boundary (what it does / does not do)
3. Update AUDIT-CONTEXT.md routing to defer to the replacement
4. Log the retirement in the SOURCES.md refresh log + PLAN.md

**Completed retirements**: `session-quality-tools.md` → first-party `/insights` + native `claude doctor` (RETIRING 2026-06-04; completed + archived 2026-07-10 — the lane's first full cycle). **Watch list**: the single watch list now lives in [`ABSORPTION-MAP.md`](../../../ABSORPTION-MAP.md) — one row per routable doc with absorber, lane, robustness-bar state, retained delta, and advance trigger (the former in-file items migrated there 2026-07-16: MCP/skills cost-economics ← `/usage` became the map's retire-toward row; install-health ← `/doctor` sits in the map's non-doc watch notes, a slice this project never claimed). Do not maintain a second list here.

---

## Phase F: Follow-lane monitoring (quarterly)

The third lane. Docs with a `follows:` frontmatter field (see CONTRIBUTING.md § Following a Canon) track an external canon that carries the conceptual load for their slice while the doc keeps only its delta. Quarterly, for each `follow`-lane row in ABSORPTION-MAP.md:

1. **Advance-trigger check** — has the row's named observable event happened (e.g., the canon's practice productized by a Supported tool, or first-party docs absorbing the slice)? If yes and all four robustness bars now clear, propose converting `follows:` → `replacement-by:` + `RETIRING` via Phase R3.
2. **Canon liveness check** — is the canon still active (posts/commits within ~6 months)? A frozen canon (the HumanLayer 12-factor precedent: no push since 2025-09) is grounds to recommend dropping the pointer, not to keep following.
3. **Output** — either "no change; `Verified` dates bumped for the rows actually re-checked" or a new `drafts/ABSORPTION-SCAN-YYYY-QQ.md` proposing a wave. A wave is NOT mandatory every quarter (Decision 9's negative precedent: don't over-apply reshaping to well-built docs).

This phase is judgment work and belongs in the quarterly cadence; the weekly review only runs mechanical map-consistency greps (weekly-review step 5b).

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

**Last Updated**: 2026-07-16 (added Phase F follow-lane monitoring; watch list migrated to ABSORPTION-MAP.md as the single store)
**Skill Version**: 2.2.0
