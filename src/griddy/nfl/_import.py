"""Shared dynamic import utility with retry logic.

This module provides a thread-safe dynamic import function with retry support
for handling race conditions during parallel module imports.
"""

import sys
from importlib import import_module


def dynamic_import(modname: str, package: str | None = None, retries: int = 3):
    """Dynamically import a module with retry logic for handling race conditions.

    This function handles edge cases where parallel imports can cause KeyError
    due to half-initialized modules in sys.modules.

    :param modname: The name of the module to import (absolute or relative)
    :param package: The package name for relative imports (e.g., __package__)
    :param retries: Number of retry attempts (default: 3)
    :returns: The imported module
    :raises KeyError: If import fails after all retries
    """
    for attempt in range(retries):
        try:
            return import_module(modname, package)
        except KeyError:
            # Clear any half-initialized module and retry
            sys.modules.pop(modname, None)
            if attempt == retries - 1:
                break
    raise KeyError(f"Failed to import module '{modname}' after {retries} attempts")
