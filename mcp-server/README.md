# Best Practices MCP Server

MCP server for validating and syncing Claude Code best practices documentation.

## Overview

This MCP server provides two workflow tools:

1. **validate_patterns** - Validate patterns for structure, links, evidence tiers, and cross-references
2. **sync_documentation** - Check and sync documentation consistency across files

## Installation

```bash
cd mcp-server
pip install -e .
```

## Configuration

The server is configured via `.mcp.json` in the project root:

```json
{
  "mcpServers": {
    "best-practices": {
      "command": "python",
      "args": ["-m", "best_practices_mcp.server"],
      "cwd": "./mcp-server/src",
      "env": {
        "REPO_ROOT": "../..",
        "PATTERNS_DIR": "patterns",
        "SOURCES_FILE": "SOURCES.md",
        "INDEX_FILE": "INDEX.md"
      }
    }
  }
}
```

## Tools

### validate_patterns

Validates pattern files for:
- **Structure**: Required sections (title, sources, evidence tier)
- **Links**: Internal links exist, external links reachable
- **Evidence**: Tier claims match source quality
- **Cross-refs**: Related patterns exist

**Actions**:
- `validate_single` - Validate a specific pattern by ID
- `validate_all` - Validate all patterns
- `check_links` - Only check link validity
- `check_evidence` - Only check evidence tier consistency

**Example**:
```
User: "Validate all patterns"
→ validate_patterns(action="validate_all", validation_type="full")

User: "Check if context-engineering pattern is valid"
→ validate_patterns(action="validate_single", pattern_id="context-engineering")
```

### sync_documentation

Checks documentation consistency:
- **Consistency**: Cross-file references match
- **INDEX.md**: Detects missing or stale entries
- **Cross-refs**: Finds missing bidirectional references

**Actions**:
- `check_consistency` - Check for inconsistencies
- `update_index` - Check INDEX.md for updates needed
- `verify_cross_refs` - Find missing cross-references
- `generate_report` - Generate documentation status report

**Example**:
```
User: "Check what cross-references are missing"
→ sync_documentation(action="verify_cross_refs", scope="patterns")

User: "Generate a documentation status report"
→ sync_documentation(action="generate_report")
```

## Resources

The server exposes two MCP resources:

- `patterns://registry` - All patterns with metadata
- `sources://registry` - All sources from SOURCES.md

## Development

Run tests:
```bash
cd mcp-server
pip install -e ".[dev]"
pytest
```

## Architecture

```
src/best_practices_mcp/
├── server.py           # MCP server entry point
├── tools/
│   ├── validate_patterns.py
│   └── sync_documentation.py
├── resources/
│   ├── pattern_registry.py
│   └── source_registry.py
└── parsers/
    ├── markdown_parser.py
    └── sources_parser.py
```
