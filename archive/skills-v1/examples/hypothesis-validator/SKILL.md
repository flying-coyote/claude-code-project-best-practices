---
name: hypothesis-validator
description: Apply systematic hypothesis validation when user formulates research claims or proposes testable hypotheses. Trigger on "I hypothesize that...", "Can you validate this claim?", or research findings requiring evidence assessment. Use confidence scoring and evidence tier classification.
allowed-tools: Read, Grep, Glob, Edit, Write
---

# Hypothesis Validator

> **ARCHIVED — not current guidance, and only partly succeeded.** Archived in the v2.0 repositioning (March 2026, DECISIONS.md § Reposition as Analytical Layer) or a later reduction. Partially superseded by [analysis/evidence-tiers.md](../../../../analysis/evidence-tiers.md). That doc's § 'Confidence Assessment (HIGH/MEDIUM/LOW) — merged 2026-07-16' carries this skill's confidence bands (same >80% / 50-80% / <50% thresholds), its hypothesis documentation format, its confidence-language guide, and — in § 'Contradiction Handling' — its contradiction step, and it adds a canonical tier-to-confidence mapping, decision thresholds, and calibration gaps. It does NOT carry this skill's operational method: the five-step workflow (Identify → Assess → Score → Analyze → Document), the testability-assessment step (independent/dependent variables, scope — absent entirely from the successor), the trigger/skip activation conditions, or hypothesis tracking by ID and status. Note also that this skill's 1-5 evidence tiers were retired 2026-07-12 (owner ruling B-F7); their record is in [archive/evidence-tiers-1-5-axis-record.md](../../../evidence-tiers-1-5-axis-record.md), not in the successor. evidence-tiers.md itself names hypothesis-validator under § 'Integration with Skills' as a consumer of its framework rather than a replaced artifact — treat that doc as the reference this skill applied, and consult this file for the method itself. Its v1-era specifics and dates are a snapshot, preserved as recorded — do not treat them as current. (Marked 2026-08-28; successor determined by mapping plus adversarial verification, which overturned 35 of 39 successor claims — see `analysis/prose-corpus-discoverability.md`.)

Validate research hypotheses using systematic methodology: assess testability, classify evidence, assign confidence levels.

## Trigger Conditions

**Activate**: "I hypothesize that...", "validate this claim", "what evidence supports", research claims, confidence assessment requests

**Skip**: Reading others' research (passive), well-established facts, brainstorming marked exploratory

## Evidence Tiers

| Tier | Type | Weight |
|------|------|--------|
| 1 | Production deployments, measured outcomes | Highest |
| 2 | Peer-reviewed research, replication | High |
| 3 | Expert consensus, documented reasoning | Medium |
| 4 | Vendor claims, theoretical assertions | Low |
| 5 | Speculation, opinion, unverified | Minimal |

## Confidence Levels

| Level | Criteria |
|-------|----------|
| HIGH (>80%) | 2+ Tier 1 sources OR multiple Tier 2 + Tier 1, no contradictions |
| MEDIUM (50-80%) | 1+ Tier 2-3 sources, some validation, minor contradictions |
| LOW (<50%) | Only Tier 4-5, theoretical only, significant contradictions |

## Steps

1. **Identify**: Extract testable hypothesis (independent/dependent variables, scope)
2. **Assess**: Classify all evidence by tier, identify gaps
3. **Score**: Assign confidence level with justification
4. **Analyze**: Document contradictions, attempt reconciliation
5. **Document**: Track with ID, status, validation plan

## Output Format

```markdown
# Hypothesis: [Title]

**Statement**: [Clear, testable hypothesis with scope]
**Confidence**: [HIGH/MEDIUM/LOW] ([XX]%)

**Evidence**:
- Tier 1: [Finding]
- Tier 2: [Finding]

**Contradictions**: [Any conflicts and resolution status]

**Language Guide**:
- HIGH: "demonstrates", "shows"
- MEDIUM: "suggests", "indicates"
- LOW: "hypothesizes", "may"

**Validation Plan**: [What's needed to increase confidence]
```

## Don't

- Accept vendor claims without independent validation
- Use "proves" or "always" with MEDIUM/LOW confidence
- Ignore contradictions when scoring
- Present LOW confidence as validated fact
- Skip evidence tier classification
