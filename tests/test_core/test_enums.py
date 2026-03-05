"""Tests for griddy.core.utils.enums."""

import enum

import pytest

from griddy.core.utils.enums import OpenEnumMeta


def _make_open_enum(name, members):
    """Create an open enum compatible with Python 3.14+."""
    ns = enum.EnumMeta.__prepare__(name, (str, enum.Enum))
    for k, v in members.items():
        ns[k] = v
    return OpenEnumMeta.__new__(OpenEnumMeta, name, (str, enum.Enum), ns)


Season = _make_open_enum("Season", {"REG": "REG", "POST": "POST", "PRE": "PRE"})


@pytest.mark.unit
class TestOpenEnumMeta:
    def test_known_value_returns_correct_value(self):
        result = Season("REG")
        assert result == "REG"

    def test_unknown_value_passes_through(self):
        result = Season("UNKNOWN_SEASON")
        assert result == "UNKNOWN_SEASON"

    def test_all_known_members(self):
        assert Season("POST") == "POST"
        assert Season("PRE") == "PRE"

    def test_unknown_value_type(self):
        result = Season("OFFSEASON")
        assert isinstance(result, str)

    def test_is_enum_subclass(self):
        assert issubclass(type(Season), enum.EnumMeta)

    def test_members_accessible_as_attributes(self):
        assert Season.REG == "REG"
        assert Season.POST == "POST"
        assert Season.PRE == "PRE"
