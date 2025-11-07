# Color Utilities

Control text, background, and border colors with semantic color utilities.

## Text Colors

```python
className="text-primary"            # Primary brand color
className="text-secondary"          # Secondary color
className="text-accent"             # Accent color
className="text-foreground"         # Main text color
className="text-muted-foreground"   # Muted text
className="text-destructive"        # Error/danger color
```

## Background Colors

```python
className="bg-primary"              # Primary background
className="bg-secondary"            # Secondary background
className="bg-accent"               # Accent background
className="bg-background"           # Page background
className="bg-muted"                # Muted background
className="bg-destructive"          # Error background
```

## Border Colors

```python
className="border-primary"          # Primary border
className="border-secondary"        # Secondary border
className="border-accent"           # Accent border
className="border-border"           # Default border
className="border-destructive"      # Error border
```

## Opacity

```python
className="opacity-0"    # opacity: 0
className="opacity-10"   # opacity: 0.1
className="opacity-20"   # opacity: 0.2
className="opacity-50"   # opacity: 0.5
className="opacity-75"   # opacity: 0.75
className="opacity-100"  # opacity: 1
```

## Examples

### Primary Button

```python
Button("Save", className="bg-primary text-white")
```

### Muted Text

```python
html.P("Secondary information", className="text-muted-foreground")
```

### Alert Box

```python
html.Div(
    "Success message",
    className="bg-secondary text-foreground border border-border p-4 rounded-lg"
)
```

### Error State

```python
html.P("Error message", className="text-destructive")
```

## Color Customization

Colors are defined using CSS variables and can be customized. See [Theming](../theming/customization.md).

## Related Utilities

- [Theming](../theming/customization.md) - Customize colors
- [Borders](borders.md) - Border utilities
