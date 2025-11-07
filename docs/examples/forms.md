# Forms Example

A complete form with validation showcasing input components and form patterns.

## Overview

This example demonstrates how to build forms with validation using Dash UI Kit input components. It includes validation logic, error handling, and submit processing.

## Live Example

Run the example:

```bash
python examples/forms.py
```

## Features Demonstrated

- ✅ Input components with labels
- ✅ Form validation with callbacks
- ✅ Error message display
- ✅ Select dropdowns
- ✅ Textarea inputs
- ✅ Button actions
- ✅ Form state management

## Complete Code

See `examples/forms.py` for the complete implementation.

## Key Components

### Input Groups

```python
InputGroup([
    Label("Email", htmlFor="email"),
    Input(id="email", type="email", placeholder="your@email.com"),
    InputError("", id="email-error")
], className="mb-4")
```

### Validation Callback

```python
@app.callback(
    [Output("email-error", "children"),
     Output("email", "error")],
    Input("submit-btn", "n_clicks"),
    State("email", "value"),
    prevent_initial_call=True
)
def validate_email(n_clicks, email):
    if not email or "@" not in email:
        return "Please enter a valid email address", True
    return "", False
```

### Form Layout

```python
Card([
    CardHeader([
        CardTitle("Contact Form"),
        CardDescription("Fill out the form below")
    ]),
    CardContent([
        # Input groups here
    ]),
    CardFooter([
        Button("Cancel", variant="outline"),
        Button("Submit", variant="default")
    ])
])
```

## Validation Patterns

### Required Field

```python
if not value or len(value.strip()) < 2:
    return "Field is required", True
return "", False
```

### Email Validation

```python
if not value or "@" not in value:
    return "Please enter a valid email", True
return "", False
```

### Length Validation

```python
if not value or len(value) < 10:
    return "Must be at least 10 characters", True
return "", False
```

### Multiple Field Validation

```python
@app.callback(
    [Output("name-error", "children"),
     Output("email-error", "children")],
    Input("submit-btn", "n_clicks"),
    [State("name", "value"),
     State("email", "value")],
    prevent_initial_call=True
)
def validate_form(n, name, email):
    name_error = ""
    email_error = ""

    if not name or len(name) < 2:
        name_error = "Name is required"

    if not email or "@" not in email:
        email_error = "Valid email is required"

    return name_error, email_error
```

## Form Patterns

### Login Form

```python
Card([
    CardHeader([CardTitle("Sign In")]),
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
        Button("Sign In", className="w-full")
    ])
])
```

### Multi-Step Form

```python
# Step 1
html.Div([
    InputGroup([...]),
    Button("Next", id="next-btn")
], id="step-1", style={"display": "block"})

# Step 2
html.Div([
    InputGroup([...]),
    Button("Submit", id="submit-btn")
], id="step-2", style={"display": "none"})
```

### Inline Form

```python
html.Div([
    Input(id="search", placeholder="Search...", className="flex-1"),
    Button("Search", className="ml-2")
], className="flex")
```

## Best Practices

1. **Always use labels**: Every input should have a label
2. **Clear error messages**: Be specific about what's wrong
3. **Validate on submit**: Not on every keystroke for better UX
4. **Required field indicators**: Mark required fields clearly
5. **Success feedback**: Show success message after submission
6. **Disable during submission**: Prevent double submissions

## Customization

### Custom Validation

```python
def validate_phone(phone):
    import re
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return re.match(pattern, phone) is not None
```

### Async Validation

```python
# Check if email exists in database
@app.callback(
    Output("email-error", "children"),
    Input("email", "value"),
    running=[(Output("email", "disabled"), True, False)]
)
def check_email_availability(email):
    # Simulate API call
    import time
    time.sleep(0.5)

    if email_exists_in_db(email):
        return "Email already registered"
    return ""
```

## Related Examples

- [Dashboard Example](dashboard.md) - Dashboard layouts
- [Data Tables Example](data-tables.md) - Table with forms

## Related Components

- [Input](../components/input.md) - Input component docs
- [Select](../components/select.md) - Select component docs
- [Button](../components/button.md) - Button component docs
