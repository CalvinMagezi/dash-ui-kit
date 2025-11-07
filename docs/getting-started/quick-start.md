# Quick Start

Get started with Dash UI Kit in minutes.

## Basic Application

Create a simple Dash application with Dash UI Kit components:

```python
from dash import Dash, html, Input, Output
from dash_ui_kit import Button, Card, CardHeader, CardTitle, CardContent

# Initialize Dash app
app = Dash(__name__)

# Define layout
app.layout = html.Div([
    Card([
        CardHeader([
            CardTitle("Welcome to Dash UI Kit")
        ]),
        CardContent([
            html.P("Build beautiful dashboards with ease!", className="mb-4"),
            Button("Click Me", id="my-button", variant="default")
        ])
    ])
], className="container mx-auto p-8")

# Add callback
@app.callback(
    Output("my-button", "children"),
    Input("my-button", "n_clicks"),
    prevent_initial_call=True
)
def update_button(n_clicks):
    return f"Clicked {n_clicks} times!"

if __name__ == "__main__":
    app.run_server(debug=True)
```

## Using Utility Classes

Dash UI Kit provides Tailwind-like utility classes:

```python
from dash import html

html.Div([
    html.H1("Title", className="text-3xl font-bold mb-4"),
    html.P("Paragraph", className="text-muted-foreground"),
    html.Div(className="flex gap-4 items-center justify-between")
])
```

## Component Variants

Most components support multiple variants:

```python
from dash_ui_kit import Button, Badge

# Button variants
Button("Primary", variant="default")
Button("Outline", variant="outline")
Button("Ghost", variant="ghost")
Button("Danger", variant="destructive")

# Badge variants
Badge("New", variant="default")
Badge("Info", variant="secondary")
Badge("Error", variant="destructive")
```

## Next Steps

- Explore [Component Documentation](../components/overview.md)
- Learn about [Utility Classes](../utilities/overview.md)
- Check out [Examples](../examples/dashboard.md)
