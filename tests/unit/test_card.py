"""Unit tests for Card components."""

import pytest
from dash import html

from dash_ui_kit import (
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
)


def test_card_renders() -> None:
    """Test Card renders with default props."""
    card = Card("Test content", id="test-card")
    assert card.children == "Test content"
    assert card.id == "test-card"
    assert "duk-card" in card.className


def test_card_variants() -> None:
    """Test Card variants."""
    variants = ["default", "outlined", "elevated"]
    for variant in variants:
        card = Card("Test", variant=variant)  # type: ignore
        if variant != "default":
            assert f"duk-card--{variant}" in card.className


def test_card_header() -> None:
    """Test CardHeader renders correctly."""
    header = CardHeader("Header content", id="test-header")
    assert header.children == "Header content"
    assert "duk-card-header" in header.className


def test_card_title() -> None:
    """Test CardTitle renders correctly."""
    title = CardTitle("Title", id="test-title")
    assert title.children == "Title"
    assert "duk-card-title" in title.className


def test_card_description() -> None:
    """Test CardDescription renders correctly."""
    desc = CardDescription("Description", id="test-desc")
    assert desc.children == "Description"
    assert "duk-card-description" in desc.className


def test_card_content() -> None:
    """Test CardContent renders correctly."""
    content = CardContent("Content", id="test-content")
    assert content.children == "Content"
    assert "duk-card-content" in content.className


def test_card_footer() -> None:
    """Test CardFooter renders correctly."""
    footer = CardFooter("Footer", id="test-footer")
    assert footer.children == "Footer"
    assert "duk-card-footer" in footer.className


def test_card_composition() -> None:
    """Test Card with all sub-components."""
    card = Card(
        [
            CardHeader([CardTitle("Title"), CardDescription("Description")]),
            CardContent("Content"),
            CardFooter("Footer"),
        ]
    )
    assert "duk-card" in card.className
    assert len(card.children) == 3
