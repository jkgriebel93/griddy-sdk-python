"""Tests for griddy.pfr.basesdk module."""

from unittest.mock import Mock

import httpx
import pytest

from griddy.core.basesdk import BaseSDK as CoreBaseSDK
from griddy.core.utils.logger import Logger
from griddy.pfr.basesdk import BaseSDK
from griddy.pfr.errors.griddypfrdefaulterror import GriddyPFRDefaultError
from griddy.pfr.errors.no_response_error import NoResponseError
from griddy.pfr.models.entities.security import Security
from griddy.pfr.sdkconfiguration import SDKConfiguration


@pytest.fixture
def mock_logger():
    return Mock(spec=Logger)


@pytest.fixture
def pfr_base_sdk(mock_logger):
    config = SDKConfiguration(
        client=httpx.Client(),
        client_supplied=False,
        async_client=None,
        async_client_supplied=True,
        debug_logger=mock_logger,
    )
    return BaseSDK(sdk_config=config)


@pytest.mark.unit
class TestPFRBaseSDK:
    def test_inherits_from_core(self):
        assert issubclass(BaseSDK, CoreBaseSDK)

    def test_default_error_cls(self, pfr_base_sdk):
        assert pfr_base_sdk._default_error_cls is GriddyPFRDefaultError

    def test_no_response_error_cls(self, pfr_base_sdk):
        assert pfr_base_sdk._no_response_error_cls is NoResponseError

    def test_security_model_cls(self, pfr_base_sdk):
        assert pfr_base_sdk._security_model_cls is Security

    def test_security_env_mapping(self, pfr_base_sdk):
        assert pfr_base_sdk._security_env_mapping == {"pfr_auth": "GRIDDY_PFR_AUTH"}
