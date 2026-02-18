"""Mixin for lazy-loading sub-SDKs via a _sub_sdk_map dict.

Sub-SDK aggregator classes (FootballStatsSDK, StatsSDK, GriddyNFL) all need
the same pattern: a ``_sub_sdk_map`` dict mapping attribute names to
``(module_path, class_name)`` tuples, with ``__getattr__`` that dynamically
imports and caches sub-SDK instances on first access.

This mixin provides that behaviour so each class only needs to define its
``_sub_sdk_map``.
"""

from typing import Any, Dict, List, Tuple

from ._import import dynamic_import


class LazySubSDKMixin:
    """Mixin that enables lazy-loading of sub-SDKs from ``_sub_sdk_map``.

    Classes using this mixin must:
    1. Define a class-level ``_sub_sdk_map: Dict[str, Tuple[str, str]]``
    2. Have ``sdk_configuration`` and ``parent_ref`` attributes (from BaseSDK)
    """

    _sub_sdk_map: Dict[str, Tuple[str, str]] = {}

    def __getattr__(self, name: str) -> Any:
        if name in self._sub_sdk_map:
            module_path, class_name = self._sub_sdk_map[name]
            try:
                module = dynamic_import(module_path)
                klass = getattr(module, class_name)
                instance = klass(self.sdk_configuration, parent_ref=self.parent_ref)
                setattr(self, name, instance)
                return instance
            except ImportError as e:
                raise AttributeError(
                    f"Failed to import module {module_path} for attribute {name}: {e}"
                ) from e
            except AttributeError as e:
                raise AttributeError(
                    f"Failed to find class {class_name} in module {module_path}: {e}"
                ) from e

        raise AttributeError(
            f"'{type(self).__name__}' object has no attribute '{name}'"
        )

    def __dir__(self) -> List[str]:
        default_attrs = list(super().__dir__())
        lazy_attrs = list(self._sub_sdk_map.keys())
        return sorted(list(set(default_attrs + lazy_attrs)))
