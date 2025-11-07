# Border Utilities

Control borders with width, style, radius, and color utilities.

## Border Width

```python
className="border"     # border-width: 1px
className="border-0"   # border-width: 0
className="border-2"   # border-width: 2px
className="border-4"   # border-width: 4px
```

## Border Sides

```python
className="border-t"   # border-top-width: 1px
className="border-r"   # border-right-width: 1px
className="border-b"   # border-bottom-width: 1px
className="border-l"   # border-left-width: 1px
```

## Border Style

```python
className="border-solid"   # border-style: solid
className="border-dashed"  # border-style: dashed
className="border-dotted"  # border-style: dotted
className="border-none"    # border-style: none
```

## Border Radius

```python
className="rounded-sm"    # border-radius: 0.25rem
className="rounded"       # border-radius: 0.25rem
className="rounded-md"    # border-radius: 0.5rem
className="rounded-lg"    # border-radius: 1rem
className="rounded-full"  # border-radius: 9999px
className="rounded-none"  # border-radius: 0
```

## Border Colors

Border colors use the same color system as other utilities:

```python
className="border-primary"
className="border-secondary"
className="border-border"    # Default border color
className="border-destructive"
```

## Examples

### Card with Border

```python
Card([...], className="border-2 border-border rounded-lg")
```

### Rounded Button

```python
Button("Click", className="rounded-full")
```

### Dashed Separator

```python
html.Hr(className="border-t border-dashed border-border")
```

### Bottom Border Only

```python
html.Div("Content", className="border-b border-border pb-4")
```

## Related Utilities

- [Colors](colors.md) - Border colors
- [Spacing](spacing.md) - Border spacing
