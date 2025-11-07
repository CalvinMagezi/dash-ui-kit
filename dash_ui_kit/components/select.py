"""Select/Dropdown component wrapper."""

from typing import Any, List, Optional, Union

from dash import dcc

from dash_ui_kit.utils.classnames import cn

OptionType = dict[str, Any]


def Select(
    id: Optional[str] = None,
    options: Optional[List[OptionType]] = None,
    value: Union[str, int, List[Union[str, int]], None] = None,
    multi: bool = False,
    searchable: bool = True,
    clearable: bool = True,
    placeholder: str = "Select...",
    disabled: bool = False,
    className: str = "",
    **kwargs: Any
) -> dcc.Dropdown:
    """
    A styled dropdown/select component based on dcc.Dropdown.

    Args:
        id: Unique identifier for Dash callbacks
        options: List of option dictionaries with 'label' and 'value' keys
        value: Currently selected value(s)
        multi: Whether to allow multiple selections
        searchable: Whether the dropdown is searchable
        clearable: Whether selected value can be cleared
        placeholder: Placeholder text
        disabled: Whether dropdown is disabled
        className: Additional CSS classes
        **kwargs: Additional props passed to dcc.Dropdown

    Returns:
        dcc.Dropdown: Styled Dash dropdown component

    Example:
        ```python
        from dash_ui_kit import Select

        # Basic select
        Select(
            id="country",
            options=[
                {"label": "USA", "value": "us"},
                {"label": "Canada", "value": "ca"},
                {"label": "Mexico", "value": "mx"}
            ],
            placeholder="Select a country"
        )

        # Multi-select
        Select(
            id="tags",
            options=[
                {"label": "Python", "value": "python"},
                {"label": "JavaScript", "value": "js"},
                {"label": "Go", "value": "go"}
            ],
            multi=True,
            placeholder="Select tags"
        )
        ```
    """
    base_classes = "duk-select"
    select_classes = cn(base_classes, className)

    return dcc.Dropdown(
        id=id,
        options=options or [],
        value=value,
        multi=multi,
        searchable=searchable,
        clearable=clearable,
        placeholder=placeholder,
        disabled=disabled,
        className=select_classes,
        **kwargs,
    )
