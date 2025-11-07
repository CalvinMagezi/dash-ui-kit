"""Default theme configuration."""

from typing import Dict, Any

default_theme: Dict[str, Any] = {
    "colors": {
        "primary": "220 80% 50%",
        "secondary": "210 40% 96%",
        "accent": "270 60% 55%",
        "background": "0 0% 100%",
        "foreground": "222 47% 11%",
        "muted": "210 40% 96%",
        "muted_foreground": "215 16% 47%",
        "border": "214 32% 91%",
        "input": "214 32% 91%",
        "ring": "220 80% 50%",
        "destructive": "0 84% 60%",
        "destructive_foreground": "0 0% 98%",
    },
    "spacing": {
        "0": "0",
        "1": "0.25rem",
        "2": "0.5rem",
        "3": "0.75rem",
        "4": "1rem",
        "5": "1.25rem",
        "6": "1.5rem",
        "8": "2rem",
        "10": "2.5rem",
        "12": "3rem",
        "16": "4rem",
        "20": "5rem",
        "24": "6rem",
    },
    "typography": {
        "xs": "0.75rem",
        "sm": "0.875rem",
        "base": "1rem",
        "lg": "1.125rem",
        "xl": "1.25rem",
        "2xl": "1.5rem",
        "3xl": "1.875rem",
        "4xl": "2.25rem",
    },
    "border_radius": {
        "sm": "0.25rem",
        "md": "0.5rem",
        "lg": "1rem",
        "full": "9999px",
    },
    "shadows": {
        "sm": "0 1px 2px 0 rgb(0 0 0 / 0.05)",
        "md": "0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)",
        "lg": "0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)",
        "xl": "0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)",
    },
}
