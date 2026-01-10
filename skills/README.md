# Claude Skills

Skills are reusable AI behavior patterns that activate based on context. They're one of the most powerful features of mature Claude Code projects.

> **Note**: As of Claude Code 2.1.3, slash commands and skills are **unified**. Custom slash commands are now skills with no behavioral difference.

## What Are Skills?

A skill is a markdown file that teaches Claude:
- **When** to activate (trigger conditions)
- **What** to do (step-by-step methodology)
- **How** to output results (structured format)
- **When NOT** to activate (equally important)

## Skill Locations

```
~/.claude/skills/           # Personal skills (available in ALL projects)
└── my-skill/
    └── SKILL.md

your-project/.claude/skills/ # Project skills (this project only)
└── project-skill/
    └── SKILL.md
```

### Hot-Reload Behavior (v2.1.0+)

Skills **automatically reload** when modified. No restart required:
- Add new skill → immediately available
- Edit existing skill → changes take effect instantly
- Delete skill → removed from availability

This enables rapid skill iteration without interrupting your session.

## Skill Structure

Every skill follows this pattern:

```markdown
---
name: Skill Name
description: When to trigger (keywords, contexts). Max 1024 chars. Third-person.
allowed-tools: Read, Grep, Glob, Bash, Write, Edit
---

# Skill Name

## IDENTITY
Who is Claude when using this skill?

## GOAL
What is the skill trying to achieve?

## TRIGGER CONDITIONS

**ACTIVATE when user:**
- [Specific trigger 1]
- [Keywords or contexts]

**DO NOT ACTIVATE when:**
- [Exclusion 1]
- [Edge cases to avoid]

## STEPS
[Step-by-step methodology]

## OUTPUT FORMAT
[Expected output structure]

## EXAMPLES
[Concrete usage examples]

## ANTI-PATTERNS
[What NOT to do]
```

### Advanced Frontmatter Fields (v2.1.0+)

Skills support additional frontmatter fields for advanced control:

```yaml
---
name: Skill Name
description: Third-person description of when to trigger.
allowed-tools: Read, Grep, Glob

# Agent execution (v2.1.0+)
agent: Explore                    # Which agent type executes this skill
                                  # Options: Explore, Plan, general-purpose, claude-code-guide

# Context isolation (v2.1.0+)
context: fork                     # Run skill in isolated context
                                  # Prevents skill from seeing/affecting main conversation

# Inline hooks (v2.1.0+)
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "bash .claude/hooks/validate-bash.sh"
  PostToolUse:
    - matcher: "Write"
      hooks:
        - type: command
          command: "bash .claude/hooks/lint-on-write.sh"
  Stop:
    - hooks:
        - type: command
          command: "bash .claude/hooks/skill-cleanup.sh"
---
```

| Field | Purpose | When to Use |
|-------|---------|-------------|
| `agent` | Specifies execution agent type | When skill needs specialized behavior (fast exploration, planning) |
| `context: fork` | Isolates skill execution | When skill shouldn't pollute main conversation context |
| `hooks` | Skill-specific hook overrides | When skill needs custom validation, logging, or cleanup |

### Context Forking Example

Use `context: fork` when a skill should run independently:

```yaml
---
name: codebase-analyzer
description: Deep analysis of codebase architecture. Use when exploring unfamiliar code.
agent: Explore
context: fork           # Skill runs in isolated context
allowed-tools: Read, Grep, Glob
---
```

**Benefits of forking**:
- Skill's intermediate work doesn't consume parent context
- Clean separation between analysis and implementation
- Failed/abandoned analysis doesn't pollute conversation

## Key Design Principles

### 1. Third-Person Descriptions

The `description` field must be third-person for skill selection to work:

```yaml
# Good - third person
description: Apply debugging methodology when user reports errors or bugs.

# Bad - first person
description: I help you debug code when you have errors.
```

### 2. Explicit DO NOT ACTIVATE

Just as important as triggers. Prevents false positives:

```markdown
**DO NOT ACTIVATE when:**
- User is in design/planning phase (no code yet)
- Error is trivial and obvious (typo, missing import)
- User explicitly wants quick fix without analysis
```

### 3. Structured Output

Skills should produce consistent, scannable output:

```markdown
## OUTPUT FORMAT

### Phase 1 Output
```
Problem Identified:
- Location: [file:line]
- Type: [category]
- Evidence: [what was observed]
```
```

### 4. Integration Mapping

Document how skills work together:

```markdown
## INTEGRATION WITH OTHER SKILLS

**Works WITH:**
- **tdd-enforcer**: Add test during fix phase
- **git-workflow-helper**: Commit with clear message

**Sequence:**
1. This skill diagnoses problem
2. tdd-enforcer writes regression test
3. git-workflow-helper commits fix
```

## Example Skills

This repo includes sanitized examples of universal skills:

### Development Skills

#### [systematic-debugger](examples/systematic-debugger/SKILL.md)
4-phase debugging: REPRODUCE → ISOLATE → UNDERSTAND → FIX

#### [tdd-enforcer](examples/tdd-enforcer/SKILL.md)
Test-driven development: RED → GREEN → REFACTOR

#### [git-workflow-helper](examples/git-workflow-helper/SKILL.md)
Git best practices: commits, branches, PRs, and safe operations

### Analysis Skills

#### [ultrathink-analyst](examples/ultrathink-analyst/SKILL.md)
Deep analysis: FRAME → ANALYZE → SYNTHESIZE methodology

#### [recursive-analyst](examples/recursive-analyst/SKILL.md)
Self-Evolution Algorithm: Multi-candidate → Iterative refinement → Crossover synthesis

### Content & Research Skills

#### [content-reviewer](examples/content-reviewer/SKILL.md)
Publication quality: evidence tiers, intellectual honesty, professional voice, balanced perspective

#### [research-extractor](examples/research-extractor/SKILL.md)
Research synthesis: systematic extraction of concepts, evidence, hypotheses from sources

### Security Skills

#### [threat-model-reviewer](examples/threat-model-reviewer/SKILL.md)
Threat modeling: UNDERSTAND → IDENTIFY (STRIDE) → ASSESS → MITIGATE

#### [detection-rule-reviewer](examples/detection-rule-reviewer/SKILL.md)
Detection engineering: accuracy, performance, evasion resistance, operational quality

## Creating Your Own Skills

### Step 1: Identify the Pattern
What repetitive workflow do you want to codify?

### Step 2: Define Triggers
When should this skill activate? Be specific.

### Step 3: Write the Methodology
Step-by-step process with clear phases.

### Step 4: Add Examples
Concrete examples showing the skill in action.

### Step 5: Document Anti-Patterns
What should the skill NOT do?

## Personal vs. Project Skills

| Type | Location | Scope | Use For |
|------|----------|-------|---------|
| **Personal** | `~/.claude/skills/` | All projects | Universal patterns (debugging, TDD) |
| **Project** | `.claude/skills/` | This project | Domain-specific (SIEM queries, blog publishing) |

## Best Practices

### Keep Skills Focused
One skill = one pattern. Don't combine debugging + testing + deployment.

### Progressive Disclosure

Complex skills should use subdirectories to manage complexity:

```
skill-name/
├── SKILL.md           # Core methodology (300-500 lines max)
├── workflows/         # Extended multi-step procedures
│   ├── phase-1.md     # Detailed phase 1 steps
│   └── phase-2.md     # Detailed phase 2 steps
└── references/        # Supporting materials
    ├── checklist.md   # Quick reference checklist
    └── examples.md    # Extended examples
```

**When to use Progressive Disclosure:**
- Core SKILL.md exceeds 500 lines
- Multiple distinct workflows exist
- Reference materials are frequently updated
- Different users need different levels of detail

**Example: hypothesis-validator skill**
```
hypothesis-validator/
├── SKILL.md                    # Core validation methodology
├── workflows/
│   ├── hypothesis-identification.md  # How to extract hypotheses
│   ├── validation-methodology.md     # 4-step validation process
│   ├── expert-validation.md          # Expert engagement workflow
│   └── documentation.md              # How to record results
└── references/
    ├── confidence-levels.md          # HIGH/MEDIUM/LOW definitions
    └── evidence-tiers.md             # Tier 1-5 classification
```

### Cross-Project Skill Deployment

For skills that should be available across all projects:

```
~/.claude/skills/              # Global personal skills
├── systematic-debugger/
│   └── SKILL.md
├── tdd-enforcer/
│   └── SKILL.md
├── git-workflow-helper/
│   └── SKILL.md
└── ultrathink-analyst/
    └── SKILL.md
```

**Benefits of personal skills:**
- Consistent behavior across all projects
- Single point of maintenance
- No duplication in project repos
- Immediate availability in new projects

**When to use personal vs. project skills:**

| Skill Type | Location | Examples |
|------------|----------|----------|
| Universal patterns | `~/.claude/skills/` | Debugging, TDD, Git workflow |
| Domain-specific | `.claude/skills/` | SIEM queries, API conventions |
| Organization-specific | `.claude/skills/` | Company coding standards |

### Read-Only by Default
Most skills should guide, not automatically change things:
```yaml
allowed-tools: Read, Grep, Glob  # Safe, read-only
```

Add write tools only when needed:
```yaml
allowed-tools: Read, Grep, Glob, Bash, Write, Edit  # Can modify
```

### Version Your Skills
```markdown
---
**Version**: 2.0
**Created**: 2025-10-17
**Updated**: 2025-12-08
**Source**: Community best practices
```

## Production Slash Command Examples

### /commit-push-pr (Boris Cherny's Daily Driver)

> "I use [/commit-push-pr] dozens of times a day."
> — Boris Cherny, Claude Code Creator

Create a chained workflow command that commits, pushes, and creates a PR in one action.

`.claude/commands/commit-push-pr.md`:
```markdown
---
description: Commit current changes, push to remote, and create a PR. Use when ready to submit work for review.
allowed-tools: Bash
---

# Commit, Push, and Create PR

Execute a complete git workflow in sequence:

1. **Stage and Commit**
   - Run `git status` to see changes
   - Stage all relevant changes (skip .env, credentials)
   - Create commit with conventional prefix (feat:, fix:, docs:, etc.)

2. **Push to Remote**
   - Push to current branch with tracking: `git push -u origin HEAD`

3. **Create Pull Request**
   - Use `gh pr create` with:
     - Title from commit message
     - Body with Summary and Test Plan sections
     - Appropriate labels if detectable

4. **Return PR URL**
   - Output the PR URL for easy access

## Chaining Pattern
```bash
git add -A && \
git commit -m "$(cat <<'EOF'
feat: Add user authentication

- Implement JWT token handling
- Add login/logout endpoints
- Include rate limiting

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
EOF
)" && \
git push -u origin HEAD && \
gh pr create --fill
```
```

### /quick-test (Pre-Commit Validation)

`.claude/commands/quick-test.md`:
```markdown
---
description: Run quick validation before committing. Use before /commit-push-pr.
allowed-tools: Bash
---

# Quick Pre-Commit Validation

1. Run type checking (if applicable)
2. Run linting
3. Run fast unit tests (skip slow/integration)
4. Report any failures clearly

If all pass, suggest: "Ready for /commit-push-pr"
```

### /context-prep (Inline Bash for Context)

Use inline bash to pre-compute context before Claude starts:

`.claude/commands/context-prep.md`:
```markdown
---
description: Gather project context for complex tasks. Use at session start.
allowed-tools: Bash, Read, Glob
---

# Context Preparation

Gather essential context upfront:

1. **Git State**: `git status --short && git log --oneline -5`
2. **Recent Changes**: `git diff --stat HEAD~5`
3. **Test Status**: `npm test -- --passWithNoTests --silent 2>&1 | tail -5`
4. **Open TODOs**: `grep -r "TODO" src/ --include="*.ts" | head -10`

Present summary in compact format for efficient token usage.
```

---

## Common Skill Categories

### Development Skills
- Debugging methodology
- Test-driven development
- Code review patterns
- Git workflow conventions

### Content Skills
- Voice consistency
- Citation management
- Publication quality checks
- Evidence tier classification

### Research Skills
- Hypothesis validation
- Literature synthesis
- Contradiction detection
- Evidence assessment

### Communication Skills
- Expert outreach
- Documentation standards
- Presentation patterns

## Pre-Built Skills & Components

If you prefer ready-to-use implementations over building from scratch, **[claude-code-templates](https://github.com/davila7/claude-code-templates)** provides 400+ components:

```bash
# Interactive setup
npx claude-code-templates@latest

# Install specific agents
npx claude-code-templates@latest --agent development-team/frontend-developer --yes
npx claude-code-templates@latest --agent development-tools/code-reviewer --yes

# Browse components at https://www.aitmpl.com
```

| Component | Count | Examples |
|-----------|-------|----------|
| Agents | 100+ | frontend-developer, code-reviewer, security-auditor |
| Commands | 159+ | /generate-tests, /optimize-bundle |
| MCPs | Multiple | GitHub, PostgreSQL, Stripe, AWS |
| Hooks | Multiple | Pre-commit validation |

This complements the patterns in this repository - we teach the **why** and **how**, claude-code-templates provides **ready-made** implementations.

## Further Reading

- [Anthropic Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Example Skills in this repo](examples/)
- [DECISIONS.md](../DECISIONS.md) for design rationale
- [claude-code-templates](https://github.com/davila7/claude-code-templates) for pre-built components
