"""Tests for griddy.nfl.__init__ explicit imports and __all__ (TGF-145)."""

import griddy.nfl as nfl_pkg


class TestNflInitExports:
    """Verify that griddy.nfl exposes the expected public API."""

    def test_all_is_defined(self):
        assert hasattr(nfl_pkg, "__all__")
        assert isinstance(nfl_pkg.__all__, list)

    def test_all_contains_expected_names(self):
        expected = {"GriddyNFL", "SDKConfiguration", "SERVERS", "VERSION", "USER_AGENT"}
        assert set(nfl_pkg.__all__) == expected

    def test_griddy_nfl_importable(self):
        from griddy.nfl import GriddyNFL

        assert GriddyNFL is not None

    def test_sdk_configuration_importable(self):
        from griddy.nfl import SDKConfiguration

        assert SDKConfiguration is not None

    def test_servers_importable(self):
        from griddy.nfl import SERVERS

        assert isinstance(SERVERS, dict)

    def test_version_is_string(self):
        assert isinstance(nfl_pkg.VERSION, str)

    def test_user_agent_is_string(self):
        assert isinstance(nfl_pkg.USER_AGENT, str)

    def test_all_names_are_accessible(self):
        for name in nfl_pkg.__all__:
            assert hasattr(nfl_pkg, name), (
                f"{name} listed in __all__ but not accessible"
            )
