"""Tests for griddy.core.utils.converters."""

import pytest

from griddy.core.utils.converters import clean_text, safe_float, safe_int


@pytest.mark.unit
class TestCleanText:
    def test_normal_text(self):
        assert clean_text("  hello  ") == "hello"

    def test_whitespace_only(self):
        assert clean_text("   ") is None

    def test_none(self):
        assert clean_text(None) is None

    def test_empty(self):
        assert clean_text("") is None

    def test_text_with_tabs(self):
        assert clean_text("\thello\n") == "hello"


@pytest.mark.unit
class TestSafeInt:
    def test_valid_int(self):
        assert safe_int(42) == 42

    def test_valid_string(self):
        assert safe_int("42") == 42

    def test_invalid_string(self):
        assert safe_int("not_a_number") is None

    def test_none(self):
        assert safe_int(None) is None

    def test_float(self):
        assert safe_int(3.14) == 3


@pytest.mark.unit
class TestSafeFloat:
    def test_valid_float(self):
        assert safe_float(3.14) == 3.14

    def test_valid_string(self):
        assert safe_float("3.14") == 3.14

    def test_invalid_string(self):
        assert safe_float("not_a_number") is None

    def test_none(self):
        assert safe_float(None) is None
