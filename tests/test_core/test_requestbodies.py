"""Tests for griddy.core.utils.requestbodies."""

import io

import pytest

from griddy.core.utils.requestbodies import (
    SERIALIZATION_METHOD_TO_CONTENT_TYPE,
    SerializedRequestBody,
    serialize_request_body,
)


@pytest.mark.unit
class TestSerializationMethodToContentType:
    def test_json(self):
        assert SERIALIZATION_METHOD_TO_CONTENT_TYPE["json"] == "application/json"

    def test_form(self):
        assert (
            SERIALIZATION_METHOD_TO_CONTENT_TYPE["form"]
            == "application/x-www-form-urlencoded"
        )

    def test_multipart(self):
        assert (
            SERIALIZATION_METHOD_TO_CONTENT_TYPE["multipart"] == "multipart/form-data"
        )

    def test_raw(self):
        assert SERIALIZATION_METHOD_TO_CONTENT_TYPE["raw"] == "application/octet-stream"

    def test_string(self):
        assert SERIALIZATION_METHOD_TO_CONTENT_TYPE["string"] == "text/plain"


@pytest.mark.unit
class TestSerializeRequestBody:
    def test_none_optional_returns_none(self):
        result = serialize_request_body(None, False, True, "json", str)
        assert result is None

    def test_json_serialization(self):
        result = serialize_request_body({"key": "value"}, False, False, "json", dict)
        assert result is not None
        assert result.media_type == "application/json"
        assert result.content is not None

    def test_string_body(self):
        result = serialize_request_body("hello", False, False, "string", str)
        assert result is not None
        assert result.media_type == "text/plain"
        assert result.content == "hello"

    def test_bytes_body(self):
        data = b"binary data"
        result = serialize_request_body(data, False, False, "raw", bytes)
        assert result is not None
        assert result.media_type == "application/octet-stream"
        assert result.content == data

    def test_bytesio_body(self):
        data = io.BytesIO(b"binary data")
        result = serialize_request_body(data, False, False, "raw", io.BytesIO)
        assert result is not None
        assert result.content is data

    def test_invalid_type_for_raw_raises(self):
        with pytest.raises(TypeError, match="invalid request body type"):
            serialize_request_body(12345, False, False, "raw", int)


@pytest.mark.unit
class TestSerializedRequestBody:
    def test_defaults(self):
        body = SerializedRequestBody()
        assert body.media_type is None
        assert body.content is None
        assert body.data is None
        assert body.files is None

    def test_with_media_type(self):
        body = SerializedRequestBody(media_type="application/json")
        assert body.media_type == "application/json"
