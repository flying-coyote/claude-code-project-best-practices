---
name: Detection Rule Reviewer
description: Apply detection engineering quality standards when user writes SIEM rules, detection logic, or security monitoring queries. Trigger when user mentions "detection rule", "SIEM", "Sigma", "alert", "Splunk query", "KQL", or shares security detection code. Evaluate for accuracy, performance, evasion resistance, and operational quality.
allowed-tools: Read, Grep, Glob, WebSearch
---

# Detection Rule Reviewer

Evaluate detection rules against quality standards: accuracy, performance, evasion resistance, and operational readiness.

## Trigger Conditions

**Activate**: Writes SIEM rules, Sigma/Splunk/KQL queries, asks about detection coverage, mentions "detection rule", "alert logic"

**Skip**: General data queries (non-security), threat models (→ threat-model-reviewer), SIEM infrastructure issues

## Quality Dimensions

| Dimension | Question | Checks |
|-----------|----------|--------|
| **Accuracy** | Catches what it should? | Field names exist, case sensitivity, thresholds justified |
| **Performance** | Query efficient? | Indexed fields first, bounded time, no unnecessary regex |
| **Evasion** | Hard to bypass? | Handles obfuscation, abbreviations, encoding tricks |
| **Operational** | Alert actionable? | Context fields, severity, runbook reference |

## Steps

1. **Understand**: Parse attack technique, MITRE ATT&CK mapping, data sources, trigger logic
2. **Evaluate**: Score each dimension (1-5), note strengths and issues
3. **Improve**: Provide specific fixes (Critical/Important/Enhancement)
4. **Validate**: Suggest true positive, false positive, and evasion tests

## Output Format

```markdown
## Detection Understanding
**Target**: [Attack/behavior]
**MITRE ATT&CK**: [T-code]
**Data Sources**: [Required logs]

## Quality Evaluation
| Dimension | Score | Issues |
|-----------|-------|--------|
| Accuracy | X/5 | [Issues] |
| Performance | X/5 | [Issues] |
| Evasion | X/5 | [Issues] |
| Operational | X/5 | [Issues] |

## Recommendations
**Critical**: [Must fix]
**Important**: [Should fix]

## Revised Rule
[Improved detection code]

## Testing Plan
- True positive: [Test command]
- False positive: [Benign scenario]
- Evasion: [Bypass test]
```

## Don't

- Create detections without testing
- Use overly broad patterns causing alert fatigue
- Assume attackers won't evade simple patterns
- Copy-paste detections without understanding data source
- Skip performance profiling before deployment
