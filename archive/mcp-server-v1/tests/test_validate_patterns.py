"""Tests for validate_patterns tool."""

import pytest
from pathlib import Path
from unittest.mock import MagicMock, AsyncMock

from best_practices_mcp.tools.validate_patterns import validate_patterns
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
        related_patterns=["context-engineering"],
        sections=["Implementation", "Example"],
        internal_links=["patterns/context-engineering.md"],
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
    registry.get_by_url.return_value = MagicMock(id="test-source", tier="A")
    return registry


@pytest.mark.asyncio
async def test_validate_single_success(mock_pattern_registry, mock_source_registry, tmp_path):
    """Test validating a single pattern."""
    # Create mock files
    patterns_dir = tmp_path / "patterns"
    patterns_dir.mkdir()
    (patterns_dir / "context-engineering.md").write_text("# Context Engineering")
    (patterns_dir / "test-pattern.md").write_text("# Test Pattern")

    result = await validate_patterns(
        action="validate_single",
        pattern_id="test-pattern",
        validation_type="structure",
        pattern_registry=mock_pattern_registry,
        source_registry=mock_source_registry,
        repo_root=tmp_path,
    )

    assert result["action"] == "validate_single"
    assert result["patterns_checked"] == 1
    assert len(result["results"]) == 1


@pytest.mark.asyncio
async def test_validate_all(mock_pattern_registry, mock_source_registry, tmp_path):
    """Test validating all patterns."""
    patterns_dir = tmp_path / "patterns"
    patterns_dir.mkdir()
    (patterns_dir / "context-engineering.md").write_text("# Context Engineering")

    result = await validate_patterns(
        action="validate_all",
        pattern_id=None,
        validation_type="structure",
        pattern_registry=mock_pattern_registry,
        source_registry=mock_source_registry,
        repo_root=tmp_path,
    )

    assert result["action"] == "validate_all"
    assert "summary" in result
    assert "valid" in result["summary"]


@pytest.mark.asyncio
async def test_validate_missing_pattern(mock_pattern_registry, mock_source_registry, tmp_path):
    """Test validating a non-existent pattern."""
    mock_pattern_registry.get_by_id.return_value = None

    result = await validate_patterns(
        action="validate_single",
        pattern_id="nonexistent",
        validation_type="full",
        pattern_registry=mock_pattern_registry,
        source_registry=mock_source_registry,
        repo_root=tmp_path,
    )

    assert "error" in result
    assert "not found" in result["error"]


@pytest.mark.asyncio
async def test_validate_unknown_action(mock_pattern_registry, mock_source_registry, tmp_path):
    """Test unknown action returns error."""
    result = await validate_patterns(
        action="unknown_action",
        pattern_id=None,
        validation_type="full",
        pattern_registry=mock_pattern_registry,
        source_registry=mock_source_registry,
        repo_root=tmp_path,
    )

    assert "error" in result
    assert "Unknown action" in result["error"]
