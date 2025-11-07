"""Unit tests for utility functions."""

import pytest

from dash_ui_kit.utils.classnames import cn


def test_cn_basic() -> None:
    """Test basic class name combination."""
    result = cn("btn", "btn-primary")
    assert result == "btn btn-primary"


def test_cn_with_none() -> None:
    """Test cn filters out None values."""
    result = cn("btn", None, "btn-primary")
    assert result == "btn btn-primary"


def test_cn_with_empty_string() -> None:
    """Test cn filters out empty strings."""
    result = cn("btn", "", "btn-primary")
    assert result == "btn btn-primary"


def test_cn_with_false() -> None:
    """Test cn filters out False values."""
    result = cn("btn", False, "btn-primary")
    assert result == "btn btn-primary"


def test_cn_with_dict() -> None:
    """Test cn with dictionary."""
    result = cn("btn", {"btn-primary": True, "btn-large": False})
    assert result == "btn btn-primary"


def test_cn_with_conditional() -> None:
    """Test cn with conditional expressions."""
    is_active = True
    result = cn("btn", is_active and "active")
    assert result == "btn active"

    is_active = False
    result = cn("btn", is_active and "active")
    assert result == "btn"


def test_cn_with_list() -> None:
    """Test cn with list of classes."""
    result = cn("btn", ["btn-primary", "btn-large"])
    assert result == "btn btn-primary btn-large"


def test_cn_empty() -> None:
    """Test cn with no arguments."""
    result = cn()
    assert result == ""


def test_cn_complex() -> None:
    """Test cn with complex combination."""
    is_primary = True
    is_large = False
    result = cn(
        "btn",
        is_primary and "btn-primary",
        {"btn-large": is_large, "btn-medium": True},
        "custom-class",
    )
    assert "btn" in result
    assert "btn-primary" in result
    assert "btn-medium" in result
    assert "custom-class" in result
    assert "btn-large" not in result
