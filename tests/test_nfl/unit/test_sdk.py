import importlib
import json
from unittest.mock import MagicMock, mock_open, patch

import pytest

from griddy.nfl import GriddyNFL
from griddy.nfl.endpoints.ngs import NextGenStats
from griddy.nfl.endpoints.pro.stats import StatsSDK
from griddy.nfl.endpoints.regular.football.stats import FootballStatsSDK


@pytest.mark.unit
class TestGriddyNFLInit:
    def test_init_with_valid_nfl_auth(self, nfl_auth_info_valid):
        nfl = GriddyNFL(nfl_auth=nfl_auth_info_valid)
        assert nfl is not None
        assert nfl.sdk_configuration is not None

    def test_init_raises_without_nfl_auth(self):
        with pytest.raises(TypeError):
            GriddyNFL()


@pytest.mark.unit
class TestAuthenticateViaBrowser:
    @patch("griddy.nfl.sdk.json.dump")
    @patch("builtins.open", new_callable=mock_open)
    @patch("griddy.nfl.utils.security.do_browser_auth")
    def test_returns_griddy_nfl_instance(self, mock_auth, mock_file, mock_json_dump):
        mock_auth.return_value = {
            "accessToken": "test_token",
            "refreshToken": "test_refresh",
            "expiresIn": 9999999999,
        }
        nfl = GriddyNFL.authenticate_via_browser(
            login_email="test@example.com",
            login_password="password",
            headless=True,
            save_credentials_path="creds.json",
        )
        assert isinstance(nfl, GriddyNFL)

    @patch("griddy.nfl.utils.security.do_browser_auth")
    def test_credentials_saved_when_path_provided(self, mock_auth, tmp_path):
        mock_auth.return_value = {
            "accessToken": "test_token",
            "refreshToken": "test_refresh",
            "expiresIn": 9999999999,
        }
        creds_path = str(tmp_path / "creds.json")
        GriddyNFL.authenticate_via_browser(
            login_email="test@example.com",
            login_password="password",
            save_credentials_path=creds_path,
        )
        with open(creds_path, "r") as f:
            saved = json.load(f)
        assert saved["accessToken"] == "test_token"

    @patch("griddy.nfl.utils.security.do_browser_auth")
    def test_no_file_written_when_path_is_none(self, mock_auth, tmp_path):
        mock_auth.return_value = {
            "accessToken": "test_token",
            "refreshToken": "test_refresh",
            "expiresIn": 9999999999,
        }
        nfl = GriddyNFL.authenticate_via_browser(
            login_email="test@example.com",
            login_password="password",
        )
        assert isinstance(nfl, GriddyNFL)
        # No files should have been created
        assert list(tmp_path.iterdir()) == []

    @patch("griddy.nfl.utils.security.do_browser_auth")
    def test_debug_logger_passed_to_browser_auth(self, mock_auth):
        mock_auth.return_value = {
            "accessToken": "test_token",
            "refreshToken": "test_refresh",
            "expiresIn": 9999999999,
        }
        logger = MagicMock()
        GriddyNFL.authenticate_via_browser(
            login_email="test@example.com",
            login_password="password",
            debug_logger=logger,
        )
        mock_auth.assert_called_once_with(
            email="test@example.com",
            password="password",
            headless=False,
            logger=logger,
        )


def _collect_sub_sdk_map_entries():
    """Collect all _sub_sdk_map entries across NFL SDK classes for parametrize."""
    entries = []
    classes = [GriddyNFL, NextGenStats, StatsSDK, FootballStatsSDK]
    for cls in classes:
        for attr_name, (module_path, class_name) in cls._sub_sdk_map.items():
            entries.append(
                pytest.param(
                    module_path,
                    class_name,
                    id=f"{cls.__name__}.{attr_name}",
                )
            )
    return entries


@pytest.mark.unit
class TestSubSdkMapImportable:
    """Validate every _sub_sdk_map entry across all NFL SDK classes is importable."""

    @pytest.mark.parametrize("module_path,class_name", _collect_sub_sdk_map_entries())
    def test_module_importable_and_class_exists(self, module_path, class_name):
        """Each _sub_sdk_map entry must point to a real module and class."""
        module = importlib.import_module(module_path)
        klass = getattr(module, class_name)
        assert callable(klass), f"{module_path}.{class_name} should be callable"
