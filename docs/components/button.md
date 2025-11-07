# Button Component

Interactive buttons with multiple variants, sizes, and states.

## Overview

The Button component provides a consistent, accessible way to create clickable buttons in your Dash applications. It supports multiple visual variants, sizes, loading states, and full integration with Dash callbacks.

## Import

```python
from dash_ui_kit import Button
```

## Basic Usage

```python
Button("Click me", id="my-button")
```

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `Any` | `None` | Button content (text or components) |
| `id` | `str` | `None` | Unique identifier for Dash callbacks |
| `variant` | `"default" \| "outline" \| "ghost" \| "destructive"` | `"default"` | Visual style variant |
| `size` | `"sm" \| "md" \| "lg"` | `"md"` | Button size |
| `disabled` | `bool` | `False` | Whether button is disabled |
| `loading` | `bool` | `False` | Whether to show loading state |
| `className` | `str` | `""` | Additional CSS classes |
| `n_clicks` | `int` | `0` | Click counter for callbacks |

## Variants

### Default (Primary)

```python
Button("Default Button", variant="default")
```

Solid background with primary color. Use for primary actions.

### Outline

```python
Button("Outline Button", variant="outline")
```

Transparent background with border. Use for secondary actions.

### Ghost

```python
Button("Ghost Button", variant="ghost")
```

Transparent background without border. Use for tertiary actions.

### Destructive

```python
Button("Delete", variant="destructive")
```

Red/danger styling. Use for destructive actions like delete or remove.

## Sizes

```python
# Small
Button("Small", size="sm")

# Medium (default)
Button("Medium", size="md")

# Large
Button("Large", size="lg")
```

## States

### Disabled

```python
Button("Disabled", disabled=True)
```

### Loading

```python
Button("Loading", loading=True)
```

Shows a loading spinner and automatically disables the button.

## With Callbacks

```python
from dash import Dash, Input, Output, html
from dash_ui_kit import Button

app = Dash(__name__)

app.layout = html.Div([
    Button("Click Me", id="my-btn", variant="default"),
    html.Div(id="output")
])

@app.callback(
    Output("output", "children"),
    Input("my-btn", "n_clicks"),
    prevent_initial_call=True
)
def handle_click(n_clicks):
    return f"Button clicked {n_clicks} times"
```

## Examples

### Action Buttons

```python
html.Div([
    Button("Save", id="save-btn", variant="default"),
    Button("Cancel", id="cancel-btn", variant="outline"),
], className="flex gap-2")
```

### With Icons (using HTML entities)

```python
Button([
    html.Span("📥 ", className="mr-2"),
    "Download"
], variant="default")
```

### Full Width

```python
Button("Continue", className="w-full", variant="default")
```

### Button Group

```python
html.Div([
    Button("Left", variant="outline"),
    Button("Center", variant="outline"),
    Button("Right", variant="outline"),
], className="flex gap-0 border rounded-md")
```

## Accessibility

- Keyboard accessible (can be focused and activated with Enter/Space)
- Disabled buttons are not focusable
- Focus ring visible on keyboard navigation
- Works with screen readers

## Styling

The Button component uses these CSS classes:

- `.duk-button` - Base button styles
- `.duk-button--{variant}` - Variant-specific styles
- `.duk-button--{size}` - Size-specific styles

You can extend styling with the `className` prop:

```python
Button("Custom", className="shadow-lg hover:scale-105")
```

## Best Practices

1. **Use appropriate variants**: Primary actions get "default", secondary get "outline"
2. **Destructive actions**: Always use "destructive" variant for delete/remove actions
3. **Loading states**: Show loading state during async operations
4. **Disable when appropriate**: Disable buttons when actions can't be performed
5. **Clear labels**: Use descriptive text that indicates the action

## Related Components

- [Card](card.md) - Often contains buttons in CardFooter
- [Input](input.md) - Typically paired with submit buttons
