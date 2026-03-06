"""Tests verifying docstrings and type annotations for the pfr/utils module (TGF-171)."""

import inspect
import typing

import pytest

from griddy.pfr.utils.browserless import AsyncBrowserless, Browserless


def _get_methods(cls):
    """Collect all public and private methods defined directly on *cls*."""
    methods = []
    for name, obj in inspect.getmembers(cls, predicate=inspect.isfunction):
        if obj.__qualname__.startswith(cls.__name__):
            methods.append((name, obj))
    return methods


_BROWSERLESS_METHODS = _get_methods(Browserless)
_ASYNC_BROWSERLESS_METHODS = _get_methods(AsyncBrowserless)


@pytest.mark.unit
class TestBrowserlessDocstrings:
    def test_class_has_docstring(self):
        assert Browserless.__doc__ is not None, (
            "Browserless is missing a class docstring"
        )
        assert len(Browserless.__doc__.strip()) > 0

    @pytest.mark.parametrize(
        "name,method",
        [pytest.param(n, m, id=n) for n, m in _BROWSERLESS_METHODS],
    )
    def test_method_has_docstring(self, name, method):
        assert method.__doc__ is not None, f"{name} is missing a docstring"
        assert len(method.__doc__.strip()) > 0, f"{name} has an empty docstring"


@pytest.mark.unit
class TestAsyncBrowserlessDocstrings:
    def test_class_has_docstring(self):
        assert AsyncBrowserless.__doc__ is not None, (
            "AsyncBrowserless is missing a class docstring"
        )
        assert len(AsyncBrowserless.__doc__.strip()) > 0

    @pytest.mark.parametrize(
        "name,method",
        [pytest.param(n, m, id=n) for n, m in _ASYNC_BROWSERLESS_METHODS],
    )
    def test_method_has_docstring(self, name, method):
        assert method.__doc__ is not None, f"{name} is missing a docstring"
        assert len(method.__doc__.strip()) > 0, f"{name} has an empty docstring"


@pytest.mark.unit
class TestBrowserlessModuleDocstring:
    def test_module_has_docstring(self):
        import griddy.pfr.utils.browserless as mod

        assert mod.__doc__ is not None, "browserless module is missing a docstring"
        assert len(mod.__doc__.strip()) > 0


# Methods that were missing return type annotations per TGF-171.
_SYNC_METHODS_NEEDING_RETURN_TYPE = [
    "fetch_data",
    "_handle_page_navigation",
    "get_page_content",
]

_ASYNC_METHODS_NEEDING_RETURN_TYPE = [
    "fetch_data",
    "_handle_page_navigation",
    "get_page_content",
]

# Methods that were missing param types per TGF-171.
_SYNC_METHODS_NEEDING_BROWSER_TYPE = ["_handle_page_navigation"]
_ASYNC_METHODS_NEEDING_BROWSER_TYPE = ["_handle_page_navigation"]


@pytest.mark.unit
class TestBrowserlessTypeAnnotations:
    @pytest.mark.parametrize("method_name", _SYNC_METHODS_NEEDING_RETURN_TYPE)
    def test_method_has_return_type(self, method_name):
        method = getattr(Browserless, method_name)
        hints = typing.get_type_hints(method)
        assert "return" in hints, f"{method_name} is missing a return type annotation"

    @pytest.mark.parametrize("method_name", _SYNC_METHODS_NEEDING_BROWSER_TYPE)
    def test_method_has_browser_param_type(self, method_name):
        method = getattr(Browserless, method_name)
        hints = typing.get_type_hints(method)
        assert "browser" in hints, (
            f"{method_name} is missing a type annotation for 'browser'"
        )


@pytest.mark.unit
class TestAsyncBrowserlessTypeAnnotations:
    @pytest.mark.parametrize("method_name", _ASYNC_METHODS_NEEDING_RETURN_TYPE)
    def test_method_has_return_type(self, method_name):
        method = getattr(AsyncBrowserless, method_name)
        hints = typing.get_type_hints(method)
        assert "return" in hints, f"{method_name} is missing a return type annotation"

    @pytest.mark.parametrize("method_name", _ASYNC_METHODS_NEEDING_BROWSER_TYPE)
    def test_method_has_browser_param_type(self, method_name):
        method = getattr(AsyncBrowserless, method_name)
        hints = typing.get_type_hints(method)
        assert "browser" in hints, (
            f"{method_name} is missing a type annotation for 'browser'"
        )
