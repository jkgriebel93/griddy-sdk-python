"""Tests for the shared format_error_message utility."""

from unittest.mock import Mock

import httpx
import pytest

from griddy.core.errors._formatting import MAX_MESSAGE_LEN, format_error_message


def _make_response(status_code=400, content_type="application/json", text="error body"):
    response = Mock(spec=httpx.Response)
    response.status_code = status_code
    response.headers = httpx.Headers({"content-type": content_type})
    response.text = text
    return response


@pytest.mark.unit
class TestFormatErrorMessage:
    def test_includes_status_code(self):
        response = _make_response(status_code=500)
        msg = format_error_message("API error", response)
        assert "Status 500" in msg

    def test_message_prefix_with_colon(self):
        response = _make_response()
        msg = format_error_message("API error", response)
        assert msg.startswith("API error: Status 400")

    def test_empty_message_starts_with_status(self):
        response = _make_response()
        msg = format_error_message("", response)
        assert msg.startswith("Status 400")

    def test_includes_body_from_response_text(self):
        response = _make_response(text="Server Error")
        msg = format_error_message("error", response)
        assert "Body: Server Error" in msg

    def test_explicit_body_overrides_response_text(self):
        response = _make_response(text="response text")
        msg = format_error_message("error", response, body="custom body")
        assert "custom body" in msg
        assert "response text" not in msg

    def test_empty_body_shows_empty_quotes(self):
        response = _make_response(text="")
        msg = format_error_message("error", response)
        assert '""' in msg

    def test_none_body_and_empty_text_shows_empty_quotes(self):
        response = _make_response(text="")
        msg = format_error_message("error", response, body=None)
        assert '""' in msg

    def test_json_content_type_excluded(self):
        response = _make_response(content_type="application/json")
        msg = format_error_message("error", response)
        assert "Content-Type" not in msg

    def test_non_json_content_type_included(self):
        response = _make_response(content_type="text/html")
        msg = format_error_message("error", response)
        assert "Content-Type text/html" in msg

    def test_content_type_with_spaces_quoted(self):
        response = _make_response(content_type="text/html; charset=utf-8")
        msg = format_error_message("error", response)
        assert 'Content-Type "text/html; charset=utf-8"' in msg

    def test_missing_content_type_shows_empty_quotes(self):
        response = Mock(spec=httpx.Response)
        response.status_code = 400
        response.headers = httpx.Headers({})
        response.text = "body"
        msg = format_error_message("error", response)
        assert 'Content-Type ""' in msg

    def test_long_body_truncated(self):
        long_body = "x" * 15000
        response = _make_response(text=long_body)
        msg = format_error_message("error", response)
        assert "...and 5000 more chars" in msg
        assert len(msg) < 15000

    def test_body_at_max_length_not_truncated(self):
        exact_body = "x" * MAX_MESSAGE_LEN
        response = _make_response(text=exact_body)
        msg = format_error_message("error", response)
        assert "more chars" not in msg

    def test_body_just_over_max_truncated(self):
        over_body = "x" * (MAX_MESSAGE_LEN + 1)
        response = _make_response(text=over_body)
        msg = format_error_message("error", response)
        assert "...and 1 more chars" in msg

    def test_result_is_stripped(self):
        response = _make_response()
        msg = format_error_message("  ", response)
        assert not msg.startswith(" ")
        assert not msg.endswith(" ")
