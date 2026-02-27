---
version-requirements:
  claude-code: "v2.0.0+"
  github-action: "/install-github-action command"
version-last-verified: "2026-02-27"
status: "PRODUCTION"
last-verified: "2026-02-16"
---

# GitHub Actions Integration

**Source**: [Boris Cherny Interview](https://paddo.dev/blog/how-boris-uses-claude-code/), [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
**Evidence Tier**: A (Primary vendor/creator)

## Overview

GitHub Actions can trigger Claude Code for automated code review, PR assistance, and CI/CD integration. This enables AI-augmented workflows without manual intervention.

**SDD Phase**: Implement (automation layer)

---

## Setting Up the GitHub Action

### Installation

Use the `/install-github-action` command within Claude Code:

```bash
# In your Claude Code session
/install-github-action
```

This adds the Claude Code GitHub Action to your repository's `.github/workflows/`.

### Manual Installation

If you prefer manual setup, create `.github/workflows/claude-code.yml`:

```yaml
name: Claude Code Review
on:
  pull_request:
    types: [opened, synchronize, reopened]
  issue_comment:
    types: [created]

permissions:
  contents: read
  pull-requests: write
  issues: write

jobs:
  claude-review:
    runs-on: ubuntu-latest
    if: |
      github.event_name == 'pull_request' ||
      (github.event_name == 'issue_comment' && contains(github.event.comment.body, '@.claude'))
    steps:
      - uses: actions/checkout@v4

      - name: Claude Code Review
        uses: anthropics/claude-code-action@v1
        with:
          anthropic-api-key: ${{ secrets.ANTHROPIC_API_KEY }}
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

### Required Secrets

| Secret | Purpose |
|--------|---------|
| `ANTHROPIC_API_KEY` | API key for Claude |
| `GITHUB_TOKEN` | Auto-provided by GitHub Actions |

---

## @.claude Tagging System

### Triggering Claude from PRs

Tag Claude in PR descriptions or comments to request AI assistance:

```markdown
## PR Description

This PR implements user authentication.

@.claude Please review for security issues
```

### Comment Triggers

Respond to specific code or request focused reviews:

```markdown
@.claude What's the time complexity of this function?
```

```markdown
@.claude Check this file for SQL injection vulnerabilities
```

### Team Workflow

> "We tag @.claude on PRs to get AI review before human review."
> — Boris Cherny, Claude Code Creator

**Recommended workflow**:
1. Open PR with code changes
2. Tag `@.claude` for automated first-pass review
3. Address AI feedback
4. Request human review
5. Capture insights in CLAUDE.md

---

## Use Cases

### 1. Automated Code Review

```yaml
# Trigger on all PRs
on:
  pull_request:
    types: [opened, synchronize]
```

Claude reviews:
- Code quality and style
- Potential bugs
- Security considerations
- Test coverage gaps

### 2. On-Demand Analysis

```yaml
# Trigger only when @.claude is mentioned
on:
  issue_comment:
    types: [created]

jobs:
  claude-assist:
    if: contains(github.event.comment.body, '@.claude')
```

### 3. Pre-Merge Validation

```yaml
# Required check before merge
on:
  pull_request:
    branches: [main]

jobs:
  claude-validate:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          mode: validate
          rules: |
            - No console.log statements
            - All functions must have docstrings
            - Tests required for new functions
```

### 4. Documentation Generation

```yaml
# Generate docs for new functions
on:
  push:
    paths:
      - 'src/**/*.ts'

jobs:
  claude-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          mode: document
          output-path: docs/api/
```

---

## Configuration Options

### Action Parameters

```yaml
- uses: anthropics/claude-code-action@v1
  with:
    # Required
    anthropic-api-key: ${{ secrets.ANTHROPIC_API_KEY }}
    github-token: ${{ secrets.GITHUB_TOKEN }}

    # Optional
    model: claude-opus-4-5-20251101  # Default model
    mode: review                      # review, validate, document, assist
    context-files: |                  # Additional context
      CLAUDE.md
      ARCHITECTURE.md
    max-tokens: 4096                  # Response length limit
```

### Modes

| Mode | Purpose | Output |
|------|---------|--------|
| `review` | General code review | PR comment with findings |
| `validate` | Check against rules | Pass/fail status |
| `document` | Generate documentation | Markdown files |
| `assist` | Answer questions | Reply to @.claude comments |

---

## Integration with CLAUDE.md

### Feedback Loop

Claude Code in GitHub Actions can read CLAUDE.md for project context:

```yaml
- uses: anthropics/claude-code-action@v1
  with:
    context-files: |
      .claude/CLAUDE.md
      ARCHITECTURE.md
```

### Capturing Learnings

When Claude identifies patterns in PR reviews:

```markdown
## From PR Reviews (via GitHub Actions)

- **PR #142**: Don't use `any` type - prefer `unknown` with type guards
- **PR #156**: Always add loading states to async operations
- **PR #163**: Database queries need explicit timeouts
```

---

## Best Practices

### 1. Start with Review Mode

Begin with automated code review before adding validation rules:

```yaml
# Simple start
- uses: anthropics/claude-code-action@v1
  with:
    mode: review
```

### 2. Add Validation Gradually

Once you identify patterns, codify them:

```yaml
# After seeing repeated issues
- uses: anthropics/claude-code-action@v1
  with:
    mode: validate
    rules: |
      - No hardcoded API keys
      - Error handling required for async calls
```

### 3. Use Branch Targeting

Restrict intensive checks to important branches:

```yaml
on:
  pull_request:
    branches: [main, develop]
```

### 4. Set Timeouts

Prevent runaway reviews:

```yaml
jobs:
  claude-review:
    timeout-minutes: 10
```

---

## Cost Considerations

| Factor | Impact | Mitigation |
|--------|--------|------------|
| PR volume | More PRs = more API calls | Trigger only on target branches |
| Review depth | Deeper review = more tokens | Use Haiku for simple checks |
| File count | More files = more context | Filter to changed files only |

### Token-Efficient Configuration

```yaml
- uses: anthropics/claude-code-action@v1
  with:
    model: claude-3-haiku-20240307  # Cheaper for simple reviews
    max-tokens: 2048                # Limit response size
    files-filter: changed           # Only review changed files
```

---

## Anti-Patterns

### Blocking on All PRs

**Problem**: Making Claude review a required check for all PRs
**Impact**: Delays, costs, potential API failures block merges
**Solution**: Make AI review advisory, not blocking (except for security)

### Ignoring Rate Limits

**Problem**: Too many PRs trigger simultaneous reviews
**Impact**: API rate limiting, failed workflows
**Solution**: Queue reviews, add concurrency limits

### No Context Files

**Problem**: Running Claude without CLAUDE.md context
**Impact**: Generic feedback, misses project conventions
**Solution**: Always include project context files

---

## Security Considerations

1. **API Key Protection**: Always use GitHub Secrets, never commit keys
2. **Permission Scope**: Grant minimal permissions (read contents, write comments)
3. **Branch Protection**: Don't let Action modify protected branches
4. **Review Output**: Claude output is advisory; human approval still required

---

## Related Patterns

- [Documentation Maintenance](./documentation-maintenance.md) - Team CLAUDE.md pattern
- [Subagent Orchestration](./subagent-orchestration.md) - Background processing
- [Plugins and Extensions](./plugins-and-extensions.md) - Permission configuration

---

## Sources

- [Boris Cherny Interview - Paddo.dev](https://paddo.dev/blog/how-boris-uses-claude-code/)
- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

*Last updated: January 2026*
