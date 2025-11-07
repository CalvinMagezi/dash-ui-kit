# Input Component

Form input components with labels, error states, and validation support.

## Overview

The Input component provides a complete form input solution with associated label, error message, and various input types. It's designed to work seamlessly with Dash callbacks for form validation and data collection.

## Import

```python
from dash_ui_kit import Input, InputGroup, Label, InputError
```

## Basic Usage

```python
Input(id="username", placeholder="Enter username")
```

## Components

### Input

Main input field component.

**Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `id` | `str` | `None` | Unique identifier for callbacks |
| `type` | `InputType` | `"text"` | Input type (text, email, password, etc.) |
| `value` | `str` | `""` | Current input value |
| `placeholder` | `str` | `""` | Placeholder text |
| `disabled` | `bool` | `False` | Whether input is disabled |
| `error` | `bool` | `False` | Whether input is in error state |
| `className` | `str` | `""` | Additional CSS classes |

### Label

Label for input fields.

**Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `Any` | `None` | Label text |
| `id` | `str` | `None` | Unique identifier |
| `htmlFor` | `str` | `None` | ID of associated input |
| `className` | `str` | `""` | Additional CSS classes |

### InputGroup

Container for grouping label, input, and error message.

**Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `Any` | `None` | Group content |
| `id` | `str` | `None` | Unique identifier |
| `className` | `str` | `""` | Additional CSS classes |

### InputError

Error message component.

**Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `Any` | `None` | Error message text |
| `id` | `str` | `None` | Unique identifier |
| `className` | `str` | `""` | Additional CSS classes |

## Input Types

### Text Input

```python
Input(id="name", type="text", placeholder="Enter your name")
```

### Email Input

```python
Input(id="email", type="email", placeholder="your@email.com")
```

### Password Input

```python
Input(id="password", type="password", placeholder="Enter password")
```

### Number Input

```python
Input(id="age", type="number", placeholder="Enter age")
```

### Date Input

```python
Input(id="birthday", type="date")
```

### Search Input

```python
Input(id="search", type="search", placeholder="Search...")
```

## Complete Input Group

```python
InputGroup([
    Label("Email Address", htmlFor="email"),
    Input(id="email", type="email", placeholder="your@email.com"),
    InputError("", id="email-error")
])
```

## Examples

### Form with Validation

```python
from dash import Dash, Input as DashInput, Output, State
from dash_ui_kit import Button, Input, InputGroup, Label, InputError, Card, CardContent

app = Dash(__name__)

app.layout = Card([
    CardContent([
        InputGroup([
            Label("Email", htmlFor="email"),
            Input(id="email", type="email"),
            InputError("", id="email-error")
        ], className="mb-4"),
        Button("Submit", id="submit-btn", variant="default")
    ])
])

@app.callback(
    [Output("email-error", "children"),
     Output("email", "error")],
    DashInput("submit-btn", "n_clicks"),
    State("email", "value"),
    prevent_initial_call=True
)
def validate_email(n_clicks, email):
    if not email or "@" not in email:
        return "Please enter a valid email address", True
    return "", False
```

### Multi-Field Form

```python
html.Div([
    InputGroup([
        Label("First Name", htmlFor="first-name"),
        Input(id="first-name", type="text")
    ], className="mb-4"),

    InputGroup([
        Label("Last Name", htmlFor="last-name"),
        Input(id="last-name", type="text")
    ], className="mb-4"),

    InputGroup([
        Label("Email", htmlFor="email"),
        Input(id="email", type="email")
    ], className="mb-4"),

    Button("Save", variant="default")
])
```

### Input with Error State

```python
InputGroup([
    Label("Username", htmlFor="username"),
    Input(id="username", type="text", error=True, value="ab"),
    InputError("Username must be at least 3 characters")
])
```

### Disabled Input

```python
InputGroup([
    Label("Account Type", htmlFor="account-type"),
    Input(id="account-type", value="Premium", disabled=True)
])
```

### Input with Helper Text

```python
InputGroup([
    Label("Password", htmlFor="password"),
    Input(id="password", type="password"),
    html.P("Must be at least 8 characters", className="text-sm text-muted-foreground mt-1")
])
```

### Inline Form

```python
html.Div([
    Input(id="search", type="search", placeholder="Search...", className="flex-1"),
    Button("Search", variant="default", className="ml-2")
], className="flex")
```

### Required Fields

```python
InputGroup([
    html.Div([
        Label("Email"),
        html.Span("*", className="text-destructive ml-1")
    ], className="flex items-center"),
    Input(id="email", type="email")
])
```

## Form Patterns

### Login Form

```python
Card([
    CardHeader([
        CardTitle("Sign In"),
        CardDescription("Enter your credentials")
    ]),
    CardContent([
        InputGroup([
            Label("Email", htmlFor="login-email"),
            Input(id="login-email", type="email")
        ], className="mb-4"),

        InputGroup([
            Label("Password", htmlFor="login-password"),
            Input(id="login-password", type="password")
        ], className="mb-4"),

        Button("Sign In", id="login-btn", variant="default", className="w-full")
    ])
])
```

### Contact Form

```python
html.Div([
    html.Div([
        InputGroup([
            Label("Name"),
            Input(id="name", type="text")
        ]),
        InputGroup([
            Label("Email"),
            Input(id="email", type="email")
        ])
    ], className="grid grid-cols-2 gap-4 mb-4"),

    InputGroup([
        Label("Message"),
        html.Textarea(id="message", className="duk-input min-h-32")
    ], className="mb-4"),

    Button("Send Message", variant="default")
])
```

## Validation with Callbacks

### Real-time Validation

```python
@app.callback(
    [Output("email", "error"),
     Output("email-error", "children")],
    Input("email", "value")
)
def validate_email_realtime(value):
    if not value:
        return False, ""
    if "@" not in value:
        return True, "Invalid email format"
    return False, ""
```

### Submit Validation

```python
@app.callback(
    Output("form-result", "children"),
    Input("submit", "n_clicks"),
    [State("name", "value"),
     State("email", "value")],
    prevent_initial_call=True
)
def handle_submit(n, name, email):
    errors = []
    if not name:
        errors.append("Name is required")
    if not email or "@" not in email:
        errors.append("Valid email is required")

    if errors:
        return html.Div([
            html.P(error, className="text-destructive text-sm")
            for error in errors
        ])

    return html.P("Form submitted successfully!", className="text-green-600")
```

## Accessibility

- Labels properly associated with inputs via `htmlFor`
- Error messages linked to inputs for screen readers
- Keyboard navigation support
- Focus visible on keyboard navigation
- Placeholder text does not replace labels

## Styling

Input components use these CSS classes:

- `.duk-input` - Base input styles
- `.duk-input--error` - Error state
- `.duk-label` - Label styles
- `.duk-input-group` - Group container
- `.duk-input-error` - Error message

## Best Practices

1. **Always use labels**: Every input should have an associated label
2. **Meaningful placeholders**: Use placeholders for examples, not as labels
3. **Clear error messages**: Provide specific, actionable error messages
4. **Validate appropriately**: Use real-time validation for format, submit validation for required fields
5. **Required indicators**: Mark required fields clearly
6. **Accessible errors**: Use InputError component for proper announcement

## Related Components

- [Button](button.md) - For form submissions
- [Select](select.md) - For dropdown selections
- [Card](card.md) - Container for forms
