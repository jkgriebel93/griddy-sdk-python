import pytest

from griddy.nfl.endpoints.pro import ProSDK
from griddy.nfl.sdkconfiguration import SDKConfiguration
from griddy.nfl.utils.logger import get_default_logger


@pytest.mark.unit
class TestProSDK:
    def test_pro_endpoints_are_routed_to_pro_server(self):
        sdk = ProSDK(
            sdk_config=SDKConfiguration(
                client=None,
                client_supplied=False,
                async_client=None,
                async_client_supplied=False,
                debug_logger=get_default_logger(),
            ),
            parent_ref=None,
        )

        assert sdk.sdk_configuration.is_pro
        server_url = sdk._get_url(base_url=None, url_variables=None)
        assert server_url == "https://pro.nfl.com"
