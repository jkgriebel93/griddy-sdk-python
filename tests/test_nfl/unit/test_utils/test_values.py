"""Tests for griddy.nfl.utils.values."""

import os
from datetime import datetime, timezone
from enum import Enum
from unittest.mock import MagicMock

import pytest
from httpx import Response

from griddy.nfl.types.basemodel import Unset
from griddy.nfl.utils.values import (
    _is_set,
    _val_to_string,
    get_global_from_env,
    match_content_type,
    match_response,
    match_status_codes,
)


@pytest.mark.unit
class TestMatchContentType:
    def test_exact_match(self):
        assert match_content_type("application/json", "application/json") is True

    def test_wildcard_star(self):
        assert match_content_type("application/json", "*") is True

    def test_wildcard_star_slash_star(self):
        assert match_content_type("application/json", "*/*") is True

    def test_type_wildcard(self):
        assert match_content_type("text/plain", "text/*") is True

    def test_subtype_wildcard(self):
        assert match_content_type("application/json", "*/json") is True

    def test_no_match(self):
        assert match_content_type("application/json", "text/html") is False

    def test_parsed_media_type_match(self):
        assert (
            match_content_type("application/json; charset=utf-8", "application/json")
            is True
        )


@pytest.mark.unit
class TestMatchStatusCodes:
    def test_exact_match(self):
        assert match_status_codes(["200"], 200) is True

    def test_no_match(self):
        assert match_status_codes(["200"], 404) is False

    def test_wildcard_4xx(self):
        assert match_status_codes(["4XX"], 404) is True

    def test_wildcard_5xx(self):
        assert match_status_codes(["5XX"], 503) is True

    def test_wildcard_no_match(self):
        assert match_status_codes(["4XX"], 500) is False

    def test_default(self):
        assert match_status_codes(["default"], 999) is True

    def test_multiple_codes(self):
        assert match_status_codes(["200", "201"], 201) is True

    def test_empty_list(self):
        assert match_status_codes([], 200) is False


@pytest.mark.unit
class TestValToString:
    def test_bool_true(self):
        assert _val_to_string(True) == "true"

    def test_bool_false(self):
        assert _val_to_string(False) == "false"

    def test_datetime(self):
        dt = datetime(2024, 1, 15, 12, 0, 0, tzinfo=timezone.utc)
        result = _val_to_string(dt)
        assert result == "2024-01-15T12:00:00Z"

    def test_enum(self):
        class Color(Enum):
            RED = "red"

        assert _val_to_string(Color.RED) == "red"

    def test_int(self):
        assert _val_to_string(42) == "42"

    def test_string(self):
        assert _val_to_string("hello") == "hello"


@pytest.mark.unit
class TestIsSet:
    def test_none_is_not_set(self):
        assert _is_set(None) is False

    def test_unset_is_not_set(self):
        assert _is_set(Unset()) is False

    def test_value_is_set(self):
        assert _is_set("hello") is True

    def test_zero_is_set(self):
        assert _is_set(0) is True

    def test_empty_string_is_set(self):
        assert _is_set("") is True


@pytest.mark.unit
class TestGetGlobalFromEnv:
    def test_value_provided(self):
        result = get_global_from_env("existing", "SOME_KEY", str)
        assert result == "existing"

    def test_env_var_present(self, monkeypatch):
        monkeypatch.setenv("TEST_KEY", "42")
        result = get_global_from_env(None, "TEST_KEY", int)
        assert result == 42

    def test_env_var_bad_cast(self, monkeypatch):
        monkeypatch.setenv("TEST_KEY", "not_a_number")
        result = get_global_from_env(None, "TEST_KEY", int)
        assert result is None

    def test_nothing_set(self, monkeypatch):
        monkeypatch.delenv("NONEXISTENT_KEY", raising=False)
        result = get_global_from_env(None, "NONEXISTENT_KEY", str)
        assert result is None


@pytest.mark.unit
class TestMatchResponse:
    def _make_response(self, status_code, content_type="application/json"):
        resp = MagicMock(spec=Response)
        resp.status_code = status_code
        resp.headers = {"content-type": content_type}
        return resp

    def test_matching_code_and_content_type(self):
        resp = self._make_response(200)
        assert match_response(resp, "200", "application/json") is True

    def test_non_matching_code(self):
        resp = self._make_response(404)
        assert match_response(resp, "200", "application/json") is False

    def test_list_of_codes(self):
        resp = self._make_response(201)
        assert match_response(resp, ["200", "201"], "application/json") is True

    def test_wildcard_content_type(self):
        resp = self._make_response(200)
        assert match_response(resp, "200", "*") is True

    def test_no_content_type_header(self):
        resp = MagicMock(spec=Response)
        resp.status_code = 200
        resp.headers = {}
        result = match_response(resp, "200", "application/octet-stream")
        assert result is True
