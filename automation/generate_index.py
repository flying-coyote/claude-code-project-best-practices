#!/usr/bin/env python3
"""
Generate INDEX.md from current file structure.

This script scans the repository and creates a markdown index
of all documentation files, organized by directory.

Usage:
    python3 automation/generate_index.py

The script is called automatically by the PostToolUse hook
when file structure changes are detected.
"""

import os
from pathlib import Path
from datetime import datetime


def generate_index(root_dir: str = ".", output_file: str = "INDEX.md"):
    """Generate markdown index of directory structure."""

    # Directories to skip
    skip_dirs = {'.git', '.claude', '__pycache__', 'node_modules', '.archive'}

    # Count files by directory
    dir_counts = {}
    all_files = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip hidden and excluded directories
        dirnames[:] = [d for d in dirnames if d not in skip_dirs and not d.startswith('.')]

        rel_path = os.path.relpath(dirpath, root_dir)
        if rel_path == '.':
            rel_path = 'root'

        # Count markdown files
        md_files = [f for f in filenames if f.endswith('.md')]

        if md_files:
            dir_counts[rel_path] = len(md_files)
            for f in sorted(md_files):
                if rel_path == 'root':
                    all_files.append(('root', f, f))
                else:
                    all_files.append((rel_path, f, f"{rel_path}/{f}"))

    # Generate content
    content = [
        "# Index",
        "",
        f"*Auto-generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
        "",
        "## Summary",
        "",
        f"**Total documents**: {sum(dir_counts.values())}",
        "",
        "| Directory | Count |",
        "|-----------|-------|",
    ]

    for dir_name, count in sorted(dir_counts.items()):
        content.append(f"| {dir_name} | {count} |")

    content.extend([
        "",
        "---",
        "",
    ])

    # Group files by directory
    current_dir = None
    for dir_name, filename, filepath in all_files:
        if dir_name != current_dir:
            current_dir = dir_name
            content.extend([
                f"## {dir_name.replace('/', ' / ').title() if dir_name != 'root' else 'Root'}",
                "",
            ])

        # Create link
        if dir_name == 'root':
            content.append(f"- [{filename}]({filename})")
        else:
            content.append(f"- [{filename}]({filepath})")

    content.append("")
    content.append("---")
    content.append("")
    content.append("*This file is auto-generated. Do not edit manually.*")
    content.append("")

    # Write file
    with open(output_file, 'w') as f:
        f.write('\n'.join(content))

    print(f"Generated {output_file} with {sum(dir_counts.values())} documents")


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    generate_index()
