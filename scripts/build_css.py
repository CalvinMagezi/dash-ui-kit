#!/usr/bin/env python3
"""
CSS Build Script
Combines all CSS files into a single bundle
"""

import os
from pathlib import Path


def minify_css(css_content: str) -> str:
    """Simple CSS minification."""
    # Remove comments
    import re

    css = re.sub(r"/\*.*?\*/", "", css_content, flags=re.DOTALL)
    # Remove extra whitespace
    css = re.sub(r"\s+", " ", css)
    # Remove spaces around special characters
    css = re.sub(r"\s*([{}:;,>~+])\s*", r"\1", css)
    return css.strip()


def get_file_size(content: str) -> str:
    """Get human-readable file size."""
    size = len(content.encode("utf-8"))
    if size < 1024:
        return f"{size} bytes"
    elif size < 1024 * 1024:
        return f"{size / 1024:.2f} KB"
    else:
        return f"{size / (1024 * 1024):.2f} MB"


def build_css() -> None:
    """Build the complete CSS bundle."""
    assets_dir = Path(__file__).parent.parent / "dash_ui_kit" / "assets"

    # Order matters!
    css_files = [
        assets_dir / "variables.css",
        assets_dir / "reset.css",
        assets_dir / "base.css",
        assets_dir / "utilities" / "spacing.css",
        assets_dir / "utilities" / "layout.css",
        assets_dir / "utilities" / "typography.css",
        assets_dir / "utilities" / "colors.css",
        assets_dir / "utilities" / "borders.css",
        assets_dir / "utilities" / "sizing.css",
        assets_dir / "utilities" / "position.css",
        assets_dir / "utilities" / "effects.css",
        assets_dir / "utilities" / "states.css",
        assets_dir / "components.css",
    ]

    # Read and combine all CSS
    combined_css = []
    combined_css.append("/**")
    combined_css.append(" * Dash UI Kit - Complete CSS Bundle")
    combined_css.append(" * Version: 0.1.0")
    combined_css.append(" * License: MIT")
    combined_css.append(" */")
    combined_css.append("")

    total_size = 0
    for css_file in css_files:
        if css_file.exists():
            with open(css_file, "r") as f:
                content = f.read()
                combined_css.append(f"\n/* {css_file.name} */")
                combined_css.append(content)
                total_size += len(content.encode("utf-8"))
                print(f"✅ Included {css_file.name} ({get_file_size(content)})")
        else:
            print(f"⚠️  Skipping {css_file.name} (not found)")

    # Write unminified version
    output_content = "\n".join(combined_css)
    output_file = assets_dir / "core.css"
    with open(output_file, "w") as f:
        f.write(output_content)
    print(f"\n✨ Built core.css ({get_file_size(output_content)})")

    # Write minified version
    minified_content = minify_css(output_content)
    minified_file = assets_dir / "core.min.css"
    with open(minified_file, "w") as f:
        f.write(minified_content)
    print(f"✨ Built core.min.css ({get_file_size(minified_content)})")

    # Calculate reduction
    reduction = (1 - len(minified_content) / len(output_content)) * 100
    print(f"\n📊 Minification reduced size by {reduction:.1f}%")

    # Check if under 50KB target
    if len(minified_content.encode("utf-8")) < 50 * 1024:
        print(f"✅ SUCCESS: Bundle is under 50KB target!")
    else:
        print(f"⚠️  WARNING: Bundle exceeds 50KB target")


if __name__ == "__main__":
    build_css()
