"""Documentation sync tool."""

import re
from pathlib import Path
from typing import Any, Optional

from ..resources.pattern_registry import PatternRegistry
from ..resources.source_registry import SourceRegistry


async def sync_documentation(
    action: str,
    scope: str,
    auto_fix: bool,
    pattern_registry: PatternRegistry,
    source_registry: SourceRegistry,
    repo_root: Path,
    index_file: Path,
) -> dict[str, Any]:
    """Check and sync documentation consistency."""

    if action == "check_consistency":
        return await _check_consistency(scope, pattern_registry, source_registry, repo_root)

    elif action == "update_index":
        return await _check_index_updates(pattern_registry, repo_root, index_file, auto_fix)

    elif action == "verify_cross_refs":
        return await _verify_cross_refs(scope, pattern_registry, source_registry, repo_root)

    elif action == "generate_report":
        return await _generate_report(pattern_registry, source_registry, repo_root, index_file)

    else:
        return {"error": f"Unknown action: {action}"}


async def _check_consistency(
    scope: str,
    pattern_registry: PatternRegistry,
    source_registry: SourceRegistry,
    repo_root: Path,
) -> dict[str, Any]:
    """Check for consistency issues across documentation."""
    inconsistencies = []
    files_checked = 0

    if scope in ("patterns", "all"):
        patterns = pattern_registry.get_all()
        files_checked += len(patterns)

        # Check CLAUDE.md references patterns correctly
        claude_md = repo_root / ".claude" / "CLAUDE.md"
        if claude_md.exists():
            claude_content = claude_md.read_text()
            files_checked += 1

            for pattern in patterns:
                # Check if pattern is in key files table
                if pattern.id not in claude_content and pattern.name not in claude_content:
                    # Only flag if it's a foundational or cross-phase pattern
                    if pattern.sdd_phase in ("foundational", "cross-phase"):
                        inconsistencies.append({
                            "file": ".claude/CLAUDE.md",
                            "issue": "Missing pattern reference",
                            "expected": f"Reference to {pattern.id}",
                            "found": "Not mentioned",
                            "suggested_fix": f"Add {pattern.id} to Patterns Directory section"
                        })

    if scope in ("sources", "all"):
        sources = source_registry.get_all()
        patterns = pattern_registry.get_all()

        # Check sources referenced in patterns exist in SOURCES.md
        for pattern in patterns:
            for source in pattern.sources:
                url = source.get("url")
                if url:
                    source_entry = source_registry.get_by_url(url)
                    if not source_entry:
                        inconsistencies.append({
                            "file": pattern.file_path,
                            "issue": "Source not in SOURCES.md",
                            "expected": f"Entry in SOURCES.md for {url}",
                            "found": "Not found",
                            "suggested_fix": f"Add source to SOURCES.md"
                        })

    return {
        "action": "check_consistency",
        "files_checked": files_checked,
        "inconsistencies": inconsistencies,
        "missing_cross_refs": [],
        "index_updates_needed": []
    }


async def _check_index_updates(
    pattern_registry: PatternRegistry,
    repo_root: Path,
    index_file: Path,
    auto_fix: bool,
) -> dict[str, Any]:
    """Check if INDEX.md needs updates."""
    index_updates_needed = []

    if not index_file.exists():
        return {
            "action": "update_index",
            "files_checked": 0,
            "inconsistencies": [],
            "missing_cross_refs": [],
            "index_updates_needed": [{
                "index_file": str(index_file),
                "update_type": "add",
                "entry": "INDEX.md file does not exist"
            }]
        }

    index_content = index_file.read_text()
    patterns = pattern_registry.get_all()

    for pattern in patterns:
        # Check if pattern is listed in INDEX.md
        if pattern.id not in index_content and pattern.name not in index_content:
            index_updates_needed.append({
                "index_file": str(index_file),
                "update_type": "add",
                "entry": f"patterns/{pattern.id}.md"
            })

    # Check for stale entries (files in INDEX.md that don't exist)
    pattern_refs = re.findall(r'patterns/([a-z0-9-]+)\.md', index_content)
    for ref in pattern_refs:
        if not pattern_registry.get_by_id(ref):
            index_updates_needed.append({
                "index_file": str(index_file),
                "update_type": "remove",
                "entry": f"patterns/{ref}.md (file no longer exists)"
            })

    return {
        "action": "update_index",
        "files_checked": len(patterns) + 1,
        "inconsistencies": [],
        "missing_cross_refs": [],
        "index_updates_needed": index_updates_needed
    }


async def _verify_cross_refs(
    scope: str,
    pattern_registry: PatternRegistry,
    source_registry: SourceRegistry,
    repo_root: Path,
) -> dict[str, Any]:
    """Verify cross-references between patterns."""
    missing_cross_refs = []
    patterns = pattern_registry.get_all()

    # Build a map of which patterns reference which
    refs_to = {p.id: set(p.related_patterns) for p in patterns}
    refs_from = {p.id: set() for p in patterns}
    for pattern_id, refs in refs_to.items():
        for ref in refs:
            if ref in refs_from:
                refs_from[ref].add(pattern_id)

    # Find patterns that should reference each other but don't
    # Based on shared sources or topics
    for pattern in patterns:
        # Check if patterns with same SDD phase reference each other
        same_phase = [p for p in patterns if p.sdd_phase == pattern.sdd_phase and p.id != pattern.id]
        for other in same_phase:
            # If they share sources, they should probably reference each other
            pattern_urls = {s.get("url") for s in pattern.sources}
            other_urls = {s.get("url") for s in other.sources}
            shared_sources = pattern_urls & other_urls - {None}

            if shared_sources and other.id not in refs_to[pattern.id]:
                missing_cross_refs.append({
                    "pattern": pattern.id,
                    "should_reference": other.id,
                    "reason": f"Patterns share {len(shared_sources)} source(s) and same SDD phase"
                })

        # Check bidirectional references
        for ref in refs_to[pattern.id]:
            if ref in refs_to and pattern.id not in refs_to[ref]:
                missing_cross_refs.append({
                    "pattern": ref,
                    "should_reference": pattern.id,
                    "reason": f"{pattern.id} references {ref}, but not vice versa"
                })

    return {
        "action": "verify_cross_refs",
        "files_checked": len(patterns),
        "inconsistencies": [],
        "missing_cross_refs": missing_cross_refs,
        "index_updates_needed": []
    }


async def _generate_report(
    pattern_registry: PatternRegistry,
    source_registry: SourceRegistry,
    repo_root: Path,
    index_file: Path,
) -> dict[str, Any]:
    """Generate a comprehensive documentation status report."""
    patterns = pattern_registry.get_all()
    sources = source_registry.get_all()

    # Count by tier
    patterns_by_tier = {
        "A": len([p for p in patterns if p.evidence_tier == "A"]),
        "B": len([p for p in patterns if p.evidence_tier == "B"]),
        "C": len([p for p in patterns if p.evidence_tier == "C"]),
        "D": len([p for p in patterns if p.evidence_tier == "D"]),
        "None": len([p for p in patterns if not p.evidence_tier]),
    }

    # Count by phase
    patterns_by_phase = {}
    for pattern in patterns:
        phase = pattern.sdd_phase or "unspecified"
        patterns_by_phase[phase] = patterns_by_phase.get(phase, 0) + 1

    # Patterns without sources
    patterns_without_sources = [p.id for p in patterns if not p.sources]

    # Cross-reference stats
    total_cross_refs = sum(len(p.related_patterns) for p in patterns)
    avg_cross_refs = total_cross_refs / len(patterns) if patterns else 0

    return {
        "action": "generate_report",
        "files_checked": len(patterns) + len(sources),
        "report": {
            "total_patterns": len(patterns),
            "total_sources": len(sources),
            "patterns_by_tier": patterns_by_tier,
            "patterns_by_phase": patterns_by_phase,
            "patterns_without_sources": patterns_without_sources,
            "cross_reference_stats": {
                "total": total_cross_refs,
                "average_per_pattern": round(avg_cross_refs, 2)
            }
        },
        "inconsistencies": [],
        "missing_cross_refs": [],
        "index_updates_needed": []
    }
