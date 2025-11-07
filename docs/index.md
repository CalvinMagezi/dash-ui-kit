# Dash UI Kit

A lightweight, secure styling library for Plotly Dash applications that provides Tailwind-like utility classes and shadcn-inspired pre-built components.

## Features

✨ **Tailwind-inspired Utilities** - Comprehensive utility classes for rapid UI development

🧩 **Pre-built Components** - Accessible, customizable components out of the box

🔒 **Zero Dependencies** - No npm packages, all assets served locally

🎭 **Theme System** - Easy customization via CSS variables

📦 **Type Safe** - Full type hints for excellent IDE support

⚡ **Lightweight** - < 50KB total CSS bundle size

♿ **Accessible** - WCAG 2.1 AA compliant components

🌓 **Dark Mode** - Built-in dark theme support

## Quick Example

```python
from dash import Dash, html, Input, Output
from dash_ui_kit import Button, Card, CardHeader, CardTitle, CardContent

app = Dash(__name__)

app.layout = html.Div([
    Card([
        CardHeader([
            CardTitle("Welcome to Dash UI Kit")
        ]),
        CardContent([
            html.P("Build beautiful dashboards with ease!"),
            Button("Get Started", id="start-btn", variant="default")
        ])
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True)
```

## Installation

```bash
pip install dash-ui-kit
```

## Next Steps

- [Quick Start Guide](getting-started/quick-start.md)
- [Component Documentation](components/overview.md)
- [Utility Classes](utilities/overview.md)
- [Theming Guide](theming/customization.md)
