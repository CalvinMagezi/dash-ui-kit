# Card Component

Flexible container components for grouping related content with a consistent layout structure.

## Overview

The Card component provides a versatile container for organizing content. It includes sub-components for headers, titles, descriptions, content areas, and footers, allowing you to create well-structured, visually appealing content blocks.

## Import

```python
from dash_ui_kit import (
    Card,
    CardHeader,
    CardTitle,
    CardDescription,
    CardContent,
    CardFooter
)
```

## Basic Usage

```python
Card([
    CardHeader([
        CardTitle("Card Title")
    ]),
    CardContent([
        html.P("Card content goes here")
    ])
])
```

## Components

### Card

Main container component.

**Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `Any` | `None` | Card content (sub-components) |
| `id` | `str` | `None` | Unique identifier |
| `variant` | `"default" \| "outlined" \| "elevated"` | `"default"` | Visual style |
| `className` | `str` | `""` | Additional CSS classes |

### CardHeader

Container for title and description.

**Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `Any` | `None` | Header content |
| `id` | `str` | `None` | Unique identifier |
| `className` | `str` | `""` | Additional CSS classes |

### CardTitle

Heading for the card.

**Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `Any` | `None` | Title text |
| `id` | `str` | `None` | Unique identifier |
| `className` | `str` | `""` | Additional CSS classes |

### CardDescription

Subtitle or description text.

**Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `Any` | `None` | Description text |
| `id` | `str` | `None` | Unique identifier |
| `className` | `str` | `""` | Additional CSS classes |

### CardContent

Main content area.

**Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `Any` | `None` | Content |
| `id` | `str` | `None` | Unique identifier |
| `className` | `str` | `""` | Additional CSS classes |

### CardFooter

Footer for actions or additional info.

**Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `Any` | `None` | Footer content |
| `id` | `str` | `None` | Unique identifier |
| `className` | `str` | `""` | Additional CSS classes |

## Variants

### Default

```python
Card([
    CardHeader([CardTitle("Default Card")]),
    CardContent("Standard card with border")
], variant="default")
```

### Outlined

```python
Card([
    CardHeader([CardTitle("Outlined Card")]),
    CardContent("Card with thicker border")
], variant="outlined")
```

### Elevated

```python
Card([
    CardHeader([CardTitle("Elevated Card")]),
    CardContent("Card with shadow, no border")
], variant="elevated")
```

## Examples

### Complete Card

```python
Card([
    CardHeader([
        CardTitle("User Profile"),
        CardDescription("Manage your account settings")
    ]),
    CardContent([
        html.P("Your profile information..."),
        html.P("Email: user@example.com")
    ]),
    CardFooter([
        Button("Edit Profile", variant="default"),
        Button("Cancel", variant="outline", className="ml-2")
    ])
])
```

### Stats Card

```python
Card([
    CardHeader([
        CardTitle("Total Revenue"),
        CardDescription("Last 30 days")
    ]),
    CardContent([
        html.P("$45,231.89", className="text-4xl font-bold"),
        html.P("+20.1% from last month", className="text-sm text-muted-foreground mt-2")
    ])
], variant="elevated")
```

### Grid of Cards

```python
html.Div([
    Card([
        CardHeader([CardTitle("Card 1")]),
        CardContent("Content 1")
    ]),
    Card([
        CardHeader([CardTitle("Card 2")]),
        CardContent("Content 2")
    ]),
    Card([
        CardHeader([CardTitle("Card 3")]),
        CardContent("Content 3")
    ])
], className="grid grid-cols-3 gap-4")
```

### Card with Badge

```python
Card([
    CardHeader([
        html.Div([
            CardTitle("Notifications"),
            Badge("3", variant="destructive", size="sm", className="ml-2")
        ], className="flex items-center")
    ]),
    CardContent([
        html.P("You have 3 unread notifications")
    ])
])
```

### Nested Cards

```python
Card([
    CardHeader([CardTitle("Parent Card")]),
    CardContent([
        Card([
            CardHeader([CardTitle("Nested Card")]),
            CardContent("Nested content")
        ], variant="outlined")
    ])
])
```

### Card with Form

```python
Card([
    CardHeader([
        CardTitle("Login"),
        CardDescription("Enter your credentials")
    ]),
    CardContent([
        InputGroup([
            Label("Email"),
            Input(id="email", type="email")
        ], className="mb-4"),
        InputGroup([
            Label("Password"),
            Input(id="password", type="password")
        ])
    ]),
    CardFooter([
        Button("Sign In", id="login-btn", variant="default", className="w-full")
    ])
], className="max-w-md mx-auto")
```

## Layout Patterns

### Horizontal Cards

```python
Card([
    html.Div([
        html.Img(src="/image.jpg", className="w-24 h-24 rounded"),
        html.Div([
            CardTitle("Title"),
            CardDescription("Description"),
        ], className="ml-4")
    ], className="flex items-center")
], variant="elevated")
```

### Card with Divider

```python
Card([
    CardHeader([CardTitle("Header")]),
    html.Hr(className="border-border"),
    CardContent([html.P("Content")])
])
```

## Accessibility

- Semantic HTML structure
- Proper heading hierarchy
- Screen reader friendly
- Keyboard navigation support

## Styling

Card components use these CSS classes:

- `.duk-card` - Base card styles
- `.duk-card--{variant}` - Variant styles
- `.duk-card-header` - Header section
- `.duk-card-title` - Title heading
- `.duk-card-description` - Description text
- `.duk-card-content` - Content area
- `.duk-card-footer` - Footer section

## Best Practices

1. **Consistent structure**: Use all sub-components for clarity
2. **Variant selection**: Use "elevated" for emphasis, "outlined" for secondary content
3. **Spacing**: Use utility classes for consistent spacing
4. **Actions in footer**: Place buttons and actions in CardFooter
5. **Responsive design**: Use grid utilities for card layouts

## Related Components

- [Button](button.md) - Often used in CardFooter
- [Badge](badge.md) - Useful for status indicators in headers
- [Input](input.md) - Forms within CardContent
