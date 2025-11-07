"""Utility functions for handling CSS class names."""

from typing import Any, Optional


def cn(*args: Any) -> str:
    """
    Combine multiple class names into a single string, filtering out None and empty strings.

    This utility function is similar to the popular 'classnames' or 'clsx' libraries
    in JavaScript, providing a convenient way to conditionally combine CSS classes.

    Args:
        *args: Any number of class names (strings), None values, or dictionaries
               where keys are class names and values are booleans indicating
               whether to include the class.

    Returns:
        str: A single space-separated string of class names.

    Examples:
        >>> cn("btn", "btn-primary")
        'btn btn-primary'

        >>> cn("btn", None, "btn-primary")
        'btn btn-primary'

        >>> cn("btn", {"btn-primary": True, "btn-large": False})
        'btn btn-primary'

        >>> is_active = True
        >>> cn("btn", is_active and "active")
        'btn active'
    """
    classes = []

    for arg in args:
        if arg is None or arg == "" or arg is False:
            continue

        if isinstance(arg, str):
            classes.append(arg)
        elif isinstance(arg, dict):
            for key, value in arg.items():
                if value:
                    classes.append(key)
        elif isinstance(arg, (list, tuple)):
            # Recursively handle lists/tuples
            classes.append(cn(*arg))

    return " ".join(filter(None, classes))
