#!/usr/bin/env python3
"""
CSS Utility Generator Script
Generates Tailwind-like utility classes for Dash UI Kit
"""

import os
from pathlib import Path
from typing import Dict, List


def generate_spacing_utilities() -> str:
    """Generate spacing utilities (padding, margin)."""
    sizes = {
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
    }

    properties = {"p": "padding", "m": "margin"}

    sides = {
        "": [""],
        "t": ["-top"],
        "r": ["-right"],
        "b": ["-bottom"],
        "l": ["-left"],
        "x": ["-left", "-right"],
        "y": ["-top", "-bottom"],
    }

    css = ["/* Spacing Utilities (Padding & Margin) */\n"]

    for prop_short, prop_full in properties.items():
        for side_short, side_list in sides.items():
            for size_name, size_value in sizes.items():
                class_name = f".{prop_short}{side_short}-{size_name}"
                if len(side_list) > 1:
                    # Handle x and y axis
                    rules = "; ".join([f"{prop_full}{side}: {size_value}" for side in side_list])
                    css.append(f"{class_name} {{ {rules}; }}")
                else:
                    side = side_list[0]
                    css.append(f"{class_name} {{ {prop_full}{side}: {size_value}; }}")

    # Auto margin
    css.append(".mx-auto { margin-left: auto; margin-right: auto; }")
    css.append(".my-auto { margin-top: auto; margin-bottom: auto; }")

    return "\n".join(css)


def generate_layout_utilities() -> str:
    """Generate layout utilities (flexbox, grid, display)."""
    css = ["/* Layout Utilities */\n"]

    # Display
    displays = ["block", "inline-block", "inline", "flex", "inline-flex", "grid", "inline-grid", "hidden"]
    for display in displays:
        value = "none" if display == "hidden" else display
        css.append(f".{display} {{ display: {value}; }}")

    # Flexbox
    css.append("\n/* Flexbox */")
    css.append(".flex-row { flex-direction: row; }")
    css.append(".flex-col { flex-direction: column; }")
    css.append(".flex-wrap { flex-wrap: wrap; }")
    css.append(".flex-nowrap { flex-wrap: nowrap; }")

    # Justify content
    justify = {
        "justify-start": "flex-start",
        "justify-end": "flex-end",
        "justify-center": "center",
        "justify-between": "space-between",
        "justify-around": "space-around",
        "justify-evenly": "space-evenly",
    }
    for class_name, value in justify.items():
        css.append(f".{class_name} {{ justify-content: {value}; }}")

    # Align items
    align = {
        "items-start": "flex-start",
        "items-end": "flex-end",
        "items-center": "center",
        "items-baseline": "baseline",
        "items-stretch": "stretch",
    }
    for class_name, value in align.items():
        css.append(f".{class_name} {{ align-items: {value}; }}")

    # Align self
    align_self = {
        "self-auto": "auto",
        "self-start": "flex-start",
        "self-end": "flex-end",
        "self-center": "center",
        "self-stretch": "stretch",
    }
    for class_name, value in align_self.items():
        css.append(f".{class_name} {{ align-self: {value}; }}")

    # Flex grow/shrink
    css.append(".flex-1 { flex: 1 1 0%; }")
    css.append(".flex-auto { flex: 1 1 auto; }")
    css.append(".flex-initial { flex: 0 1 auto; }")
    css.append(".flex-none { flex: none; }")

    # Gap
    gaps = {"1": "0.25rem", "2": "0.5rem", "3": "0.75rem", "4": "1rem", "6": "1.5rem", "8": "2rem"}
    for size, value in gaps.items():
        css.append(f".gap-{size} {{ gap: {value}; }}")
        css.append(f".gap-x-{size} {{ column-gap: {value}; }}")
        css.append(f".gap-y-{size} {{ row-gap: {value}; }}")

    # Grid
    css.append("\n/* Grid */")
    for i in range(1, 13):
        css.append(f".grid-cols-{i} {{ grid-template-columns: repeat({i}, minmax(0, 1fr)); }}")

    return "\n".join(css)


def generate_typography_utilities() -> str:
    """Generate typography utilities."""
    css = ["/* Typography Utilities */\n"]

    # Font sizes
    sizes = {
        "xs": "0.75rem",
        "sm": "0.875rem",
        "base": "1rem",
        "lg": "1.125rem",
        "xl": "1.25rem",
        "2xl": "1.5rem",
        "3xl": "1.875rem",
        "4xl": "2.25rem",
    }
    for name, value in sizes.items():
        css.append(f".text-{name} {{ font-size: {value}; }}")

    # Font weights
    weights = {"normal": "400", "medium": "500", "semibold": "600", "bold": "700"}
    for name, value in weights.items():
        css.append(f".font-{name} {{ font-weight: {value}; }}")

    # Text alignment
    aligns = ["left", "center", "right", "justify"]
    for align in aligns:
        css.append(f".text-{align} {{ text-align: {align}; }}")

    # Text transform
    css.append(".uppercase { text-transform: uppercase; }")
    css.append(".lowercase { text-transform: lowercase; }")
    css.append(".capitalize { text-transform: capitalize; }")

    # Line height
    css.append(".leading-tight { line-height: 1.25; }")
    css.append(".leading-normal { line-height: 1.5; }")
    css.append(".leading-relaxed { line-height: 1.75; }")

    # Text decoration
    css.append(".underline { text-decoration: underline; }")
    css.append(".line-through { text-decoration: line-through; }")
    css.append(".no-underline { text-decoration: none; }")

    return "\n".join(css)


def generate_color_utilities() -> str:
    """Generate color utilities."""
    css = ["/* Color Utilities */\n"]

    colors = {
        "primary": "var(--color-primary)",
        "secondary": "var(--color-secondary)",
        "accent": "var(--color-accent)",
        "background": "var(--color-background)",
        "foreground": "var(--color-foreground)",
        "muted": "var(--color-muted)",
        "muted-foreground": "var(--color-muted-foreground)",
        "border": "var(--color-border)",
        "destructive": "var(--color-destructive)",
    }

    # Text colors
    for name, value in colors.items():
        css.append(f".text-{name} {{ color: hsl({value}); }}")

    # Background colors
    for name, value in colors.items():
        css.append(f".bg-{name} {{ background-color: hsl({value}); }}")

    # Border colors
    for name, value in colors.items():
        css.append(f".border-{name} {{ border-color: hsl({value}); }}")

    # Opacity utilities
    for opacity in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        css.append(f".opacity-{opacity} {{ opacity: {opacity / 100}; }}")

    return "\n".join(css)


def generate_border_utilities() -> str:
    """Generate border utilities."""
    css = ["/* Border Utilities */\n"]

    # Border width
    css.append(".border { border-width: 1px; }")
    css.append(".border-0 { border-width: 0; }")
    css.append(".border-2 { border-width: 2px; }")
    css.append(".border-4 { border-width: 4px; }")

    # Border sides
    sides = ["t", "r", "b", "l"]
    side_names = {"t": "top", "r": "right", "b": "bottom", "l": "left"}
    for side in sides:
        css.append(f".border-{side} {{ border-{side_names[side]}-width: 1px; }}")

    # Border style
    css.append(".border-solid { border-style: solid; }")
    css.append(".border-dashed { border-style: dashed; }")
    css.append(".border-dotted { border-style: dotted; }")
    css.append(".border-none { border-style: none; }")

    # Border radius
    radius = {
        "sm": "0.25rem",
        "md": "0.5rem",
        "lg": "1rem",
        "full": "9999px",
        "none": "0",
    }
    for name, value in radius.items():
        css.append(f".rounded-{name} {{ border-radius: {value}; }}")

    css.append(".rounded { border-radius: 0.25rem; }")

    return "\n".join(css)


def generate_effect_utilities() -> str:
    """Generate effect utilities (shadows, transitions)."""
    css = ["/* Effect Utilities */\n"]

    # Shadows
    shadows = {
        "sm": "var(--shadow-sm)",
        "md": "var(--shadow-md)",
        "lg": "var(--shadow-lg)",
        "xl": "var(--shadow-xl)",
        "none": "none",
    }
    for name, value in shadows.items():
        if name == "none":
            css.append(f".shadow-{name} {{ box-shadow: {value}; }}")
        else:
            css.append(f".shadow-{name} {{ box-shadow: {value}; }}")

    css.append(".shadow { box-shadow: var(--shadow-md); }")

    # Transitions
    css.append(".transition { transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter; transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1); transition-duration: 150ms; }")
    css.append(".transition-all { transition-property: all; transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1); transition-duration: 150ms; }")
    css.append(".transition-colors { transition-property: color, background-color, border-color, text-decoration-color, fill, stroke; transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1); transition-duration: 150ms; }")

    # Duration
    css.append(".duration-75 { transition-duration: 75ms; }")
    css.append(".duration-100 { transition-duration: 100ms; }")
    css.append(".duration-150 { transition-duration: 150ms; }")
    css.append(".duration-200 { transition-duration: 200ms; }")
    css.append(".duration-300 { transition-duration: 300ms; }")
    css.append(".duration-500 { transition-duration: 500ms; }")

    return "\n".join(css)


def generate_state_utilities() -> str:
    """Generate state utilities (hover, focus, active, disabled)."""
    css = ["/* State Utilities */\n"]

    css.append("/* Hover states */")
    css.append(".hover\\:opacity-80:hover { opacity: 0.8; }")
    css.append(".hover\\:opacity-90:hover { opacity: 0.9; }")
    css.append(".hover\\:bg-primary:hover { background-color: hsl(var(--color-primary)); }")
    css.append(".hover\\:bg-secondary:hover { background-color: hsl(var(--color-secondary)); }")
    css.append(".hover\\:bg-accent:hover { background-color: hsl(var(--color-accent)); }")
    css.append(".hover\\:bg-muted:hover { background-color: hsl(var(--color-muted)); }")

    css.append("\n/* Focus states */")
    css.append(".focus\\:ring:focus { outline: 2px solid hsl(var(--color-ring)); outline-offset: 2px; }")
    css.append(".focus\\:ring-2:focus { box-shadow: 0 0 0 2px hsl(var(--color-ring)); }")

    css.append("\n/* Active states */")
    css.append(".active\\:scale-95:active { transform: scale(0.95); }")

    css.append("\n/* Disabled states */")
    css.append(".disabled\\:opacity-50:disabled { opacity: 0.5; }")
    css.append(".disabled\\:pointer-events-none:disabled { pointer-events: none; }")

    return "\n".join(css)


def generate_sizing_utilities() -> str:
    """Generate width and height utilities."""
    css = ["/* Sizing Utilities */\n"]

    # Width
    css.append(".w-full { width: 100%; }")
    css.append(".w-auto { width: auto; }")
    css.append(".w-screen { width: 100vw; }")

    for i in [1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24]:
        css.append(f".w-{i} {{ width: {i * 0.25}rem; }}")

    # Height
    css.append(".h-full { height: 100%; }")
    css.append(".h-auto { height: auto; }")
    css.append(".h-screen { height: 100vh; }")

    for i in [1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24]:
        css.append(f".h-{i} {{ height: {i * 0.25}rem; }}")

    # Min/Max width
    css.append(".min-w-0 { min-width: 0; }")
    css.append(".min-w-full { min-width: 100%; }")
    css.append(".max-w-xs { max-width: 20rem; }")
    css.append(".max-w-sm { max-width: 24rem; }")
    css.append(".max-w-md { max-width: 28rem; }")
    css.append(".max-w-lg { max-width: 32rem; }")
    css.append(".max-w-xl { max-width: 36rem; }")
    css.append(".max-w-2xl { max-width: 42rem; }")
    css.append(".max-w-full { max-width: 100%; }")

    # Min/Max height
    css.append(".min-h-screen { min-height: 100vh; }")
    css.append(".min-h-full { min-height: 100%; }")

    return "\n".join(css)


def generate_position_utilities() -> str:
    """Generate position utilities."""
    css = ["/* Position Utilities */\n"]

    positions = ["static", "fixed", "absolute", "relative", "sticky"]
    for pos in positions:
        css.append(f".{pos} {{ position: {pos}; }}")

    # Inset
    css.append(".inset-0 { top: 0; right: 0; bottom: 0; left: 0; }")
    css.append(".inset-x-0 { left: 0; right: 0; }")
    css.append(".inset-y-0 { top: 0; bottom: 0; }")

    # Individual sides
    for side in ["top", "right", "bottom", "left"]:
        css.append(f".{side}-0 {{ {side}: 0; }}")

    # Z-index
    css.append(".z-0 { z-index: 0; }")
    css.append(".z-10 { z-index: 10; }")
    css.append(".z-20 { z-index: 20; }")
    css.append(".z-30 { z-index: 30; }")
    css.append(".z-40 { z-index: 40; }")
    css.append(".z-50 { z-index: 50; }")

    return "\n".join(css)


def main() -> None:
    """Generate all utility CSS files."""
    base_dir = Path(__file__).parent.parent / "dash_ui_kit" / "assets" / "utilities"
    base_dir.mkdir(parents=True, exist_ok=True)

    utilities = {
        "spacing.css": generate_spacing_utilities(),
        "layout.css": generate_layout_utilities(),
        "typography.css": generate_typography_utilities(),
        "colors.css": generate_color_utilities(),
        "borders.css": generate_border_utilities(),
        "effects.css": generate_effect_utilities(),
        "states.css": generate_state_utilities(),
        "sizing.css": generate_sizing_utilities(),
        "position.css": generate_position_utilities(),
    }

    for filename, content in utilities.items():
        filepath = base_dir / filename
        with open(filepath, "w") as f:
            f.write(content)
        print(f"✅ Generated {filename} ({len(content)} bytes)")

    print(f"\n✨ Successfully generated {len(utilities)} utility files!")


if __name__ == "__main__":
    main()
