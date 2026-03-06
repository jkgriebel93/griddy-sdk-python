"""Tests for griddy.core.utils.datetimes."""

from datetime import timezone

import pytest

from griddy.core.utils.datetimes import parse_date


@pytest.mark.unit
class TestParseDate:
    def test_iso_format(self):
        result = parse_date("2024-01-15T12:00:00")
        assert result is not None
        assert result.year == 2024
        assert result.month == 1
        assert result.tzinfo == timezone.utc

    def test_iso_format_with_z(self):
        result = parse_date("2024-01-15T12:00:00Z")
        assert result is not None
        assert result.year == 2024

    def test_iso_with_microseconds(self):
        result = parse_date("2024-01-15T12:00:00.123456")
        assert result is not None

    def test_iso_with_microseconds_z(self):
        result = parse_date("2024-01-15T12:00:00.123456Z")
        assert result is not None

    def test_date_time_space(self):
        result = parse_date("2024-01-15 12:00:00")
        assert result is not None

    def test_date_only(self):
        result = parse_date("2024-01-15")
        assert result is not None
        assert result.day == 15

    def test_us_date_format(self):
        result = parse_date("01/15/2024")
        assert result is not None
        assert result.month == 1

    def test_us_date_time_format(self):
        result = parse_date("01/15/2024 12:00:00")
        assert result is not None

    def test_invalid_string(self):
        result = parse_date("not-a-date")
        assert result is None

    def test_none(self):
        result = parse_date(None)
        assert result is None

    def test_empty(self):
        result = parse_date("")
        assert result is None
