"""Tests verifying docstrings and type annotations for the pfr/parsers module (TGF-170)."""

import inspect
import typing

import pytest

from griddy.pfr.parsers.player_profile import PlayerProfileParser


def _get_methods(cls):
    """Collect all public and private methods defined directly on *cls*."""
    methods = []
    for name, obj in inspect.getmembers(cls, predicate=inspect.isfunction):
        if obj.__qualname__.startswith(cls.__name__):
            methods.append((name, obj))
    return methods


_PARSER_METHODS = _get_methods(PlayerProfileParser)


@pytest.mark.unit
class TestPlayerProfileParserDocstrings:
    def test_class_has_docstring(self):
        assert PlayerProfileParser.__doc__ is not None, (
            "PlayerProfileParser is missing a class docstring"
        )
        assert len(PlayerProfileParser.__doc__.strip()) > 0

    @pytest.mark.parametrize(
        "name,method",
        [pytest.param(n, m, id=n) for n, m in _PARSER_METHODS],
    )
    def test_method_has_docstring(self, name, method):
        assert method.__doc__ is not None, f"{name} is missing a docstring"
        assert len(method.__doc__.strip()) > 0, f"{name} has an empty docstring"


@pytest.mark.unit
class TestPlayerProfileParserModuleDocstring:
    def test_module_has_docstring(self):
        import griddy.pfr.parsers.player_profile as mod

        assert mod.__doc__ is not None, "player_profile module is missing a docstring"
        assert len(mod.__doc__.strip()) > 0


# The four methods that were missing return type annotations per TGF-170.
_METHODS_NEEDING_RETURN_TYPE = [
    "_extract_birth_info",
    "_extract_bio_info",
    "_extract_overheader_indices",
    "_group_by_over_header",
]


@pytest.mark.unit
class TestPlayerProfileParserTypeAnnotations:
    @pytest.mark.parametrize("method_name", _METHODS_NEEDING_RETURN_TYPE)
    def test_method_has_return_type(self, method_name):
        method = getattr(PlayerProfileParser, method_name)
        hints = typing.get_type_hints(method)
        assert "return" in hints, f"{method_name} is missing a return type annotation"
