# Community Resources Directory

**Last Updated**: February 27, 2026

---

## Purpose

This project is a **meta-guide** that curates and enhances community Claude Code resources. We point to community leaders for tool recommendations and implementation details, while providing:

1. **Evidence tier assessment** - Evaluate quality and maturity of community resources
2. **Integration guidance** - Decision matrices for choosing between resources
3. **Deprecation tracking** - Monitor community resources for staleness or breaking changes
4. **Gap analysis** - Identify areas not covered by community
5. **Unique methodology** - SDD, evidence tiers, measurement discipline

**We defer to community consensus where it exists.**

---

## Active Community Projects

### 🏆 Tier A: Highly Recommended

#### 1. shanraisshan/claude-code-best-practice
**URL**: https://github.com/shanraisshan/claude-code-best-practice
**Stars**: 5.6k+
**Focus**: Tools, MCPs, productivity tips, quick-start guides

**What they do best**:
- Tool discovery (MCPs, extensions, integrations)
- Quick tips and workflow optimizations
- Community-curated recommendations
- Fast updates as ecosystem evolves

**What we add**:
- Evidence tier validation of their recommendations
- Context budget analysis for tool choices
- Deprecation tracking (e.g., Claude in Chrome → Playwright)
- Integration with SDD methodology

**When to use**:
- Looking for tool recommendations
- Want quick productivity wins
- Exploring the MCP ecosystem
- Need community validation

---

#### 2. obra/superpowers
**URL**: https://github.com/obra/superpowers
**Focus**: Production-grade TDD, debugging, orchestration skills

**What they do best**:
- Strict TDD enforcement (RED-GREEN-REFACTOR)
- Systematic debugging frameworks
- Multi-agent orchestration patterns
- Production-ready skill implementations

**What we add**:
- Lightweight learning alternatives (tdd-enforcer, systematic-debugger skills)
- Integration with Claude Code's native skill system
- SDD methodology integration
- Evidence tier assessment

**When to use**:
- Production projects requiring strict TDD
- Complex debugging scenarios
- Advanced orchestration needs
- Want battle-tested frameworks

---

#### 3. Claude.com Official Plugin Directory
**URL**: https://claude.com/plugins
**Focus**: Official plugin registry and discovery

**What they do best**:
- Authoritative plugin catalog
- Security and quality vetting
- Installation instructions
- Plugin compatibility information

**What we add**:
- Decision matrix (Skills vs MCP vs Hooks vs Plugins)
- Token efficiency analysis
- Economics comparison (50% cost difference for skills vs MCPs)
- Integration patterns

**When to use**:
- Looking for vetted extensions
- Want official support
- Need security guarantees
- Installing plugins for first time

---

### 🎯 Tier B: Specialized Resources

#### 4. Anthropic Engineering Blog
**URL**: https://www.anthropic.com/engineering
**Focus**: Vendor features, advanced techniques, research

**What they do best**:
- Authoritative feature documentation
- Beta feature announcements
- Token efficiency research
- Measurement data (e.g., 85% reduction with tool search)

**What we add**:
- Local Claude Code examples
- SDD integration for new features
- Production validation of claims
- Cross-reference with community patterns

**When to use**:
- Learning new features (tool search, programmatic calling)
- Need authoritative measurements
- Tracking beta features
- Understanding architectural decisions

---

#### 5. valgard (Dev.to)
**URL**: https://dev.to/valgard/claude-code-must-haves-january-2026-kem
**Focus**: MCP context budget analysis, production measurements

**What they do best**:
- Real-world context budget measurements
- Production MCP recommendations
- Performance analysis

**What we add**:
- Ongoing revalidation (quarterly)
- Integration with context engineering patterns
- Maturity assessment (EMERGING → PRODUCTION)

**When to use**:
- Optimizing MCP selection
- Understanding context budget impact
- Production deployment decisions

---

## Decision Matrix: Which Resource When?

| Need | Primary Resource | This Project's Role | Why Split This Way |
|------|-----------------|---------------------|-------------------|
| **Tool Discovery** | shanraisshan | Evidence tiers, deprecation tracking | Community maintains tool lists faster |
| **MCP Recommendations** | shanraisshan + valgard | Context budget analysis, maturity assessment | Community discovers, we validate |
| **TDD Enforcement** | obra/superpowers | Lightweight learning alternatives | They enforce, we teach |
| **Debugging Frameworks** | obra/superpowers | Integration with Claude Code skills | Production vs learning contexts |
| **Plugin Discovery** | claude.com/plugins | Economics analysis, decision matrix | Official directory, we help choose |
| **Vendor Features** | Anthropic blog | Local examples, SDD integration | They document, we contextualize |
| **Production Patterns** | This project | - | Unique: SDD, evidence tiers, measurements |

---

## What This Project Uniquely Provides

### 1. Evidence Tier System
**No community equivalent**

Dual-tier framework for assessing claim quality:
- **Document tiers** (A-D): Source authority
- **Measurement tiers** (1-5): Claim specificity with revalidation dates

See: [evidence-tiers.md](patterns/evidence-tiers.md)

---

### 2. Spec-Driven Development (SDD) Methodology
**No community equivalent**

4-phase model (Specify → Plan → Tasks → Implement) adapted for Claude Code with:
- Practical implementation guidance
- Integration with native Claude Code features
- Multi-session continuity patterns

See: [spec-driven-development.md](patterns/spec-driven-development.md)

---

### 3. Context Engineering Deep Analysis
**No community equivalent**

Mathematical analysis of context budget with:
- Deterministic vs probabilistic context strategies
- "Correctness Over Compression" principle
- Production patterns for 200K token budgets

See: [context-engineering.md](patterns/context-engineering.md)

---

### 4. Security Frameworks for AI Agents
**No community equivalent**

Applied OWASP principles to AI coding agents:
- 7 MCP failure modes with mitigations
- STRIDE threat modeling for skills
- OS-level sandboxing patterns

See: [mcp-patterns.md](patterns/mcp-patterns.md), [secure-code-generation.md](patterns/secure-code-generation.md)

---

### 5. Measurement Discipline
**No community equivalent**

Quantified claims with expiry dates across 23+ patterns:
- Revalidation tracking
- Maturity promotion criteria (EMERGING → PRODUCTION)
- Evidence quality assessment

Example: "Context7 + Sequential Thinking: 25K tokens (12.5% of context) - revalidate 2027-01-01"

---

### 6. Advanced Orchestration Patterns
**Partial community overlap**

10 advanced subagent patterns beyond vendor docs:
- Fresh context per subagent
- State externalization patterns
- Multi-agent coordination

See: [subagent-orchestration.md](patterns/subagent-orchestration.md), [gsd-orchestration.md](patterns/gsd-orchestration.md)

---

### 7. Integration Guidance
**No community equivalent**

Decision matrices and comparative frameworks:
- Skills vs MCP vs Hooks vs Commands (when to use what)
- Framework selection (Native vs GSD vs CAII)
- Tool ecosystem comparisons (Claude Code vs alternatives)

See: [plugins-and-extensions.md](patterns/plugins-and-extensions.md), [framework-selection-guide.md](patterns/framework-selection-guide.md)

---

## Maintenance Philosophy

### How We Track Community Resources

#### Quarterly Review Process
Every 90 days:
1. **Validate links** - Ensure community resources still exist
2. **Check freshness** - Compare update dates, flag stale resources
3. **Revalidate recommendations** - Have "top tools" changed?
4. **Track breaking changes** - MCP deprecations, API changes
5. **Update evidence tiers** - Promote or demote based on validation

See: [QUARTERLY-REVIEW.md](QUARTERLY-REVIEW.md)

#### Deprecation Tracking
We monitor community resources for:
- **Link rot** - Resources going offline
- **Outdated recommendations** - Tools superseded by better alternatives
- **Breaking changes** - API changes affecting documented patterns
- **Security issues** - Vulnerabilities in recommended tools

Example: Tracked "Claude in Chrome" deprecation (2026-01-10) and provided Playwright migration path.

See: [DEPRECATIONS.md](DEPRECATIONS.md)

---

## Community Coordination

### How to Report Issues

**Found a broken link or outdated recommendation?**
1. Open issue: https://github.com/flying-coyote/claude-code-project-best-practices/issues
2. Label: `community-resource`
3. Include: Resource name, issue description, suggested fix

**Discovered new community resource?**
1. Check evidence tier criteria ([evidence-tiers.md](patterns/evidence-tiers.md))
2. Assess maturity (EMERGING vs PRODUCTION)
3. Submit PR or open issue with assessment

---

## Acknowledgments

This meta-guide exists because these projects share openly:

- **shanraisshan** - Maintaining comprehensive tool directory, fast community pulse
- **obra** - Production-grade skill implementations, TDD enforcement
- **valgard** - Context budget research, real-world measurements
- **Anthropic** - Transparent engineering blog, beta feature access

We stand on the shoulders of giants. Our role: curate, validate, integrate.

---

## Related Documentation

- [SOURCES.md](SOURCES.md) - Full source database with evidence tiers
- [SOURCES-QUICK-REFERENCE.md](SOURCES-QUICK-REFERENCE.md) - Top 20 Tier A/B sources
- [ARCHITECTURE.md](ARCHITECTURE.md) - Project philosophy and meta-guide approach
- [evidence-tiers.md](patterns/evidence-tiers.md) - Evidence tier assessment framework

---

*This directory maintained through quarterly review process. Last review: February 27, 2026*
