"""Tests for griddy.pfr.__init__ explicit imports and __all__ (TGF-145)."""

import griddy.pfr as pfr_pkg


class TestPfrInitExports:
    """Verify that griddy.pfr exposes the expected public API."""

    def test_all_is_defined(self):
        assert hasattr(pfr_pkg, "__all__")
        assert isinstance(pfr_pkg.__all__, list)

    def test_all_contains_expected_names(self):
        expected = {
            "AsyncScrapingBackend",
            "GriddyPFR",
            "ScrapingBackend",
            "SDKConfiguration",
            "SERVERS",
            "VERSION",
            "USER_AGENT",
        }
        assert set(pfr_pkg.__all__) == expected

    def test_griddy_pfr_importable(self):
        from griddy.pfr import GriddyPFR

        assert GriddyPFR is not None

    def test_sdk_configuration_importable(self):
        from griddy.pfr import SDKConfiguration

        assert SDKConfiguration is not None

    def test_servers_importable(self):
        from griddy.pfr import SERVERS

        assert isinstance(SERVERS, dict)

    def test_version_is_string(self):
        assert isinstance(pfr_pkg.VERSION, str)

    def test_user_agent_is_string(self):
        assert isinstance(pfr_pkg.USER_AGENT, str)

    def test_all_names_are_accessible(self):
        for name in pfr_pkg.__all__:
            assert hasattr(pfr_pkg, name), (
                f"{name} listed in __all__ but not accessible"
            )
