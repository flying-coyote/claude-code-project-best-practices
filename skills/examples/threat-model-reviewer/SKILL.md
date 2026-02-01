---
name: Threat Model Reviewer
description: Apply systematic threat modeling review when user designs systems, evaluates security architectures, or analyzes attack surfaces. Trigger when user mentions "threat model", "security review", "attack surface", "STRIDE", "trust boundary", or asks about potential threats. Use structured methodology to identify threats, assess risks, and recommend mitigations.
allowed-tools: Read, Grep, Glob, WebSearch
---

# Threat Model Reviewer

Systematically identify, classify, and prioritize threats using STRIDE framework.

## Trigger Conditions

**Activate**: Designs systems with security implications, asks about threats, mentions "threat model", "attack surface", "what could go wrong"

**Skip**: Specific bugs (→ systematic-debugger), general concepts without specific system, compliance checklists

## STRIDE Framework

| Category | Question | Examples |
|----------|----------|----------|
| **S**poofing | Can identity be faked? | Credential theft, session hijacking |
| **T**ampering | Can data be modified? | MITM, SQL injection |
| **R**epudiation | Can actions be denied? | Missing audit logs |
| **I**nfo Disclosure | Can data leak? | Verbose errors, insecure storage |
| **D**enial of Service | Can service be disrupted? | Resource exhaustion, DDoS |
| **E**levation of Privilege | Can permissions exceed? | Privilege escalation, IDOR |

## Risk Matrix

| Likelihood | Low Impact | Medium | High |
|------------|------------|--------|------|
| High | Medium | High | **Critical** |
| Medium | Low | Medium | High |
| Low | Low | Low | Medium |

## Steps

1. **Understand**: Map components, data flows, trust boundaries, sensitive assets
2. **Identify**: Apply STRIDE to each component/flow
3. **Assess**: Score likelihood × impact, prioritize risks
4. **Mitigate**: Recommend controls (Prevent, Detect, Respond, Recover)

## Output Format

```markdown
## System Understanding
**Components**: [List with trust levels]
**Trust Boundaries**: [What they separate]
**Sensitive Assets**: [Location, sensitivity]

## Threat Identification
### [Component]
- T1: [Threat] - [Scenario] - Current mitigation: [X]

## Risk Assessment
| ID | Threat | Likelihood | Impact | Risk |
|----|--------|------------|--------|------|
| T1 | [name] | High | High | Critical |

## Mitigations
**T1**:
- Prevent: [Control]
- Detect: [Monitoring]
- Effort: [Low/Med/High]
```

## Don't

- Skip threat identification for "simple" systems
- Assume cloud/framework handles all security
- Mark all risks as "critical" (dilutes prioritization)
- Ignore supply chain and third-party risks
- Create threat model once and never update
