"""Tests for BaseSDK TypeVar generic (TGF-92).

Verifies that BaseSDK is generic over T_Config, and that NFL/PFR
subclasses correctly bind their provider-specific SDKConfiguration.
"""

from dataclasses import dataclass
from typing import Dict, Optional, Tuple, get_type_hints
from unittest.mock import Mock

import httpx
import pytest

from griddy.core.basesdk import BaseSDK, T_Config
from griddy.core.sdkconfiguration import SDKConfiguration as CoreSDKConfiguration
from griddy.core.utils.logger import Logger


@pytest.fixture
def mock_logger():
    return Mock(spec=Logger)


@pytest.fixture
def core_sdk_config(mock_logger):
    return CoreSDKConfiguration(
        client=httpx.Client(),
        client_supplied=False,
        async_client=httpx.AsyncClient(),
        async_client_supplied=False,
        debug_logger=mock_logger,
        server_url="https://example.com",
    )


class TestBaseSDKGeneric:
    """Verify BaseSDK is generic and T_Config is bound to CoreSDKConfiguration."""

    def test_basesdk_instantiates_with_core_config(self, core_sdk_config):
        sdk = BaseSDK(sdk_config=core_sdk_config)
        assert sdk.sdk_configuration is core_sdk_config

    def test_basesdk_sdk_configuration_attribute_set(self, core_sdk_config):
        sdk = BaseSDK(sdk_config=core_sdk_config)
        assert sdk.sdk_configuration.server_url == "https://example.com"

    def test_typevar_bound_is_core_sdk_configuration(self):
        assert T_Config.__bound__ is CoreSDKConfiguration


class TestNFLBaseSDKBinding:
    """Verify NFL BaseSDK binds T_Config to NFL SDKConfiguration."""

    def test_nfl_basesdk_inherits_from_generic_basesdk(self):
        from griddy.nfl.basesdk import BaseSDK as NFLBaseSDK
        from griddy.nfl.sdkconfiguration import SDKConfiguration as NFLSDKConfiguration

        # Check NFL BaseSDK is a subclass of core BaseSDK
        assert issubclass(NFLBaseSDK, BaseSDK)

        # Verify the generic parameter is set via __orig_bases__
        orig_bases = NFLBaseSDK.__orig_bases__
        # Should have CoreBaseSDK[SDKConfiguration] in bases
        assert any(
            hasattr(base, "__origin__") and base.__origin__ is BaseSDK
            for base in orig_bases
        )

    def test_nfl_basesdk_instantiation(self, mock_logger):
        from griddy.nfl.basesdk import BaseSDK as NFLBaseSDK
        from griddy.nfl.sdkconfiguration import SDKConfiguration as NFLSDKConfiguration

        config = NFLSDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=httpx.AsyncClient(),
            async_client_supplied=False,
            debug_logger=mock_logger,
            server_url="https://api.nfl.com",
        )
        sdk = NFLBaseSDK(sdk_config=config)
        assert sdk.sdk_configuration is config
        assert sdk.sdk_configuration.server_type == "regular"


class TestPFRBaseSDKBinding:
    """Verify PFR BaseSDK binds T_Config to PFR SDKConfiguration."""

    def test_pfr_basesdk_inherits_from_generic_basesdk(self):
        from griddy.pfr.basesdk import BaseSDK as PFRBaseSDK

        assert issubclass(PFRBaseSDK, BaseSDK)

        orig_bases = PFRBaseSDK.__orig_bases__
        assert any(
            hasattr(base, "__origin__") and base.__origin__ is BaseSDK
            for base in orig_bases
        )

    def test_pfr_basesdk_instantiation(self, mock_logger):
        from griddy.pfr.basesdk import BaseSDK as PFRBaseSDK
        from griddy.pfr.sdkconfiguration import SDKConfiguration as PFRSDKConfiguration

        config = PFRSDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=httpx.AsyncClient(),
            async_client_supplied=False,
            debug_logger=mock_logger,
            server_url="https://www.pro-football-reference.com",
        )
        sdk = PFRBaseSDK(sdk_config=config)
        assert sdk.sdk_configuration is config
        assert sdk.sdk_configuration.server_type == "default"


class TestCustomSubclass:
    """Verify that custom subclasses can bind their own config types."""

    def test_custom_subclass_with_extended_config(self, mock_logger):
        @dataclass
        class CustomConfig(CoreSDKConfiguration):
            custom_field: str = "test_value"

            def get_server_details(self) -> Tuple[str, Dict[str, str]]:
                return "https://custom.example.com", {}

        class CustomSDK(BaseSDK[CustomConfig]):
            pass

        config = CustomConfig(
            client=httpx.Client(),
            client_supplied=False,
            async_client=httpx.AsyncClient(),
            async_client_supplied=False,
            debug_logger=mock_logger,
        )
        sdk = CustomSDK(sdk_config=config)
        assert sdk.sdk_configuration.custom_field == "test_value"
