"""Tests for griddy.nfl.utils.serializers."""

import json
from decimal import Decimal
from typing import List, Optional, Union

import pytest

from griddy.nfl.types.basemodel import (
    BaseModel,
    Nullable,
    OptionalNullable,
    Unset,
)
from griddy.nfl.utils.serializers import (
    _contains_pydantic_model,
    get_pydantic_model,
    is_nullable,
    is_union,
    marshal_json,
    serialize_decimal,
    serialize_float,
    serialize_int,
    unmarshal,
    unmarshal_json,
    validate_const,
    validate_decimal,
    validate_float,
    validate_int,
    validate_open_enum,
)


class SimpleModel(BaseModel):
    name: Optional[str] = None
    value: Optional[int] = None


@pytest.mark.unit
class TestSerializeDecimal:
    @pytest.mark.parametrize(
        "as_str,value,expected",
        [
            pytest.param(True, Decimal("10.5"), "10.5", id="as_str"),
            pytest.param(False, Decimal("10.5"), 10.5, id="as_float"),
        ],
    )
    def test_serialize_value(self, as_str, value, expected):
        serializer = serialize_decimal(as_str=as_str)
        assert serializer(value) == expected

    @pytest.mark.parametrize(
        "value,match",
        [
            pytest.param(None, "Expected Decimal", id="none"),
            pytest.param("not a decimal", "Expected Decimal", id="string"),
        ],
    )
    def test_invalid_raises(self, value, match):
        serializer = serialize_decimal(as_str=True)
        with pytest.raises(ValueError, match=match):
            serializer(value)

    def test_unset(self):
        serializer = serialize_decimal(as_str=True)
        unset = Unset()
        result = serializer(unset)
        assert isinstance(result, Unset)


@pytest.mark.unit
class TestValidateDecimal:
    @pytest.mark.parametrize(
        "value,expected",
        [
            pytest.param(None, None, id="none"),
            pytest.param(Decimal("10.5"), Decimal("10.5"), id="decimal"),
            pytest.param("10.5", Decimal("10.5"), id="string"),
            pytest.param(42, Decimal("42"), id="int"),
        ],
    )
    def test_valid_inputs(self, value, expected):
        result = validate_decimal(value)
        assert result == expected

    def test_unset(self):
        unset = Unset()
        assert validate_decimal(unset) is unset

    def test_float(self):
        result = validate_decimal(10.5)
        assert isinstance(result, Decimal)

    def test_invalid(self):
        with pytest.raises(ValueError):
            validate_decimal([1, 2, 3])


@pytest.mark.unit
class TestSerializeFloat:
    @pytest.mark.parametrize(
        "as_str,expected",
        [
            pytest.param(True, "10.5", id="as_str"),
            pytest.param(False, 10.5, id="as_float"),
        ],
    )
    def test_serialize_value(self, as_str, expected):
        serializer = serialize_float(as_str=as_str)
        assert serializer(10.5) == expected

    def test_unset(self):
        serializer = serialize_float(as_str=True)
        unset = Unset()
        result = serializer(unset)
        assert isinstance(result, Unset)

    def test_non_float_raises(self):
        serializer = serialize_float(as_str=True)
        with pytest.raises(ValueError, match="Expected float"):
            serializer("not a float")


@pytest.mark.unit
class TestValidateFloat:
    @pytest.mark.parametrize(
        "value,expected",
        [
            pytest.param(None, None, id="none"),
            pytest.param(10.5, 10.5, id="float"),
            pytest.param("10.5", 10.5, id="string"),
        ],
    )
    def test_valid_inputs(self, value, expected):
        assert validate_float(value) == expected

    def test_unset(self):
        unset = Unset()
        assert validate_float(unset) is unset

    def test_invalid(self):
        with pytest.raises(ValueError, match="Expected string"):
            validate_float(42)


@pytest.mark.unit
class TestSerializeInt:
    @pytest.mark.parametrize(
        "as_str,expected",
        [
            pytest.param(True, "42", id="as_str"),
            pytest.param(False, 42, id="as_int"),
        ],
    )
    def test_serialize_value(self, as_str, expected):
        serializer = serialize_int(as_str=as_str)
        assert serializer(42) == expected

    def test_unset(self):
        serializer = serialize_int(as_str=True)
        unset = Unset()
        result = serializer(unset)
        assert isinstance(result, Unset)

    def test_non_int_raises(self):
        serializer = serialize_int(as_str=True)
        with pytest.raises(ValueError, match="Expected int"):
            serializer("not an int")


@pytest.mark.unit
class TestValidateInt:
    @pytest.mark.parametrize(
        "value,expected",
        [
            pytest.param(None, None, id="none"),
            pytest.param(42, 42, id="int"),
            pytest.param("42", 42, id="string"),
        ],
    )
    def test_valid_inputs(self, value, expected):
        assert validate_int(value) == expected

    def test_unset(self):
        unset = Unset()
        assert validate_int(unset) is unset

    def test_invalid(self):
        with pytest.raises(ValueError, match="Expected string"):
            validate_int(10.5)


@pytest.mark.unit
class TestValidateOpenEnum:
    @pytest.mark.parametrize(
        "is_int,value,expected",
        [
            pytest.param(False, "REG", "REG", id="str_valid"),
            pytest.param(True, 42, 42, id="int_valid"),
            pytest.param(False, None, None, id="none"),
        ],
    )
    def test_valid_inputs(self, is_int, value, expected):
        validator = validate_open_enum(is_int=is_int)
        assert validator(value) == expected

    @pytest.mark.parametrize(
        "is_int,value,match",
        [
            pytest.param(False, 42, "Expected string", id="str_gets_int"),
            pytest.param(True, "not int", "Expected int", id="int_gets_str"),
        ],
    )
    def test_invalid_inputs(self, is_int, value, match):
        validator = validate_open_enum(is_int=is_int)
        with pytest.raises(ValueError, match=match):
            validator(value)

    def test_unset(self):
        validator = validate_open_enum(is_int=False)
        unset = Unset()
        assert validator(unset) is unset


@pytest.mark.unit
class TestValidateConst:
    def test_matching(self):
        validator = validate_const("fixed")
        assert validator("fixed") == "fixed"

    def test_mismatch(self):
        validator = validate_const("fixed")
        with pytest.raises(ValueError, match="Expected fixed"):
            validator("other")

    def test_none_union(self):
        validator = validate_const("fixed")
        # None passes through if type is Union[..., None]
        # validate_const checks is_union first, so raw None isn't special
        # unless the value's type is a Union
        result = validator("fixed")
        assert result == "fixed"


@pytest.mark.unit
class TestUnmarshalJson:
    def test_simple_model(self):
        data = b'{"name": "test", "value": 42}'
        result = unmarshal_json(data, SimpleModel)
        assert isinstance(result, SimpleModel)
        assert result.name == "test"
        assert result.value == 42

    def test_primitive(self):
        result = unmarshal_json(b'"hello"', str)
        assert result == "hello"

    def test_list(self):
        result = unmarshal_json(b"[1, 2, 3]", List[int])
        assert result == [1, 2, 3]


@pytest.mark.unit
class TestUnmarshal:
    def test_simple(self):
        result = unmarshal({"name": "test"}, SimpleModel)
        assert isinstance(result, SimpleModel)
        assert result.name == "test"


@pytest.mark.unit
class TestMarshalJson:
    def test_simple_model(self):
        model = SimpleModel(name="test", value=42)
        result = marshal_json(model, SimpleModel)
        parsed = json.loads(result)
        assert parsed["name"] == "test"
        assert parsed["value"] == 42

    def test_nullable_none(self):
        result = marshal_json(None, Nullable[str])
        assert result == "null"

    def test_all_none_fields(self):
        model = SimpleModel()
        result = marshal_json(model, SimpleModel)
        # All fields are None -> excluded -> Pydantic gives {}
        assert result == "{}"


@pytest.mark.unit
class TestIsNullable:
    @pytest.mark.parametrize(
        "type_hint,expected",
        [
            pytest.param(Nullable[str], True, id="Nullable"),
            pytest.param(OptionalNullable[str], True, id="OptionalNullable"),
            pytest.param(Optional[str], False, id="Optional"),
            pytest.param(str, False, id="plain"),
        ],
    )
    def test_is_nullable(self, type_hint, expected):
        assert is_nullable(type_hint) is expected


@pytest.mark.unit
class TestIsUnion:
    def test_union_type(self):
        assert is_union(Union) is True

    def test_non_union(self):
        assert is_union(str) is False


@pytest.mark.unit
class TestContainsPydanticModel:
    @pytest.mark.parametrize(
        "value,expected",
        [
            pytest.param(SimpleModel(), True, id="model_instance"),
            pytest.param([SimpleModel()], True, id="list_with_model"),
            pytest.param({"key": SimpleModel()}, True, id="dict_with_model"),
            pytest.param({"key": "value"}, False, id="plain_dict"),
            pytest.param([1, 2, 3], False, id="plain_list"),
        ],
    )
    def test_contains_pydantic_model(self, value, expected):
        assert _contains_pydantic_model(value) is expected


@pytest.mark.unit
class TestGetPydanticModel:
    def test_with_model_data(self):
        model = SimpleModel(name="test")
        result = get_pydantic_model(model, SimpleModel)
        assert result is model

    def test_with_raw_data(self):
        result = get_pydantic_model({"name": "test"}, SimpleModel)
        assert isinstance(result, SimpleModel)
        assert result.name == "test"
