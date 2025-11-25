# Implementation Plan: Deduplicate dynamic_import Logic

## Priority: 3
## Estimated Effort: Low
## Impact: Medium - Eliminates code duplication, single source of truth

---

## Problem Statement

The `dynamic_import()` function is duplicated in two locations with identical implementations:

1. **`src/griddy/nfl/sdk.py`** (lines 246-255)
2. **`src/griddy/nfl/endpoints/pro/stats/__init__.py`** (lines 70-78)

Both implementations:
- Take a module name and retry count
- Attempt imports with retry logic
- Handle `KeyError` for half-initialized modules
- Clear `sys.modules` on failure

---

## Current Duplicated Code

### Location 1: `sdk.py`

```python
def dynamic_import(self, modname, retries=3):
    for attempt in range(retries):
        try:
            return importlib.import_module(modname)
        except KeyError:
            # Clear any half-initialized module and retry
            sys.modules.pop(modname, None)
            if attempt == retries - 1:
                break
    raise KeyError(f"Failed to import module '{modname}' after {retries} attempts")
```

### Location 2: `endpoints/pro/stats/__init__.py`

```python
def dynamic_import(self, modname, retries=3):
    for attempt in range(retries):
        try:
            return importlib.import_module(modname)
        except KeyError:
            sys.modules.pop(modname, None)
            if attempt == retries - 1:
                break
    raise KeyError(f"Failed to import module '{modname}' after {retries} attempts")
```

### Location 3: `utils/__init__.py`

There's also a similar function in utils:

```python
def dynamic_import(modname, retries=3):
    for attempt in range(retries):
        try:
            return import_module(modname, __package__)
        except KeyError:
            sys.modules.pop(modname, None)
            if attempt == retries - 1:
                break
    raise KeyError(f"Failed to import module '{modname}' after {retries} attempts")
```

Note: This version uses `import_module(modname, __package__)` for relative imports.

---

## Implementation Steps

### Step 1: Create Centralized Import Utility

**File:** `src/griddy/nfl/utils/imports.py` (new file)

```python
"""Dynamic import utilities for lazy-loading SDK components."""

import importlib
import sys
from typing import Any


def dynamic_import(
    modname: str,
    package: str | None = None,
    retries: int = 3,
) -> Any:
    """
    Dynamically import a module with retry logic.

    Handles edge cases where modules may be half-initialized during
    complex import chains by clearing sys.modules and retrying.

    Args:
        modname: The module name to import (absolute or relative)
        package: Package for relative imports (required if modname starts with '.')
        retries: Number of import attempts before raising

    Returns:
        The imported module

    Raises:
        KeyError: If import fails after all retries
        ImportError: If the module cannot be found

    Example:
        # Absolute import
        module = dynamic_import("griddy.nfl.endpoints.pro.players")

        # Relative import (from within griddy.nfl.utils)
        module = dynamic_import(".metadata", package="griddy.nfl.utils")
    """
    for attempt in range(retries):
        try:
            if package is not None:
                return importlib.import_module(modname, package)
            return importlib.import_module(modname)
        except KeyError:
            # Clear any half-initialized module and retry
            # This can happen during circular import resolution
            full_name = modname if package is None else f"{package}.{modname.lstrip('.')}"
            sys.modules.pop(full_name, None)
            sys.modules.pop(modname, None)
            if attempt == retries - 1:
                break

    raise KeyError(f"Failed to import module '{modname}' after {retries} attempts")


def lazy_import(modname: str, classname: str, package: str | None = None) -> Any:
    """
    Lazily import a class from a module.

    Args:
        modname: The module containing the class
        classname: The name of the class to import
        package: Package for relative imports

    Returns:
        The imported class

    Raises:
        AttributeError: If the class is not found in the module
        KeyError: If the module cannot be imported
    """
    module = dynamic_import(modname, package=package)
    return getattr(module, classname)
```

### Step 2: Update utils/__init__.py

**File:** `src/griddy/nfl/utils/__init__.py`

```python
# Add to imports
from .imports import dynamic_import, lazy_import

# Add to __all__
__all__ = [
    # ... existing exports ...
    "dynamic_import",
    "lazy_import",
]

# Remove the local dynamic_import function (lines 163-172)
```

### Step 3: Update sdk.py

**File:** `src/griddy/nfl/sdk.py`

```python
# Before
import importlib
import sys
# ...

class GriddyNFL(BaseSDK):
    # ...

    def dynamic_import(self, modname, retries=3):
        for attempt in range(retries):
            try:
                return importlib.import_module(modname)
            except KeyError:
                sys.modules.pop(modname, None)
                if attempt == retries - 1:
                    break
        raise KeyError(f"Failed to import module '{modname}' after {retries} attempts")

    def __getattr__(self, name: str):
        if name in self._sub_sdk_map:
            module_path, class_name = self._sub_sdk_map[name]
            try:
                module = self.dynamic_import(module_path)
                # ...
```

```python
# After
from griddy.nfl.utils import dynamic_import
# Remove: import importlib
# Remove: import sys (if no longer needed)

class GriddyNFL(BaseSDK):
    # Remove the dynamic_import method entirely

    def __getattr__(self, name: str):
        if name in self._sub_sdk_map:
            module_path, class_name = self._sub_sdk_map[name]
            try:
                module = dynamic_import(module_path)  # Use utility function
                # ...
```

### Step 4: Update StatsSDK

**File:** `src/griddy/nfl/endpoints/pro/stats/__init__.py`

```python
# Before
import importlib
import sys
# ...

class StatsSDK(ProSDK):
    # ...

    def dynamic_import(self, modname, retries=3):
        for attempt in range(retries):
            try:
                return importlib.import_module(modname)
            except KeyError:
                sys.modules.pop(modname, None)
                if attempt == retries - 1:
                    break
        raise KeyError(f"Failed to import module '{modname}' after {retries} attempts")

    def __getattr__(self, name: str):
        if name in self._sub_sdk_map:
            module_path, class_name = self._sub_sdk_map[name]
            try:
                module = self.dynamic_import(module_path)
                # ...
```

```python
# After
from griddy.nfl.utils import dynamic_import
# Remove: import importlib
# Remove: import sys (if no longer needed)

class StatsSDK(ProSDK):
    # Remove the dynamic_import method entirely

    def __getattr__(self, name: str):
        if name in self._sub_sdk_map:
            module_path, class_name = self._sub_sdk_map[name]
            try:
                module = dynamic_import(module_path)  # Use utility function
                # ...
```

### Step 5: Consider Extracting Lazy Loading Mixin

Since both `GriddyNFL` and `StatsSDK` share the same `__getattr__` and `__dir__` patterns, consider a mixin:

**File:** `src/griddy/nfl/utils/lazy_loading.py` (optional enhancement)

```python
"""Mixin for lazy-loading sub-SDKs."""

from typing import Dict, Tuple, Any
from .imports import dynamic_import


class LazyLoadingMixin:
    """
    Mixin that provides lazy loading of sub-SDKs.

    Classes using this mixin must define:
    - _sub_sdk_map: Dict[str, Tuple[str, str]] mapping attribute names to (module_path, class_name)
    - sdk_configuration: SDKConfiguration instance
    - parent_ref: Optional reference to parent SDK
    """

    _sub_sdk_map: Dict[str, Tuple[str, str]]

    def __getattr__(self, name: str) -> Any:
        if name in self._sub_sdk_map:
            module_path, class_name = self._sub_sdk_map[name]
            try:
                module = dynamic_import(module_path)
                klass = getattr(module, class_name)
                instance = klass(self.sdk_configuration, parent_ref=getattr(self, 'parent_ref', self))
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

    def __dir__(self):
        default_attrs = list(super().__dir__())
        lazy_attrs = list(self._sub_sdk_map.keys())
        return sorted(list(set(default_attrs + lazy_attrs)))
```

Then update classes:

```python
# sdk.py
from griddy.nfl.utils.lazy_loading import LazyLoadingMixin

class GriddyNFL(LazyLoadingMixin, BaseSDK):
    # Remove __getattr__ and __dir__ methods
    pass

# endpoints/pro/stats/__init__.py
from griddy.nfl.utils.lazy_loading import LazyLoadingMixin

class StatsSDK(LazyLoadingMixin, ProSDK):
    # Remove __getattr__ and __dir__ methods
    pass
```

### Step 6: Add Unit Tests

**File:** `tests/test_nfl/test_utils/test_imports.py`

```python
import pytest
from griddy.nfl.utils.imports import dynamic_import, lazy_import


class TestDynamicImport:
    def test_imports_existing_module(self):
        module = dynamic_import("griddy.nfl.models")
        assert hasattr(module, "Security")

    def test_raises_on_nonexistent_module(self):
        with pytest.raises(ImportError):
            dynamic_import("griddy.nfl.nonexistent_module")

    def test_relative_import_with_package(self):
        module = dynamic_import(".metadata", package="griddy.nfl.utils")
        assert module is not None

    def test_retries_on_key_error(self, mocker):
        # Mock to raise KeyError once, then succeed
        import_mock = mocker.patch("importlib.import_module")
        import_mock.side_effect = [KeyError("test"), mocker.MagicMock()]

        result = dynamic_import("some.module", retries=3)
        assert import_mock.call_count == 2


class TestLazyImport:
    def test_imports_class_from_module(self):
        klass = lazy_import("griddy.nfl.models", "Security")
        assert klass.__name__ == "Security"

    def test_raises_on_missing_class(self):
        with pytest.raises(AttributeError):
            lazy_import("griddy.nfl.models", "NonexistentClass")
```

---

## Validation Checklist

- [ ] `utils/imports.py` created with `dynamic_import()` and `lazy_import()`
- [ ] `utils/__init__.py` updated to export new functions
- [ ] `sdk.py` updated to use utility function
- [ ] `endpoints/pro/stats/__init__.py` updated to use utility function
- [ ] (Optional) `LazyLoadingMixin` created and applied
- [ ] Unit tests added for import utilities
- [ ] All existing tests pass
- [ ] SDK initialization works correctly
- [ ] Sub-SDK lazy loading works correctly

---

## Files Modified

| File | Change Type |
|------|-------------|
| `utils/imports.py` | New file |
| `utils/__init__.py` | Add exports, remove duplicate |
| `sdk.py` | Remove method, use utility |
| `endpoints/pro/stats/__init__.py` | Remove method, use utility |
| `utils/lazy_loading.py` | New file (optional) |
| `tests/test_nfl/test_utils/test_imports.py` | New tests |

---

## Line Count Impact

| Location | Before | After | Saved |
|----------|--------|-------|-------|
| `sdk.py` | 10 lines | 1 import | 9 lines |
| `stats/__init__.py` | 9 lines | 1 import | 8 lines |
| `utils/__init__.py` | 10 lines | 1 import | 9 lines |
| **Total** | **29 lines** | **3 imports** | **26 lines** |

Plus improved maintainability - changes only need to happen in one place.
