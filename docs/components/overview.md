# Components Overview

Dash UI Kit provides a set of pre-built, accessible components that follow consistent design patterns.

## Available Components

### Core Components

- **[Button](button.md)** - Interactive buttons with multiple variants and sizes
- **[Card](card.md)** - Flexible containers for grouping related content
- **[Input](input.md)** - Form inputs with labels and error states
- **[Badge](badge.md)** - Small labels and status indicators
- **[Select](select.md)** - Dropdown selections with search and multi-select

## Component Principles

All components follow these principles:

### 1. Composable

Components are designed to work together:

```python
Card([
    CardHeader([CardTitle("Title")]),
    CardContent([
        InputGroup([
            Label("Email"),
            Input(type="email"),
        ]),
        Button("Submit")
    ])
])
```

### 2. Customizable

All components accept `className` for additional styling:

```python
Button("Click", className="w-full mt-4")
Card(className="max-w-md mx-auto")
```

### 3. Type-Safe

Full type hints for excellent IDE support:

```python
Button(
    children="Click me",
    variant="default",  # Autocomplete: default, outline, ghost, destructive
    size="md"           # Autocomplete: sm, md, lg
)
```

### 4. Accessible

Components are built with accessibility in mind:

- Keyboard navigation support
- ARIA attributes
- Screen reader compatibility
- Focus management

## Common Patterns

### Form Layout

```python
Card([
    CardHeader([CardTitle("Contact Form")]),
    CardContent([
        InputGroup([
            Label("Name"),
            Input(id="name")
        ]),
        InputGroup([
            Label("Email"),
            Input(id="email", type="email")
        ])
    ]),
    CardFooter([
        Button("Submit", variant="default")
    ])
])
```

### Dashboard Stats

```python
html.Div([
    Card([
        CardHeader([CardTitle("Users")]),
        CardContent([
            html.P("1,234", className="text-4xl font-bold"),
            Badge("↑ 12%", variant="default")
        ])
    ]),
    Card([
        CardHeader([CardTitle("Revenue")]),
        CardContent([
            html.P("$45,678", className="text-4xl font-bold"),
            Badge("↑ 8%", variant="default")
        ])
    ])
], className="grid grid-cols-2 gap-4")
```

## Next Steps

- Explore individual component documentation
- Check out [Examples](../examples/dashboard.md)
- Learn about [Utility Classes](../utilities/overview.md)
