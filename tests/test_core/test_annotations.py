"""Tests for griddy.core.utils.annotations."""

from enum import Enum

import pytest

from griddy.core.utils.annotations import get_discriminator


class Color(Enum):
    RED = "red"
    BLUE = "blue"


class FakeModel:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


@pytest.mark.unit
class TestGetDiscriminator:
    def test_dict_with_key(self):
        result = get_discriminator({"type": "pass"}, "type", "type")
        assert result == "pass"

    def test_object_with_attribute(self):
        obj = FakeModel(kind="rush")
        result = get_discriminator(obj, "kind", "kind")
        assert result == "rush"

    def test_object_with_uppercase_attribute(self):
        obj = FakeModel(KIND="rush")
        result = get_discriminator(obj, "kind", "kind")
        assert result == "rush"

    def test_enum_attribute(self):
        obj = FakeModel(color=Color.RED)
        result = get_discriminator(obj, "color", "color")
        assert result == "red"

    def test_enum_uppercase_attribute(self):
        obj = FakeModel(COLOR=Color.BLUE)
        result = get_discriminator(obj, "color", "color")
        assert result == "blue"

    def test_nested_dict(self):
        model = {"outer": {"type": "nested_value"}}
        result = get_discriminator(model, "type", "type")
        assert result == "nested_value"

    def test_nested_list_in_dict(self):
        model = {"items": [{"type": "list_item"}]}
        result = get_discriminator(model, "type", "type")
        assert result == "list_item"

    def test_list_of_dicts(self):
        model = [{"type": "first"}]
        result = get_discriminator(model, "type", "type")
        assert result == "first"

    def test_raises_when_not_found(self):
        with pytest.raises(ValueError, match="Could not find discriminator"):
            get_discriminator({"no_match": 1}, "type", "type")

    def test_raises_for_empty_dict(self):
        with pytest.raises(ValueError, match="Could not find discriminator"):
            get_discriminator({}, "type", "type")
