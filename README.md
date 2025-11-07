# Dash UI Kit

[![PyPI version](https://badge.fury.io/py/dash-ui-kit.svg)](https://badge.fury.io/py/dash-ui-kit)
[![Python versions](https://img.shields.io/pypi/pyversions/dash-ui-kit.svg)](https://pypi.org/project/dash-ui-kit/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/CalvinMagezi/dash-ui-kit/workflows/Tests/badge.svg)](https://github.com/CalvinMagezi/dash-ui-kit/actions)
[![Coverage](https://codecov.io/gh/CalvinMagezi/dash-ui-kit/branch/main/graph/badge.svg)](https://codecov.io/gh/CalvinMagezi/dash-ui-kit)

A lightweight, secure styling library for Plotly Dash applications that provides Tailwind-like utility classes and shadcn-inspired pre-built components.

## ✨ Features

- 🎨 **Tailwind-inspired Utilities** - Comprehensive utility classes for rapid UI development
- 🧩 **Pre-built Components** - Accessible, customizable components out of the box
- 🔒 **Zero Dependencies** - No npm packages, all assets served locally
- 🎭 **Theme System** - Easy customization via CSS variables
- 📦 **Type Safe** - Full type hints for excellent IDE support
- ⚡ **Lightweight** - < 50KB total CSS bundle size
- ♿ **Accessible** - WCAG 2.1 AA compliant components
- 🌓 **Dark Mode** - Built-in dark theme support

## 🚀 Quick Start

### Installation

```bash
pip install dash-ui-kit
```

### Basic Usage

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
            html.P("Build beautiful dashboards with ease!", className="text-muted mb-4"),
            Button("Get Started", id="start-btn", variant="default", size="lg")
        ])
    ], className="max-w-md mx-auto mt-8")
], className="min-h-screen bg-background p-4")

@app.callback(
    Output("start-btn", "children"),
    Input("start-btn", "n_clicks"),
    prevent_initial_call=True
)
def update_button(n_clicks):
    return f"Clicked {n_clicks} times!"

if __name__ == "__main__":
    app.run_server(debug=True)
```

## 📚 Components

### Button

Multiple variants and sizes for different use cases:

```python
from dash_ui_kit import Button

# Variants
Button("Primary", variant="default")
Button("Outline", variant="outline")
Button("Ghost", variant="ghost")
Button("Danger", variant="destructive")

# Sizes
Button("Small", size="sm")
Button("Medium", size="md")
Button("Large", size="lg")

# States
Button("Disabled", disabled=True)
Button("Loading", loading=True)
```

### Card

Flexible card component with sub-components:

```python
from dash_ui_kit import Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter

Card([
    CardHeader([
        CardTitle("Card Title"),
        CardDescription("Card description goes here")
    ]),
    CardContent([
        html.P("Your content here")
    ]),
    CardFooter([
        Button("Action")
    ])
])
```

### Input

Form inputs with labels and error states:

```python
from dash_ui_kit import Input, InputGroup, Label, InputError

InputGroup([
    Label("Email", htmlFor="email"),
    Input(id="email", type="email", placeholder="Enter your email"),
    InputError("Invalid email address", id="email-error")
])
```

### Badge

Small labels and tags:

```python
from dash_ui_kit import Badge

Badge("New", variant="default")
Badge("Warning", variant="secondary")
Badge("Error", variant="destructive")
```

## 🎨 Utility Classes

Dash UI Kit includes a comprehensive set of utility classes inspired by Tailwind CSS:

### Spacing

```python
html.Div(className="p-4 m-2")  # Padding and margin
html.Div(className="px-6 py-3")  # Horizontal and vertical
html.Div(className="mt-4 mb-2")  # Individual sides
```

### Layout

```python
html.Div(className="flex items-center justify-between")
html.Div(className="grid grid-cols-3 gap-4")
html.Div(className="flex-col space-y-2")
```

### Typography

```python
html.H1(className="text-3xl font-bold text-primary")
html.P(className="text-sm text-muted")
```

### Colors

```python
html.Div(className="bg-primary text-white")
html.Div(className="bg-secondary text-foreground")
html.Div(className="border-2 border-accent")
```

### Effects

```python
html.Div(className="rounded-lg shadow-md")
html.Button(className="hover:opacity-80 transition")
```

## 🎭 Theming

Customize the look and feel using CSS variables:

```css
:root {
  --color-primary: 220 80% 50%;
  --color-secondary: 210 40% 96%;
  --color-accent: 270 60% 55%;
  --color-background: 0 0% 100%;
  --color-foreground: 222 47% 11%;
  --color-muted: 210 40% 96%;
  --color-border: 214 32% 91%;

  --spacing-base: 0.25rem;
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 1rem;
}
```

### Dark Mode

```python
html.Div(className="dark", children=[
    # Your app content
])
```

## 📖 Documentation

Full documentation is available at [https://dash-ui-kit.readthedocs.io/](https://dash-ui-kit.readthedocs.io/)

- [Getting Started](https://dash-ui-kit.readthedocs.io/getting-started)
- [Components](https://dash-ui-kit.readthedocs.io/components)
- [Utilities](https://dash-ui-kit.readthedocs.io/utilities)
- [Theming](https://dash-ui-kit.readthedocs.io/theming)
- [Examples](https://dash-ui-kit.readthedocs.io/examples)

## 🧪 Development

### Setup

```bash
# Clone the repository
git clone https://github.com/CalvinMagezi/dash-ui-kit.git
cd dash-ui-kit

# Install dependencies
pip install -e ".[dev]"

# Set up pre-commit hooks
pre-commit install
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=dash_ui_kit --cov-report=html

# Run specific test types
pytest -m unit
pytest -m integration
```

### Building CSS

```bash
# Generate utility CSS
python scripts/generate_utilities.py

# Build complete CSS bundle
python scripts/build_css.py
```

### Documentation

```bash
# Serve documentation locally
mkdocs serve

# Build documentation
mkdocs build
```

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linters (`pytest`, `black .`, `ruff .`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by [Tailwind CSS](https://tailwindcss.com/)
- Component design inspired by [shadcn/ui](https://ui.shadcn.com/)
- Built for [Plotly Dash](https://dash.plotly.com/)

## 📬 Contact

Calvin Magezi - [@CalvinMagezi](https://github.com/CalvinMagezi)

Project Link: [https://github.com/CalvinMagezi/dash-ui-kit](https://github.com/CalvinMagezi/dash-ui-kit)

## 🗺️ Roadmap

- [x] Core utility system
- [x] Basic components (Button, Card, Input, Badge)
- [ ] Advanced components (Modal, Alert, Table, Tabs)
- [ ] Responsive utilities
- [ ] CLI tools
- [ ] Theme generator
- [ ] VSCode extension

---

Made with ❤️ by Calvin at TotalEnergies
