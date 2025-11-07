# Effects Utilities

Control visual effects like shadows, transitions, and opacity.

## Shadows

```python
className="shadow-sm"    # Small shadow
className="shadow"       # Medium shadow (default)
className="shadow-md"    # Medium shadow
className="shadow-lg"    # Large shadow
className="shadow-xl"    # Extra large shadow
className="shadow-none"  # No shadow
```

## Transitions

```python
className="transition"        # Transition common properties
className="transition-all"    # Transition all properties
className="transition-colors" # Transition color properties
```

## Transition Duration

```python
className="duration-75"   # 75ms
className="duration-100"  # 100ms
className="duration-150"  # 150ms
className="duration-200"  # 200ms
className="duration-300"  # 300ms
className="duration-500"  # 500ms
```

## Hover Effects

Combine with hover state for interactive effects:

```python
className="hover:opacity-80"   # Reduce opacity on hover
className="hover:opacity-90"   # Slightly reduce opacity
className="hover:shadow-lg"    # Increase shadow on hover
```

## Examples

### Elevated Card

```python
Card([...], className="shadow-lg")
```

### Interactive Button

```python
Button(
    "Hover Me",
    className="transition hover:opacity-80 duration-200"
)
```

### Subtle Card Hover

```python
Card(
    [...],
    className="shadow-md hover:shadow-lg transition duration-300"
)
```

### Fade Effect

```python
html.Div(
    "Fading content",
    className="opacity-50 hover:opacity-100 transition duration-500"
)
```

## Shadow Customization

Shadows are defined using CSS variables. See [Theming](../theming/customization.md) to customize.

## Best Practices

1. Use transitions for smooth effects
2. Keep durations reasonable (150-300ms)
3. Use shadows sparingly for depth
4. Combine with hover for interactivity

## Related Utilities

- [Colors](colors.md) - Color utilities
- [Borders](borders.md) - Border utilities
