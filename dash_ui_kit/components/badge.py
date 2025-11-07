"""Badge component for labels and tags."""

from typing import Any, Literal, Optional

from dash import html

from dash_ui_kit.utils.classnames import cn
from dash_ui_kit.utils.types import Children

VariantType = Literal["default", "secondary", "outline", "destructive"]
SizeType = Literal["sm", "md", "lg"]


def Badge(
    children: Children = None,
    id: Optional[str] = None,
    variant: VariantType = "default",
    size: SizeType = "md",
    className: str = "",
    **kwargs: Any
) -> html.Span:
    """
    A badge component for displaying labels, tags, or status indicators.

    Args:
        children: Badge content (text)
        id: Unique identifier for Dash callbacks
        variant: Visual style variant
            - "default": Primary colored badge
            - "secondary": Muted/secondary badge
            - "outline": Outlined badge
            - "destructive": Danger/warning badge
        size: Badge size
            - "sm": Small
            - "md": Medium
            - "lg": Large
        className: Additional CSS classes
        **kwargs: Additional props passed to html.Span

    Returns:
        html.Span: Styled badge component

    Example:
        ```python
        from dash_ui_kit import Badge

        # Basic badge
        Badge("New")

        # Variant examples
        Badge("Primary", variant="default")
        Badge("Secondary", variant="secondary")
        Badge("Outline", variant="outline")
        Badge("Error", variant="destructive")

        # Size examples
        Badge("Small", size="sm")
        Badge("Medium", size="md")
        Badge("Large", size="lg")
        ```
    """
    # Base badge classes
    base_classes = "duk-badge"

    # Variant classes
    variant_classes = f"duk-badge--{variant}"

    # Size classes
    size_classes = f"duk-badge--{size}"

    # Compose final class string
    badge_classes = cn(base_classes, variant_classes, size_classes, className)

    return html.Span(children, id=id, className=badge_classes, **kwargs)
