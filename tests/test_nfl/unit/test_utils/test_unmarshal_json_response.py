"""Tests for griddy.nfl.utils.unmarshal_json_response."""

from typing import Optional
from unittest.mock import MagicMock

import httpx
import pytest

from griddy.nfl import errors
from griddy.nfl.types.basemodel import BaseModel
from griddy.nfl.utils.unmarshal_json_response import (
    int_to_str,
    unmarshal_json_response,
)


class SimpleModel(BaseModel):
    name: Optional[str] = None
    value: Optional[int] = None


@pytest.mark.unit
class TestIntToStr:
    def test_int_converted(self):
        assert int_to_str(42) == "42"

    def test_str_passthrough(self):
        assert int_to_str("hello") == "hello"

    def test_none_passthrough(self):
        assert int_to_str(None) is None


@pytest.mark.unit
class TestUnmarshalJsonResponse:
    def _make_response(self, text=""):
        resp = MagicMock(spec=httpx.Response)
        resp.text = text
        resp.status_code = 200
        resp.headers = {"content-type": "application/json"}
        return resp

    def test_successful_unmarshal(self):
        http_res = self._make_response()
        body = '{"name": "test", "value": 42}'
        result = unmarshal_json_response(SimpleModel, http_res, body)
        assert isinstance(result, SimpleModel)
        assert result.name == "test"
        assert result.value == 42

    def test_uses_response_text_when_body_none(self):
        http_res = self._make_response(text='{"name": "from_response"}')
        result = unmarshal_json_response(SimpleModel, http_res)
        assert result.name == "from_response"

    def test_validation_error_raises_response_validation_error(self):
        http_res = self._make_response()
        # Invalid JSON that will fail validation
        body = '{"name": 123, "value": "not_an_int"}'

        class StrictModel(BaseModel):
            name: str
            value: int

        # This should raise ResponseValidationError
        # but it depends on whether validation actually fails
        # Let's use a type that will definitely fail
        with pytest.raises(errors.ResponseValidationError):
            unmarshal_json_response(StrictModel, http_res, '{"name": [1,2,3]}')
