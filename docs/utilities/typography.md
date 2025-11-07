# Typography Utilities

Control text appearance with font size, weight, alignment, and style utilities.

## Font Size

```python
className="text-xs"    # font-size: 0.75rem
className="text-sm"    # font-size: 0.875rem
className="text-base"  # font-size: 1rem
className="text-lg"    # font-size: 1.125rem
className="text-xl"    # font-size: 1.25rem
className="text-2xl"   # font-size: 1.5rem
className="text-3xl"   # font-size: 1.875rem
className="text-4xl"   # font-size: 2.25rem
```

## Font Weight

```python
className="font-normal"    # font-weight: 400
className="font-medium"    # font-weight: 500
className="font-semibold"  # font-weight: 600
className="font-bold"      # font-weight: 700
```

## Text Alignment

```python
className="text-left"     # text-align: left
className="text-center"   # text-align: center
className="text-right"    # text-align: right
className="text-justify"  # text-align: justify
```

## Text Transform

```python
className="uppercase"   # text-transform: uppercase
className="lowercase"   # text-transform: lowercase
className="capitalize"  # text-transform: capitalize
```

## Line Height

```python
className="leading-tight"    # line-height: 1.25
className="leading-normal"   # line-height: 1.5
className="leading-relaxed"  # line-height: 1.75
```

## Text Decoration

```python
className="underline"      # text-decoration: underline
className="line-through"   # text-decoration: line-through
className="no-underline"   # text-decoration: none
```

## Examples

### Heading

```python
html.H1("Page Title", className="text-4xl font-bold mb-4")
```

### Subtitle

```python
html.P("Subtitle text", className="text-xl text-muted-foreground")
```

### Body Text

```python
html.P("Body content", className="text-base leading-relaxed")
```

### Label

```python
html.Label("Form Label", className="text-sm font-medium")
```

## Related Utilities

- [Colors](colors.md) - For text colors
- [Spacing](spacing.md) - For text spacing
