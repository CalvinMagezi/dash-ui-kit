# Theming and Customization

Customize Dash UI Kit to match your brand with CSS variables and theme overrides.

## Overview

Dash UI Kit uses CSS variables for all colors, spacing, and design tokens, making it easy to customize the entire library without touching the source code.

## Quick Start

### Method 1: Override CSS Variables

Create a custom CSS file and override the variables:

```css
/* custom_theme.css */
:root {
  --color-primary: 260 100% 50%;  /* Purple primary color */
  --color-accent: 160 80% 45%;    /* Teal accent */
  --radius-md: 1rem;              /* More rounded corners */
}
```

Load it in your Dash app:

```python
app = Dash(__name__, assets_folder="assets")
# Place custom_theme.css in assets/ folder
```

### Method 2: Inline Styles with CSS Variables

```python
app.layout = html.Div([
    # Your content
], style={
    "--color-primary": "220 80% 60%",
    "--radius-md": "0.75rem"
})
```

## Available CSS Variables

### Colors

All colors use HSL format (Hue Saturation Lightness):

```css
:root {
  /* Primary brand color */
  --color-primary: 220 80% 50%;

  /* Secondary/muted color */
  --color-secondary: 210 40% 96%;

  /* Accent color */
  --color-accent: 270 60% 55%;

  /* Background colors */
  --color-background: 0 0% 100%;
  --color-foreground: 222 47% 11%;

  /* Muted colors */
  --color-muted: 210 40% 96%;
  --color-muted-foreground: 215 16% 47%;

  /* Border and input colors */
  --color-border: 214 32% 91%;
  --color-input: 214 32% 91%;
  --color-ring: 220 80% 50%;

  /* Destructive/error color */
  --color-destructive: 0 84% 60%;
  --color-destructive-foreground: 0 0% 98%;
}
```

### Spacing

```css
:root {
  --spacing-0: 0;
  --spacing-1: 0.25rem;
  --spacing-2: 0.5rem;
  --spacing-3: 0.75rem;
  --spacing-4: 1rem;
  --spacing-5: 1.25rem;
  --spacing-6: 1.5rem;
  --spacing-8: 2rem;
  --spacing-10: 2.5rem;
  --spacing-12: 3rem;
  --spacing-16: 4rem;
  --spacing-20: 5rem;
  --spacing-24: 6rem;
}
```

### Typography

```css
:root {
  /* Font sizes */
  --font-size-xs: 0.75rem;
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  --font-size-2xl: 1.5rem;
  --font-size-3xl: 1.875rem;
  --font-size-4xl: 2.25rem;

  /* Font weights */
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  /* Line heights */
  --line-height-tight: 1.25;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.75;
}
```

### Border Radius

```css
:root {
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 1rem;
  --radius-full: 9999px;
}
```

### Shadows

```css
:root {
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
  --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
}
```

### Transition Timings

```css
:root {
  --duration-fast: 150ms;
  --duration-normal: 250ms;
  --duration-slow: 350ms;
}
```

## Theme Examples

### Brand Theme

```css
/* assets/brand_theme.css */
:root {
  /* Company brand colors */
  --color-primary: 210 100% 50%;     /* Brand blue */
  --color-accent: 330 80% 55%;       /* Brand pink */

  /* Adjust secondary colors */
  --color-secondary: 210 40% 98%;

  /* Brand fonts */
  --font-size-base: 1.125rem;        /* Larger base font */
}
```

### Dark Theme

Dash UI Kit includes a dark theme:

```python
app.layout = html.Div([
    # Your content
], className="dark")
```

Custom dark theme:

```css
.dark {
  --color-background: 222 47% 11%;
  --color-foreground: 210 40% 98%;
  --color-muted: 217 33% 17%;
  --color-muted-foreground: 215 20% 65%;
  --color-border: 217 33% 17%;
  --color-input: 217 33% 17%;
  --color-secondary: 217 33% 17%;
}
```

### Minimal Theme

```css
:root {
  /* Monochrome palette */
  --color-primary: 0 0% 20%;
  --color-secondary: 0 0% 96%;
  --color-accent: 0 0% 40%;

  /* Flat design */
  --shadow-md: none;
  --shadow-lg: none;

  /* Sharp corners */
  --radius-md: 0;
  --radius-lg: 0;
}
```

### Playful Theme

```css
:root {
  /* Vibrant colors */
  --color-primary: 280 100% 60%;     /* Purple */
  --color-accent: 160 100% 50%;      /* Cyan */

  /* Rounded design */
  --radius-md: 1rem;
  --radius-lg: 1.5rem;

  /* Strong shadows */
  --shadow-md: 0 8px 16px rgb(0 0 0 / 0.15);
}
```

## Dynamic Theming

### Theme Switcher

```python
from dash import Dash, Input, Output, html
from dash_ui_kit import Button, Select

app = Dash(__name__)

app.layout = html.Div([
    Select(
        id="theme-select",
        options=[
            {"label": "Light", "value": "light"},
            {"label": "Dark", "value": "dark"},
            {"label": "Blue", "value": "blue"}
        ],
        value="light",
        className="w-48 mb-4"
    ),
    html.Div(id="content", children=[
        Card([
            CardHeader([CardTitle("Theme Example")]),
            CardContent([
                html.P("This content changes with the theme")
            ])
        ])
    ])
], id="app-container")

@app.callback(
    Output("app-container", "className"),
    Input("theme-select", "value")
)
def update_theme(theme):
    theme_classes = {
        "light": "",
        "dark": "dark",
        "blue": "theme-blue"
    }
    return theme_classes.get(theme, "")
```

Define custom theme in CSS:

```css
.theme-blue {
  --color-primary: 210 100% 50%;
  --color-background: 210 20% 98%;
}
```

### User Preference Detection

```python
app.layout = html.Div([
    # Your content
], id="app-container")

app.clientside_callback(
    """
    function() {
        const darkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
        return darkMode ? 'dark' : '';
    }
    """,
    Output("app-container", "className"),
    Input("app-container", "id")
)
```

## Component-Specific Customization

### Custom Button Style

```python
Button(
    "Custom Button",
    className="bg-gradient-to-r from-purple-500 to-pink-500"
)
```

### Custom Card

```python
Card([
    CardContent([...])
], className="border-4 border-dashed border-purple-500")
```

## Advanced Customization

### Extend with Custom CSS

```css
/* assets/custom.css */

/* Custom button variant */
.duk-button--custom {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

/* Custom card style */
.card-gradient {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  color: white;
}
```

Use in your app:

```python
Button("Gradient", className="duk-button--custom")
Card([...], className="card-gradient")
```

### CSS Modules (Python-side)

```python
# themes/custom.py
custom_theme = {
    "primary": "260 100% 60%",
    "secondary": "210 40% 96%",
    "accent": "160 80% 50%"
}

# Apply in your app
app.layout = html.Div([...], style={
    f"--color-{key}": value
    for key, value in custom_theme.items()
})
```

## Best Practices

### Do

✅ Override CSS variables for global changes
✅ Use semantic color names
✅ Test dark mode compatibility
✅ Maintain sufficient contrast ratios
✅ Document your custom theme

### Don't

❌ Don't modify source CSS files
❌ Don't hardcode colors in components
❌ Don't break accessibility with custom colors
❌ Don't forget to test all component states

## Accessibility Considerations

When customizing colors:

1. **Contrast Ratios**: Maintain WCAG AA standards (4.5:1 for text)
2. **Focus Indicators**: Ensure focus rings are visible
3. **State Differentiation**: Don't rely on color alone
4. **Dark Mode**: Test all custom colors in dark mode

## Export Your Theme

Create a shareable theme file:

```python
# my_theme.py
"""
Company Brand Theme for Dash UI Kit
"""

THEME_CSS = """
:root {
  --color-primary: 210 100% 50%;
  --color-accent: 330 80% 55%;
  --radius-md: 0.75rem;
}
"""

def apply_theme(app):
    """Apply theme to Dash app."""
    # Write to assets folder
    with open("assets/custom_theme.css", "w") as f:
        f.write(THEME_CSS)
```

## Resources

- [CSS Variables Reference](css-variables.md)
- [Dark Mode Guide](dark-mode.md)
- [Color Palette Generator](https://uicolors.app/)
- [Contrast Checker](https://webaim.org/resources/contrastchecker/)
