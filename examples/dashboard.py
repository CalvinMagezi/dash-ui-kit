"""Dashboard example showcasing multiple components."""

from dash import Dash, html

from dash_ui_kit import (
    Badge,
    Button,
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
)

app = Dash(__name__)

app.layout = html.Div(
    [
        # Header
        html.Div(
            [
                html.H1(
                    "Analytics Dashboard",
                    className="text-3xl font-bold text-foreground",
                ),
                html.P(
                    "Welcome back! Here's your overview.",
                    className="text-muted-foreground",
                ),
            ],
            className="mb-8",
        ),
        # Stats cards
        html.Div(
            [
                Card(
                    [
                        CardHeader(
                            [
                                CardTitle("Total Users"),
                                CardDescription("Active users this month"),
                            ]
                        ),
                        CardContent(
                            [
                                html.P("12,345", className="text-4xl font-bold"),
                                html.P(
                                    "+20.1% from last month",
                                    className="text-sm text-muted-foreground mt-2",
                                ),
                            ]
                        ),
                    ],
                    className="flex-1",
                ),
                Card(
                    [
                        CardHeader(
                            [
                                CardTitle("Revenue"),
                                CardDescription("Total revenue this month"),
                            ]
                        ),
                        CardContent(
                            [
                                html.P("$45,231", className="text-4xl font-bold"),
                                html.P(
                                    "+15.2% from last month",
                                    className="text-sm text-muted-foreground mt-2",
                                ),
                            ]
                        ),
                    ],
                    className="flex-1",
                ),
                Card(
                    [
                        CardHeader(
                            [
                                CardTitle("Orders"),
                                CardDescription("Processed this week"),
                            ]
                        ),
                        CardContent(
                            [
                                html.P("573", className="text-4xl font-bold"),
                                html.P(
                                    "+8.5% from last week",
                                    className="text-sm text-muted-foreground mt-2",
                                ),
                            ]
                        ),
                    ],
                    className="flex-1",
                ),
            ],
            className="grid grid-cols-3 gap-4 mb-6",
        ),
        # Recent activity card
        Card(
            [
                CardHeader(
                    [
                        html.Div(
                            [
                                CardTitle("Recent Activity"),
                                html.Div(
                                    [
                                        Badge("New", variant="default", size="sm"),
                                    ],
                                    className="ml-2",
                                ),
                            ],
                            className="flex items-center",
                        ),
                        CardDescription("Latest updates from your team"),
                    ]
                ),
                CardContent(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.P(
                                            "New user registration",
                                            className="font-medium",
                                        ),
                                        html.P(
                                            "John Doe joined the platform",
                                            className="text-sm text-muted-foreground",
                                        ),
                                    ],
                                    className="flex-1",
                                ),
                                html.P("2 min ago", className="text-sm text-muted-foreground"),
                            ],
                            className="flex justify-between items-start mb-4 pb-4 border-b border-border",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.P(
                                            "Payment processed",
                                            className="font-medium",
                                        ),
                                        html.P(
                                            "Order #1234 completed",
                                            className="text-sm text-muted-foreground",
                                        ),
                                    ],
                                    className="flex-1",
                                ),
                                html.P("15 min ago", className="text-sm text-muted-foreground"),
                            ],
                            className="flex justify-between items-start mb-4 pb-4 border-b border-border",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.P(
                                            "System update",
                                            className="font-medium",
                                        ),
                                        html.P(
                                            "Version 2.0 deployed successfully",
                                            className="text-sm text-muted-foreground",
                                        ),
                                    ],
                                    className="flex-1",
                                ),
                                html.P("1 hour ago", className="text-sm text-muted-foreground"),
                            ],
                            className="flex justify-between items-start",
                        ),
                    ]
                ),
                CardFooter(
                    [
                        Button(
                            "View All Activity",
                            variant="outline",
                            size="sm",
                            className="w-full",
                        )
                    ]
                ),
            ],
            variant="elevated",
        ),
    ],
    className="container mx-auto p-8 min-h-screen bg-background",
)

if __name__ == "__main__":
    app.run_server(debug=True)
