"""Unit tests for Input components."""

import pytest

from dash_ui_kit import Input, InputError, InputGroup, Label


def test_input_renders() -> None:
    """Test Input renders with default props."""
    input_field = Input(id="test-input")
    assert input_field.id == "test-input"
    assert "duk-input" in input_field.className


def test_input_types() -> None:
    """Test different input types."""
    types = ["text", "email", "password", "number"]
    for input_type in types:
        input_field = Input(type=input_type)  # type: ignore
        assert input_field.type == input_type


def test_input_error_state() -> None:
    """Test input error state."""
    input_field = Input(error=True)
    assert "duk-input--error" in input_field.className


def test_input_disabled() -> None:
    """Test input disabled state."""
    input_field = Input(disabled=True)
    assert input_field.disabled is True


def test_input_placeholder() -> None:
    """Test input placeholder."""
    input_field = Input(placeholder="Enter text")
    assert input_field.placeholder == "Enter text"


def test_input_value() -> None:
    """Test input value."""
    input_field = Input(value="Test value")
    assert input_field.value == "Test value"


def test_label_renders() -> None:
    """Test Label renders correctly."""
    label = Label("Email", htmlFor="email-input")
    assert label.children == "Email"
    assert label.htmlFor == "email-input"
    assert "duk-label" in label.className


def test_input_group_renders() -> None:
    """Test InputGroup renders correctly."""
    group = InputGroup([Label("Test"), Input()], id="test-group")
    assert len(group.children) == 2
    assert "duk-input-group" in group.className


def test_input_error_renders() -> None:
    """Test InputError renders correctly."""
    error = InputError("This field is required", id="test-error")
    assert error.children == "This field is required"
    assert "duk-input-error" in error.className
