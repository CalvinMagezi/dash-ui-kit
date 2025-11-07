# Spacing Utilities

Control element spacing with padding and margin utilities.

## Padding

Add internal spacing to elements.

### All Sides

```python
className="p-0"   # padding: 0
className="p-1"   # padding: 0.25rem (4px)
className="p-2"   # padding: 0.5rem (8px)
className="p-3"   # padding: 0.75rem (12px)
className="p-4"   # padding: 1rem (16px)
className="p-5"   # padding: 1.25rem (20px)
className="p-6"   # padding: 1.5rem (24px)
className="p-8"   # padding: 2rem (32px)
className="p-10"  # padding: 2.5rem (40px)
className="p-12"  # padding: 3rem (48px)
className="p-16"  # padding: 4rem (64px)
className="p-20"  # padding: 5rem (80px)
className="p-24"  # padding: 6rem (96px)
```

### Horizontal (X-axis)

```python
className="px-4"  # padding-left + padding-right: 1rem
```

### Vertical (Y-axis)

```python
className="py-4"  # padding-top + padding-bottom: 1rem
```

### Individual Sides

```python
className="pt-4"  # padding-top
className="pr-4"  # padding-right
className="pb-4"  # padding-bottom
className="pl-4"  # padding-left
```

## Margin

Add external spacing around elements.

### All Sides

```python
className="m-0"   # margin: 0
className="m-1"   # margin: 0.25rem (4px)
className="m-2"   # margin: 0.5rem (8px)
className="m-3"   # margin: 0.75rem (12px)
className="m-4"   # margin: 1rem (16px)
className="m-5"   # margin: 1.25rem (20px)
className="m-6"   # margin: 1.5rem (24px)
className="m-8"   # margin: 2rem (32px)
className="m-10"  # margin: 2.5rem (40px)
className="m-12"  # margin: 3rem (48px)
className="m-16"  # margin: 4rem (64px)
className="m-20"  # margin: 5rem (80px)
className="m-24"  # margin: 6rem (96px)
```

### Horizontal (X-axis)

```python
className="mx-4"  # margin-left + margin-right: 1rem
```

### Vertical (Y-axis)

```python
className="my-4"  # margin-top + margin-bottom: 1rem
```

### Individual Sides

```python
className="mt-4"  # margin-top
className="mr-4"  # margin-right
className="mb-4"  # margin-bottom
className="ml-4"  # margin-left
```

### Auto Margins

Center elements horizontally:

```python
className="mx-auto"  # margin-left: auto; margin-right: auto
className="my-auto"  # margin-top: auto; margin-bottom: auto
```

## Size Scale Reference

| Class | Value | Pixels | Use Case |
|-------|-------|--------|----------|
| `*-0` | 0 | 0px | Remove spacing |
| `*-1` | 0.25rem | 4px | Tight spacing |
| `*-2` | 0.5rem | 8px | Small spacing |
| `*-3` | 0.75rem | 12px | Default spacing |
| `*-4` | 1rem | 16px | Medium spacing |
| `*-5` | 1.25rem | 20px | Comfortable spacing |
| `*-6` | 1.5rem | 24px | Large spacing |
| `*-8` | 2rem | 32px | Section spacing |
| `*-10` | 2.5rem | 40px | Large sections |
| `*-12` | 3rem | 48px | Page sections |
| `*-16` | 4rem | 64px | Major sections |
| `*-20` | 5rem | 80px | Hero spacing |
| `*-24` | 6rem | 96px | Extra large spacing |

## Examples

### Card Padding

```python
Card([
    CardHeader([
        CardTitle("Title")
    ], className="p-6"),  # Header padding
    CardContent([
        html.P("Content")
    ], className="p-6 pt-0")  # Content padding, no top
])
```

### Button Spacing

```python
html.Div([
    Button("Save"),
    Button("Cancel")
], className="flex gap-2")  # Space between buttons
```

### Form Spacing

```python
html.Div([
    InputGroup([...], className="mb-4"),
    InputGroup([...], className="mb-4"),
    InputGroup([...], className="mb-6"),
    Button("Submit")
])
```

### Centered Content

```python
html.Div([
    html.H1("Welcome", className="mb-4"),
    html.P("Description")
], className="max-w-md mx-auto p-8")
```

### Section Spacing

```python
html.Div([
    html.Section([...], className="py-12"),
    html.Section([...], className="py-12"),
    html.Section([...], className="py-12")
])
```

### Nested Spacing

```python
Card([
    CardContent([
        html.Div([
            html.H3("Title", className="mb-2"),
            html.P("Description", className="mb-4"),
            Button("Action")
        ], className="p-4 bg-muted rounded-lg")
    ], className="p-6")
])
```

### Grid Gaps

```python
html.Div([
    Card(...),
    Card(...),
    Card(...)
], className="grid grid-cols-3 gap-4")  # 16px gap
```

### List Spacing

```python
html.Ul([
    html.Li("Item 1", className="mb-2"),
    html.Li("Item 2", className="mb-2"),
    html.Li("Item 3")
])
```

### Responsive Padding

```python
# Different padding for different content types
html.Div([
    html.Div("Tight content", className="p-2"),
    html.Div("Normal content", className="p-4"),
    html.Div("Spacious content", className="p-8")
])
```

## Common Patterns

### Container Padding

```python
html.Div([
    # Content
], className="container mx-auto px-4")
```

### Card Layout

```python
Card([
    CardHeader(className="p-6"),
    CardContent(className="px-6 pb-6"),
    CardFooter(className="px-6 pb-6")
])
```

### Dashboard Grid

```python
html.Div([
    Card(..., className="p-6"),
    Card(..., className="p-6"),
    Card(..., className="p-6")
], className="grid grid-cols-3 gap-6 p-6")
```

### Form Layout

```python
html.Form([
    html.Div([...], className="mb-4"),
    html.Div([...], className="mb-4"),
    html.Div([...], className="mt-6")
])
```

## Best Practices

### Do

✅ Use consistent spacing scale
✅ Use larger spacing for section breaks
✅ Use smaller spacing within components
✅ Use `gap` utilities for flex/grid spacing
✅ Use `mx-auto` for centering

### Don't

❌ Don't mix spacing scales arbitrarily
❌ Don't use magic numbers
❌ Don't overuse large spacing
❌ Don't forget responsive needs

## Accessibility

- Adequate spacing improves readability
- Touch targets should have sufficient padding (minimum 44x44px)
- Consistent spacing improves navigation for screen readers

## Related Utilities

- [Layout](layout.md) - For positioning and display
- [Sizing](../api-reference.md) - For width and height
