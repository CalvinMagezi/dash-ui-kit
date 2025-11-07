"""
Dash UI Kit - A lightweight styling library for Plotly Dash applications.

Provides Tailwind-like utility classes and shadcn-inspired pre-built components.
"""

from dash_ui_kit.__version__ import __version__, __version_info__

# Import components
from dash_ui_kit.components.button import Button
from dash_ui_kit.components.card import (
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
)
from dash_ui_kit.components.input import Input, InputError, InputGroup, Label
from dash_ui_kit.components.badge import Badge
from dash_ui_kit.components.select import Select

# Import utilities
from dash_ui_kit.utils.classnames import cn

__all__ = [
    # Version
    "__version__",
    "__version_info__",
    # Components
    "Button",
    "Card",
    "CardContent",
    "CardDescription",
    "CardFooter",
    "CardHeader",
    "CardTitle",
    "Input",
    "InputError",
    "InputGroup",
    "Label",
    "Badge",
    "Select",
    # Utilities
    "cn",
]
