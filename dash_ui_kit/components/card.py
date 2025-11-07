"""Card component with sub-components for structured content."""

from typing import Any, Literal, Optional

from dash import html

from dash_ui_kit.utils.classnames import cn
from dash_ui_kit.utils.types import Children

VariantType = Literal["default", "outlined", "elevated"]


def Card(
    children: Children = None,
    id: Optional[str] = None,
    variant: VariantType = "default",
    className: str = "",
    **kwargs: Any
) -> html.Div:
    """
    A card container component for grouping related content.

    Args:
        children: Card content (typically CardHeader, CardContent, CardFooter)
        id: Unique identifier for Dash callbacks
        variant: Visual style variant
            - "default": Standard card with border
            - "outlined": Card with thicker border
            - "elevated": Card with shadow, no border
        className: Additional CSS classes
        **kwargs: Additional props passed to html.Div

    Returns:
        html.Div: Styled card container

    Example:
        ```python
        from dash_ui_kit import Card, CardHeader, CardTitle, CardContent

        Card([
            CardHeader([
                CardTitle("Card Title")
            ]),
            CardContent([
                html.P("Card content goes here")
            ])
        ])
        ```
    """
    base_classes = "duk-card"
    variant_classes = f"duk-card--{variant}" if variant != "default" else ""

    card_classes = cn(base_classes, variant_classes, className)

    return html.Div(children, id=id, className=card_classes, **kwargs)


def CardHeader(
    children: Children = None,
    id: Optional[str] = None,
    className: str = "",
    **kwargs: Any
) -> html.Div:
    """
    Card header section, typically contains CardTitle and CardDescription.

    Args:
        children: Header content
        id: Unique identifier
        className: Additional CSS classes
        **kwargs: Additional props

    Returns:
        html.Div: Styled card header
    """
    return html.Div(children, id=id, className=cn("duk-card-header", className), **kwargs)


def CardTitle(
    children: Children = None,
    id: Optional[str] = None,
    className: str = "",
    **kwargs: Any
) -> html.H3:
    """
    Card title component.

    Args:
        children: Title text
        id: Unique identifier
        className: Additional CSS classes
        **kwargs: Additional props

    Returns:
        html.H3: Styled card title
    """
    return html.H3(children, id=id, className=cn("duk-card-title", className), **kwargs)


def CardDescription(
    children: Children = None,
    id: Optional[str] = None,
    className: str = "",
    **kwargs: Any
) -> html.P:
    """
    Card description component.

    Args:
        children: Description text
        id: Unique identifier
        className: Additional CSS classes
        **kwargs: Additional props

    Returns:
        html.P: Styled card description
    """
    return html.P(
        children, id=id, className=cn("duk-card-description", className), **kwargs
    )


def CardContent(
    children: Children = None,
    id: Optional[str] = None,
    className: str = "",
    **kwargs: Any
) -> html.Div:
    """
    Card content section, main body of the card.

    Args:
        children: Card content
        id: Unique identifier
        className: Additional CSS classes
        **kwargs: Additional props

    Returns:
        html.Div: Styled card content
    """
    return html.Div(
        children, id=id, className=cn("duk-card-content", className), **kwargs
    )


def CardFooter(
    children: Children = None,
    id: Optional[str] = None,
    className: str = "",
    **kwargs: Any
) -> html.Div:
    """
    Card footer section, typically contains actions or additional info.

    Args:
        children: Footer content
        id: Unique identifier
        className: Additional CSS classes
        **kwargs: Additional props

    Returns:
        html.Div: Styled card footer
    """
    return html.Div(
        children, id=id, className=cn("duk-card-footer", className), **kwargs
    )
