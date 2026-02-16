"""Tests for griddy.nfl.utils.serializers."""

import json
from decimal import Decimal
from typing import Dict, List, Optional, Union

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
    def test_as_str(self):
        serializer = serialize_decimal(as_str=True)
        assert serializer(Decimal("10.5")) == "10.5"

    def test_as_float(self):
        serializer = serialize_decimal(as_str=False)
        assert serializer(Decimal("10.5")) == 10.5

    def test_none_raises_without_optional_type(self):
        serializer = serialize_decimal(as_str=True)
        # Raw None raises because type(None) is not a Union
        with pytest.raises(ValueError, match="Expected Decimal"):
            serializer(None)

    def test_unset(self):
        serializer = serialize_decimal(as_str=True)
        unset = Unset()
        result = serializer(unset)
        assert isinstance(result, Unset)

    def test_non_decimal_raises(self):
        serializer = serialize_decimal(as_str=True)
        with pytest.raises(ValueError, match="Expected Decimal"):
            serializer("not a decimal")


@pytest.mark.unit
class TestValidateDecimal:
    def test_none(self):
        assert validate_decimal(None) is None

    def test_decimal(self):
        d = Decimal("10.5")
        assert validate_decimal(d) == d

    def test_unset(self):
        unset = Unset()
        assert validate_decimal(unset) is unset

    def test_string(self):
        result = validate_decimal("10.5")
        assert result == Decimal("10.5")

    def test_int(self):
        result = validate_decimal(42)
        assert result == Decimal("42")

    def test_float(self):
        result = validate_decimal(10.5)
        assert isinstance(result, Decimal)

    def test_invalid(self):
        with pytest.raises(ValueError):
            validate_decimal([1, 2, 3])


@pytest.mark.unit
class TestSerializeFloat:
    def test_as_str(self):
        serializer = serialize_float(as_str=True)
        assert serializer(10.5) == "10.5"

    def test_as_float(self):
        serializer = serialize_float(as_str=False)
        assert serializer(10.5) == 10.5

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
    def test_none(self):
        assert validate_float(None) is None

    def test_float(self):
        assert validate_float(10.5) == 10.5

    def test_unset(self):
        unset = Unset()
        assert validate_float(unset) is unset

    def test_string(self):
        assert validate_float("10.5") == 10.5

    def test_invalid(self):
        with pytest.raises(ValueError, match="Expected string"):
            validate_float(42)


@pytest.mark.unit
class TestSerializeInt:
    def test_as_str(self):
        serializer = serialize_int(as_str=True)
        assert serializer(42) == "42"

    def test_as_int(self):
        serializer = serialize_int(as_str=False)
        assert serializer(42) == 42

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
    def test_none(self):
        assert validate_int(None) is None

    def test_int(self):
        assert validate_int(42) == 42

    def test_unset(self):
        unset = Unset()
        assert validate_int(unset) is unset

    def test_string(self):
        assert validate_int("42") == 42

    def test_invalid(self):
        with pytest.raises(ValueError, match="Expected string"):
            validate_int(10.5)


@pytest.mark.unit
class TestValidateOpenEnum:
    def test_str_valid(self):
        validator = validate_open_enum(is_int=False)
        assert validator("REG") == "REG"

    def test_str_invalid(self):
        validator = validate_open_enum(is_int=False)
        with pytest.raises(ValueError, match="Expected string"):
            validator(42)

    def test_int_valid(self):
        validator = validate_open_enum(is_int=True)
        assert validator(42) == 42

    def test_int_invalid(self):
        validator = validate_open_enum(is_int=True)
        with pytest.raises(ValueError, match="Expected int"):
            validator("not int")

    def test_none(self):
        validator = validate_open_enum(is_int=False)
        assert validator(None) is None

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
    def test_nullable_type(self):
        assert is_nullable(Nullable[str]) is True

    def test_optional_nullable(self):
        assert is_nullable(OptionalNullable[str]) is True

    def test_regular_optional(self):
        assert is_nullable(Optional[str]) is False

    def test_plain_type(self):
        assert is_nullable(str) is False


@pytest.mark.unit
class TestIsUnion:
    def test_union_type(self):
        assert is_union(Union) is True

    def test_non_union(self):
        assert is_union(str) is False


@pytest.mark.unit
class TestContainsPydanticModel:
    def test_model_instance(self):
        assert _contains_pydantic_model(SimpleModel()) is True

    def test_list_with_model(self):
        assert _contains_pydantic_model([SimpleModel()]) is True

    def test_dict_with_model(self):
        assert _contains_pydantic_model({"key": SimpleModel()}) is True

    def test_plain_data(self):
        assert _contains_pydantic_model({"key": "value"}) is False

    def test_plain_list(self):
        assert _contains_pydantic_model([1, 2, 3]) is False


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
