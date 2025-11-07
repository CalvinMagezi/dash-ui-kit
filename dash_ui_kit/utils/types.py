"""Type definitions for dash-ui-kit."""

from typing import Any, Dict, List, Literal, Optional, Union

# Component children can be a single element or list of elements
DashComponent = Any
Children = Union[DashComponent, List[DashComponent], str, int, float, None]

# Common component props
ComponentProps = Dict[str, Any]

# Size variants used across components
SizeType = Literal["sm", "md", "lg"]

# Common color variants
VariantType = Literal["default", "secondary", "outline", "ghost", "destructive"]

# Input types
InputType = Literal[
    "text", "email", "password", "number", "tel", "url", "search", "date", "time"
]
