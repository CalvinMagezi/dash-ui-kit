"""Basic usage example of Dash UI Kit components."""

from dash import Dash, Input, Output, html

from dash_ui_kit import Badge, Button, Card, CardContent, CardHeader, CardTitle

# Initialize Dash app
app = Dash(__name__)

# Define app layout
app.layout = html.Div(
    [
        html.H1("Dash UI Kit - Basic Usage", className="text-4xl font-bold mb-8"),
        # Button examples
        Card(
            [
                CardHeader([CardTitle("Buttons")]),
                CardContent(
                    [
                        html.Div(
                            [
                                Button("Default", id="btn-1", variant="default"),
                                Button("Outline", id="btn-2", variant="outline"),
                                Button("Ghost", id="btn-3", variant="ghost"),
                                Button(
                                    "Destructive", id="btn-4", variant="destructive"
                                ),
                            ],
                            className="flex gap-2 mb-4",
                        ),
                        html.Div(
                            [
                                Button("Small", size="sm"),
                                Button("Medium", size="md"),
                                Button("Large", size="lg"),
                            ],
                            className="flex gap-2 mb-4",
                        ),
                        html.Div(
                            id="button-output",
                            className="text-sm text-muted-foreground",
                        ),
                    ]
                ),
            ],
            className="mb-6",
        ),
        # Badge examples
        Card(
            [
                CardHeader([CardTitle("Badges")]),
                CardContent(
                    [
                        html.Div(
                            [
                                Badge("Default", variant="default"),
                                Badge("Secondary", variant="secondary"),
                                Badge("Outline", variant="outline"),
                                Badge("Destructive", variant="destructive"),
                            ],
                            className="flex gap-2 mb-4",
                        ),
                        html.Div(
                            [
                                Badge("Small", size="sm"),
                                Badge("Medium", size="md"),
                                Badge("Large", size="lg"),
                            ],
                            className="flex gap-2",
                        ),
                    ]
                ),
            ],
            className="mb-6",
        ),
    ],
    className="container mx-auto p-8 min-h-screen bg-background",
)


# Callback for button clicks
@app.callback(
    Output("button-output", "children"),
    [
        Input("btn-1", "n_clicks"),
        Input("btn-2", "n_clicks"),
        Input("btn-3", "n_clicks"),
        Input("btn-4", "n_clicks"),
    ],
)
def update_output(n1: int, n2: int, n3: int, n4: int) -> str:
    """Update output based on button clicks."""
    total = (n1 or 0) + (n2 or 0) + (n3 or 0) + (n4 or 0)
    return f"Total clicks: {total}"


if __name__ == "__main__":
    app.run_server(debug=True)
