"""Tests for griddy.pfr.basesdk module."""

from unittest.mock import Mock

import httpx
import pytest

from griddy.core.basesdk import BaseSDK as CoreBaseSDK
from griddy.core.utils.logger import Logger
from griddy.pfr.basesdk import BaseSDK, EndpointConfig
from griddy.pfr.errors import ParsingError
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

    def test_execute_endpoint_enriches_parsing_error_with_url(self, pfr_base_sdk):
        def bad_parser(html):
            raise ParsingError(
                "Could not find table", selector="games", html_sample=html[:500]
            )

        config = EndpointConfig(
            path_template="/years/{season}/games.htm",
            operation_id="get_schedule",
            wait_for_element="table#games",
            parser=bad_parser,
            response_type=dict,
            path_params={"season": 2024},
        )

        pfr_base_sdk.browserless = Mock()
        pfr_base_sdk.browserless.get_page_content.return_value = "<html></html>"

        with pytest.raises(ParsingError) as exc_info:
            pfr_base_sdk._execute_endpoint(config)

        err = exc_info.value
        assert err.selector == "games"
        assert err.url is not None
        assert "/years/2024/games.htm" in err.url
        assert err.html_sample == "<html></html>"
