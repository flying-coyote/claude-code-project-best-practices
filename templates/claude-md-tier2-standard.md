# {{Project Name}}

<!-- TIER 2: Standard (80-120 lines). Use for most production projects.
     Adds resource map, architecture context, and security boundaries. -->

{{One-paragraph description: what it does, who uses it, what stack.}}

## Commands

<!-- Only commands Claude needs. Group by workflow. -->

### Build & Test
- `{{build}}` -- Build
- `{{test}}` -- Run all tests
- `{{test single}}` -- Run a single test file
- `{{lint}}` -- Lint and format

### Development
- `{{dev server}}` -- Start dev server
- `{{db migrate}}` -- Run database migrations

## Resource Map

<!-- This is the most valuable section. Tell Claude where things live
     so it doesn't waste time exploring. -->

### Source (`src/`)
- `{{src/api/}}` -- API routes and handlers
- `{{src/lib/}}` -- Shared utilities and clients
- `{{src/models/}}` -- Data models and types

### Configuration
- `{{config file}}` -- Runtime configuration
- `{{env example}}` -- Environment variables (DO NOT commit .env)

### Tests (`tests/`)
- `{{tests/unit/}}` -- Unit tests (fast, no external deps)
- `{{tests/integration/}}` -- Integration tests (require {{service}})

## Architecture

<!-- 2-3 sentences about how the system works. Not documentation —
     just enough for Claude to make informed decisions. -->

{{Brief description of the architecture: request flow, key abstractions,
external dependencies.}}

## Rules

<!-- Rules should be things Claude gets wrong without explicit guidance.
     Move detailed domain rules to .claude/rules/ files. -->

- File naming: {{convention}}
- Always run `{{test command}}` before committing
- Stage specific files (`git add file1 file2`), never `git add .`
- Do not modify `{{protected files}}` without asking
- {{Security boundary: e.g., "Never log or commit credentials, tokens, or .env files"}}

## Domain Context

<!-- Context that helps Claude understand the problem domain.
     Keep brief — details go in rules files. -->

{{2-3 sentences about the domain. E.g., "This processes Zeek network logs.
Field names like id.orig_h (source IP) and id.resp_p (destination port)
follow Zeek conventions, not our naming."}}
