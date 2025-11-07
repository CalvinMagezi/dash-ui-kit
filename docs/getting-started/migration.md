# Migration Guide

## From Plain Dash

Migrating from plain Dash to Dash UI Kit is straightforward:

### Before (Plain Dash)

```python
from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.Button(
        "Click me",
        id="btn",
        style={
            "padding": "8px 16px",
            "backgroundColor": "#007bff",
            "color": "white",
            "border": "none",
            "borderRadius": "4px"
        }
    )
])
```

### After (Dash UI Kit)

```python
from dash import Dash, html
from dash_ui_kit import Button

app = Dash(__name__)

app.layout = html.Div([
    Button("Click me", id="btn", variant="default")
])
```

## From Other CSS Frameworks

### From Dash Bootstrap Components

```python
# Before (dbc)
import dash_bootstrap_components as dbc

dbc.Button("Click me", color="primary")
dbc.Card([
    dbc.CardHeader("Title"),
    dbc.CardBody("Content")
])

# After (Dash UI Kit)
from dash_ui_kit import Button, Card, CardHeader, CardTitle, CardContent

Button("Click me", variant="default")
Card([
    CardHeader([CardTitle("Title")]),
    CardContent("Content")
])
```

## Key Differences

1. **Utility-First Approach**: Use className utilities instead of inline styles
2. **Component Composition**: Card uses sub-components for structure
3. **Type Safety**: Full type hints for better IDE support
4. **Lighter Bundle**: No Bootstrap dependency

## Need Help?

If you encounter issues during migration, please:

1. Check the [Component Documentation](../components/overview.md)
2. Review [Examples](../examples/dashboard.md)
3. Open an issue on [GitHub](https://github.com/CalvinMagezi/dash-ui-kit/issues)
