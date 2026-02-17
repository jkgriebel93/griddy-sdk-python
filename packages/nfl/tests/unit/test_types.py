"""
Unit tests for griddy.nfl.types module
"""

from dataclasses import field

import pytest
from pydantic import Field

from griddy_nfl.types import (
    UNSET,
    UNSET_SENTINEL,
    BaseModel,
    Nullable,
    OptionalNullable,
    UnrecognizedInt,
    UnrecognizedStr,
)


@pytest.mark.unit
class TestUNSET:
    """Test cases for UNSET singleton and utilities"""

    def test_unset_is_singleton(self):
        """Test that UNSET is a singleton instance"""
        from griddy_nfl.types import UNSET as unset1
        from griddy_nfl.types.basemodel import UNSET as unset2

        assert unset1 is unset2

    def test_unset_boolean_false(self):
        """Test that UNSET evaluates to False in boolean context"""
        assert not UNSET
        assert bool(UNSET) is False

    def test_unset_sentinel_value(self):
        """Test the UNSET_SENTINEL string value"""
        assert UNSET_SENTINEL == "~?~unset~?~sentinel~?~"
        assert isinstance(UNSET_SENTINEL, str)

    def test_unset_serialization(self):
        """Test that UNSET serializes to UNSET_SENTINEL"""
        serialized = UNSET.model_dump(mode="python")
        assert serialized == UNSET_SENTINEL

    def test_unset_in_conditional(self):
        """Test UNSET in conditional expressions"""
        value = UNSET

        if value:
            pytest.fail("UNSET should evaluate to False")
        else:
            pass  # Expected behavior

    def test_unset_comparison(self):
        """Test UNSET comparisons"""
        assert UNSET is UNSET
        assert UNSET == UNSET

        # UNSET should not equal other falsy values
        assert UNSET is not None
        assert UNSET is not False
        assert UNSET != None


@pytest.mark.unit
class TestBaseModel:
    """Test cases for BaseModel"""

    def test_base_model_config(self):
        """Test BaseModel configuration settings"""
        config = BaseModel.model_config

        assert config["populate_by_name"] is True
        assert config["arbitrary_types_allowed"] is True
        assert config["protected_namespaces"] == ()

    def test_base_model_creation(self):
        """Test creating a simple BaseModel subclass"""

        class TestModel(BaseModel):
            name: str
            value: int

        instance = TestModel(name="test", value=42)

        assert instance.name == "test"
        assert instance.value == 42

    def test_base_model_with_alias(self):
        """Test BaseModel with field aliases"""

        class TestModel(BaseModel):
            my_field: str = Field(alias="myField")

        # Should work with alias
        instance = TestModel(myField="test")
        assert instance.my_field == "test"

        # Should also work with field name due to populate_by_name
        instance2 = TestModel(my_field="test2")
        assert instance2.my_field == "test2"

    def test_base_model_serialization(self):
        """Test BaseModel serialization"""

        class TestModel(BaseModel):
            name: str
            count: int

        instance = TestModel(name="example", count=5)
        data = instance.model_dump()

        assert data == {"name": "example", "count": 5}

    def test_base_model_arbitrary_types(self):
        """Test that BaseModel allows arbitrary types"""

        class CustomType:
            def __init__(self, value):
                self.value = value

        class TestModel(BaseModel):
            custom: CustomType

        custom_obj = CustomType("test")
        instance = TestModel(custom=custom_obj)

        assert instance.custom is custom_obj
        assert instance.custom.value == "test"

    def test_base_model_protected_namespaces(self):
        """Test that BaseModel allows 'model_' prefix fields"""

        class TestModel(BaseModel):
            model_name: str  # This would normally conflict with pydantic

        instance = TestModel(model_name="test")
        assert instance.model_name == "test"


@pytest.mark.unit
class TestNullableTypes:
    """Test cases for Nullable and OptionalNullable type aliases"""

    def test_nullable_type_allows_none(self):
        """Test that Nullable type allows None"""

        class TestModel(BaseModel):
            value: Nullable[str]

        instance1 = TestModel(value="test")
        assert instance1.value == "test"

        instance2 = TestModel(value=None)
        assert instance2.value is None

    def test_nullable_type_requires_value(self):
        """Test that Nullable requires a value (str or None)"""

        class TestModel(BaseModel):
            value: Nullable[str]

        # Should require the field to be present
        with pytest.raises(Exception):  # Pydantic ValidationError
            TestModel()

    def test_optional_nullable_with_unset(self):
        """Test OptionalNullable with UNSET default"""

        class TestModel(BaseModel):
            value: OptionalNullable[str] = field(default_factory=lambda: UNSET)

        # Can omit the field
        instance1 = TestModel()
        assert instance1.value is UNSET

        # Can provide a value
        instance2 = TestModel(value="test")
        assert instance2.value == "test"

        # Can provide None
        instance3 = TestModel(value=None)
        assert instance3.value is None

    def test_optional_nullable_serialization(self):
        """Test OptionalNullable serialization"""

        class TestModel(BaseModel):
            value: OptionalNullable[str] = field(default_factory=lambda: UNSET)

        # UNSET should serialize to sentinel
        instance = TestModel()
        data = instance.model_dump(mode="python")
        assert data["value"] == UNSET_SENTINEL

    def test_nullable_with_different_types(self):
        """Test Nullable with various types"""

        class TestModel(BaseModel):
            str_field: Nullable[str]
            int_field: Nullable[int]
            list_field: Nullable[list]

        instance = TestModel(str_field=None, int_field=42, list_field=["a", "b"])

        assert instance.str_field is None
        assert instance.int_field == 42
        assert instance.list_field == ["a", "b"]


@pytest.mark.unit
class TestUnrecognizedTypes:
    """Test cases for UnrecognizedInt and UnrecognizedStr"""

    def test_unrecognized_int_is_int_alias(self):
        """Test that UnrecognizedInt is an alias for int"""
        value: UnrecognizedInt = 42
        assert isinstance(value, int)
        assert value == 42

    def test_unrecognized_str_is_str_alias(self):
        """Test that UnrecognizedStr is an alias for str"""
        value: UnrecognizedStr = "test"
        assert isinstance(value, str)
        assert value == "test"

    def test_unrecognized_types_in_models(self):
        """Test using Unrecognized types in models"""

        class TestModel(BaseModel):
            unknown_int: UnrecognizedInt
            unknown_str: UnrecognizedStr

        instance = TestModel(unknown_int=999, unknown_str="unknown_value")

        assert isinstance(instance.unknown_int, int)
        assert isinstance(instance.unknown_str, str)
        assert instance.unknown_int == 999
        assert instance.unknown_str == "unknown_value"


@pytest.mark.unit
class TestTypesModuleImports:
    """Test the types module exports"""

    def test_all_types_exported(self):
        """Test that all expected types are exported from the module"""
        from griddy_nfl import types

        expected_exports = [
            "BaseModel",
            "Nullable",
            "OptionalNullable",
            "UnrecognizedInt",
            "UnrecognizedStr",
            "UNSET",
            "UNSET_SENTINEL",
        ]

        for export in expected_exports:
            assert hasattr(types, export), f"Missing export: {export}"

    def test_types_module_all_list(self):
        """Test that __all__ contains expected types"""
        from griddy_nfl import types

        assert set(types.__all__) == {
            "BaseModel",
            "Nullable",
            "OptionalNullable",
            "UnrecognizedInt",
            "UnrecognizedStr",
            "UNSET",
            "UNSET_SENTINEL",
        }


@pytest.mark.unit
class TestComplexTypeScenarios:
    """Test complex scenarios combining multiple type features"""

    def test_model_with_mixed_optionality(self):
        """Test model with required, nullable, and optional fields"""

        class TestModel(BaseModel):
            required: str
            nullable: Nullable[str]
            optional: OptionalNullable[str] = field(default_factory=lambda: UNSET)

        # All combinations should work
        instance1 = TestModel(required="test", nullable="value", optional="opt")
        assert instance1.required == "test"
        assert instance1.nullable == "value"
        assert instance1.optional == "opt"

        instance2 = TestModel(required="test", nullable=None)
        assert instance2.nullable is None
        assert instance2.optional is UNSET

    def test_nested_models_with_optional_fields(self):
        """Test nested models with OptionalNullable fields"""

        class InnerModel(BaseModel):
            value: str

        class OuterModel(BaseModel):
            inner: OptionalNullable[InnerModel] = field(default_factory=lambda: UNSET)

        # Can omit inner
        instance1 = OuterModel()
        assert instance1.inner is UNSET

        # Can provide inner
        instance2 = OuterModel(inner=InnerModel(value="test"))
        assert instance2.inner.value == "test"

        # Can set to None
        instance3 = OuterModel(inner=None)
        assert instance3.inner is None

    def test_serialization_with_unset_fields(self):
        """Test serialization behavior with UNSET fields"""

        class TestModel(BaseModel):
            required: str
            optional1: OptionalNullable[str] = field(default_factory=lambda: UNSET)
            optional2: OptionalNullable[int] = field(default_factory=lambda: UNSET)

        instance = TestModel(required="test", optional1="value")

        data = instance.model_dump(mode="python")

        assert data["required"] == "test"
        assert data["optional1"] == "value"
        assert data["optional2"] == UNSET_SENTINEL
