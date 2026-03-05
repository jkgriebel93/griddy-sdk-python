"""Tests for PFRBaseModel shared validators."""

from typing import Dict, List, Optional

import pytest
from pydantic import ValidationError

from griddy.pfr.models.base import PFRBaseModel


class NestedModel(PFRBaseModel):
    value: str


class ModelWithOptionalNested(PFRBaseModel):
    nested: Optional[NestedModel] = None
    name: str = "test"


class ModelWithRequiredNested(PFRBaseModel):
    nested: NestedModel


class ModelWithMultipleOptionals(PFRBaseModel):
    first: Optional[NestedModel] = None
    second: Optional[NestedModel] = None
    label: Optional[str] = None
    count: Optional[int] = None


class ModelWithOptionalDict(PFRBaseModel):
    data: Optional[Dict[str, str]] = None


class ModelWithOptionalList(PFRBaseModel):
    items: Optional[List[str]] = None


@pytest.mark.unit
class TestEmptyDictToNone:
    """Test the _empty_dicts_to_none model validator."""

    def test_empty_dict_converted_to_none_for_optional_field(self):
        result = ModelWithOptionalNested(nested={})
        assert result.nested is None

    def test_populated_dict_still_parsed_as_model(self):
        result = ModelWithOptionalNested(nested={"value": "hello"})
        assert result.nested is not None
        assert result.nested.value == "hello"

    def test_none_value_stays_none(self):
        result = ModelWithOptionalNested(nested=None)
        assert result.nested is None

    def test_missing_optional_field_uses_default(self):
        result = ModelWithOptionalNested()
        assert result.nested is None

    def test_required_field_with_empty_dict_raises(self):
        with pytest.raises(ValidationError):
            ModelWithRequiredNested(nested={})

    def test_multiple_optional_fields_empty_dicts(self):
        result = ModelWithMultipleOptionals(first={}, second={})
        assert result.first is None
        assert result.second is None

    def test_multiple_optional_fields_mixed(self):
        result = ModelWithMultipleOptionals(
            first={"value": "a"}, second={}, label="test"
        )
        assert result.first is not None
        assert result.first.value == "a"
        assert result.second is None
        assert result.label == "test"

    def test_non_dict_optional_fields_unaffected(self):
        result = ModelWithMultipleOptionals(label="hello", count=42)
        assert result.label == "hello"
        assert result.count == 42

    def test_empty_dict_for_optional_dict_field_becomes_none(self):
        result = ModelWithOptionalDict(data={})
        assert result.data is None

    def test_populated_dict_for_dict_field_kept(self):
        result = ModelWithOptionalDict(data={"key": "val"})
        assert result.data == {"key": "val"}

    def test_non_dict_input_passes_through(self):
        """The validator should not interfere with non-dict input."""
        with pytest.raises(ValidationError):
            ModelWithOptionalNested.model_validate("not a dict")

    def test_empty_list_not_converted(self):
        result = ModelWithOptionalList(items=[])
        assert result.items == []

    def test_inherits_base_model_config(self):
        """PFRBaseModel should inherit populate_by_name and other config."""
        assert ModelWithOptionalNested.model_config["populate_by_name"] is True
        assert ModelWithOptionalNested.model_config["arbitrary_types_allowed"] is True


@pytest.mark.unit
class TestPFRBaseModelInheritance:
    """Verify PFRBaseModel works correctly in the inheritance chain."""

    def test_serialize_model_still_works(self):
        """The serialize_model from BaseModel should still function."""
        obj = ModelWithOptionalNested(nested={"value": "test"})
        serialized = obj.model_dump()
        assert "nested" in serialized
        assert serialized["nested"]["value"] == "test"

    def test_serialize_excludes_unset_optional(self):
        obj = ModelWithOptionalNested(name="hello")
        serialized = obj.model_dump()
        assert serialized["name"] == "hello"

    def test_lazy_import_from_models_package(self):
        """PFRBaseModel should be importable from griddy.pfr.models."""
        from griddy.pfr import models

        assert hasattr(models, "PFRBaseModel")
        assert models.PFRBaseModel is PFRBaseModel
