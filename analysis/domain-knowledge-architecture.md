---
version-requirements:
  claude-code: "v2.1.0+"
version-last-verified: "2026-03-30"
measurement-claims:
  - claim: "CLAUDE.md instructions followed ~80% of the time"
    source: "Boris Cherny (March 2026)"
    date: "2026-03-01"
    revalidate: "2026-09-01"
  - claim: "Skills consume ~2% of context budget each"
    source: "Anthropic documentation"
    date: "2026-03-19"
    revalidate: "2026-09-19"
  - claim: "Quality degrades at 60% context capacity"
    source: "Boris Cherny (March 2026)"
    date: "2026-03-01"
    revalidate: "2026-09-01"
  - claim: "CLAUDE.md performance degrades beyond ~150 instructions"
    source: "Boris Cherny (March 2026)"
    date: "2026-03-01"
    revalidate: "2026-09-01"
  - claim: "MCP servers add 300-800ms baseline latency"
    source: "MCP patterns analysis"
    date: "2026-03-01"
    revalidate: "2026-09-01"
status: PRODUCTION
last-verified: "2026-03-30"
evidence-tier: Mixed
applies-to-signals: [project-type-domain-heavy, vault-genealogy]
revalidate-by: 2026-09-30
---

# Domain Knowledge Architecture: Making Expertise Findable Without Overwhelming Context

**Evidence Tier**: Mixed (A-B) — Synthesized from Anthropic guidance, Manus patterns, behavioral insights, and production validation

## Purpose

This document addresses a fundamental tension in domain-heavy projects: **the LLM needs domain expertise to solve problems correctly, but loading that expertise into context degrades performance on the actual task.**

This is the companion document to [Harness Engineering](./harness-engineering.md), focused specifically on the domain knowledge layer of the harness stack.

---

## The Problem

Complex engineering domains — security rule ecosystems, infrastructure-as-code, regulatory compliance, scientific computing, financial modeling — share three interrelated failure modes:

### 1. Discovery Failure

The LLM doesn't know what resources exist. It reinvents solutions instead of reusing existing rules, scripts, patterns, or utilities. The codebase has the answer, but the LLM doesn't know where to look.

**Observable symptoms**:

- Agent writes new utility functions when the codebase already has them
- Agent creates rules/patterns that duplicate existing coverage
- Agent proposes approaches that ignore established project conventions
- Different sessions produce fundamentally different solutions to the same problem

### 2. Context Saturation

Loading enough domain knowledge to be useful fills too much of the context window, degrading quality on the actual task. The 60% context capacity threshold ([Behavioral Insights](./behavioral-insights.md)) means domain knowledge competes directly with working context.

**Observable symptoms**:

- Quality degrades as the session progresses
- Agent loses track of the original objective after exploring domain references
- Token costs escalate without proportional quality improvement
- Auto-compaction fires mid-task, losing domain context

### 3. Methodology Inconsistency

Without enforced methodology, different sessions and different team members get wildly different approaches. The LLM has no consistent framework for *how* to apply domain knowledge, even when it can find it.

**Observable symptoms**:

- Senior developers get better results than juniors (knowledge in heads, not infrastructure)
- Same task produces different approaches on different days
- No standard validation steps for domain-specific outputs
- Code review catches basic methodology errors that should be enforced

---

## The Progressive Disclosure Stack

The solution is not "load everything" or "load nothing." It's **progressive disclosure** — make domain knowledge available in layers, each loading only when needed, at the right context cost.

| Layer | Mechanism | What It Contains | When It Loads | Context Cost |
|-------|-----------|-----------------|---------------|-------------|
| **Always-on** | CLAUDE.md | Project purpose, key commands, resource map | Every session | ~60 lines (minimal) |
| **Path-triggered** | `.claude/rules/` | Domain-specific conventions per file type | When working with matching files | Per-file, on demand |
| **On-demand** | Skills | Methodology for specific task types | When task matches skill description | ~2% context each |
| **Lookup** | MCP servers | Live access to databases, APIs, registries | When explicitly called | Per-query |
| **External memory** | File system | Reference docs, catalogs, prior decisions | When agent reads specific files | Per-read |
| **Deep dive** | Subagents | Specialized investigation in fresh context | When delegated | Zero main context cost |

### Why This Works

This mirrors the pattern that Manus discovered independently — **file system as external memory**. And it's why Claude Code's 4-tool design (read, write, edit, bash) works: the tools let the LLM **pull** context on demand rather than having it **pushed** into the context window.

The Vercel experiment confirms the principle from the other direction: removing specialized tools that pushed context and replacing them with general-purpose tools that let the model pull what it needed improved accuracy from 80% to 100%.

---

## The Resource Map Pattern

**This is the core recommendation for domain-heavy projects.**

Instead of loading domain knowledge into CLAUDE.md or skills, maintain a **resource map** — a lightweight index that tells the LLM *where to look*, not *what the answer is*.

### What a Resource Map Contains

```markdown
## Project Resources

### Detection Rules
- **Location**: rules/ (organized by protocol)
- **Lookup**: grep rules/ for existing coverage before creating new rules
- **Conventions**: see .claude/rules/detection-rules.md (auto-loads when editing rule files)
- **Validation**: run `make validate-rules` before committing

### Analysis Scripts
- **Location**: scripts/analysis/ (organized by data source)
- **Lookup**: ls scripts/analysis/ to see available analyzers
- **When to use**: data extraction, log parsing, report generation

### Configuration Templates
- **Location**: config/templates/
- **Reference docs**: docs/configuration-guide.md
- **Validation**: run `make validate-config`

### External Resources
- **Threat intel**: accessible via MCP (threat-intel-server)
- **Rule database**: query via MCP (rule-db-server) for coverage gaps
- **Team decisions**: docs/decisions/ (ADR format)
```

### Why Resource Maps Work

1. **Small footprint**: Fits in CLAUDE.md's ~60-line budget or a referenced file
2. **Points, doesn't contain**: The map tells the LLM where to find knowledge, not what the knowledge is
3. **Enables pull, not push**: The LLM uses Read, Grep, or MCP to fetch only what it needs
4. **Self-updating**: File paths and MCP endpoints stay current as the project evolves
5. **Team-consistent**: Every session and every team member starts with the same map

### Where to Put the Resource Map

| Approach | When to Use |
|----------|------------|
| Inline in CLAUDE.md | Small projects, <10 resource categories |
| Referenced file (`@docs/resource-map.md`) | Medium projects, resource map would bloat CLAUDE.md |
| SessionStart hook that generates map | Dynamic projects where resources change frequently |

---

## Path-Scoped Rules for Domain Conventions

For ecosystems with distinct file types or directories, `.claude/rules/` with path frontmatter provides **zero-cost context until the LLM actually touches matching files**.

### Structure

```markdown
<!-- .claude/rules/suricata-rules.md -->
---
paths:
  - "rules/**/*.rules"
  - "**/*.sid"
---

When working with Suricata rules:
- Check existing rules in rules/ before creating new ones
- Follow the SID allocation scheme in docs/sid-ranges.md
- Validate with `suricata -T -c suricata.yaml -S <rulefile>`
- Reference: docs/rule-writing-guide.md for syntax conventions
- Performance: avoid PCRE when content matches suffice
```

```markdown
<!-- .claude/rules/zeek-scripts.md -->
---
paths:
  - "scripts/**/*.zeek"
  - "**/*.bro"
---

When working with Zeek scripts:
- Check scripts/packages/ for existing analyzers before writing new ones
- Follow naming conventions in docs/zeek-style-guide.md
- Test with `zeek -r sample.pcap scripts/your-script.zeek`
- Log format: use Zeek's logging framework, not print statements
```

```markdown
<!-- .claude/rules/yara-rules.md -->
---
paths:
  - "yara/**/*.yar"
  - "**/*.yara"
---

When working with YARA rules:
- Check yara/ for existing rules covering similar malware families
- Follow naming: <malware_family>_<variant>_<description>.yar
- Validate with `yara -w <rulefile> <testfile>`
- Reference: docs/yara-best-practices.md
- Include: rule metadata (author, date, description, reference)
```

### Key Insight

Path-scoped rules load **only** when the LLM touches matching files. For a project with 6 domain areas, only the relevant rules load — not all 6. This is the progressive disclosure pattern applied to conventions.

### Rules vs Skills vs CLAUDE.md

| Content Type | Mechanism | Loads When | Context Cost |
|-------------|-----------|-----------|-------------|
| Universal project conventions | CLAUDE.md | Every session | Always-on (~60 lines) |
| File-type-specific conventions | `.claude/rules/` | Touching matching files | On-demand (per-rule) |
| Task-type methodology | Skills | Task matches description | ~2% per skill |
| Reference documentation | File system | Explicitly read | Per-read |

---

## MCP for Live Domain Lookups

When domain knowledge lives in external systems, MCP servers provide live lookup without pre-loading.

### When to Use MCP vs File-Based Lookups

| Data Characteristic | Use MCP | Use File-Based |
|--------------------|---------|---------------|
| Changes frequently (daily/weekly) | Yes | No |
| Too large to maintain locally | Yes | No |
| Requires authentication/API access | Yes | No |
| Stable, manageable size | No | Yes (much faster) |
| Needs to work offline | No | Yes |

### Example Use Cases

| Need | MCP Approach | File-Based Alternative |
|------|-------------|----------------------|
| "What rules already cover this threat?" | Query rule database via MCP | `grep -r` the rules/ directory |
| "Is this identifier already allocated?" | Query registry via MCP | Maintain local allocation file |
| "What's the current detection coverage?" | Dashboard API via MCP | Periodic export to markdown |
| "What threat intel exists for this IOC?" | Threat intel API via MCP | No good alternative — use MCP |
| "What's the syntax for this rule keyword?" | Not needed — file-based | docs/syntax-reference.md |

**Decision principle**: Use MCP for data that is dynamic or authoritative-at-source. Use file-based lookups for stable reference material. MCP adds 300-800ms latency per call — acceptable for lookups, unacceptable for high-frequency access.

---

## Skills for Domain Methodology

Skills encode *how* to approach domain-specific tasks — the methodology, not the reference material.

### What Goes in a Skill vs What Doesn't

| Content | In the Skill | In Referenced Files |
|---------|-------------|-------------------|
| Step-by-step workflow | Yes | No |
| Decision criteria | Yes | No |
| Validation commands | Yes | No |
| Syntax reference | No | Yes (docs/) |
| Complete rule examples | No | Yes (examples/) |
| API documentation | No | Yes (docs/) or MCP |

### Example Domain Skill

```yaml
---
name: detection-engineering
description: |
  Methodology for creating or modifying detection rules.
  Trigger: working with rule files, threat detection, alert tuning.
paths:
  - "rules/**"
  - "detections/**"
---

## Detection Engineering Workflow

1. **Check existing coverage**
   - grep rules/ for signatures related to the threat
   - Review docs/coverage-matrix.md for documented gaps

2. **Assess detection approach**
   - Network signature (Suricata) vs behavioral (Zeek) vs file-based (YARA)
   - See docs/detection-approach-guide.md for decision criteria

3. **Write rule following conventions**
   - Conventions auto-load from .claude/rules/ when editing rule files
   - Reference docs/rule-writing-guide.md for syntax

4. **Validate**
   - Run `make validate-rules` for syntax checking
   - Test against sample data in test-data/

5. **Document**
   - Add detection rationale to the rule metadata
   - Update docs/coverage-matrix.md if filling a gap
```

### Why Skills, Not CLAUDE.md

- **Skills load on demand** (~2% context each, only when relevant)
- **CLAUDE.md loads every session** (always-on cost)
- **Path-scoped skills** load only when touching matching files
- **Skills can be hot-reloaded** (v2.1.0+) during iterative development

### Skill Budget

| Guideline | Threshold | Source |
|-----------|----------|--------|
| Max skill file size | 500 lines | Anthropic documentation |
| Context cost per skill | ~2% of context window | Anthropic documentation |
| Recommended active skills | 1-3 per task | Derived from context budget |

If a skill exceeds 500 lines, it's trying to be a reference document. Split the methodology from the reference material.

---

## Diagnostic Framework: Why Can't My LLM Find the Right Resources?

| Symptom | Diagnosis | Solution Pattern | Implementation |
|---------|-----------|-----------------|----------------|
| LLM writes new code when existing utility exists | No resource map | Create resource map | List resource categories + locations in CLAUDE.md or referenced file |
| LLM uses wrong conventions for domain files | No path-scoped rules | Add `.claude/rules/` | One rule file per domain area with path frontmatter |
| LLM doesn't follow consistent methodology | No domain skills | Create methodology skills | Workflow steps + validation, not reference docs |
| LLM loads too much context understanding domain | Skills too large or too many | Enforce skill budget | Keep under 500 lines; move reference to external files |
| LLM can't access live domain data | No MCP integration | Add MCP for dynamic lookups | Only for truly dynamic or externally-authoritative data |
| LLM gives different approaches each session | No enforced methodology | Skill (methodology) + hook (enforcement) | Hook validates outputs match methodology |
| Domain knowledge stale in CLAUDE.md | Static instructions | Dynamic context injection | Use `!command` in skill frontmatter or MCP for live data |
| New team members' LLMs miss conventions | Knowledge in people, not infrastructure | Encode in harness | rules/ + skills + resource map, all in `.claude/` tracked in git |
| LLM uses outdated rule syntax | Reference docs not version-linked | Version-aware references | Include version constraints in rules; validate with tools |
| LLM doesn't validate domain outputs | No quality gate for domain work | Add domain-specific hooks | PostToolUse hook running domain validators |

---

## The Context Budget Framework

Practical allocation guidelines for domain-heavy projects:

| Budget Zone | Allocation | Contents | Overflow Action |
|-------------|-----------|----------|----------------|
| **Always-on** | ~5% | CLAUDE.md + resource map | If >5%, move content to referenced files |
| **Path-triggered** | ~10% | Rules matching current files | If >10%, consolidate rules; use broader path patterns |
| **On-demand** | ~15% | 1-3 active skills | If >15%, reduce active skills; use `disable-model-invocation` |
| **Working context** | ~70% | The actual task (code, files, tool results) | This is the protected zone — never sacrifice it |

### The 15% Rule

**If always-on + path-triggered + on-demand context exceeds ~15% of the context window, the harness is overloaded.**

Signs of overload:

- Auto-compaction fires before the task is complete
- Agent loses track of the task objective
- Quality degrades earlier than expected in the session
- Token costs are high relative to task complexity

### Recovery Steps

1. **Audit what's loaded**: Check CLAUDE.md line count, active rules, active skills
2. **Apply resource map pattern**: Replace inline knowledge with pointers
3. **Path-scope everything possible**: Rules and skills with `paths:` frontmatter
4. **Disable auto-triggering**: Use `disable-model-invocation: true` for skills that should only activate explicitly
5. **Move reference material out of skills**: Skills = methodology only; reference = external files

---

## Anti-Patterns

| Anti-Pattern | What It Looks Like | Why It Fails | Fix |
|-------------|-------------------|-------------|-----|
| **Encyclopedia CLAUDE.md** | 200+ line CLAUDE.md with all domain knowledge inline | Exceeds ~150 line cap; ~80% adherence degrades further with length | Resource map + skills + rules |
| **Eager loading** | Every domain skill loads every session regardless of task | Context bloat (each skill ~2%, 10 skills = 20%) | Path-scoping + `disable-model-invocation` |
| **MCP for everything** | MCP server for data that changes monthly | 300-800ms latency per call, token overhead | File-based for stable data; MCP only for dynamic |
| **Knowledge in heads** | Senior devs get good results, juniors don't | Knowledge isn't encoded in infrastructure | Encode as rules/ + skills + resource map in `.claude/` |
| **One giant skill** | 1000-line skill covering entire domain | Exceeds 500-line cap; loads unnecessary context | Split by task type with path-scoping |
| **Reference in skills** | Skill contains full syntax reference, API docs | Wastes ~2% context on rarely-needed reference | Skill = methodology only; reference = docs/ files |
| **No validation gate** | Domain outputs not automatically checked | Errors caught only in manual review | PostToolUse hook with domain-specific validators |

---

## Generalization: Applying to Any Complex Domain

While examples above use security engineering domains, the patterns apply to any domain-heavy project:

| Domain | Resource Map Contents | Path-Scoped Rules | Skills | MCP |
|--------|----------------------|-------------------|--------|-----|
| **Security (Suricata/Zeek/YARA)** | Rule directories, coverage matrix, threat intel | Per-rule-language conventions | Detection engineering workflow | Threat intel API, rule database |
| **Infrastructure (Terraform/K8s)** | Module registry, state locations, environment map | Per-provider conventions | Infrastructure change workflow | Cloud provider APIs, state backends |
| **Compliance (SOX/HIPAA/PCI)** | Control catalog, evidence locations, audit schedule | Per-regulation requirements | Compliance assessment workflow | Audit system API, evidence repository |
| **Scientific (data pipelines)** | Dataset catalog, model registry, experiment tracker | Per-framework conventions | Experiment workflow | Data warehouse, model serving API |
| **Financial (trading systems)** | Instrument catalog, risk models, regulatory constraints | Per-asset-class conventions | Trade validation workflow | Market data API, risk systems |

The pattern is always:

1. **Resource map** tells the LLM where to look
2. **Path-scoped rules** teach conventions when touching relevant files
3. **Skills** encode methodology for domain tasks
4. **MCP** provides live access to dynamic external data
5. **File system** serves as external memory for stable reference material

---

## Sources

### Tier A (Primary Vendor / Expert Practitioner)

- Boris Cherny: CLAUDE.md adherence (~80%), context thresholds (60%), instruction cap (~150 lines) — March 2026
- Anthropic: Skills documentation (2% context budget, 500-line cap), hooks reference, rules documentation
- Anthropic: ["Effective harnesses for long-running agents"](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) (November 2025)

### Tier B (Validated / Production)

- Manus: File system as external memory pattern — context engineering lessons (2025-2026)
- Vercel: Text-to-SQL experiment — general-purpose tools outperform specialized tools
- Prompt Engineering: ["The AI Model Doesn't Matter Anymore"](https://www.youtube.com/watch?v=1Ohf2aeSPFA) (February 2026)

### Related Analysis

- [Harness Engineering](./harness-engineering.md) — Umbrella concept, diagnostic framework, philosophy comparison
- [Behavioral Insights](./behavioral-insights.md) — Context thresholds, CLAUDE.md adherence, instruction processing
- [Plugins & Extensions](./plugins-and-extensions.md) — Extension mechanism selection (skills vs MCP vs hooks vs rules)
- [MCP vs Skills Economics](./mcp-vs-skills-economics.md) — Cost analysis for mechanism selection
- [Safety & Sandboxing](./safety-and-sandboxing.md) — Security constraints as domain knowledge

---

*Last updated: March 2026*
