"""Best Practices MCP Server - Pattern validation and documentation sync."""

import asyncio
import os
from pathlib import Path
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Resource,
    Tool,
    TextContent,
)
from pydantic import AnyUrl

from .tools.validate_patterns import validate_patterns
from .tools.sync_documentation import sync_documentation
from .resources.pattern_registry import PatternRegistry
from .resources.source_registry import SourceRegistry

# Initialize server
server = Server("best-practices-mcp")

# Configuration from environment
REPO_ROOT = Path(os.environ.get("REPO_ROOT", Path(__file__).parent.parent.parent.parent.parent))
PATTERNS_DIR = REPO_ROOT / os.environ.get("PATTERNS_DIR", "patterns")
SOURCES_FILE = REPO_ROOT / os.environ.get("SOURCES_FILE", "SOURCES.md")
INDEX_FILE = REPO_ROOT / os.environ.get("INDEX_FILE", "INDEX.md")

# Initialize registries
pattern_registry = PatternRegistry(PATTERNS_DIR)
source_registry = SourceRegistry(SOURCES_FILE)


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="validate_patterns",
            description="Validate patterns for structure, links, evidence tiers, and cross-references",
            inputSchema={
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["validate_single", "validate_all", "check_links", "check_evidence"],
                        "description": "Validation action to perform"
                    },
                    "pattern_id": {
                        "type": "string",
                        "description": "Pattern ID for validate_single action (e.g., 'context-engineering')"
                    },
                    "validation_type": {
                        "type": "string",
                        "enum": ["structure", "links", "evidence", "cross-refs", "full"],
                        "default": "full",
                        "description": "Type of validation to run"
                    }
                },
                "required": ["action"]
            }
        ),
        Tool(
            name="sync_documentation",
            description="Check and sync documentation consistency across files",
            inputSchema={
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["check_consistency", "update_index", "verify_cross_refs", "generate_report"],
                        "description": "Sync action to perform"
                    },
                    "scope": {
                        "type": "string",
                        "enum": ["patterns", "sources", "skills", "all"],
                        "default": "all",
                        "description": "Scope of documentation to check"
                    },
                    "auto_fix": {
                        "type": "boolean",
                        "default": False,
                        "description": "Generate fix suggestions"
                    }
                },
                "required": ["action"]
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle tool calls."""
    if name == "validate_patterns":
        result = await validate_patterns(
            action=arguments["action"],
            pattern_id=arguments.get("pattern_id"),
            validation_type=arguments.get("validation_type", "full"),
            pattern_registry=pattern_registry,
            source_registry=source_registry,
            repo_root=REPO_ROOT
        )
    elif name == "sync_documentation":
        result = await sync_documentation(
            action=arguments["action"],
            scope=arguments.get("scope", "all"),
            auto_fix=arguments.get("auto_fix", False),
            pattern_registry=pattern_registry,
            source_registry=source_registry,
            repo_root=REPO_ROOT,
            index_file=INDEX_FILE
        )
    else:
        result = {"error": f"Unknown tool: {name}"}

    import json
    return [TextContent(type="text", text=json.dumps(result, indent=2))]


@server.list_resources()
async def list_resources() -> list[Resource]:
    """List available resources."""
    return [
        Resource(
            uri=AnyUrl("patterns://registry"),
            name="Pattern Registry",
            description="All documented patterns with metadata",
            mimeType="application/json"
        ),
        Resource(
            uri=AnyUrl("sources://registry"),
            name="Source Registry",
            description="All references from SOURCES.md with tier classification",
            mimeType="application/json"
        )
    ]


@server.read_resource()
async def read_resource(uri: AnyUrl) -> str:
    """Read resource content."""
    import json

    uri_str = str(uri)
    if uri_str == "patterns://registry":
        await pattern_registry.refresh()
        return json.dumps(pattern_registry.to_dict(), indent=2)
    elif uri_str == "sources://registry":
        await source_registry.refresh()
        return json.dumps(source_registry.to_dict(), indent=2)
    else:
        raise ValueError(f"Unknown resource: {uri}")


async def run_server():
    """Run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


def main():
    """Entry point."""
    asyncio.run(run_server())


if __name__ == "__main__":
    main()
