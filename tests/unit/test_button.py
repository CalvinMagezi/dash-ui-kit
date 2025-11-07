"""Unit tests for Button component."""

import pytest

from dash_ui_kit import Button


def test_button_renders() -> None:
    """Test button renders with default props."""
    button = Button("Click me", id="test-btn")
    assert button.children == "Click me"
    assert button.id == "test-btn"
    assert "duk-button" in button.className


def test_button_variants() -> None:
    """Test all button variants render correctly."""
    variants = ["default", "outline", "ghost", "destructive"]
    for variant in variants:
        button = Button("Test", variant=variant)  # type: ignore
        assert f"duk-button--{variant}" in button.className


def test_button_sizes() -> None:
    """Test all button sizes."""
    sizes = ["sm", "md", "lg"]
    for size in sizes:
        button = Button("Test", size=size)  # type: ignore
        assert f"duk-button--{size}" in button.className


def test_button_disabled() -> None:
    """Test disabled state."""
    button = Button("Test", disabled=True)
    assert button.disabled is True


def test_button_loading() -> None:
    """Test loading state."""
    button = Button("Test", loading=True)
    assert button.disabled is True


def test_button_custom_classname() -> None:
    """Test custom className is preserved."""
    button = Button("Test", className="custom-class")
    assert "custom-class" in button.className
    assert "duk-button" in button.className


def test_button_n_clicks() -> None:
    """Test n_clicks prop."""
    button = Button("Test", n_clicks=5)
    assert button.n_clicks == 5
