"""Input component with label and error state support."""

from typing import Any, Literal, Optional

from dash import dcc, html

from dash_ui_kit.utils.classnames import cn
from dash_ui_kit.utils.types import Children, InputType


def InputGroup(
    children: Children = None,
    id: Optional[str] = None,
    className: str = "",
    **kwargs: Any
) -> html.Div:
    """
    Container for grouping label, input, and error message.

    Args:
        children: Input group content (Label, Input, InputError)
        id: Unique identifier
        className: Additional CSS classes
        **kwargs: Additional props

    Returns:
        html.Div: Input group container

    Example:
        ```python
        InputGroup([
            Label("Email", htmlFor="email"),
            Input(id="email", type="email"),
            InputError("Invalid email", id="email-error")
        ])
        ```
    """
    return html.Div(
        children, id=id, className=cn("duk-input-group", className), **kwargs
    )


def Label(
    children: Children = None,
    id: Optional[str] = None,
    htmlFor: Optional[str] = None,
    className: str = "",
    **kwargs: Any
) -> html.Label:
    """
    Label for form inputs.

    Args:
        children: Label text
        id: Unique identifier
        htmlFor: ID of the associated input element
        className: Additional CSS classes
        **kwargs: Additional props

    Returns:
        html.Label: Styled label
    """
    return html.Label(
        children, id=id, htmlFor=htmlFor, className=cn("duk-label", className), **kwargs
    )


def Input(
    id: Optional[str] = None,
    type: InputType = "text",
    value: str = "",
    placeholder: str = "",
    disabled: bool = False,
    error: bool = False,
    className: str = "",
    **kwargs: Any
) -> dcc.Input:
    """
    Text input component with various types.

    Args:
        id: Unique identifier for Dash callbacks
        type: Input type (text, email, password, number, etc.)
        value: Current input value
        placeholder: Placeholder text
        disabled: Whether input is disabled
        error: Whether input is in error state
        className: Additional CSS classes
        **kwargs: Additional props passed to dcc.Input

    Returns:
        dcc.Input: Styled Dash input component

    Example:
        ```python
        # Basic input
        Input(id="username", placeholder="Enter username")

        # Email input
        Input(id="email", type="email", placeholder="your@email.com")

        # Password input
        Input(id="password", type="password")

        # Input with error
        Input(id="email", error=True)
        ```
    """
    base_classes = "duk-input"
    error_class = "duk-input--error" if error else ""

    input_classes = cn(base_classes, error_class, className)

    return dcc.Input(
        id=id,
        type=type,
        value=value,
        placeholder=placeholder,
        disabled=disabled,
        className=input_classes,
        **kwargs,
    )


def InputError(
    children: Children = None,
    id: Optional[str] = None,
    className: str = "",
    **kwargs: Any
) -> html.P:
    """
    Error message for inputs.

    Args:
        children: Error message text
        id: Unique identifier
        className: Additional CSS classes
        **kwargs: Additional props

    Returns:
        html.P: Styled error message
    """
    return html.P(
        children, id=id, className=cn("duk-input-error", className), **kwargs
    )
