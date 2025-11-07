"""Unit tests for Select component."""

import pytest

from dash_ui_kit import Select


def test_select_renders() -> None:
    """Test Select renders with default props."""
    select = Select(id="test-select")
    assert select.id == "test-select"
    assert "duk-select" in select.className


def test_select_with_options() -> None:
    """Test Select with options."""
    options = [
        {"label": "Option 1", "value": "1"},
        {"label": "Option 2", "value": "2"},
    ]
    select = Select(options=options)
    assert len(select.options) == 2


def test_select_multi() -> None:
    """Test multi-select."""
    select = Select(multi=True)
    assert select.multi is True


def test_select_searchable() -> None:
    """Test searchable prop."""
    select = Select(searchable=False)
    assert select.searchable is False


def test_select_clearable() -> None:
    """Test clearable prop."""
    select = Select(clearable=False)
    assert select.clearable is False


def test_select_disabled() -> None:
    """Test disabled state."""
    select = Select(disabled=True)
    assert select.disabled is True


def test_select_placeholder() -> None:
    """Test placeholder."""
    select = Select(placeholder="Choose an option")
    assert select.placeholder == "Choose an option"


def test_select_value() -> None:
    """Test value prop."""
    select = Select(value="1")
    assert select.value == "1"
