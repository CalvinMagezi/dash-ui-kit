# API Reference

Complete API documentation for all Dash UI Kit components and utilities.

## Components

### Button

```python
Button(
    children: Any = None,
    id: str | None = None,
    variant: "default" | "outline" | "ghost" | "destructive" = "default",
    size: "sm" | "md" | "lg" = "md",
    disabled: bool = False,
    loading: bool = False,
    className: str = "",
    n_clicks: int = 0,
    **kwargs: Any
) -> html.Button
```

**Parameters:**

- `children`: Button content (text or components)
- `id`: Unique identifier for Dash callbacks
- `variant`: Visual style variant
- `size`: Button size
- `disabled`: Whether button is disabled
- `loading`: Whether to show loading state
- `className`: Additional CSS classes
- `n_clicks`: Click counter for callbacks
- `**kwargs`: Additional props passed to html.Button

**Returns:** `html.Button` component

**Example:**
```python
Button("Click me", id="btn", variant="default", size="md")
```

---

### Card

```python
Card(
    children: Any = None,
    id: str | None = None,
    variant: "default" | "outlined" | "elevated" = "default",
    className: str = "",
    **kwargs: Any
) -> html.Div
```

**Sub-components:**

#### CardHeader
```python
CardHeader(
    children: Any = None,
    id: str | None = None,
    className: str = "",
    **kwargs: Any
) -> html.Div
```

#### CardTitle
```python
CardTitle(
    children: Any = None,
    id: str | None = None,
    className: str = "",
    **kwargs: Any
) -> html.H3
```

#### CardDescription
```python
CardDescription(
    children: Any = None,
    id: str | None = None,
    className: str = "",
    **kwargs: Any
) -> html.P
```

#### CardContent
```python
CardContent(
    children: Any = None,
    id: str | None = None,
    className: str = "",
    **kwargs: Any
) -> html.Div
```

#### CardFooter
```python
CardFooter(
    children: Any = None,
    id: str | None = None,
    className: str = "",
    **kwargs: Any
) -> html.Div
```

**Example:**
```python
Card([
    CardHeader([CardTitle("Title")]),
    CardContent("Content")
])
```

---

### Input

```python
Input(
    id: str | None = None,
    type: "text" | "email" | "password" | "number" | "tel" | "url" | "search" | "date" | "time" = "text",
    value: str = "",
    placeholder: str = "",
    disabled: bool = False,
    error: bool = False,
    className: str = "",
    **kwargs: Any
) -> dcc.Input
```

**Sub-components:**

#### Label
```python
Label(
    children: Any = None,
    id: str | None = None,
    htmlFor: str | None = None,
    className: str = "",
    **kwargs: Any
) -> html.Label
```

#### InputGroup
```python
InputGroup(
    children: Any = None,
    id: str | None = None,
    className: str = "",
    **kwargs: Any
) -> html.Div
```

#### InputError
```python
InputError(
    children: Any = None,
    id: str | None = None,
    className: str = "",
    **kwargs: Any
) -> html.P
```

**Example:**
```python
InputGroup([
    Label("Email", htmlFor="email"),
    Input(id="email", type="email"),
    InputError("", id="email-error")
])
```

---

### Badge

```python
Badge(
    children: Any = None,
    id: str | None = None,
    variant: "default" | "secondary" | "outline" | "destructive" = "default",
    size: "sm" | "md" | "lg" = "md",
    className: str = "",
    **kwargs: Any
) -> html.Span
```

**Example:**
```python
Badge("New", variant="default", size="sm")
```

---

### Select

```python
Select(
    id: str | None = None,
    options: List[dict] | None = None,
    value: str | int | List[str | int] | None = None,
    multi: bool = False,
    searchable: bool = True,
    clearable: bool = True,
    placeholder: str = "Select...",
    disabled: bool = False,
    className: str = "",
    **kwargs: Any
) -> dcc.Dropdown
```

**Parameters:**

- `options`: List of option dictionaries with 'label' and 'value' keys

**Example:**
```python
Select(
    id="country",
    options=[
        {"label": "USA", "value": "us"},
        {"label": "Canada", "value": "ca"}
    ],
    multi=False
)
```

---

## Utilities

### cn (classnames)

Combine class names conditionally.

```python
cn(*args: Any) -> str
```

**Parameters:**

- `*args`: Any number of class names, None values, or dictionaries

**Returns:** Combined class string

**Examples:**

```python
from dash_ui_kit.utils import cn

# Basic combination
cn("btn", "btn-primary")  # "btn btn-primary"

# With conditionals
cn("btn", is_active and "active")  # "btn active" or "btn"

# With dictionary
cn("btn", {"active": is_active, "disabled": is_disabled})

# With lists
cn("btn", ["btn-primary", "btn-large"])
```

---

## Type Definitions

### VariantType

```python
Literal["default", "secondary", "outline", "ghost", "destructive"]
```

Component style variants.

### SizeType

```python
Literal["sm", "md", "lg"]
```

Component sizes.

### InputType

```python
Literal["text", "email", "password", "number", "tel", "url", "search", "date", "time"]
```

HTML input types.

### Children

```python
Union[DashComponent, List[DashComponent], str, int, float, None]
```

Valid children for components.

---

## Constants

### Version

```python
from dash_ui_kit import __version__

print(__version__)  # "0.1.0"
```

---

## Exceptions

Dash UI Kit does not raise custom exceptions. Invalid props will trigger standard Python TypeErrors or Dash validation errors.

---

## Exports

### Main Module

```python
from dash_ui_kit import (
    # Components
    Button,
    Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter,
    Input, InputGroup, Label, InputError,
    Badge,
    Select,

    # Utilities
    cn,

    # Version
    __version__
)
```

### Type Definitions

```python
from dash_ui_kit.utils.types import (
    Children,
    VariantType,
    SizeType,
    InputType
)
```

---

## CSS Classes

### Button Classes

- `.duk-button` - Base button
- `.duk-button--default` - Default variant
- `.duk-button--outline` - Outline variant
- `.duk-button--ghost` - Ghost variant
- `.duk-button--destructive` - Destructive variant
- `.duk-button--sm` - Small size
- `.duk-button--md` - Medium size
- `.duk-button--lg` - Large size

### Card Classes

- `.duk-card` - Base card
- `.duk-card--outlined` - Outlined variant
- `.duk-card--elevated` - Elevated variant
- `.duk-card-header` - Card header
- `.duk-card-title` - Card title
- `.duk-card-description` - Card description
- `.duk-card-content` - Card content
- `.duk-card-footer` - Card footer

### Input Classes

- `.duk-input` - Base input
- `.duk-input--error` - Error state
- `.duk-label` - Label
- `.duk-input-group` - Input group
- `.duk-input-error` - Error message

### Badge Classes

- `.duk-badge` - Base badge
- `.duk-badge--default` - Default variant
- `.duk-badge--secondary` - Secondary variant
- `.duk-badge--outline` - Outline variant
- `.duk-badge--destructive` - Destructive variant
- `.duk-badge--sm` - Small size
- `.duk-badge--md` - Medium size
- `.duk-badge--lg` - Large size

### Select Classes

- `.duk-select` - Base select

---

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

---

## License

MIT License - See [LICENSE](https://github.com/CalvinMagezi/dash-ui-kit/blob/main/LICENSE)

---

## Contributing

See [CONTRIBUTING.md](https://github.com/CalvinMagezi/dash-ui-kit/blob/main/CONTRIBUTING.md)

---

## Changelog

See [CHANGELOG.md](https://github.com/CalvinMagezi/dash-ui-kit/blob/main/CHANGELOG.md)
