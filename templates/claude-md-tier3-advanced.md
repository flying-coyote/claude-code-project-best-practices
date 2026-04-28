# {{Project Name}}

<!-- TIER 3: Advanced (120-150 lines). Use for complex domain projects with
     multiple subsystems, security-sensitive data, or team coordination needs.
     Keep under 150 lines — push domain detail to .claude/rules/ files. -->

{{One-paragraph description: what, who, stack, deployment model.}}

## Commands

### Build & Test
- `{{build}}` -- Build
- `{{test all}}` -- Full test suite
- `{{test unit}}` -- Unit tests only (fast)
- `{{test integration}}` -- Integration tests (requires {{services}})
- `{{lint}}` -- Lint and format

### Development
- `{{dev}}` -- Start development environment
- `{{db}}` -- Database operations

### Deployment
- `{{deploy staging}}` -- Deploy to staging
- `{{deploy prod}}` -- Deploy to production (requires approval)

## Resource Map

### Core (`{{src/}}`)
- `{{src/api/}}` -- API layer (routes, handlers, middleware)
- `{{src/core/}}` -- Business logic (domain models, services)
- `{{src/lib/}}` -- Shared utilities (clients, helpers, types)
- `{{src/connectors/}}` -- External system integrations

### Configuration (`{{config/}}`)
- `{{config/}}` -- Runtime configuration files
- `.env.example` -- Required environment variables
- `{{ci config}}` -- CI/CD pipeline definition

### Tests (`{{tests/}}`)
- `{{tests/unit/}}` -- Unit tests
- `{{tests/integration/}}` -- Integration tests
- `{{tests/fixtures/}}` -- Test data and mocks

### Documentation (`{{docs/}}`)
- `{{docs/}}` -- Architecture decisions, API docs

## Architecture

<!-- Brief system overview. Details go in docs/ or rules files. -->

{{2-4 sentences: request flow, key abstractions, subsystem boundaries,
external dependencies. Focus on what Claude needs to make good decisions.}}

### Key Abstractions

<!-- Name the 3-5 most important types/interfaces Claude will encounter. -->

- `{{TypeA}}` -- {{what it represents}}
- `{{TypeB}}` -- {{what it represents}}
- `{{TypeC}}` -- {{what it represents}}

## Rules

### Code Quality
- Always run `{{test command}}` before committing
- Stage specific files, never `git add .`
- Follow existing patterns — read before writing
- {{Language/framework convention}}

### Security Boundaries
- Never commit `.env`, credentials, tokens, or API keys
- {{Data handling rule: e.g., "PII must be tokenized before LLM processing"}}
- {{Access control rule}}

### Domain Rules
<!-- Keep this section short. Detailed rules go in .claude/rules/ files
     that load only when editing files in the relevant directory. -->
- {{Critical domain rule 1}}
- {{Critical domain rule 2}}
- See `.claude/rules/` for detailed domain guidance

## External Dependencies

<!-- List external systems Claude should know about but not modify directly. -->

| System | Purpose | How We Connect |
|--------|---------|----------------|
| {{SIEM}} | {{purpose}} | {{API/MCP/SDK}} |
| {{Database}} | {{purpose}} | {{connection method}} |
