# Skills Quick Reference

**Purpose**: Fast lookup for skill triggers, purposes, and integration patterns
**For detailed skill documentation**: See individual SKILL.md files in examples/

---

## Personal Skills (Universal)

Available in ALL projects via `~/.claude/skills/`

### systematic-debugger
**Purpose**: 4-phase root cause debugging methodology
**Triggers**: "bug", "error", "failing", "not working", "debug", error messages
**Workflow**: REPRODUCE → ISOLATE → UNDERSTAND → FIX
**Integration**: Works with tdd-enforcer (write regression test), git-workflow-helper (commit fix)

### tdd-enforcer
**Purpose**: Test-Driven Development enforcement
**Triggers**: "implement", "add feature", "create function", "build", coding without tests
**Workflow**: RED → GREEN → REFACTOR
**Integration**: Works with systematic-debugger (test-first debugging), git-workflow-helper (commit with tests)

### ultrathink-analyst
**Purpose**: Deep analysis for complex problems
**Triggers**: "ultrathink", "deep analysis", "systematic analysis", "comprehensive evaluation", complex multi-dimensional problems
**Workflow**: FRAME → ANALYZE → SYNTHESIZE
**Integration**: Works with hypothesis-validator (research questions), content-reviewer (publication analysis)

### git-workflow-helper
**Purpose**: Git best practices and workflow guidance
**Triggers**: "git", "commit", "branch", "merge", "push", "pull request"
**Output**: Conventional commits with proper messages, safe git operations
**Integration**: Terminal step for most workflows (commit after completion)

---

## Example Skills by Category

This repository includes 8 production-validated example skills demonstrating common patterns.

### Development Skills

#### [systematic-debugger](examples/systematic-debugger/SKILL.md)
- **Pattern**: 4-phase methodology
- **Use case**: Code debugging, test failures, unexpected behavior
- **Output**: Root cause analysis with systematic investigation
- **Risk level**: 🟢 ZERO RISK (git-controlled files only)

#### [tdd-enforcer](examples/tdd-enforcer/SKILL.md)
- **Pattern**: RED-GREEN-REFACTOR cycle
- **Use case**: Writing new code, adding features, fixing bugs
- **Output**: Test-driven development workflow, prevents code before tests
- **Risk level**: 🟢 ZERO RISK (git-controlled files only)

#### [git-workflow-helper](examples/git-workflow-helper/SKILL.md)
- **Pattern**: Git best practices automation
- **Use case**: Version control operations, preparing commits, PRs
- **Output**: Conventional commits, proper branching, safe operations
- **Risk level**: 🟢 ZERO RISK (git operations on current repo)

### Analysis Skills

#### [ultrathink-analyst](examples/ultrathink-analyst/SKILL.md)
- **Pattern**: Multi-phase deep analysis
- **Use case**: Strategic decisions, architecture choices, complex problem-solving
- **Output**: Multi-dimensional analysis with evidence-based recommendations
- **Risk level**: 🟢 ZERO RISK (git-controlled files only)

### Content & Research Skills

#### [content-reviewer](examples/content-reviewer/SKILL.md)
- **Pattern**: Quality gate for publication
- **Use case**: Blog posts, papers, external content review
- **Output**: Evidence tier validation, intellectual honesty check, voice consistency
- **Risk level**: 🟡 LOW RISK (controlled content review)
- **Integrations**: academic-citation-manager, hypothesis-validator

#### [research-extractor](examples/research-extractor/SKILL.md)
- **Pattern**: Systematic concept extraction
- **Use case**: Processing academic papers, technical articles, research synthesis
- **Output**: Structured concept extraction, bibliography entries, hypothesis links
- **Risk level**: 🔴 HIGH RISK (processes external documents - 5-layer defense)
- **Security**: Source classification, content summary, user confirmation, provenance tracking, injection detection

### Security Skills

#### [threat-model-reviewer](examples/threat-model-reviewer/SKILL.md)
- **Pattern**: STRIDE-based threat modeling
- **Use case**: Security architecture review, threat identification
- **Workflow**: UNDERSTAND → IDENTIFY (STRIDE) → ASSESS → MITIGATE
- **Risk level**: 🟢 ZERO RISK (git-controlled files only)

#### [detection-rule-reviewer](examples/detection-rule-reviewer/SKILL.md)
- **Pattern**: Detection engineering quality assurance
- **Use case**: SIEM rules, detection logic, security queries
- **Output**: Accuracy check, performance validation, evasion resistance, operational quality
- **Risk level**: 🟢 ZERO RISK (git-controlled files only)

---

## Skill Integration Patterns

### Research Workflow
```
1. research-extractor → Extract concepts from papers
2. academic-citation-manager → Classify evidence tier
3. hypothesis-validator → Link evidence to hypotheses
4. ultrathink-analyst → Deep analysis of findings
5. content-reviewer → Quality gate before publication
```

### Debugging Workflow
```
1. systematic-debugger → 4-phase root cause analysis
2. tdd-enforcer → Write regression test (RED phase)
3. systematic-debugger → Verify fix resolves root cause
4. tdd-enforcer → Refactor with test coverage (GREEN → REFACTOR)
5. git-workflow-helper → Commit fix with proper message
```

### Publication Workflow
```
1. Draft content (user writes)
2. content-reviewer → Evidence tier validation, balanced perspective
3. academic-citation-manager → Verify attribution
4. hypothesis-validator → Check claims match confidence
5. git-workflow-helper → Commit final version
```

### Security Analysis Workflow
```
1. threat-model-reviewer → Identify threats (STRIDE)
2. detection-rule-reviewer → Create detection rules
3. tdd-enforcer → Write tests for detection logic
4. git-workflow-helper → Commit rules and tests
```

---

## When to Activate (Quick Decision Tree)

### "I have a bug/error"
→ **systematic-debugger** (4-phase root cause analysis)

### "I need to write new code"
→ **tdd-enforcer** (write test first, then code)

### "I need deep analysis of complex problem"
→ **ultrathink-analyst** (FRAME-ANALYZE-SYNTHESIZE)

### "I'm working with git/version control"
→ **git-workflow-helper** (commit messages, branching, PRs)

### "I'm publishing content externally"
→ **content-reviewer** (evidence tiers, intellectual honesty, voice)

### "I'm extracting insights from research papers"
→ **research-extractor** (systematic extraction, HIGH RISK - 5-layer defense)

### "I need security threat modeling"
→ **threat-model-reviewer** (STRIDE framework)

### "I'm writing detection rules for SIEM"
→ **detection-rule-reviewer** (accuracy, performance, evasion resistance)

---

## Skill Activation Examples

### Example 1: Debug Production Error
**User**: "This DuckDB query is throwing a 'column not found' error"

**Skills Activated**:
- **systematic-debugger** → REPRODUCE (minimal test case) → ISOLATE (which column) → UNDERSTAND (schema mismatch) → FIX (update query)
- **tdd-enforcer** → Write regression test before fixing
- **git-workflow-helper** → Commit: "fix: resolve column name case sensitivity in DuckDB query"

### Example 2: Deep Architecture Analysis
**User**: "I need comprehensive analysis of whether to use Iceberg or Delta Lake for security data lake"

**Skills Activated**:
- **ultrathink-analyst** → FRAME (requirements, constraints) → ANALYZE (compare architectures) → SYNTHESIZE (recommendation with trade-offs)
- **academic-citation-manager** → Cite Ryan Blue (Iceberg creator), Databricks research
- **git-workflow-helper** → Document decision in architecture/decisions/ADR-001

### Example 3: Publish Blog Post
**User**: "Ready to publish blog post about Apache Iceberg performance"

**Skills Activated**:
- **content-reviewer** → Evidence tier check (require Tier A-B for claims) → Balanced perspective → Voice consistency
- **academic-citation-manager** → Verify citation of Ryan Blue research (Tier A)
- **hypothesis-validator** → Confirm confidence levels match evidence
- **git-workflow-helper** → Commit: "docs: publish blog post on Iceberg performance benchmarks"

### Example 4: Extract Research from Paper
**User**: "Extract key insights from this Netflix Iceberg production paper PDF"

**Skills Activated**:
- **research-extractor** (HIGH RISK) →
  - Layer 1: Source classification (Netflix = Tier 1)
  - Layer 2: Content summary first
  - Layer 3: User confirmation
  - Layer 4: Provenance tracking
  - Layer 5: Injection detection
- **academic-citation-manager** → Add to bibliography (Tier 1 source)
- **hypothesis-validator** → Link to hypothesis about Iceberg scalability

---

## Security Risk Profiles

### 🟢 ZERO RISK (6 skills)
**systematic-debugger, tdd-enforcer, ultrathink-analyst, git-workflow-helper, threat-model-reviewer, detection-rule-reviewer**
- Process only git-controlled project files
- No external document processing
- Standard file access validation
- Trust model: Version control ensures safety

### 🟡 LOW RISK (1 skill)
**content-reviewer**
- Reviews controlled external content
- User confirmation for quality assessments
- No writes without approval
- Trust model: User-provided content only

### 🔴 HIGH RISK (1 skill)
**research-extractor**
- Processes arbitrary external documents (PDFs, papers, web)
- **5-layer defense required**:
  1. Source classification
  2. Content summary first
  3. User confirmation
  4. Provenance tracking
  5. Injection detection
- Vulnerable to prompt injection attacks
- Trust model: External documents may contain malicious content

**Reference**: See [SECURITY-GUIDELINES.md](./SECURITY-GUIDELINES.md) for complete security framework

---

## Progressive Disclosure Pattern

Several example skills demonstrate progressive disclosure (3-tier context loading):

### Tier 1: SKILL.md (Always Loaded)
- Trigger conditions
- Workflow routing table
- Quick reference
- Security classification

### Tier 2: workflows/ (Loaded on Demand)
- Detailed step-by-step protocols
- Decision trees
- Quality standards

### Tier 3: references/ (Just-in-Time Lookup)
- Quick-lookup databases
- Evidence tier frameworks
- Template libraries

**Token savings**: 50-86% reduction (measured across 4 production skills)

**Example**:
```
research-extractor/
├── SKILL.md              # 121 lines (was 542 lines)
├── workflows/
│   ├── extraction.md     # Loaded when extracting
│   ├── validation.md     # Loaded when validating
│   └── documentation.md  # Loaded when documenting
└── references/
    ├── evidence-tiers.md # Loaded for tier lookup
    └── templates.md      # Loaded for output format
```

**Reference**: See [progressive-disclosure.md](../patterns/progressive-disclosure.md) for full pattern

---

## Creating Your Own Skills

### 1. Identify the Pattern
What repetitive workflow do you want to codify?

### 2. Choose Template
- Simple skill (<200 lines): Use standard template
- Complex skill (>200 lines): Use progressive disclosure

### 3. Define Triggers
- **ACTIVATE when**: Specific, detailed conditions
- **DO NOT ACTIVATE when**: Equally important - prevents false positives

### 4. Classify Security Risk
- 🟢 ZERO: Git-controlled files only
- 🟡 LOW: Trusted structured sources
- 🟠 MEDIUM: Controlled external content
- 🔴 HIGH: Arbitrary external documents

### 5. Document Integration
How does this skill work with others? What's the typical sequence?

### 6. Add Examples
2-3 concrete examples showing the skill in action

**Reference**: See [SKILL-TEMPLATE.md](./SKILL-TEMPLATE.md) for complete template

---

## Testing Skills

### Quick Activation Tests

Test if skills trigger correctly:

**Development**:
```
"Help me debug this code error" → systematic-debugger
"Implement a new feature with tests" → tdd-enforcer
"Create a git commit" → git-workflow-helper
```

**Analysis**:
```
"Deep analysis of this architecture" → ultrathink-analyst
```

**Content/Research**:
```
"Review this blog post draft" → content-reviewer
"Extract insights from this paper" → research-extractor
```

**Security**:
```
"Review this system for threats" → threat-model-reviewer
"Review this SIEM detection rule" → detection-rule-reviewer
```

---

## Maintenance

### Weekly
- Review skill activation patterns
- Note any false positives/negatives
- Update trigger conditions if needed

### Monthly
- Review skill integration effectiveness
- Update examples based on usage
- Refine DO NOT ACTIVATE conditions

### Quarterly
- Measure token usage (if using progressive disclosure)
- Validate security controls (especially HIGH RISK skills)
- Update evidence tiers and confidence levels

---

## Related Documentation

**Core Guides**:
- [Skills README](./README.md) - Comprehensive skills guide
- [SKILL-TEMPLATE.md](./SKILL-TEMPLATE.md) - Template for creating skills
- [SECURITY-GUIDELINES.md](./SECURITY-GUIDELINES.md) - Security framework

**Patterns**:
- [Progressive Disclosure](../patterns/progressive-disclosure.md) - 3-tier token optimization
- [Evidence Tiers](../patterns/evidence-tiers.md) - Source quality classification
- [Confidence Scoring](../patterns/confidence-scoring.md) - Hypothesis confidence levels

---

**Last Updated**: 2025-12-13
**Total Example Skills**: 8
**Categories**: Development (3), Analysis (1), Content/Research (2), Security (2)
