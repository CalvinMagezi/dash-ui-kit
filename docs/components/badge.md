# Badge Component

Small labels and status indicators for displaying metadata, counts, and status information.

## Overview

The Badge component provides a compact way to display labels, tags, counts, and status information. It supports multiple variants and sizes to fit different use cases.

## Import

```python
from dash_ui_kit import Badge
```

## Basic Usage

```python
Badge("New")
```

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `Any` | `None` | Badge content (text or components) |
| `id` | `str` | `None` | Unique identifier |
| `variant` | `"default" \| "secondary" \| "outline" \| "destructive"` | `"default"` | Visual style variant |
| `size` | `"sm" \| "md" \| "lg"` | `"md"` | Badge size |
| `className` | `str` | `""` | Additional CSS classes |

## Variants

### Default (Primary)

```python
Badge("New", variant="default")
```

Solid primary color. Use for important status or new items.

### Secondary

```python
Badge("Info", variant="secondary")
```

Muted background. Use for secondary or informational badges.

### Outline

```python
Badge("Draft", variant="outline")
```

Transparent with border. Use for neutral status indicators.

### Destructive

```python
Badge("Error", variant="destructive")
```

Red/danger color. Use for errors, warnings, or critical status.

## Sizes

```python
# Small
Badge("Small", size="sm")

# Medium (default)
Badge("Medium", size="md")

# Large
Badge("Large", size="lg")
```

## Examples

### Status Indicators

```python
html.Div([
    Badge("Active", variant="default"),
    Badge("Pending", variant="secondary"),
    Badge("Draft", variant="outline"),
    Badge("Error", variant="destructive")
], className="flex gap-2")
```

### Notification Count

```python
html.Div([
    html.Span("Messages"),
    Badge("3", variant="destructive", size="sm", className="ml-2")
], className="flex items-center")
```

### Tags

```python
html.Div([
    Badge("Python", variant="outline", size="sm"),
    Badge("JavaScript", variant="outline", size="sm"),
    Badge("React", variant="outline", size="sm")
], className="flex gap-2")
```

### With Icons

```python
Badge([
    html.Span("✓ ", className="mr-1"),
    "Verified"
], variant="default")
```

### In Card Headers

```python
Card([
    CardHeader([
        html.Div([
            CardTitle("Notifications"),
            Badge("5", variant="destructive", size="sm", className="ml-2")
        ], className="flex items-center")
    ]),
    CardContent([
        html.P("You have 5 unread notifications")
    ])
])
```

### Product Labels

```python
html.Div([
    html.H3("Premium Plan"),
    Badge("Popular", variant="default", size="sm", className="ml-2")
], className="flex items-center")
```

### Status with Color Coding

```python
def get_status_badge(status):
    variants = {
        "success": "default",
        "pending": "secondary",
        "warning": "outline",
        "error": "destructive"
    }
    return Badge(status.title(), variant=variants.get(status, "secondary"))

# Usage
html.Div([
    get_status_badge("success"),
    get_status_badge("pending"),
    get_status_badge("error")
], className="flex gap-2")
```

### Table Status Column

```python
html.Table([
    html.Thead([
        html.Tr([
            html.Th("Name"),
            html.Th("Status"),
            html.Th("Priority")
        ])
    ]),
    html.Tbody([
        html.Tr([
            html.Td("Task 1"),
            html.Td(Badge("Complete", variant="default", size="sm")),
            html.Td(Badge("High", variant="destructive", size="sm"))
        ]),
        html.Tr([
            html.Td("Task 2"),
            html.Td(Badge("In Progress", variant="secondary", size="sm")),
            html.Td(Badge("Medium", variant="outline", size="sm"))
        ])
    ])
])
```

### Version Badge

```python
html.Div([
    html.H1("Dash UI Kit"),
    Badge("v0.1.0", variant="secondary", size="sm", className="ml-2")
], className="flex items-center")
```

### Category Tags

```python
html.Div([
    html.H3("Article Title", className="mb-2"),
    html.Div([
        Badge("Tutorial", variant="outline", size="sm"),
        Badge("Python", variant="outline", size="sm"),
        Badge("Beginner", variant="outline", size="sm")
    ], className="flex gap-2")
])
```

### Counter Badge

```python
html.Button([
    html.Span("Cart"),
    Badge("12", variant="destructive", size="sm", className="ml-2")
], className="duk-button duk-button--outline duk-button--md")
```

### Feature Flags

```python
html.Div([
    html.Span("Dark Mode"),
    Badge("Beta", variant="secondary", size="sm", className="ml-2")
], className="flex items-center")
```

### List with Badges

```python
html.Ul([
    html.Li([
        html.Span("Feature 1 "),
        Badge("New", variant="default", size="sm")
    ], className="mb-2"),
    html.Li([
        html.Span("Feature 2 "),
        Badge("Updated", variant="secondary", size="sm")
    ], className="mb-2"),
    html.Li([
        html.Span("Feature 3 "),
        Badge("Deprecated", variant="outline", size="sm")
    ])
])
```

### User Role Badge

```python
html.Div([
    html.Img(src="/avatar.jpg", className="w-10 h-10 rounded-full"),
    html.Div([
        html.P("John Doe", className="font-medium"),
        Badge("Admin", variant="default", size="sm")
    ], className="ml-3")
], className="flex items-center")
```

## Use Cases

### E-commerce

```python
html.Div([
    html.Img(src="/product.jpg"),
    html.Div([
        Badge("Sale", variant="destructive", size="sm", className="absolute top-2 right-2")
    ])
], className="relative")
```

### Dashboard Metrics

```python
Card([
    CardHeader([CardTitle("API Status")]),
    CardContent([
        html.Div([
            html.Span("Uptime"),
            Badge("99.9%", variant="default", size="sm", className="ml-2")
        ], className="flex justify-between items-center mb-2"),
        html.Div([
            html.Span("Response Time"),
            Badge("45ms", variant="secondary", size="sm", className="ml-2")
        ], className="flex justify-between items-center")
    ])
])
```

### Notification Badge

```python
html.Div([
    html.Button("Notifications", className="duk-button duk-button--ghost duk-button--md"),
    Badge("3", variant="destructive", size="sm",
          className="absolute -top-1 -right-1 min-w-5 h-5 flex items-center justify-center rounded-full")
], className="relative")
```

## Dynamic Badges with Callbacks

```python
from dash import Dash, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.Div(id="badge-container"),
    Button("Update Status", id="update-btn")
])

@app.callback(
    Output("badge-container", "children"),
    Input("update-btn", "n_clicks")
)
def update_badge(n_clicks):
    if not n_clicks:
        return Badge("Idle", variant="secondary")

    status_map = {
        1: ("Processing", "default"),
        2: ("Complete", "default"),
        3: ("Error", "destructive")
    }

    status = (n_clicks % 3) + 1
    text, variant = status_map[status]
    return Badge(text, variant=variant)
```

## Accessibility

- Uses semantic HTML (span element)
- Color is not the only indicator (text provides context)
- Sufficient color contrast for readability
- Works with screen readers

## Styling

The Badge component uses these CSS classes:

- `.duk-badge` - Base badge styles
- `.duk-badge--{variant}` - Variant-specific styles
- `.duk-badge--{size}` - Size-specific styles

You can extend styling with the `className` prop:

```python
Badge("Custom", className="animate-pulse")
```

## Best Practices

1. **Keep it short**: Badges work best with 1-3 words or short numbers
2. **Use appropriate variants**: Match variant to semantic meaning
3. **Consistent usage**: Use similar patterns across your app
4. **Don't overuse**: Too many badges can clutter the UI
5. **Provide context**: Badge meaning should be clear from context or text

## Related Components

- [Button](button.md) - Can contain badges for counters
- [Card](card.md) - Often contain badges in headers
