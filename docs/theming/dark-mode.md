# Dark Mode

Enable and customize dark mode in your Dash applications.

## Quick Start

Add the `dark` class to enable dark mode:

```python
app.layout = html.Div([
    # Your content here
], className="dark")
```

## Dark Mode Colors

When dark mode is enabled, these CSS variables are automatically adjusted:

```css
.dark {
  --color-primary: 220 80% 60%;
  --color-secondary: 217 33% 17%;
  --color-accent: 270 60% 65%;
  --color-background: 222 47% 11%;
  --color-foreground: 210 40% 98%;
  --color-muted: 217 33% 17%;
  --color-muted-foreground: 215 20% 65%;
  --color-border: 217 33% 17%;
  --color-input: 217 33% 17%;
  --color-ring: 220 80% 60%;
  --color-destructive: 0 84% 65%;
  --color-destructive-foreground: 0 0% 98%;
}
```

## Theme Toggle

### Basic Toggle

```python
from dash import Dash, Input, Output, html, callback
from dash_ui_kit import Button

app = Dash(__name__)

app.layout = html.Div([
    Button("Toggle Theme", id="theme-toggle"),
    html.Div(id="app-content", children=[
        # Your content
    ])
], id="app-container")

@callback(
    Output("app-container", "className"),
    Input("theme-toggle", "n_clicks"),
    prevent_initial_call=True
)
def toggle_theme(n_clicks):
    return "dark" if n_clicks % 2 else ""
```

### With Icon

```python
@callback(
    [Output("app-container", "className"),
     Output("theme-toggle", "children")],
    Input("theme-toggle", "n_clicks"),
    prevent_initial_call=True
)
def toggle_theme(n_clicks):
    is_dark = n_clicks % 2
    return (
        "dark" if is_dark else "",
        "🌙" if not is_dark else "☀️"
    )
```

## User Preference Detection

Detect system dark mode preference:

```python
app.layout = html.Div([
    # Your content
], id="app-container")

app.clientside_callback(
    """
    function() {
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        return prefersDark ? 'dark' : '';
    }
    """,
    Output("app-container", "className"),
    Input("app-container", "id")
)
```

## Persistent Theme

Save theme preference to localStorage:

```python
app.clientside_callback(
    """
    function(n_clicks) {
        const container = document.getElementById('app-container');
        const isDark = container.classList.contains('dark');
        const newTheme = isDark ? '' : 'dark';

        // Save to localStorage
        localStorage.setItem('theme', newTheme);

        return newTheme;
    }
    """,
    Output("app-container", "className"),
    Input("theme-toggle", "n_clicks"),
    prevent_initial_call=True
)

# Load saved theme on page load
app.clientside_callback(
    """
    function() {
        return localStorage.getItem('theme') || '';
    }
    """,
    Output("app-container", "className"),
    Input("app-container", "id")
)
```

## Custom Dark Theme

Override dark mode colors:

```css
/* assets/custom_dark.css */
.dark {
  --color-primary: 180 100% 50%;    /* Cyan primary */
  --color-background: 230 35% 7%;   /* Deep blue background */
  --color-foreground: 210 40% 98%;
}
```

## Component-Specific Adjustments

Some components may need dark mode specific styles:

```python
Card([
    CardContent([
        html.P("Content")
    ])
], className="bg-background dark:bg-muted")
```

## Testing Dark Mode

Test your app in both modes:

```python
# Light mode
app.layout = html.Div([...], className="")

# Dark mode
app.layout = html.Div([...], className="dark")
```

## Best Practices

1. **Test in both modes**: Always test your app in light and dark mode
2. **Sufficient contrast**: Ensure text is readable in both modes
3. **Images**: Consider different images for dark mode
4. **Charts**: Adjust chart colors for dark backgrounds
5. **Transitions**: Add smooth transitions when switching themes

## Accessibility

- Maintain WCAG contrast ratios in dark mode
- Don't rely on color alone to convey information
- Test with screen readers in both modes

## Related

- [CSS Variables](css-variables.md) - All theme variables
- [Customization](customization.md) - Theming guide
