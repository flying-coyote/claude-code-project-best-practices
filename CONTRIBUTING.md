# Contributing to Claude Code Project Best Practices

Thank you for your interest in contributing! This repository provides evidence-based analysis of Claude Code patterns and practices.

## Contribution Philosophy

This repository follows strict quality standards:
- **Evidence-based**: All analysis must cite authoritative sources (Tier A or B)
- **Analytical focus**: We evaluate and compare, not provide implementation guides
- **Quantified claims**: Behavioral observations require source attribution and dates

## What We Accept

### New Analysis (High Value)
- Evidence-based evaluations of new claims or approaches
- Quantified behavioral observations from expert practitioners
- Comparative analysis of tools, frameworks, or approaches
- Source verification and revalidation of existing claims

### Analysis Improvements (Medium Value)
- Updated metrics from recent validation
- New source material for existing analysis documents
- Clarifications based on reader confusion
- Cross-reference improvements

### Documentation Improvements (Lower Value)
- Typo fixes
- Broken link repairs
- Formatting improvements

## What We Don't Accept

- Implementation guides (defer to ECC or superpowers)
- Theoretical patterns without production validation
- Content without source attribution
- Claims without evidence tier classification

## How to Contribute

### 1. Check Existing Issues
Before starting, check if your idea is already being discussed:
- Browse [Issues](https://github.com/flying-coyote/claude-code-project-best-practices/issues)
- Search for related analysis documents in the repo

### 2. Open a Discussion Issue
For new analysis documents or significant changes:
```markdown
Title: [Analysis Proposal] Name of Analysis

## Source
- Tier: [A/B/C]
- URL: [link]
- Description: [brief]

## Production Validation
- Projects tested: [number]
- Measured results: [metrics if available]

## Analysis Summary
[What claim or approach does it evaluate?]
[What evidence supports or contradicts it?]
[When does this apply?]

## Integration
[How does it relate to existing analysis documents?]
```

### 3. Submit a Pull Request

#### For Analysis Contributions

**File Structure**:
```bash
# Create analysis document
touch analysis/your-analysis.md

# Add source to SOURCES.md with evidence tier
# Add cross-references to related analysis documents
```

**Analysis Document Template**:
```markdown
# Analysis Title

**Source**: [Author/Source Name with URL]
**Evidence Tier**: [A/B/C] — Claim Strength: [1-5]
**Last Validated**: YYYY-MM-DD

## The Claim

[What claim or approach is being evaluated?]

## Evidence

[Evidence for and against, with source attribution]

## Comparative Analysis

[How does this compare to alternatives?]

## Measured Results (if applicable)

[Quantified metrics from production validation]

## Related Analysis

- [Related Analysis 1](./related-1.md)
- [Related Analysis 2](./related-2.md)
```

#### For Documentation Contributions

Small fixes can go directly to PR:
- Typos
- Broken links
- Formatting issues
- Minor clarifications

### 4. Pass Validation Checklist

Before submitting, verify:

**For New Analysis Documents**:
- [ ] Has authoritative source (Tier A or B)
- [ ] Evaluated against production evidence (3+ projects for Tier B)
- [ ] Includes comparative analysis or quantified metrics
- [ ] Has clear claim statement with evidence tier classification
- [ ] Documents limitations and trade-offs
- [ ] Cross-references related analysis documents
- [ ] Added to SOURCES.md with evidence tier
- [ ] Mentioned in appropriate README sections

**For Documentation Changes**:
- [ ] Markdown formatting is correct
- [ ] Links are valid and working
- [ ] No typos or grammar errors
- [ ] Changes align with existing voice/style

### 5. PR Description Template

```markdown
## What This Changes
[Brief description]

## Why This Is Needed
[Problem being solved]

## Evidence/Validation
- Source: [Tier A/B/C - link]
- Tested in: [number] projects
- Results: [metrics if applicable]

## Checklist
- [ ] Followed validation checklist above
- [ ] Updated SOURCES.md
- [ ] Added cross-references
- [ ] Tested locally
```

## Review Process

1. **Initial Triage** (24-48 hours)
   - Check if it aligns with contribution guidelines
   - Verify evidence tier is A or B
   - Request clarifications if needed

2. **Technical Review** (3-7 days)
   - Validate pattern against existing practices
   - Check for conflicts or redundancies
   - Verify production validation claims

3. **Integration Review**
   - Ensure cross-references are complete
   - Check SOURCES.md is updated
   - Verify self-compliance

4. **Merge or Request Changes**
   - Merged if approved
   - Changes requested with specific guidance
   - Closed if doesn't meet criteria (with explanation)

## Deprecation Process

When deprecating a pattern, tool, or recommendation, follow this checklist to prevent coordination gaps across the repository.

### Deprecation Checklist

**Before deprecating**, ensure you have:
- [ ] **Authoritative source** for deprecation (Anthropic announcement, security advisory, superseding feature)
- [ ] **Migration path** documented (what to use instead)
- [ ] **Grace period** defined (recommended: 90 days for tool deprecations)

**Steps to deprecate**:

1. **Update DEPRECATIONS.md**:
   ```markdown
   ### [Tool/Pattern Name]

   **Status**: ❌ DEPRECATED
   **Deprecated Date**: YYYY-MM-DD
   **Reason**: [Brief explanation]
   **Grace Period Ends**: YYYY-MM-DD (if applicable)

   **Migration Path**:
   [Clear instructions on what to use instead]
   ```

2. **Search all analysis documents for references**:
   ```bash
   # Find all mentions of deprecated item
   grep -r "deprecated-tool-name" analysis/
   grep -r "deprecated-item" analysis/
   ```

3. **Update or remove recommendations**:
   - Add deprecation notice where still referenced (if in grace period)
   - Remove from "recommended" or "top N" lists
   - Update decision matrices and configuration examples
   - Replace with migration path where appropriate

4. **Add migration notes**:
   - In analysis documents that reference deprecated item, add:
     ```markdown
     > ⚠️ **Deprecated**: [Tool] was deprecated YYYY-MM-DD.
     > Use [replacement] instead. See [DEPRECATIONS.md](../DEPRECATIONS.md#tool-name).
     ```

5. **Run comprehensive grep**:
   ```bash
   # Catch any missed references
   grep -ri "deprecated-item" . --exclude-dir=.git --exclude-dir=node_modules
   ```

6. **Update related files**:
   - [ ] SOURCES.md (mark source as deprecated if tool-specific)
   - [ ] README.md (remove from features/tools list)
   - [ ] INDEX.md (regenerate if pattern removed)
   - [ ] QUICKSTART.md (update if quick start references deprecated item)

7. **Grace period tracking** (if applicable):
   - Add to QUARTERLY-REVIEW.md checklist to remove after grace period
   - Set calendar reminder for grace period end date

### Example: Claude in Chrome Deprecation

See [AUDIT-2026-02-27.md](AUDIT-2026-02-27.md) for case study of deprecation coordination issues.

**What went wrong**:
- DEPRECATIONS.md updated ✅
- mcp-daily-essentials.md still recommended it ❌
- tool-ecosystem.md recommended alternative ✅

**Lesson**: Must update ALL analysis documents that reference deprecated item, not just DEPRECATIONS.md.

### After Grace Period

When grace period expires:
1. Remove all mentions from analysis documents (no more "deprecated" notices)
2. Update DEPRECATIONS.md to mark grace period as ended
3. Grep to verify complete removal
4. Consider moving to ARCHIVE.md if historical value

## Evidence Tier Definitions

### Tier A: Primary Sources
- Direct from Anthropic (engineering blog, documentation)
- Official specifications and standards
- First-party production data from Anthropic

### Tier B: Validated Secondary
- Peer-reviewed or expert-validated work
- Production-tested implementations (3+ projects)
- Industry-accepted practices with documentation
- Measured results from real-world usage

### Tier C: Industry Knowledge
- Vendor documentation
- Community best practices
- Well-documented analyst reports

### Tier D: Opinions/Speculation
- Personal experience (single project)
- Theoretical projections
- Unvalidated claims

**We primarily accept Tier A and B contributions.**

## Style Guide

### Writing Voice
- **Practical over theoretical**: Focus on implementation
- **Concise over comprehensive**: Respect reader's time
- **Evidence over opinion**: Always cite sources
- **Honest about limitations**: Acknowledge trade-offs

### Markdown Conventions
- Use ATX headers (`#` not underlines)
- Code blocks specify language: ` ```bash ` not ` ``` `
- Tables for structured comparisons
- Bold for **emphasis**, italics for *examples*

### File Naming
- Lowercase with dashes: `analysis-name.md`
- Descriptive: `context-engineering.md` not `context.md`
- Consistent with existing analysis documents

## Questions?

- Open an [Issue](https://github.com/flying-coyote/claude-code-project-best-practices/issues) for questions
- Reference [DECISIONS.md](DECISIONS.md) for design rationale
- Review [SOURCES.md](SOURCES.md) for evidence tier examples

## Code of Conduct

- Be respectful and professional
- Focus on analysis, not individuals
- Assume good intent
- Provide constructive feedback
- Acknowledge prior art and sources

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for helping improve Claude Code evidence-based analysis!**
