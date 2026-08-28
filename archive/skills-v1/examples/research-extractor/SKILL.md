---
name: research-extractor
description: Systematically extract and document insights from research sources (papers, articles, documentation, talks). Trigger when user analyzes academic papers, reviews technical content, reads industry articles, or mentions "this paper", "according to research", "the article discusses". Capture concepts, evidence, hypotheses, and bibliography entries with proper attribution.
allowed-tools: Read, Grep, Glob, Write
---

# Research Extractor

> **ARCHIVED — but nothing live replaces it.** Archived in the v2.0 repositioning (March 2026, DECISIONS.md § Reposition as Analytical Layer) or a later reduction. Archived, with no live successor. analysis/evidence-tiers.md is NOT a successor to this file: it supplies the evidence-grading vocabulary this skill consumed, but contains none of the skill's actual material — no source-metadata capture template, no concept/evidence/hypothesis extraction procedure, no contradiction-against-existing-knowledge step, and no bibliography entry format ('bibliograph', 'Source Metadata', and 'Concepts Extracted' return zero hits across analysis/). Its § 'Integration with Skills' merely names research-extractor as a downstream consumer, which is a dangling pointer to this archived file rather than coverage of it. The 1-5 tier table here is also not carried forward: that axis was retired by owner ruling B-F7 (2026-07-12) in favor of Tier A-D, with the record moved to archive/evidence-tiers-1-5-axis-record.md. The extraction workflow is an open coverage gap — read this file as historical reference only, and consult analysis/evidence-tiers.md solely for the current A-D grading scheme. This is a **coverage gap, not a currency gap** — the material is unreplaced, not merely out of date, so a reader who discards it is left with nothing. Its specifics are v1-era; its subject is still uncovered. (Marked 2026-08-28; successor determined by mapping plus adversarial verification, which overturned 35 of 39 successor claims — see `analysis/prose-corpus-discoverability.md`.)

Extract concepts, evidence, hypotheses, and bibliography entries from sources with proper attribution and evidence tier classification.

## Trigger Conditions

**Activate**: Analyzes papers/articles, mentions "this paper", "according to research", references publications, extracts concepts from sources

**Skip**: Implementing code, quick factual lookup, "quick summary only", personal notes

## Evidence Tiers

| Tier | Criteria | Examples |
|------|----------|----------|
| 1 | Production deployments, measured outcomes | Company engineering blog with metrics |
| 2 | Peer-reviewed, reproducible | Academic journal, conference paper |
| 3 | Expert consensus, documented reasoning | NIST, expert blogs |
| 4 | Vendor claims, unvalidated | Marketing white papers |
| 5 | Speculation, no data | Opinion pieces |

## Steps

1. **Identify Source**: Capture metadata (title, author, publication, date, URL/DOI, type)
2. **Classify Tier**: Apply evidence tier based on source type and validation
3. **Extract**: Concepts, evidence, hypotheses, contradictions
4. **Integrate**: Link to existing knowledge, note contradictions, identify gaps

## Output Format

```markdown
# Research Extraction: [Source Title]

## Source Metadata
- **Title**: [Full title]
- **Author(s)**: [Complete list]
- **Publication**: [Venue]
- **Date**: [Date]
- **URL/DOI**: [Link]
- **Evidence Tier**: [1-5] - [Rationale]

## Concepts Extracted
### [Concept Name]
**Summary**: [1-2 sentences]
**Evidence Tier**: [X]
**Related To**: [Existing concepts]

## Evidence Collected
### [Claim supported]
**Finding**: [What demonstrated]
**Data**: [Specific numbers]
**Tier**: [X]

## Contradictions
**This Source**: [Position A]
**Existing Knowledge**: [Position B]

## Bibliography Entry
[Author], "[Title]," [Venue], [Date]. [URL]
Evidence Tier: [X]
```

## Don't

- Accept claims without noting evidence tier
- Treat vendor claims as Tier 1-2 evidence
- Extract without proper attribution
- Skip contradiction checking
- Cherry-pick supporting evidence only
