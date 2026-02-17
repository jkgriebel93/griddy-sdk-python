"""Tests for griddy.nfl._lazy_load and griddy.nfl._import."""

import sys
from unittest.mock import MagicMock, patch

import pytest

from griddy_nfl._import import dynamic_import
from griddy_nfl._lazy_load import LazySubSDKMixin


@pytest.mark.unit
class TestDynamicImport:
    def test_successful_import(self):
        mod = dynamic_import("json")
        assert hasattr(mod, "dumps")

    def test_retries_on_key_error(self):
        call_count = 0
        original_import = (
            __builtins__.__import__
            if hasattr(__builtins__, "__import__")
            else __import__
        )

        with patch("griddy_nfl._import.import_module") as mock_import:
            # First call raises KeyError, second succeeds
            import json

            mock_import.side_effect = [KeyError("bad"), json]
            result = dynamic_import("json", retries=3)
            assert result is json
            assert mock_import.call_count == 2

    def test_all_retries_exhausted(self):
        with patch("griddy_nfl._import.import_module") as mock_import:
            mock_import.side_effect = KeyError("bad")
            with pytest.raises(KeyError, match="Failed to import"):
                dynamic_import("nonexistent_module", retries=2)


@pytest.mark.unit
class TestLazySubSDKMixin:
    def test_getattr_unknown_attribute(self):
        class TestSDK(LazySubSDKMixin):
            _sub_sdk_map = {}
            sdk_configuration = None
            parent_ref = None

        sdk = TestSDK()
        with pytest.raises(AttributeError, match="has no attribute 'unknown'"):
            _ = sdk.unknown

    def test_dir_includes_sub_sdk_keys(self):
        class TestSDK(LazySubSDKMixin):
            _sub_sdk_map = {
                "games": ("griddy_nfl.endpoints.regular.games", "Games"),
                "teams": (
                    "griddy_nfl.endpoints.regular.football_teams",
                    "FootballTeams",
                ),
            }
            sdk_configuration = None
            parent_ref = None

        sdk = TestSDK()
        d = dir(sdk)
        assert "games" in d
        assert "teams" in d

    def test_getattr_import_error(self):
        class TestSDK(LazySubSDKMixin):
            _sub_sdk_map = {
                "bad": ("nonexistent.module.path", "BadClass"),
            }
            sdk_configuration = None
            parent_ref = None

        sdk = TestSDK()
        with pytest.raises(AttributeError, match="Failed to import"):
            _ = sdk.bad

    def test_getattr_class_not_found(self):
        class TestSDK(LazySubSDKMixin):
            _sub_sdk_map = {
                "bad": ("json", "NonExistentClass"),
            }
            sdk_configuration = None
            parent_ref = None

        sdk = TestSDK()
        with pytest.raises(AttributeError, match="Failed to find class"):
            _ = sdk.bad
