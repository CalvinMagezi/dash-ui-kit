# Data Tables Example

Examples of creating styled data tables using Dash UI Kit utilities.

## Overview

While Dash UI Kit doesn't include a dedicated table component, you can easily create styled tables using utility classes and the native Dash `dash_table.DataTable` component.

## Basic Table

### Using HTML Table

```python
from dash import html

html.Table([
    html.Thead([
        html.Tr([
            html.Th("Name", className="text-left p-4 font-semibold"),
            html.Th("Email", className="text-left p-4 font-semibold"),
            html.Th("Status", className="text-left p-4 font-semibold"),
        ], className="border-b border-border")
    ]),
    html.Tbody([
        html.Tr([
            html.Td("John Doe", className="p-4"),
            html.Td("john@example.com", className="p-4"),
            html.Td(Badge("Active", variant="default", size="sm"), className="p-4"),
        ], className="border-b border-border hover:bg-muted"),
        html.Tr([
            html.Td("Jane Smith", className="p-4"),
            html.Td("jane@example.com", className="p-4"),
            html.Td(Badge("Pending", variant="secondary", size="sm"), className="p-4"),
        ], className="border-b border-border hover:bg-muted"),
    ])
], className="w-full border border-border rounded-lg")
```

## Table in Card

```python
Card([
    CardHeader([
        CardTitle("User List"),
        CardDescription("Manage your users")
    ]),
    CardContent([
        html.Table([
            # Table content
        ], className="w-full")
    ])
])
```

## With Dash DataTable

```python
from dash import dash_table
import pandas as pd

df = pd.DataFrame({
    "Name": ["John", "Jane", "Bob"],
    "Email": ["john@ex.com", "jane@ex.com", "bob@ex.com"],
    "Status": ["Active", "Pending", "Active"]
})

dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{"name": i, "id": i} for i in df.columns],
    style_table={'overflowX': 'auto'},
    style_cell={
        'textAlign': 'left',
        'padding': '12px',
        'fontFamily': 'inherit',
    },
    style_header={
        'backgroundColor': 'hsl(var(--color-muted))',
        'fontWeight': 'bold',
        'borderBottom': '1px solid hsl(var(--color-border))',
    },
    style_data={
        'backgroundColor': 'hsl(var(--color-background))',
        'color': 'hsl(var(--color-foreground))',
        'borderBottom': '1px solid hsl(var(--color-border))',
    },
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'hsl(var(--color-muted) / 0.3)',
        },
        {
            'if': {'state': 'active'},
            'backgroundColor': 'hsl(var(--color-secondary))',
        }
    ]
)
```

## Table Patterns

### With Actions

```python
html.Tr([
    html.Td("John Doe", className="p-4"),
    html.Td("john@example.com", className="p-4"),
    html.Td([
        Button("Edit", variant="ghost", size="sm", className="mr-2"),
        Button("Delete", variant="ghost", size="sm")
    ], className="p-4 text-right"),
], className="border-b border-border")
```

### With Selection

```python
html.Tr([
    html.Td([
        html.Input(type="checkbox", className="w-4 h-4")
    ], className="p-4 w-12"),
    html.Td("John Doe", className="p-4"),
    html.Td("john@example.com", className="p-4"),
])
```

### Sortable Headers

```python
html.Th([
    html.Div([
        html.Span("Name"),
        html.Span("↕️", className="ml-2 text-xs")
    ], className="flex items-center cursor-pointer")
], className="p-4")
```

### Empty State

```python
html.Tbody([
    html.Tr([
        html.Td([
            html.Div([
                html.P("No data available", className="text-muted-foreground"),
                Button("Add Item", variant="outline", size="sm", className="mt-2")
            ], className="text-center py-8")
        ], colspan="3")
    ])
])
```

## Styling Tips

### Striped Rows

```python
# Odd rows
className="odd:bg-muted"

# Or manually:
html.Tr([...], className="bg-muted" if index % 2 else "")
```

### Compact Table

```python
# Smaller padding
html.Td("Content", className="p-2 text-sm")
```

### Bordered Table

```python
html.Table([...], className="w-full border-2 border-border")
```

### Scrollable Table

```python
html.Div([
    html.Table([...])
], className="overflow-x-auto")
```

## Full Example

```python
from dash import Dash, html
from dash_ui_kit import Card, CardHeader, CardTitle, CardContent, Badge, Button

app = Dash(__name__)

app.layout = html.Div([
    Card([
        CardHeader([
            CardTitle("User Management")
        ]),
        CardContent([
            html.Div([
                html.Table([
                    html.Thead([
                        html.Tr([
                            html.Th("Name", className="text-left p-4 font-semibold"),
                            html.Th("Email", className="text-left p-4 font-semibold"),
                            html.Th("Role", className="text-left p-4 font-semibold"),
                            html.Th("Status", className="text-left p-4 font-semibold"),
                            html.Th("Actions", className="text-right p-4 font-semibold"),
                        ], className="border-b-2 border-border")
                    ]),
                    html.Tbody([
                        html.Tr([
                            html.Td("John Doe", className="p-4"),
                            html.Td("john@example.com", className="p-4 text-muted-foreground"),
                            html.Td("Admin", className="p-4"),
                            html.Td(Badge("Active", variant="default", size="sm"), className="p-4"),
                            html.Td([
                                Button("Edit", variant="ghost", size="sm", className="mr-2"),
                                Button("Delete", variant="ghost", size="sm")
                            ], className="p-4 text-right"),
                        ], className="border-b border-border hover:bg-muted transition"),
                        # More rows...
                    ])
                ], className="w-full")
            ], className="overflow-x-auto")
        ])
    ], className="max-w-6xl mx-auto")
], className="p-8 min-h-screen bg-background")

if __name__ == "__main__":
    app.run_server(debug=True)
```

## Related

- [Card Component](../components/card.md)
- [Badge Component](../components/badge.md)
- [Button Component](../components/button.md)
- [Dash DataTable Docs](https://dash.plotly.com/datatable)
