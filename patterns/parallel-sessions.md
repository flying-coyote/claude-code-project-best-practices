# Parallel Sessions Pattern

**Source**: [Boris Cherny Interview](https://paddo.dev/blog/how-boris-uses-claude-code/)
**Evidence Tier**: A (Primary vendor/creator)

## Overview

Running multiple Claude Code sessions simultaneously maximizes productivity by allowing parallel work streams. This pattern documents Boris Cherny's workflow of running 5 terminal sessions plus 5-10 web sessions.

**SDD Phase**: Implement (parallel execution strategy)

---

## The Multi-Session Workflow

### Boris Cherny's Setup

> "I run 5 terminal instances of Claude Code with system notifications, and 5-10 web sessions on claude.ai simultaneously."
> — Boris Cherny, Claude Code Creator

### Session Configuration

| Session Type | Count | Purpose | Notification |
|--------------|-------|---------|--------------|
| Terminal (Claude Code) | 5 | Code execution, file ops | System notifications |
| Web (claude.ai) | 5-10 | Research, planning, drafting | Browser tabs |

---

## Terminal Session Setup

### Numbered Sessions

Number your terminal sessions for easy reference:

```bash
# Terminal 1: Primary development
claude --session-name "dev-1"

# Terminal 2: Testing/validation
claude --session-name "test-2"

# Terminal 3: Research/exploration
claude --session-name "research-3"

# Terminal 4: Documentation
claude --session-name "docs-4"

# Terminal 5: Git/deployment
claude --session-name "git-5"
```

### Session Specialization

| Session | Focus | Common Tasks |
|---------|-------|--------------|
| **dev-1** | Primary implementation | Feature coding, bug fixes |
| **test-2** | Testing | Running tests, writing tests, debugging |
| **research-3** | Exploration | Codebase research, finding patterns |
| **docs-4** | Documentation | README updates, comments, API docs |
| **git-5** | Git operations | Commits, PRs, branch management |

### System Notifications

Enable notifications to track when sessions complete:

```bash
# On macOS
claude --notify

# On Linux (requires notify-send)
claude --notify-command "notify-send 'Claude Code' 'Session complete'"
```

---

## Web Session Patterns

### When to Use Web vs Terminal

| Use Case | Prefer Web (claude.ai) | Prefer Terminal (Claude Code) |
|----------|------------------------|------------------------------|
| Research questions | Artifacts | Local file access |
| Long-form planning | Better for diagrams | - |
| Code execution | - | Direct file system |
| Quick iterations | - | Faster tool execution |
| Sharing outputs | Easy export | Requires copy/paste |

### Web Session Organization

Use browser tabs or windows organized by purpose:

```
Window 1: Planning & Architecture
├── Tab 1: Feature A planning
├── Tab 2: Architecture discussion
└── Tab 3: Trade-off analysis

Window 2: Research
├── Tab 1: Technology research
├── Tab 2: Best practices lookup
└── Tab 3: Documentation drafting

Window 3: Overflow
├── Tabs as needed for parallel tasks
```

---

## Teleport Coordination

### Transferring Context

Use `--teleport` to share context between local and web sessions:

```bash
# Generate teleport link from terminal session
/teleport

# Paste the link in web session to transfer context
```

### When to Teleport

| From | To | Use Case |
|------|-----|----------|
| Terminal | Web | Share code context for discussion |
| Web | Terminal | Import planned approach for execution |
| Terminal | Terminal | Hand off between session specializations |

---

## Parallel Execution Strategies

### Strategy 1: Task Parallelization

Distribute independent tasks across sessions:

```
Session 1: Implement feature A (frontend)
Session 2: Implement feature A (backend API)
Session 3: Write tests for feature A
Session 4: Update documentation
Session 5: Review and prepare PR
```

### Strategy 2: Pipeline Processing

Chain dependent tasks across sessions:

```
Session 1: Research → outputs findings.md
Session 2: Design → reads findings.md, outputs design.md
Session 3: Implement → reads design.md, writes code
Session 4: Test → runs tests on new code
Session 5: Deploy → creates PR, monitors CI
```

### Strategy 3: Exploration vs Execution

Separate research from implementation:

```
Web Sessions (5-10): Exploration, planning, research
Terminal Sessions (5): Execution, file operations, git

Web Session 1: "How should we architect the auth system?"
             → Outputs design decision

Terminal Session 1: Implements the decided architecture
```

---

## Input Notifications

### Avoiding Forgotten Sessions

Sessions that need input can sit idle. Use notifications to stay aware:

```bash
# Enable input notifications (when Claude needs clarification)
claude --notify-on-input
```

### Workflow Check-In Pattern

Periodically check all sessions:

```
Every 15-30 minutes:
1. Check Terminal 1-5 for completion or input needed
2. Review Web tabs for completed artifacts
3. Redistribute work based on progress
```

---

## Best Practices

### 1. Context Isolation

Keep sessions focused on specific domains:

```
Good: Session 1 handles all frontend work
Bad: Session 1 switching between frontend, backend, and DevOps
```

### 2. Artifact Handoff

Use files to pass information between sessions:

```
Session 1: Writes research-findings.md
Session 2: Reads research-findings.md, writes implementation-plan.md
Session 3: Reads implementation-plan.md, writes code
```

### 3. Git Branch per Session

Avoid conflicts by using separate branches:

```bash
# Session 1
git checkout -b feature/auth-frontend

# Session 2
git checkout -b feature/auth-backend

# Later: merge both to feature/auth
```

### 4. Session Naming Convention

Use consistent naming for easy tracking:

```
Terminal sessions: [project]-[purpose]-[number]
Example: webapp-dev-1, webapp-test-2

Web sessions: Browser tab titles or bookmarks
Example: "WebApp Planning", "Auth Research"
```

---

## Resource Management

### System Resources

| Factor | Impact | Mitigation |
|--------|--------|------------|
| Memory | Multiple Claudes = multiple contexts | Close unused sessions |
| API Rate | Parallel calls count against limits | Stagger heavy operations |
| Focus | Too many sessions = context switching | Cap at 5 terminal + 5 web |

### When to Scale Down

- Approaching API rate limits
- Tasks becoming interdependent
- Mental overhead exceeding benefit
- Nearing project completion (fewer parallel tasks)

### When to Scale Up

- Many independent tasks
- Long-running operations (tests, builds)
- Research-heavy phases
- Time-sensitive deadlines

---

## Anti-Patterns

### Session Sprawl

**Problem**: Opening new sessions for every small task
**Impact**: Too many contexts to track, forgotten sessions
**Solution**: Reuse sessions, max 5 terminal + 10 web

### Cross-Session Dependencies

**Problem**: Sessions waiting on each other's outputs
**Impact**: Parallelization benefits lost
**Solution**: Design tasks for true independence, use file handoffs

### No Session Focus

**Problem**: Every session does everything
**Impact**: Context pollution, confused Claude instances
**Solution**: Specialize sessions (dev, test, docs, git, research)

### Forgetting Sessions

**Problem**: Sessions sit idle waiting for input
**Impact**: Wasted time, incomplete work
**Solution**: Enable notifications, regular check-ins

---

## Example Daily Workflow

```
9:00 AM - Setup
├── Open Terminal sessions 1-5
├── Open Web browser with 5 tabs
└── Assign initial tasks

9:30 AM - Morning Sprint
├── Terminal 1: Feature implementation
├── Terminal 2: Parallel test writing
├── Terminal 3: Research for afternoon work
├── Web tabs: Planning, documentation drafting
└── Check all sessions every 15 min

12:00 PM - Midday Sync
├── Review morning outputs
├── Merge completed branches
├── Reassign sessions for afternoon
└── Close completed sessions, open new if needed

3:00 PM - Afternoon Push
├── Terminal 1: Continue implementation
├── Terminal 2: Integration testing
├── Terminal 5: PR preparation
├── Web: Final documentation polish
└── Begin winding down sessions

5:00 PM - Wrap Up
├── /commit-push-pr in remaining sessions
├── Close all Claude Code sessions
├── Stop hooks remind of uncommitted work
└── Document any insights in CLAUDE.md
```

---

## Related Patterns

- [Subagent Orchestration](./subagent-orchestration.md) - In-session parallelism
- [Documentation Maintenance](./documentation-maintenance.md) - Team CLAUDE.md updates
- [Long-Running Agent](./long-running-agent.md) - External artifacts for context bridging

---

## Sources

- [Boris Cherny Interview - Paddo.dev](https://paddo.dev/blog/how-boris-uses-claude-code/)
- [VentureBeat - Creator of Claude Code Workflow](https://venturebeat.com/technology/the-creator-of-claude-code-just-revealed-his-workflow-and-developers-are)

*Last updated: January 2026*
