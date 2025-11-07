# Select Component

Styled dropdown component for selecting one or multiple options from a list.

## Overview

The Select component is a styled wrapper around Dash's `dcc.Dropdown` that integrates seamlessly with the Dash UI Kit design system. It supports single and multi-select modes, searchable options, and custom styling.

## Import

```python
from dash_ui_kit import Select
```

## Basic Usage

```python
Select(
    id="country",
    options=[
        {"label": "USA", "value": "us"},
        {"label": "Canada", "value": "ca"},
        {"label": "Mexico", "value": "mx"}
    ],
    placeholder="Select a country"
)
```

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `id` | `str` | `None` | Unique identifier for callbacks |
| `options` | `List[dict]` | `None` | List of option dictionaries |
| `value` | `str \| int \| List` | `None` | Currently selected value(s) |
| `multi` | `bool` | `False` | Allow multiple selections |
| `searchable` | `bool` | `True` | Enable search functionality |
| `clearable` | `bool` | `True` | Allow clearing selection |
| `placeholder` | `str` | `"Select..."` | Placeholder text |
| `disabled` | `bool` | `False` | Whether dropdown is disabled |
| `className` | `str` | `""` | Additional CSS classes |

## Examples

### Single Selection

```python
Select(
    id="language",
    options=[
        {"label": "Python", "value": "python"},
        {"label": "JavaScript", "value": "js"},
        {"label": "Go", "value": "go"},
        {"label": "Rust", "value": "rust"}
    ],
    placeholder="Select a language"
)
```

### Multi-Select

```python
Select(
    id="skills",
    options=[
        {"label": "React", "value": "react"},
        {"label": "Vue", "value": "vue"},
        {"label": "Angular", "value": "angular"},
        {"label": "Svelte", "value": "svelte"}
    ],
    multi=True,
    placeholder="Select skills"
)
```

### With Default Value

```python
Select(
    id="theme",
    options=[
        {"label": "Light", "value": "light"},
        {"label": "Dark", "value": "dark"},
        {"label": "Auto", "value": "auto"}
    ],
    value="light",
    placeholder="Select theme"
)
```

### Non-Searchable

```python
Select(
    id="size",
    options=[
        {"label": "Small", "value": "sm"},
        {"label": "Medium", "value": "md"},
        {"label": "Large", "value": "lg"}
    ],
    searchable=False,
    placeholder="Select size"
)
```

### Non-Clearable

```python
Select(
    id="required",
    options=[
        {"label": "Option 1", "value": "1"},
        {"label": "Option 2", "value": "2"}
    ],
    clearable=False,
    value="1"
)
```

### Disabled

```python
Select(
    id="disabled",
    options=[
        {"label": "Option 1", "value": "1"}
    ],
    disabled=True,
    value="1"
)
```

## Form Integration

### With Label

```python
InputGroup([
    Label("Select Country", htmlFor="country-select"),
    Select(
        id="country-select",
        options=[
            {"label": "United States", "value": "us"},
            {"label": "Canada", "value": "ca"},
            {"label": "United Kingdom", "value": "uk"}
        ]
    )
])
```

### With Validation

```python
from dash import Input, Output, State

app.layout = html.Div([
    InputGroup([
        Label("Category", htmlFor="category"),
        Select(
            id="category",
            options=[
                {"label": "Electronics", "value": "electronics"},
                {"label": "Clothing", "value": "clothing"},
                {"label": "Food", "value": "food"}
            ]
        ),
        InputError("", id="category-error")
    ]),
    Button("Submit", id="submit-btn")
])

@app.callback(
    Output("category-error", "children"),
    Input("submit-btn", "n_clicks"),
    State("category", "value"),
    prevent_initial_call=True
)
def validate_category(n, value):
    if not value:
        return "Please select a category"
    return ""
```

## Dynamic Options

### From Database/API

```python
@app.callback(
    Output("city", "options"),
    Input("country", "value")
)
def update_cities(country):
    cities = {
        "us": [
            {"label": "New York", "value": "ny"},
            {"label": "Los Angeles", "value": "la"}
        ],
        "ca": [
            {"label": "Toronto", "value": "tor"},
            {"label": "Vancouver", "value": "van"}
        ]
    }
    return cities.get(country, [])
```

### Dependent Dropdowns

```python
app.layout = html.Div([
    Select(
        id="country",
        options=[
            {"label": "USA", "value": "us"},
            {"label": "Canada", "value": "ca"}
        ],
        placeholder="Select country"
    ),
    Select(
        id="state",
        options=[],
        placeholder="Select state"
    )
])

@app.callback(
    [Output("state", "options"),
     Output("state", "value")],
    Input("country", "value")
)
def update_states(country):
    if not country:
        return [], None

    states = {
        "us": [
            {"label": "California", "value": "ca"},
            {"label": "Texas", "value": "tx"}
        ],
        "ca": [
            {"label": "Ontario", "value": "on"},
            {"label": "Quebec", "value": "qc"}
        ]
    }
    return states.get(country, []), None
```

## Advanced Usage

### Grouped Options

```python
Select(
    id="product",
    options=[
        {"label": "Electronics", "value": "electronics", "disabled": True},
        {"label": "  Laptop", "value": "laptop"},
        {"label": "  Phone", "value": "phone"},
        {"label": "Clothing", "value": "clothing", "disabled": True},
        {"label": "  Shirt", "value": "shirt"},
        {"label": "  Pants", "value": "pants"}
    ]
)
```

### With Icons/Emojis

```python
Select(
    id="status",
    options=[
        {"label": "✅ Complete", "value": "complete"},
        {"label": "⏳ In Progress", "value": "progress"},
        {"label": "❌ Failed", "value": "failed"}
    ]
)
```

### Large Option List

```python
# Generate large list
options = [
    {"label": f"Option {i}", "value": i}
    for i in range(100)
]

Select(
    id="large-list",
    options=options,
    searchable=True,
    placeholder="Search from 100 options"
)
```

## Common Patterns

### Filter Control

```python
html.Div([
    html.Label("Filter by:"),
    html.Div([
        Select(
            id="filter-category",
            options=[
                {"label": "All", "value": "all"},
                {"label": "Active", "value": "active"},
                {"label": "Inactive", "value": "inactive"}
            ],
            value="all",
            className="w-48"
        ),
        Select(
            id="filter-date",
            options=[
                {"label": "Last 7 days", "value": "7"},
                {"label": "Last 30 days", "value": "30"},
                {"label": "Last 90 days", "value": "90"}
            ],
            value="7",
            className="w-48 ml-2"
        )
    ], className="flex gap-2")
], className="mb-4")
```

### Settings Panel

```python
Card([
    CardHeader([CardTitle("Settings")]),
    CardContent([
        InputGroup([
            Label("Language"),
            Select(
                id="language",
                options=[
                    {"label": "English", "value": "en"},
                    {"label": "Spanish", "value": "es"},
                    {"label": "French", "value": "fr"}
                ],
                value="en"
            )
        ], className="mb-4"),

        InputGroup([
            Label("Timezone"),
            Select(
                id="timezone",
                options=[
                    {"label": "UTC-8 (PST)", "value": "pst"},
                    {"label": "UTC-5 (EST)", "value": "est"},
                    {"label": "UTC+0 (GMT)", "value": "gmt"}
                ],
                value="est"
            )
        ])
    ])
])
```

### Multi-Select Tags

```python
InputGroup([
    Label("Tags"),
    Select(
        id="tags",
        options=[
            {"label": "Python", "value": "python"},
            {"label": "JavaScript", "value": "js"},
            {"label": "TypeScript", "value": "ts"},
            {"label": "React", "value": "react"},
            {"label": "Vue", "value": "vue"}
        ],
        multi=True,
        placeholder="Select tags"
    )
])
```

## With Callbacks

### Simple Callback

```python
app.layout = html.Div([
    Select(
        id="animal",
        options=[
            {"label": "Dog", "value": "dog"},
            {"label": "Cat", "value": "cat"},
            {"label": "Bird", "value": "bird"}
        ]
    ),
    html.Div(id="output")
])

@app.callback(
    Output("output", "children"),
    Input("animal", "value")
)
def display_selection(value):
    if not value:
        return "No selection"
    return f"You selected: {value}"
```

### Multi-Select Processing

```python
@app.callback(
    Output("summary", "children"),
    Input("skills", "value")
)
def show_skills(skills):
    if not skills:
        return "No skills selected"

    return html.Div([
        html.P(f"Selected {len(skills)} skills:"),
        html.Ul([
            html.Li(skill) for skill in skills
        ])
    ])
```

## Accessibility

- Keyboard navigation (arrow keys, Enter, Escape)
- Search functionality for large lists
- Clear indication of selected items
- Focus management
- Screen reader compatible

## Styling

The Select component uses these CSS classes:

- `.duk-select` - Base select styles
- Inherits Dash Dropdown styling with custom overrides

## Best Practices

1. **Appropriate options count**: Use searchable for >10 options
2. **Clear labels**: Provide descriptive option labels
3. **Default values**: Set sensible defaults when appropriate
4. **Placeholder text**: Use helpful placeholder text
5. **Multi-select**: Use for selecting multiple related items
6. **Validation**: Validate required selections on submit

## Related Components

- [Input](input.md) - For text input
- [Button](button.md) - For form submission
- [Card](card.md) - Container for forms
