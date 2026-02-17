"""Tests for griddy.nfl.utils.headers."""

from typing import Dict, List, Optional

import pytest
from httpx import Headers
from pydantic import Field
from typing_extensions import Annotated

from griddy_nfl.types.basemodel import BaseModel
from griddy_nfl.utils.headers import (
    _serialize_header,
    get_headers,
    get_response_headers,
)
from griddy_nfl.utils.metadata import FieldMetadata, HeaderMetadata


class SimpleHeaderParams(BaseModel):
    x_api_key: Annotated[
        Optional[str],
        Field(alias="x-api-key"),
        FieldMetadata(header=HeaderMetadata()),
    ] = None
    x_version: Annotated[
        Optional[str],
        Field(alias="x-version"),
        FieldMetadata(header=HeaderMetadata()),
    ] = None


class ExplodeHeaderParams(BaseModel):
    x_tags: Annotated[
        Optional[Dict[str, str]],
        Field(alias="x-tags"),
        FieldMetadata(header=HeaderMetadata(explode=True)),
    ] = None


@pytest.mark.unit
class TestGetHeaders:
    def test_simple_headers(self):
        params = SimpleHeaderParams(x_api_key="key123", x_version="v2")
        result = get_headers(params)
        assert result["x-api-key"] == "key123"
        assert result["x-version"] == "v2"

    def test_none_values_skipped(self):
        params = SimpleHeaderParams(x_api_key="key123")
        result = get_headers(params)
        assert "x-api-key" in result
        assert "x-version" not in result

    def test_non_model_returns_empty(self):
        result = get_headers("not a model")
        assert result == {}

    def test_none_params_returns_empty(self):
        result = get_headers(None)
        assert result == {}


@pytest.mark.unit
class TestSerializeHeader:
    def test_scalar_value(self):
        result = _serialize_header(False, "hello")
        assert result == "hello"

    def test_none_returns_empty(self):
        result = _serialize_header(False, None)
        assert result == ""

    def test_list_value(self):
        result = _serialize_header(False, ["a", "b", "c"])
        assert result == "a,b,c"

    def test_dict_non_explode(self):
        result = _serialize_header(False, {"key1": "val1", "key2": "val2"})
        assert "key1" in result
        assert "val1" in result

    def test_dict_explode(self):
        result = _serialize_header(True, {"key1": "val1", "key2": "val2"})
        assert "key1=val1" in result
        assert "key2=val2" in result

    def test_int_value(self):
        result = _serialize_header(False, 42)
        assert result == "42"

    def test_bool_value(self):
        result = _serialize_header(False, True)
        assert result == "true"


@pytest.mark.unit
class TestGetResponseHeaders:
    def test_basic_headers(self):
        headers = Headers(
            {"content-type": "application/json", "x-request-id": "abc123"}
        )
        result = get_response_headers(headers)
        assert "content-type" in result
        assert result["content-type"] == ["application/json"]
        assert result["x-request-id"] == ["abc123"]

    def test_empty_headers(self):
        headers = Headers({})
        result = get_response_headers(headers)
        assert result == {}
