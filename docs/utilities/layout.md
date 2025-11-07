# Layout Utilities

Control element layout with flexbox, grid, and display utilities.

## Display

Control how elements are displayed.

```python
className="block"         # display: block
className="inline-block"  # display: inline-block
className="inline"        # display: inline
className="flex"          # display: flex
className="inline-flex"   # display: inline-flex
className="grid"          # display: grid
className="inline-grid"   # display: inline-grid
className="hidden"        # display: none
```

## Flexbox

### Direction

```python
className="flex-row"      # flex-direction: row
className="flex-col"      # flex-direction: column
className="flex-wrap"     # flex-wrap: wrap
className="flex-nowrap"   # flex-wrap: nowrap
```

### Justify Content

```python
className="justify-start"    # justify-content: flex-start
className="justify-end"      # justify-content: flex-end
className="justify-center"   # justify-content: center
className="justify-between"  # justify-content: space-between
className="justify-around"   # justify-content: space-around
className="justify-evenly"   # justify-content: space-evenly
```

### Align Items

```python
className="items-start"    # align-items: flex-start
className="items-end"      # align-items: flex-end
className="items-center"   # align-items: center
className="items-baseline" # align-items: baseline
className="items-stretch"  # align-items: stretch
```

### Align Self

```python
className="self-auto"     # align-self: auto
className="self-start"    # align-self: flex-start
className="self-end"      # align-self: flex-end
className="self-center"   # align-self: center
className="self-stretch"  # align-self: stretch
```

### Flex Grow/Shrink

```python
className="flex-1"        # flex: 1 1 0%
className="flex-auto"     # flex: 1 1 auto
className="flex-initial"  # flex: 0 1 auto
className="flex-none"     # flex: none
```

### Gap

```python
className="gap-1"    # gap: 0.25rem
className="gap-2"    # gap: 0.5rem
className="gap-3"    # gap: 0.75rem
className="gap-4"    # gap: 1rem
className="gap-6"    # gap: 1.5rem
className="gap-8"    # gap: 2rem

# Axis-specific gaps
className="gap-x-4"  # column-gap: 1rem
className="gap-y-4"  # row-gap: 1rem
```

## Grid

### Grid Template Columns

```python
className="grid-cols-1"   # grid-template-columns: repeat(1, minmax(0, 1fr))
className="grid-cols-2"   # grid-template-columns: repeat(2, minmax(0, 1fr))
className="grid-cols-3"   # grid-template-columns: repeat(3, minmax(0, 1fr))
className="grid-cols-4"   # grid-template-columns: repeat(4, minmax(0, 1fr))
className="grid-cols-6"   # grid-template-columns: repeat(6, minmax(0, 1fr))
className="grid-cols-12"  # grid-template-columns: repeat(12, minmax(0, 1fr))
```

## Examples

### Centered Content

```python
html.Div(
    [html.H1("Centered")],
    className="flex items-center justify-center min-h-screen"
)
```

### Card Grid

```python
html.Div([
    Card(...),
    Card(...),
    Card(...)
], className="grid grid-cols-3 gap-4")
```

### Navigation Bar

```python
html.Div([
    html.Div("Logo"),
    html.Div([
        Button("Home"),
        Button("About"),
        Button("Contact")
    ], className="flex gap-2")
], className="flex items-center justify-between p-4")
```

### Sidebar Layout

```python
html.Div([
    html.Div("Sidebar", className="w-64 bg-muted"),
    html.Div("Main Content", className="flex-1")
], className="flex")
```

## Related Utilities

- [Spacing](spacing.md) - For gaps and padding
- [Sizing](#) - For width and height control
