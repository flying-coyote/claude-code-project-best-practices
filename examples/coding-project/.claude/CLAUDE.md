# my-awesome-library Project Context

## Project Purpose

A TypeScript utility library providing common helper functions for string manipulation, date formatting, and data validation.

## Current Phase

Active development - v1.0 release planned

## Code Quality Standards

- Write clean, maintainable code with clear intent
- Test-driven development where applicable
- Meaningful commit messages following conventional format
- No premature optimization
- Avoid over-engineering - only make requested changes
- 90%+ test coverage for public APIs

## Thinking Methodology

For deep analysis, use the FRAME-ANALYZE-SYNTHESIZE approach:
- **FRAME**: Define problem, identify assumptions, clarify success criteria
- **ANALYZE**: Evaluate alternatives, identify failure modes, assess trade-offs
- **SYNTHESIZE**: Recommend approach, document rationale, plan implementation

## Git Workflow

Commit messages follow conventional format:
- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `refactor:` Code refactoring
- `test:` Test additions/changes
- `chore:` Maintenance tasks

## Project Structure

```
src/           # Source code
tests/         # Test files
docs/          # API documentation
dist/          # Build output (gitignored)
```

## Testing

- Run tests: `npm test`
- Run with coverage: `npm run test:coverage`
- All PRs require passing tests
