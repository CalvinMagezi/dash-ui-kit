"""Form example with validation."""

from dash import Dash, Input, Output, State, html

from dash_ui_kit import (
    Button,
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
    Input as DukInput,
    InputError,
    InputGroup,
    Label,
    Select,
)

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1("Contact Form", className="text-3xl font-bold mb-8 text-center"),
        Card(
            [
                CardHeader(
                    [
                        CardTitle("Get in Touch"),
                        CardDescription(
                            "Fill out the form below and we'll get back to you soon."
                        ),
                    ]
                ),
                CardContent(
                    [
                        # Name input
                        InputGroup(
                            [
                                Label("Full Name", htmlFor="name"),
                                DukInput(
                                    id="name",
                                    type="text",
                                    placeholder="John Doe",
                                ),
                                InputError("", id="name-error"),
                            ],
                            className="mb-4",
                        ),
                        # Email input
                        InputGroup(
                            [
                                Label("Email", htmlFor="email"),
                                DukInput(
                                    id="email",
                                    type="email",
                                    placeholder="john@example.com",
                                ),
                                InputError("", id="email-error"),
                            ],
                            className="mb-4",
                        ),
                        # Subject select
                        InputGroup(
                            [
                                Label("Subject", htmlFor="subject"),
                                Select(
                                    id="subject",
                                    options=[
                                        {"label": "General Inquiry", "value": "general"},
                                        {"label": "Technical Support", "value": "support"},
                                        {"label": "Sales", "value": "sales"},
                                        {"label": "Feedback", "value": "feedback"},
                                    ],
                                    placeholder="Select a subject",
                                ),
                                InputError("", id="subject-error"),
                            ],
                            className="mb-4",
                        ),
                        # Message textarea
                        InputGroup(
                            [
                                Label("Message", htmlFor="message"),
                                html.Textarea(
                                    id="message",
                                    placeholder="Your message here...",
                                    className="duk-input min-h-32",
                                ),
                                InputError("", id="message-error"),
                            ]
                        ),
                    ]
                ),
                CardFooter(
                    [
                        Button(
                            "Cancel",
                            id="cancel-btn",
                            variant="outline",
                            className="mr-2",
                        ),
                        Button("Submit", id="submit-btn", variant="default"),
                    ]
                ),
            ],
            className="max-w-2xl mx-auto",
            variant="elevated",
        ),
        # Result message
        html.Div(id="form-result", className="max-w-2xl mx-auto mt-4"),
    ],
    className="container mx-auto p-8 min-h-screen bg-background",
)


@app.callback(
    [
        Output("name-error", "children"),
        Output("email-error", "children"),
        Output("subject-error", "children"),
        Output("message-error", "children"),
        Output("form-result", "children"),
    ],
    Input("submit-btn", "n_clicks"),
    [
        State("name", "value"),
        State("email", "value"),
        State("subject", "value"),
        State("message", "value"),
    ],
    prevent_initial_call=True,
)
def handle_submit(
    n_clicks: int, name: str, email: str, subject: str, message: str
) -> tuple:
    """Handle form submission with validation."""
    errors = ["", "", "", ""]
    has_errors = False

    # Validate name
    if not name or len(name.strip()) < 2:
        errors[0] = "Name must be at least 2 characters"
        has_errors = True

    # Validate email
    if not email or "@" not in email:
        errors[1] = "Please enter a valid email address"
        has_errors = True

    # Validate subject
    if not subject:
        errors[2] = "Please select a subject"
        has_errors = True

    # Validate message
    if not message or len(message.strip()) < 10:
        errors[3] = "Message must be at least 10 characters"
        has_errors = True

    if has_errors:
        return (*errors, "")

    # Success message
    success = Card(
        [
            CardContent(
                [
                    html.P(
                        "✅ Form submitted successfully!",
                        className="text-lg font-medium text-center",
                    )
                ]
            )
        ],
        className="bg-secondary",
    )

    return ("", "", "", "", success)


if __name__ == "__main__":
    app.run_server(debug=True)
