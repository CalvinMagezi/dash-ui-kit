"""Button component with multiple variants and sizes."""

from typing import Any, Literal, Optional, Union

from dash import html

from dash_ui_kit.utils.classnames import cn
from dash_ui_kit.utils.types import Children

VariantType = Literal["default", "outline", "ghost", "destructive"]
SizeType = Literal["sm", "md", "lg"]


def Button(
    children: Children = None,
    id: Optional[str] = None,
    variant: VariantType = "default",
    size: SizeType = "md",
    disabled: bool = False,
    loading: bool = False,
    className: str = "",
    n_clicks: int = 0,
    **kwargs: Any
) -> html.Button:
    """
    A button component with multiple variants and sizes.

    Args:
        children: Button content (text or components)
        id: Unique identifier for Dash callbacks
        variant: Visual style variant
            - "default": Primary colored button
            - "outline": Outlined button
            - "ghost": Text-only button
            - "destructive": Danger/warning button
        size: Button size
            - "sm": Small (32px height)
            - "md": Medium (40px height)
            - "lg": Large (48px height)
        disabled: Whether button is disabled
        loading: Whether to show loading state
        className: Additional CSS classes
        n_clicks: Click counter (Dash callback property)
        **kwargs: Additional props passed to html.Button

    Returns:
        html.Button: Styled Dash button component

    Example:
        ```python
        from dash_ui_kit import Button

        # Basic button
        Button("Click me", id="submit-btn")

        # Variant examples
        Button("Primary", variant="default")
        Button("Outline", variant="outline")
        Button("Ghost", variant="ghost")
        Button("Delete", variant="destructive")

        # Size examples
        Button("Small", size="sm")
        Button("Medium", size="md")
        Button("Large", size="lg")

        # States
        Button("Disabled", disabled=True)
        Button("Loading", loading=True)
        ```
    """
    # Base button classes
    base_classes = "duk-button"

    # Variant classes
    variant_classes = f"duk-button--{variant}"

    # Size classes
    size_classes = f"duk-button--{size}"

    # Compose final class string
    button_classes = cn(base_classes, variant_classes, size_classes, className)

    # Handle loading state
    if loading:
        children = html.Div(
            [
                html.Span("⏳", className="inline-block animate-spin mr-2"),
                children,
            ],
            className="flex items-center",
        )
        disabled = True

    return html.Button(
        children,
        id=id,
        className=button_classes,
        disabled=disabled or loading,
        n_clicks=n_clicks,
        **kwargs,
    )
