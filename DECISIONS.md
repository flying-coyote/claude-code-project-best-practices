# Design Decisions

This document explains the reasoning behind key design choices and alternatives that were considered.

## Decision 1: Prompt-Based Setup vs. Template Repository

### Alternatives Considered

| Approach | Pros | Cons |
|----------|------|------|
| **Template repo** (`gh repo create --template`) | Version-controlled, one command | Rigid structure, hard to customize, requires GitHub |
| **Shell script** (bash bootstrap) | Automated, consistent | Not interactive, can't adapt to project context |
| **Copy-paste files** | Simple, portable | Manual, error-prone, no guidance |
| **AI-guided prompt** | Interactive, adaptive, explains choices | Requires Claude Code, slightly longer |

### Decision: AI-Guided Prompt

**Why**: The prompt approach lets Claude:
1. Assess your project's characteristics before setup
2. Ask relevant questions about your needs
3. Explain what each component does as it creates them
4. Adapt to edge cases (existing files, unusual structures)

**Trade-off accepted**: Requires Claude Code to run. But if you're setting up Claude Code infrastructure, you already have Claude Code.

---

## Decision 2: Four Presets vs. Single Template

### Alternatives Considered

| Approach | Pros | Cons |
|----------|------|------|
| **Single template** | Simple, one-size-fits-all | Doesn't fit diverse project types |
| **Many presets** (10+) | Very specific configurations | Overwhelming choice, maintenance burden |
| **No presets** (fully custom) | Maximum flexibility | Requires too many decisions upfront |
| **Four presets** | Covers major categories, manageable | Some projects don't fit cleanly |

### Decision: Four Presets (coding, writing, research, hybrid)

**Why**: These four categories cover the vast majority of projects:
- **coding**: Software development, libraries, tools
- **writing**: Books, blogs, documentation
- **research**: Analysis, literature reviews, studies
- **hybrid**: Mixed-purpose (most real projects)

**Trade-off accepted**: Some projects don't fit neatly. That's what `hybrid` is for, and users can always customize after setup.

---

## Decision 3: What to Include by Default

### Components Evaluated

| Component | Included by Default? | Reasoning |
|-----------|---------------------|-----------|
| **CLAUDE.md** | Yes (always) | Core value - project context |
| **Session hook** | Optional (asked) | Useful but adds complexity |
| **Post-tool hook** | No | Only useful for specific workflows |
| **Stop hook** | No | Rarely needed |
| **Slash commands** | No | Project-specific, add later |
| **Custom skills** | No | Advanced feature, add later |

### Decision: Minimal by Default

**Why**: Start with just what's needed:
1. **CLAUDE.md** - Always created (the core value)
2. **Session hook** - Asked about (useful context display)
3. Everything else - Add later if needed

**Philosophy**: It's easier to add components than remove them. Over-engineering at setup leads to unused complexity.

---

## Decision 4: Hook Complexity

### Alternatives Considered

| Approach | What it shows | Complexity |
|----------|--------------|------------|
| **No hooks** | Nothing | None |
| **Simple hook** | Branch + uncommitted count | Low |
| **Medium hook** | + Recent commits + phase | Medium |
| **Complex hook** | + In-progress tasks + cross-repo status | High |

### Decision: Medium Complexity Hook (Opt-in)

**Why**: The session-start hook shows:
- Current branch
- Uncommitted changes count
- Recent commits (last 3)
- Current phase (if ARCHITECTURE.md exists)

This implements Anthropic's "verify before work" pattern without requiring additional tracking files.

**Not included**: Cross-repo progress tracking, JSON task files. These are powerful but add maintenance overhead.

---

## Decision 5: Quality Standards by Preset

### How Standards Differ

| Preset | Primary Standards |
|--------|------------------|
| **coding** | Clean code, TDD, conventional commits, no over-engineering |
| **writing** | Evidence-based, balanced perspective, voice consistency |
| **research** | Evidence tiers, hypothesis tracking, source attribution |
| **hybrid** | Combined subset of all three |

### Decision: Preset-Specific Standards

**Why**: Different project types have different quality concerns:
- A library doesn't need citation standards
- A book doesn't need TDD enforcement
- Research needs rigorous evidence tracking

**Trade-off**: The `hybrid` preset has broader standards, which means more to follow. This is intentional for mixed-purpose projects.

---

## Decision 6: Audit vs. Bootstrap Separation

### Alternatives Considered

| Approach | Behavior |
|----------|----------|
| **Single prompt** | Detects state, either bootstraps or audits |
| **Two prompts** | Separate prompts for new vs. existing |

### Decision: Two Separate Prompts

**Why**: Different mental models and workflows:
- **Bootstrap**: "I'm starting fresh, set me up"
- **Audit**: "I have something, how can I improve it?"

Combining them adds complexity and makes each less focused.

---

## Decision 7: Where to Store This Repository

### Alternatives Considered

| Location | Pros | Cons |
|----------|------|------|
| **GitHub Gist** | Simple, single file | Can't have directory structure |
| **Personal repo** | Full control | Less discoverable |
| **Organization repo** | Team access | Requires org setup |
| **Public repo** | Maximum reach, community | Maintenance responsibility |

### Decision: Public GitHub Repository

**Why**: The goal is to share these patterns widely. A public repo:
- Is easily referenced in prompts via raw URLs
- Can accept community contributions
- Establishes credibility through transparency
- Allows versioning and improvement over time

---

## Anti-Patterns Avoided

### 1. Over-Specification
**Avoided**: Detailed templates for every possible project type.
**Why**: Creates maintenance burden and decision paralysis.

### 2. Mandatory Components
**Avoided**: Forcing all hooks and features on every project.
**Why**: Not every project needs automation. Start minimal.

### 3. External Dependencies
**Avoided**: Requiring specific tools beyond Claude Code.
**Why**: Maximum portability and simplicity.

### 4. Complex Scripting
**Avoided**: Bash scripts with many options and flags.
**Why**: AI-guided setup is more flexible and self-documenting.

---

## Future Considerations

These were considered but deferred:

1. **MCP Server Integration**: Could provide tools for project management. Deferred until clearer use case emerges.

2. **Cross-Project Sync**: Keeping multiple projects' patterns in sync. Complex coordination problem.

3. **Version Migration**: Updating projects when best practices change. Need real usage patterns first.

4. **Team Features**: Shared conventions across team members. Scope creep for v1.

---

## Decision 8: Adopting Spec-Driven Development as Foundational Methodology

### Context

Spec-driven development (SDD) has emerged as an industry standard for AI-assisted development in 2025:
- GitHub Spec Kit: 59K+ stars, tool-agnostic 4-phase workflow
- Kiro (AWS): IDE with specs built-in
- BMAD Method: Multi-agent lifecycle management
- Agent Skills: Now an open standard (agentskills.io), adopted by OpenAI

The question: Should this project remain narrowly "Claude Code-specific" or align with industry best practices?

### Alternatives Considered

| Approach | Pros | Cons |
|----------|------|------|
| **Stay Claude Code-specific** | Deep expertise, clear scope | May age poorly, fights standardization |
| **Become tool-agnostic SDD resource** | Broader audience | Loses depth, duplicates Spec Kit |
| **Adopt SDD methodology, Claude Code implementation** | Industry-aligned, maintains depth | Requires reframing existing content |

### Decision: Adopt SDD as Methodology, Claude Code as Primary Implementation

**This repository documents AI-driven development best practices**, using Claude Code as the primary implementation context. We adopt industry-standard SDD principles rather than treating them as external.

### Core Methodology (Aligned with Spec Kit)

The 4-phase model applies to all significant work:

| Phase | Purpose | Claude Code Implementation |
|-------|---------|---------------------------|
| **Specify** | Define what to build | CLAUDE.md, requirements in specs/ |
| **Plan** | Technical design | Architecture docs, design decisions |
| **Tasks** | Break down work | Structured task lists, TodoWrite |
| **Implement** | Execute with context | Skills, hooks, one feature at a time |

### What This Means for Content

**Reframe existing patterns as SDD implementations:**
- `long-running-agent.md` → SDD's external artifacts pattern in Claude Code
- `context-engineering.md` → How specs become deterministic context
- `memory-architecture.md` → Living documentation pattern
- `documentation-maintenance.md` → ARCH/PLAN/INDEX as spec artifacts

**Elevate Spec Kit, BMAD, Kiro from "sources to monitor" to "aligned standards":**
- GitHub Spec Kit: Reference implementation of 4-phase model
- BMAD: Reference for multi-agent patterns
- Kiro: Reference for IDE-integrated specs

### Evidence Tier Alignment

| Source | Previous Tier | New Tier | Rationale |
|--------|---------------|----------|-----------|
| GitHub Spec Kit | B (secondary) | A (standard) | 59K stars, industry adoption |
| Kiro (AWS) | B (secondary) | B (major vendor) | AWS official, emerging |
| BMAD Method | C (community) | B (validated) | Production use, MIT licensed |
| agentskills.io | - | A (specification) | Open standard, multi-vendor |

### Staying Current: Review Cadence

| Source Type | Frequency | Action |
|-------------|-----------|--------|
| Anthropic Engineering Blog | Weekly | Incorporate immediately |
| Spec Kit / agentskills.io | Weekly | Align with spec changes |
| SDD frameworks (BMAD, Kiro) | Monthly | Adopt proven patterns |
| Community resources | Monthly | Validate and incorporate |

### Trade-offs Accepted

1. **Broader scope** requires more maintenance, but aligns with industry direction
2. **Less Claude Code-specific** but patterns still use Claude Code as primary example
3. **Adopting external methodology** rather than inventing our own, but standing on proven foundations

### Migration Path

Existing patterns remain valid—they implement SDD principles. New content should:
1. Reference the phase it supports (Specify/Plan/Tasks/Implement)
2. Show Claude Code implementation of cross-platform patterns
3. Acknowledge when patterns work across tools

---

## Decision: Rename SETUP-PROJECT.md → MAKE-PROJECT-RECOMMENDATIONS.md (2026-03)

### Context

The file's purpose is to analyze a project and recommend appropriate infrastructure tier, not just "set up" a project.

### Decision

Rename to MAKE-PROJECT-RECOMMENDATIONS.md to better reflect its role:
- Analyzes project characteristics
- Recommends tier based on needs
- Guides through setup (but recommendation is the value)

### Alternatives Considered

| Name | Pros | Cons |
|------|------|------|
| RECOMMEND-INFRASTRUCTURE.md | Accurate | Too narrow, doesn't convey setup guidance |
| GUIDED-SETUP.md | Conveys interactivity | Doesn't convey the recommendation aspect |
| SETUP-WIZARD.md | Playful, clear | Too informal for professional context |
| **MAKE-PROJECT-RECOMMENDATIONS.md** | Accurately describes AI's role | Slightly longer name |

### Why This Name

"Make recommendations" accurately describes what the AI does: it analyzes, recommends, and then guides implementation. The emphasis is on intelligent recommendation, not just mechanical setup.

---

## Decision: Reframe Tier 2 as Recommended Baseline (2026-03)

### Context

Users were confused by Tier 1 being called "Baseline", thinking it was the standard starting point. This led to projects missing CLAUDE.md context management, causing:
- Context loss across sessions
- Repeated explanations of project structure
- Inconsistent behavior

### Decision

Reframe tier language to set correct expectations:
- **Tier 1: Minimal** (not "Baseline") - Optional lightweight fallback
- **Tier 2: Active (Recommended Baseline)** - Starting point for most projects
- **Tier 3: Team** - Collaborative projects

### Data Supporting This

| Source | Evidence |
|--------|----------|
| Boris Cherny (Claude Code creator) | Uses CLAUDE.md in all active projects |
| Anthropic official docs | Recommends CLAUDE.md ~60 lines as standard |
| User feedback | Projects without CLAUDE.md lose context across sessions |
| Pattern analysis | 28 of 34 patterns reference CLAUDE.md as foundation |

### Why This Framing

Sets correct expectations: Tier 2 should be default, Tier 1 is the exception. The language now matches the actual recommended practice rather than implying all projects should start minimal.

### Trade-offs Accepted

Some projects may still choose Tier 1 for minimal overhead, but they'll do so with clear understanding of what they're giving up (context management).

---

## Decision: Simplify from Tiers to Single Recommended Setup (2026-03-06)

### Context
After implementing "Tier 2 as Recommended Baseline" decision, realized the tier numbering system itself creates unnecessary complexity and decision fatigue.

### Problem with Tiers

**Decision paralysis**: "Which tier do I need?" question creates friction
- Users hesitate to adopt because they're unsure which tier is "right"
- False hierarchy: Numbers imply "higher = better"
- Mismatch with reality: 95% of projects need same setup (what was Tier 2)

**Ambiguity**: "Tier" used for 4 different systems
- Infrastructure tiers (1-4): Project setup components
- Evidence tiers (A-D): Source quality classification
- Confidence tiers (1-5): Pattern certainty scoring
- Skill tiers (1-3): Skill complexity levels

### Alternatives Considered

| Approach | Pros | Cons |
|----------|------|------|
| **Keep 4 tiers** | Granular choice, familiar | Decision fatigue, false hierarchy |
| **3 tiers** (combine 1+2) | Simpler than 4 | Still numbered, still tiered |
| **2 options** (basic/advanced) | Clear dichotomy | Loses nuance for teams/docs |
| **Single setup + options** | No decision paralysis | Less granular (but most projects don't need granularity) |

### Decision: Single Recommended Setup + Optional Advanced Features

**New model**:
```
Standard Setup (15-30 min) - ALL PROJECTS
  ├─ CLAUDE.md (~60 lines)
  ├─ Stop hook (prevent lost work)
  ├─ SessionStart hook (show git status)
  └─ Permission rules (pre-approve safe commands)

Advanced (optional):
  ├─ GitHub Actions (if team)
  └─ Version tracking (if docs project)
```

**Why this works**:
- Removes "which tier?" decision - there's one recommended path
- Matches actual usage - 95% of projects install Tier 2 anyway
- Advanced features presented AFTER standard setup, not as choice upfront
- Eliminates confusion between infrastructure tiers and evidence/confidence tiers

### Implementation

**Changed files**:
- README.md Quick Start → Single "Recommended Setup" section
- patterns/project-infrastructure.md → "Recommended Setup" + "Advanced Patterns"
- QUICKSTART.md → One setup path, advanced features at bottom
- prompts/MAKE-PROJECT-RECOMMENDATIONS.md → Install standard, then ask about advanced

**Preserved**:
- Evidence tiers (A-D) still used for source classification
- Confidence scoring (1-5) still used for pattern certainty
- Skill tiers (1-3) still used for complexity levels

### Data Supporting This

| Observation | Evidence |
|-------------|----------|
| Most projects need same setup | User feedback: "I thought Tier 1 was standard, missed CLAUDE.md benefits" |
| Decision fatigue | Support questions: "Should I use Tier 1 or 2?" (answer: 2) |
| Boris Cherny uses in all projects | Creator of Claude Code uses CLAUDE.md + hooks in all active projects |
| Tier numbering confusing | Multiple tier systems (infrastructure, evidence, confidence) cause ambiguity |

### Trade-offs Accepted

**Drawback**: Some users want minimal overhead (just Stop hook)
**Mitigation**: FAQ addresses this - recommended setup IS minimal (~60 lines in CLAUDE.md, 15-30 min setup)

**Drawback**: External links may reference "Tier 2"
**Mitigation**: Add note to DEPRECATIONS.md explaining tier language removed

### Impact

- Simpler mental model: one clear path for 95% of projects
- Reduced friction: no decision about which tier
- Less ambiguity: "tier" now only for evidence/confidence systems
- Better matches reality: most projects need CLAUDE.md + hooks

---

## Decision: Remove Infrastructure Tier Language (2026-03-06)

### Context
The Tier 1/2/3/4 infrastructure system created false hierarchy and decision paralysis. 95% of projects need the same setup (what was Tier 2).

### Decision
Replace numbered tiers with single recommended setup (CLAUDE.md + hooks + permissions) + optional advanced features (GitHub Actions, Version Tracking).

### Impact
- Simpler mental model, reduced decision fatigue
- Clearer that one path works for most projects
- Files changed: README.md, patterns/project-infrastructure.md, QUICKSTART.md, prompts/MAKE-PROJECT-RECOMMENDATIONS.md, cross-references

### Note
Evidence tiers (A-D), confidence scoring (1-5), and skill tiers (1-3) still use tier language — only infrastructure tiers were removed.

---

## Decision: Reposition as Analytical Layer — v2.0 (2026-03)

### Context

By March 2026, the repo had grown to 36 patterns that increasingly overlapped with everything-claude-code (110K+ stars, 125+ skills) and superpowers (disciplined methodology). Maintaining differentiation through more patterns was unsustainable.

### Alternatives Considered

| Approach | Pros | Cons |
|----------|------|------|
| **Continue adding patterns** | Familiar, incremental | Duplication with ECC, maintenance burden |
| **Merge into ECC** | Larger audience | Loses evidence-based analytical focus |
| **Reposition as analytical layer** | Unique niche, sustainable | Requires archiving 24 patterns |

### Decision: Reposition as Evidence-Based Analytical Layer

Archive 24 v1 patterns to `archive/patterns-v1/` and focus on 14 analysis documents that provide insights absent from ECC and superpowers:

- Evidence tier classification system (A-D + 1-5)
- Quantified behavioral insights (~80% CLAUDE.md adherence, 60% context threshold)
- Comparative analysis (MCP vs Skills economics, orchestration approaches)
- Security analysis with OWASP mapping

### Three-Project Ecosystem

| Project | Role |
|---------|------|
| **everything-claude-code** | Batteries-included tooling |
| **superpowers** | Disciplined methodology |
| **This project** | Evidence-based analysis |

### Trade-offs Accepted

- 24 patterns archived (preserved, not deleted)
- Narrower scope, but defensible differentiation
- Requires ongoing source monitoring to stay current

---

## Decision: Expand to 26 Analysis Documents — v2.1 (2026-04)

### Context

After v2.0 repositioning, 10 gap areas were identified where real production evidence from a 7-repo portfolio (third-brain, mndr-review-automation, health-inventory, zeek-iceberg-demo, network-visualization-services, Splunk-db-connect-benchmark, tme-mcp-server) could fill analytical gaps not covered by any existing resource.

### Alternatives Considered

| Approach | Pros | Cons |
|----------|------|------|
| **Stay at 14 docs** | Minimal maintenance | Misses unique portfolio evidence |
| **Add 2-3 high-priority docs** | Focused expansion | Leaves 7 gaps undocumented |
| **Document all 10 gaps** | Complete coverage of available evidence | Larger maintenance surface |

### Decision: Document All 10 Gap Areas (14 → 26 documents)

Each gap had Tier A evidence from direct production observation that was unavailable elsewhere. The 12 new documents:

| Document | Unique Evidence |
|----------|----------------|
| harness-engineering.md | Harness diagnostic framework + infrastructure patterns |
| domain-knowledge-architecture.md | Domain knowledge encoding for LLM-assisted development |
| agent-driven-development.md | 7-repo portfolio: 10-100% co-authoring, infrastructure maturity model |
| local-cloud-llm-orchestration.md | Hybrid MLX+Claude: tokenization boundary, 7 hallucination scrubbers |
| mcp-client-integration.md | Two MCP architectures: structured tools vs orchestrated playbooks |
| federated-query-architecture.md | 15/15 benchmarks, 86-99% cost savings vs Splunk |
| automated-config-assessment.md | Baseline-deviation-remediation, 3,816+ sensors, 100% detection |
| claude-md-progressive-disclosure.md | 3-tier CLAUDE.md evolution, ~150 instruction budget |
| memory-system-patterns.md | Auto-memory sizing by project type across 5 projects |
| evidence-based-revalidation.md | Hypothesis confidence tracking with remaining gaps |
| security-data-pipeline.md | Zeek → OCSF → Parquet → Iceberg, 30K records/sec |
| cross-project-synchronization.md | 4-phase enrichment cascade, dynamic importlib, cron monitoring |

### Data Supporting This

- All 12 documents grounded in real code with specific file paths, function signatures, and measured values
- 100% source attribution with revalidation dates
- Cross-referenced bidirectionally with existing analysis docs
- No overlap with ECC or superpowers content

### Trade-offs Accepted

- Larger maintenance surface (26 vs 14 docs)
- All measurement claims require revalidation every 6 months
- Some documents are domain-specific (security data pipeline, config assessment) — acceptable because they demonstrate Claude Code patterns, not just domain knowledge

---

*Last updated: April 2026*
