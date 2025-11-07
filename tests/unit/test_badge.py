"""Unit tests for Badge component."""

import pytest

from dash_ui_kit import Badge


def test_badge_renders() -> None:
    """Test Badge renders with default props."""
    badge = Badge("New", id="test-badge")
    assert badge.children == "New"
    assert badge.id == "test-badge"
    assert "duk-badge" in badge.className


def test_badge_variants() -> None:
    """Test all badge variants."""
    variants = ["default", "secondary", "outline", "destructive"]
    for variant in variants:
        badge = Badge("Test", variant=variant)  # type: ignore
        assert f"duk-badge--{variant}" in badge.className


def test_badge_sizes() -> None:
    """Test all badge sizes."""
    sizes = ["sm", "md", "lg"]
    for size in sizes:
        badge = Badge("Test", size=size)  # type: ignore
        assert f"duk-badge--{size}" in badge.className


def test_badge_custom_classname() -> None:
    """Test custom className is preserved."""
    badge = Badge("Test", className="custom-class")
    assert "custom-class" in badge.className
    assert "duk-badge" in badge.className
