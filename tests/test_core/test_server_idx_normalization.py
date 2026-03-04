"""Tests for server_idx normalization in __post_init__ (TGF-93).

Verifies that NFL and PFR SDKConfiguration normalize server_idx=None to 0
at construction time, rather than mutating inside get_server_details().
"""

from unittest.mock import Mock

import httpx
import pytest

from griddy.core.utils.logger import Logger


@pytest.fixture
def mock_logger():
    return Mock(spec=Logger)


@pytest.mark.unit
class TestNFLServerIdxNormalization:
    """Verify NFL SDKConfiguration normalizes server_idx in __post_init__."""

    def test_none_server_idx_normalized_at_construction(self, mock_logger):
        from griddy.nfl.sdkconfiguration import SDKConfiguration

        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_idx=None,
        )
        assert config.server_idx == 0

    def test_get_server_details_does_not_mutate(self, mock_logger):
        from griddy.nfl.sdkconfiguration import SDKConfiguration

        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_idx=None,
        )
        idx_before = config.server_idx
        config.get_server_details()
        assert config.server_idx == idx_before

    def test_explicit_server_idx_preserved(self, mock_logger):
        from griddy.nfl.sdkconfiguration import SDKConfiguration

        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_idx=1,
        )
        assert config.server_idx == 1


@pytest.mark.unit
class TestPFRServerIdxNormalization:
    """Verify PFR SDKConfiguration normalizes server_idx in __post_init__."""

    def test_none_server_idx_normalized_at_construction(self, mock_logger):
        from griddy.pfr.sdkconfiguration import SDKConfiguration

        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_idx=None,
        )
        assert config.server_idx == 0

    def test_get_server_details_does_not_mutate(self, mock_logger):
        from griddy.pfr.sdkconfiguration import SDKConfiguration

        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_idx=None,
        )
        idx_before = config.server_idx
        config.get_server_details()
        assert config.server_idx == idx_before

    def test_explicit_server_idx_preserved(self, mock_logger):
        from griddy.pfr.sdkconfiguration import SDKConfiguration

        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_idx=1,
        )
        assert config.server_idx == 1
