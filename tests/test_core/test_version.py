"""Tests for unified version sourcing via importlib.metadata (TGF-129)."""

import importlib.metadata


class TestUnifiedVersion:
    """All version references should resolve to the same value from pyproject.toml."""

    def test_importlib_metadata_version(self):
        version = importlib.metadata.version("griddy")
        assert version
        assert isinstance(version, str)

    def test_griddy_version_module(self):
        from griddy._version import __version__

        assert __version__ == importlib.metadata.version("griddy")

    def test_griddy_init_version(self):
        from griddy import __version__

        assert __version__ == importlib.metadata.version("griddy")

    def test_nfl_version_matches(self):
        from griddy.nfl._version import __version__

        assert __version__ == importlib.metadata.version("griddy")

    def test_pfr_version_matches(self):
        from griddy.pfr._version import __version__

        assert __version__ == importlib.metadata.version("griddy")

    def test_nfl_public_version_matches(self):
        from griddy.nfl import VERSION

        assert VERSION == importlib.metadata.version("griddy")

    def test_pfr_public_version_matches(self):
        from griddy.pfr import VERSION

        assert VERSION == importlib.metadata.version("griddy")

    def test_nfl_sdkconfiguration_version(self):
        from griddy.nfl.sdkconfiguration import SDKConfiguration

        assert SDKConfiguration.sdk_version == importlib.metadata.version("griddy")

    def test_pfr_sdkconfiguration_version(self):
        from griddy.pfr.sdkconfiguration import SDKConfiguration

        assert SDKConfiguration.sdk_version == importlib.metadata.version("griddy")
