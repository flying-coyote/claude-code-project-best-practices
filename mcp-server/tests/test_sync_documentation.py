"""Tests for sync_documentation tool."""

import pytest
from pathlib import Path
from unittest.mock import MagicMock

from best_practices_mcp.tools.sync_documentation import sync_documentation
from best_practices_mcp.parsers.markdown_parser import PatternMetadata


@pytest.fixture
def mock_pattern():
    """Create a mock pattern for testing."""
    return PatternMetadata(
        id="test-pattern",
        name="Test Pattern",
        file_path="patterns/test-pattern.md",
        sources=[{"title": "Test Source", "url": "https://example.com", "tier": "A"}],
        evidence_tier="A",
        sdd_phase="specify",
        related_patterns=[],
        sections=["Implementation"],
        internal_links=[],
        external_links=["https://example.com"],
    )


@pytest.fixture
def mock_pattern_registry(mock_pattern):
    """Create a mock pattern registry."""
    registry = MagicMock()
    registry.get_all.return_value = [mock_pattern]
    registry.get_by_id.return_value = mock_pattern
    return registry


@pytest.fixture
def mock_source_registry():
    """Create a mock source registry."""
    registry = MagicMock()
    registry.get_all.return_value = []
    registry.get_by_url.return_value = None
    return registry


@pytest.mark.asyncio
async def test_check_consistency(mock_pattern_registry, mock_source_registry, tmp_path):
    """Test consistency checking."""
    # Create mock CLAUDE.md
    claude_dir = tmp_path / ".claude"
    claude_dir.mkdir()
    (claude_dir / "CLAUDE.md").write_text("# Project\n\ntest-pattern mentioned here")

    result = await sync_documentation(
        action="check_consistency",
        scope="patterns",
        auto_fix=False,
        pattern_registry=mock_pattern_registry,
        source_registry=mock_source_registry,
        repo_root=tmp_path,
        index_file=tmp_path / "INDEX.md",
    )

    assert result["action"] == "check_consistency"
    assert "files_checked" in result
    assert "inconsistencies" in result


@pytest.mark.asyncio
async def test_update_index_missing_file(mock_pattern_registry, mock_source_registry, tmp_path):
    """Test INDEX.md update detection when file doesn't exist."""
    result = await sync_documentation(
        action="update_index",
        scope="all",
        auto_fix=False,
        pattern_registry=mock_pattern_registry,
        source_registry=mock_source_registry,
        repo_root=tmp_path,
        index_file=tmp_path / "INDEX.md",
    )

    assert result["action"] == "update_index"
    assert len(result["index_updates_needed"]) > 0


@pytest.mark.asyncio
async def test_verify_cross_refs(mock_pattern_registry, mock_source_registry, tmp_path):
    """Test cross-reference verification."""
    result = await sync_documentation(
        action="verify_cross_refs",
        scope="patterns",
        auto_fix=False,
        pattern_registry=mock_pattern_registry,
        source_registry=mock_source_registry,
        repo_root=tmp_path,
        index_file=tmp_path / "INDEX.md",
    )

    assert result["action"] == "verify_cross_refs"
    assert "missing_cross_refs" in result


@pytest.mark.asyncio
async def test_generate_report(mock_pattern_registry, mock_source_registry, tmp_path):
    """Test report generation."""
    result = await sync_documentation(
        action="generate_report",
        scope="all",
        auto_fix=False,
        pattern_registry=mock_pattern_registry,
        source_registry=mock_source_registry,
        repo_root=tmp_path,
        index_file=tmp_path / "INDEX.md",
    )

    assert result["action"] == "generate_report"
    assert "report" in result
    assert "total_patterns" in result["report"]


@pytest.mark.asyncio
async def test_unknown_action(mock_pattern_registry, mock_source_registry, tmp_path):
    """Test unknown action returns error."""
    result = await sync_documentation(
        action="unknown_action",
        scope="all",
        auto_fix=False,
        pattern_registry=mock_pattern_registry,
        source_registry=mock_source_registry,
        repo_root=tmp_path,
        index_file=tmp_path / "INDEX.md",
    )

    assert "error" in result
    assert "Unknown action" in result["error"]
