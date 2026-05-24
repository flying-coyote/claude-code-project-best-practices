# Archive

**Purpose**: Completed work items and historical milestones
**Note**: Active work is tracked in [PLAN.md](PLAN.md)

---

## Completed Milestones

### v2.1 - Production Evidence Integration (April–May 2026)

- **Memory & knowledge stack archetypes** (April 28, 2026): split omnibus recommendations into 7 per-archetype docs (`memory-systems-archetype-{a..g}-*.md`) + methodology + graphify vs. understand-anything A/B testbed. Doc count 28 → 38. Empirical findings on Pass 2 LLM extraction (1187 nodes, 67 communities, ~25% hallucination spot-check on EXTRACTED edges).
- **Egress-constrained archetype reframe + genealogy baseline** (April 29, 2026): renamed Archetype C-PII → C-Egress-Constrained after reframing genealogy projects' egress posture. New empirical doc `memory-systems-genealogy-baseline.md` — 3 subagents × 3 queries × 3 projects, 8/9 DEFINITIVE on the unaugmented stack.
- **Memory testbed experiments** (May 2026): Experiment #1 expanded to 20 brick-wall memory files; dedicated brick-wall files collapsed Q2 from 6–9 reads to 3.
- **Quality refresh + consumer-trust pass** (May 24, 2026): URL canonicalization to `code.claude.com`; +4 verified Tier B sources (Builder.io, Morph, Shipyard, VoltAgent); backfilled `## Sources` footers across 16 analysis docs; inlined vendor-reported caveats on Tier C metrics; cross-linked 7-repo portfolio evidence into framework-selection and orchestration-comparison docs.

### v2.0 - Adaptive Routing + Opus 4.7 Integration (April 2026)

- **Adaptive routing protocol** (April 22, 2026): `AUDIT-CONTEXT.md` routing map from project signals to applicable analysis docs. Typical audit now fetches 4–8 of 28 docs, not the source index alone. `ONE-LINE-PROMPT.md` rewritten as 4-step flow; every recommendation cites the analysis doc + evidence tier.
- **Opus 4.7 migration evidence** (April 22, 2026): `analysis/model-migration-anti-patterns.md` cross-version anti-pattern matrix (4.5 → 4.6 → 4.7); six Vertrees anti-patterns mapped to Anthropic migration guide; behavioral-insights, harness-engineering, claude-md-progressive-disclosure, agent-evaluation, evidence-based-revalidation updated for 4.7.
- **7-repo portfolio analysis** (April 2026): added `analysis/agent-driven-development.md` with quantified evidence from 7 production repos (infrastructure maturity model, cross-repo coordination, security boundaries, velocity data — Nick Schrock's 1000+ PRs/3 weeks, Tenzir's 3x velocity claim).
- **9 new analysis docs covering identified gaps** (April 2026): local-cloud-llm-orchestration, mcp-client-integration, federated-query-architecture, automated-config-assessment, claude-md-progressive-disclosure, memory-system-patterns, evidence-based-revalidation, security-data-pipeline, cross-project-synchronization.

### v1.3 - Production Patterns Integration (December 13, 2025)
- Added production patterns from second-brain integration
- Completed multi-workflow refactoring documentation
- Added 5 new patterns:
  - planning-first-development.md
  - plugins-and-extensions.md
  - skills-domain-knowledge.md
  - spec-driven-development.md
  - subagent-orchestration.md
- Added hypothesis-validator skill example

### v1.2 - Self-Compliance (December 8, 2025)
- Repository now follows its own documented patterns
- Created meta-project infrastructure (.claude/)
- Added PostToolUse and Stop hooks
- Created INDEX.md automation
- Added security guidelines for skills
- Updated SKILL-TEMPLATE.md with Workflow Routing + Security
- Created ARCHITECTURE.md and PLAN.md
- Added 4 new patterns:
  - progressive-disclosure.md
  - advanced-hooks.md
  - documentation-maintenance.md
  - memory-architecture.md

### v1.1 - Nate B. Jones Patterns (December 7-8, 2025)
- Added Nate B. Jones patterns:
  - context-engineering.md
  - agent-principles.md
  - mcp-patterns.md
- Fixed broken URL in SOURCES.md
- Expanded SOURCES.md with article mapping

### v1.0 - Initial Release (November 2025)
- Initial patterns from Anthropic Engineering Blog
- Core skill structure and examples
- Basic template system
- 4 presets (coding, writing, research, hybrid)

---

## Completed Goals

### High Priority (All Complete)
- ✅ Validation: Test patterns on this repo itself
- ✅ Documentation: Ensure all patterns have examples
- ✅ Self-compliance: Repository follows its own patterns

### Medium Priority (Mostly Complete)
- ✅ Community: Accept contributions (CONTRIBUTING.md created)
- ⚠️ Examples: Update example projects (partially complete)

### Low Priority (Addressed)
- ✅ Automation: Hook patterns documented (3 hooks)

---

## Metrics at Archive Time

**v2.1 snapshot (May 24, 2026)**:

| Metric | v1 Target | v1 Achieved | v2.1 Current |
|--------|-----------|-------------|---------------|
| Analysis documents | — | — | **41** |
| Patterns documented (v1) | 10+ | **17** | (archived to `archive/patterns-v1/`) |
| Source database entries | — | — | **130+** |
| Source attribution | 100% | **100%** | **100%** (Sources footers across all 41 docs) |
| Self-compliance | 100% | **100%** | **100%** |
| Total documents (repo-wide) | — | **48** | tracked in INDEX.md |

---

## Deferred Items

These items were evaluated and consciously deferred:

| Item | Reason | Revisit When |
|------|--------|--------------|
| MCP server for pattern lookup | Requires design decisions (transport, operations, hosting) | When design is clarified |
| Video walkthrough | External infrastructure required | Out of scope |
| Fabric integration guide | Low priority (Tier C source) | Community demand |
| Cross-project skill sync | Needs real use cases first | Community feedback |

---

*This file is updated when work items are completed or milestones are reached.*
