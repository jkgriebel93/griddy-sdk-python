"""Shared module-level __getattr__/__dir__ for lazy dynamic imports.

Many ``__init__.py`` files use a ``_dynamic_imports`` dict mapping attribute
names to relative module paths, with identical ``__getattr__``/``__dir__``
implementations.  This module provides reusable ``dynamic_getattr`` and
``dynamic_dir`` functions so that pattern only needs to be written once.
"""

import builtins

from ._import import dynamic_import


def dynamic_getattr(
    attr_name: str,
    dynamic_imports: dict[str, str],
    package: str | None,
    module_name: str,
) -> object:
    """Module-level ``__getattr__`` backed by a *dynamic_imports* mapping.

    :param attr_name: The attribute being looked up.
    :param dynamic_imports: ``{attr: relative_module}`` mapping.
    :param package: ``__package__`` of the calling module (for relative imports).
    :param module_name: ``__name__`` of the calling module (for error messages).
    """
    relative_module = dynamic_imports.get(attr_name)
    if relative_module is None:
        raise AttributeError(
            f"No {attr_name} found in _dynamic_imports for module name -> {module_name} "
        )

    try:
        module = dynamic_import(relative_module, package)
        return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(
            f"Failed to import {attr_name} from {relative_module}: {e}"
        ) from e
    except AttributeError as e:
        raise AttributeError(
            f"Failed to get {attr_name} from {relative_module}: {e}"
        ) from e


def dynamic_dir(dynamic_imports: dict[str, str]) -> list[str]:
    """Module-level ``__dir__`` that exposes lazy-importable names."""
    return builtins.sorted(builtins.list(dynamic_imports.keys()))
