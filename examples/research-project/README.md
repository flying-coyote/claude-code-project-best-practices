# Research Project Example

**Type**: Systematic literature review / research and analysis project

**Demonstrates**: Claude Code setup for research, hypothesis tracking, and evidence synthesis

---

## What This Example Shows

### Tier 1 Infrastructure (5 minutes)
✅ **Stop hook** - Warns about uncommitted research findings
- Critical for research: prevents losing analysis progress
- Custom message: "save your findings" emphasizes data preservation
- See `.claude/settings.json` lines 8-17

### Tier 2 Infrastructure (15 minutes)
✅ **Pre-approved permissions** - Research commands, git operations
- `python -m`, `jupyter` (for data analysis)
- `git status`, `git diff`, `git log`
- See `.claude/settings.json` lines 2-7

✅ **Minimal CLAUDE.md** - 37 lines (target ~60)
- Evidence tiers (critical for research validity)
- Hypothesis tracking format (standardization after 5 violations)
- Research integrity violations to avoid (learned from mistakes)
- See `.claude/CLAUDE.md`

### Key Research-Specific Features

✅ **Evidence Tier System**
- 4-tier classification (A/B/C/D) for all claims
- Strong claims require Tier A evidence only
- Enforces research rigor and source quality

✅ **Hypothesis Tracking Standard**
- Standardized format after 5 format violations
- Prevents inconsistent hypothesis documentation
- See template in CLAUDE.md

✅ **Research Integrity Checklist**
- Documents actual violations from this project
- Not generic guidelines - specific mistakes made
- 6 correlation/causation mix-ups, 4 language precision errors, 2 omitted contradictions

---

## File Structure

```
research-project/
  .claude/
    CLAUDE.md              # Minimal context (37 lines)
    settings.json          # Hooks + permissions
  README.md               # This file (explains the example)
  hypotheses/             # Hypothesis tracking
    HYP-001-productivity.md
    HYP-002-quality.md
    README.md             # Tracking template
  sources/                # Source materials
  analysis/               # Data synthesis
  contradictions/         # Unresolved conflicts
  BIBLIOGRAPHY.md         # Complete source list with tiers
  FINDINGS.md             # Summary of results
```

---

## Key Differences from Other Project Types

### 1. Evidence Tiers are Central
**Why in CLAUDE.md**: Research validity depends on source quality
- Every claim needs tier classification
- Strong claims require Tier A only
- Claude repeatedly forgets this without reminder

**Not just documentation**: This is a quality gate, not a style guide.

---

### 2. Hypothesis Tracking Format
**What's included**:
```markdown
## Hypothesis Tracking Format
Each hypothesis file must include:
- Statement, rationale, confidence level (HIGH/MEDIUM/LOW)
- Supporting evidence (with tiers), contradicting evidence
- This format was violated 5 times → standardize
```

**Why**: After 5 inconsistent hypothesis files, standardization was necessary.

**Principle**: Document standards only after they've been violated multiple times.

---

### 3. Research Integrity as Gotchas
**Not generic guidelines**:
```markdown
## Research Integrity Violations to Avoid
- Repeatedly mixed correlation/causation (6 instances in draft)
- Used "definitely" instead of "may indicate" (4 corrections needed)
- Omitted contradicting evidence (caught in peer review twice)
```

These are **actual mistakes from this project**, not generic research ethics.

---

### 4. Citation and Source Management
**Project-specific rules**:
- Sources must match BIBLIOGRAPHY.md entries (broke 3 citations)
- Tier A sources require DOI or permanent URL (2 became inaccessible)
- Expert quotes need date, context, consent flag

These are **learned from errors**, not preemptive documentation.

---

## Usage

### Quick Start (Copy this setup)
```bash
# In your research project
mkdir -p .claude
cp examples/research-project/.claude/CLAUDE.md .claude/
cp examples/research-project/.claude/settings.json .claude/

# Customize CLAUDE.md:
# 1. Replace evidence tiers if you use different system
# 2. Update hypothesis format to match your methodology
# 3. Replace integrity violations with YOUR actual mistakes
```

### Customize for Your Research

1. **Evidence Tiers**:
   - Adjust tier definitions for your field
   - Academic research may have stricter criteria
   - Industry research may use different validation

2. **Hypothesis Format**:
   - Adapt to your research methodology
   - Experimental design has different needs than literature review
   - Include fields your analysis requires

3. **Integrity Violations**:
   - Start with empty list
   - Add violations as they occur
   - Remove after 3+ sessions without recurrence

4. **Commands**:
   - Add analysis tools you use (R, SPSS, Stata, etc.)
   - Include dataset validation commands
   - Pre-approve statistical analysis scripts

---

## Common Adaptations

### For Data Science / ML Research
**settings.json**:
```json
"permissions": {
  "allow": [
    "Bash(python -m pytest*)",
    "Bash(python train.py*)",
    "Bash(jupyter notebook*)",
    "Bash(tensorboard*)",
    "Bash(git lfs*)"
  ]
}
```

**CLAUDE.md additions**:
```markdown
## Dataset Requirements
- All datasets in data/ with README.md metadata
- Train/val/test splits documented with random seeds
- Data preprocessing steps logged in notebooks/preprocessing.ipynb
```

### For Qualitative Research
**Evidence tiers** (different criteria):
```markdown
## Evidence Tiers (Qualitative)
- **Tier A**: Primary sources, transcripts, original documents
- **Tier B**: Published analysis, expert interpretation
- **Tier C**: Secondary sources, summaries
- **Tier D**: Personal impressions, preliminary observations
```

**CLAUDE.md additions**:
```markdown
## Known Gotchas
- Interview transcripts must anonymize participant IDs (P001, P002, not names)
- Code themes in codes/CODEBOOK.md before applying (changed 4 times mid-analysis)
- Each quote requires participant ID, date, and context sentence
```

### For Meta-Analysis
**Hypothesis tracking** (stricter):
```markdown
## Hypothesis Format (Pre-registered)
Each hypothesis must include:
- H_N: Statement (exactly as pre-registered)
- Pre-registration ID and date (unchangeable)
- Planned analysis method
- Actual analysis method (if deviated, explain)
- Supporting/contradicting studies (with effect sizes)
```

---

## Hook Examples for Research

### Citation Validator
Check bibliography consistency before committing:
```json
{
  "matcher": "Bash(git commit*)",
  "hooks": [{
    "type": "command",
    "command": "python scripts/validate_citations.py || (echo '⚠️ Citation errors detected'; exit 1)"
  }]
}
```

### Hypothesis Count on Stop
Show progress on session end:
```json
{
  "matcher": "",
  "hooks": [{
    "type": "command",
    "command": "bash -c 'echo \"📊 Total hypotheses: $(ls hypotheses/HYP-*.md 2>/dev/null | wc -l | tr -d \" \")\"'"
  }]
}
```

### Evidence Tier Check on Write
Validate evidence tiers when writing findings:
```json
{
  "matcher": "Write(FINDINGS.md)",
  "hooks": [{
    "type": "command",
    "command": "python scripts/check_evidence_tiers.py FINDINGS.md || echo '⚠️ Missing evidence tiers'"
  }]
}
```

---

## Validation Checklist

After setting up:
- [ ] CLAUDE.md is under 60 lines (this example: 37 lines)
- [ ] Evidence tiers match your field's standards
- [ ] Hypothesis format reflects your methodology
- [ ] Integrity violations are YOUR actual mistakes, not generic advice
- [ ] Stop hook warns about uncommitted research
- [ ] Pre-approved commands match your analysis tools
- [ ] Citation/source requirements are project-specific

---

## Research Workflow with Claude Code

### Literature Review Phase
1. **Session start**: Review uncommitted notes, recent commits
2. **Source extraction**: Read papers, extract claims with evidence tiers
3. **Hypothesis updates**: Add supporting/contradicting evidence
4. **Session end**: Commit findings, push to backup

### Analysis Phase
1. **Load context**: CLAUDE.md reminds of evidence standards
2. **Synthesize**: Identify patterns, conflicts, gaps
3. **Validate**: Check claims against evidence tier requirements
4. **Document**: Update FINDINGS.md with tiered references

### Validation Phase
1. **Review**: Claude checks for integrity violations
2. **Cite**: Verify all claims have appropriate evidence
3. **Contradict**: Surface documented contradictions
4. **Finalize**: Commit validated findings

**Key**: CLAUDE.md keeps research standards top-of-mind without requiring manual tracking.

---

## Related Patterns

- [evidence-tiers.md](../../patterns/evidence-tiers.md) - Dual tier system for claims
- [confidence-scoring.md](../../patterns/confidence-scoring.md) - HIGH/MEDIUM/LOW assessment
- [context-engineering.md](../../patterns/context-engineering.md) - External artifacts as memory
- [FOUNDATIONAL-PRINCIPLES.md](../../FOUNDATIONAL-PRINCIPLES.md) - The Big 3

---

## Notes

- This is a **reference example**, not a real research project
- No actual research data included (focus on .claude/ structure)
- Customize evidence tiers for your field
- Research integrity violations should reflect YOUR mistakes
- Adapt hypothesis format to your methodology

**Last Updated**: February 2026
