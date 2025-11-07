# Utility Classes Overview

Dash UI Kit provides a comprehensive set of utility classes inspired by Tailwind CSS, allowing you to rapidly build UIs with consistent styling.

## Philosophy

Utility classes allow you to build custom designs without writing custom CSS. Each class does one thing well, and by combining them, you can create any design you need.

### Traditional Approach

```python
# With custom CSS
html.Div("Content", style={"padding": "16px", "margin-bottom": "8px", "background-color": "#f0f0f0"})
```

### Utility-First Approach

```python
# With utility classes
html.Div("Content", className="p-4 mb-2 bg-muted")
```

## Available Utility Categories

### [Spacing](spacing.md)
Margin and padding utilities for controlling element spacing.

```python
className="p-4 m-2 px-6 py-3 mt-4 mb-2"
```

### [Layout](layout.md)
Flexbox, grid, and display utilities for layout control.

```python
className="flex items-center justify-between gap-4"
```

### [Typography](typography.md)
Font size, weight, alignment, and text utilities.

```python
className="text-lg font-bold text-center"
```

### [Colors](colors.md)
Text, background, and border color utilities.

```python
className="text-primary bg-secondary border-accent"
```

### [Borders](borders.md)
Border width, style, and radius utilities.

```python
className="border-2 border-solid rounded-lg"
```

### [Effects](effects.md)
Shadow, transition, and visual effect utilities.

```python
className="shadow-lg transition duration-300"
```

## Core Concepts

### Composability

Utilities are designed to be combined:

```python
html.Div(
    "Styled Content",
    className="p-4 bg-primary text-white rounded-lg shadow-md hover:shadow-lg transition"
)
```

### Responsive Prefixes (Coming Soon)

Future versions will support responsive utilities:

```python
className="w-full md:w-1/2 lg:w-1/3"  # Coming soon
```

### State Variants

Utilities support hover, focus, and active states:

```python
className="bg-primary hover:opacity-80 focus:ring active:scale-95"
```

## Common Patterns

### Card Layout

```python
html.Div([
    html.H3("Title", className="text-2xl font-bold mb-2"),
    html.P("Description", className="text-muted-foreground mb-4"),
    Button("Action", className="w-full")
], className="p-6 bg-background border border-border rounded-lg shadow-md")
```

### Centered Content

```python
html.Div(
    [html.H1("Welcome")],
    className="flex items-center justify-center min-h-screen"
)
```

### Grid Layout

```python
html.Div([
    html.Div("Item 1", className="p-4 bg-muted rounded-lg"),
    html.Div("Item 2", className="p-4 bg-muted rounded-lg"),
    html.Div("Item 3", className="p-4 bg-muted rounded-lg")
], className="grid grid-cols-3 gap-4")
```

### Form Row

```python
html.Div([
    InputGroup([...], className="flex-1"),
    InputGroup([...], className="flex-1")
], className="flex gap-4")
```

## Naming Convention

Utilities follow a consistent naming pattern:

- **Property-Value**: `p-4`, `m-2`, `text-lg`
- **Property-Side-Value**: `pt-4`, `ml-2`, `border-t`
- **Property-Variant**: `text-primary`, `bg-muted`
- **State-Property-Value**: `hover:opacity-80`, `focus:ring`

## Size Scale

Most utilities use a consistent size scale:

| Size | Value | Pixels |
|------|-------|--------|
| 0 | 0 | 0px |
| 1 | 0.25rem | 4px |
| 2 | 0.5rem | 8px |
| 3 | 0.75rem | 12px |
| 4 | 1rem | 16px |
| 5 | 1.25rem | 20px |
| 6 | 1.5rem | 24px |
| 8 | 2rem | 32px |
| 10 | 2.5rem | 40px |
| 12 | 3rem | 48px |
| 16 | 4rem | 64px |

## Color Palette

Utilities use semantic color names:

- `primary` - Main brand color
- `secondary` - Secondary/muted color
- `accent` - Accent color
- `background` - Page background
- `foreground` - Text color
- `muted` - Muted background
- `muted-foreground` - Muted text
- `border` - Border color
- `destructive` - Error/danger color

## Performance

Utility classes are pre-generated and optimized:

- **22KB minified** - The entire CSS bundle
- **No runtime cost** - Pure CSS, no JavaScript
- **Tree-shakeable** - Only used classes loaded (future feature)

## Best Practices

### Do

✅ Use utilities for common styling needs
✅ Combine utilities for custom designs
✅ Use semantic color names
✅ Extract repetitive patterns into components
✅ Use the `cn()` utility for conditional classes

```python
from dash_ui_kit.utils import cn

className = cn(
    "p-4 rounded-lg",
    is_active and "bg-primary text-white",
    is_disabled and "opacity-50 pointer-events-none"
)
```

### Don't

❌ Don't use inline styles when utilities exist
❌ Don't create custom CSS for one-off styles
❌ Don't use magic numbers (use scale values)
❌ Don't forget about accessibility

## Examples

### Dashboard Card

```python
Card([
    CardHeader([
        html.Div([
            CardTitle("Revenue"),
            Badge("↑ 12%", variant="default", size="sm")
        ], className="flex items-center justify-between")
    ]),
    CardContent([
        html.P("$45,231.89", className="text-4xl font-bold"),
        html.P("Last 30 days", className="text-sm text-muted-foreground mt-2")
    ])
], className="max-w-sm")
```

### Alert Box

```python
html.Div([
    html.P("✓", className="text-2xl"),
    html.Div([
        html.H4("Success", className="font-bold"),
        html.P("Your changes have been saved.", className="text-sm")
    ], className="ml-3")
], className="flex items-start p-4 bg-secondary border border-border rounded-lg")
```

### Navigation Bar

```python
html.Div([
    html.Div("Logo", className="font-bold text-xl"),
    html.Div([
        Button("Home", variant="ghost", size="sm"),
        Button("About", variant="ghost", size="sm"),
        Button("Contact", variant="ghost", size="sm")
    ], className="flex gap-2")
], className="flex items-center justify-between p-4 border-b border-border")
```

## Next Steps

- Explore specific [utility categories](spacing.md)
- Check out [component documentation](../components/overview.md)
- Learn about [theming](../theming/customization.md)
