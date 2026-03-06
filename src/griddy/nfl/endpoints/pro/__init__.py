from typing import Optional

from griddy.nfl.basesdk import BaseSDK
from griddy.nfl.sdkconfiguration import SDKConfiguration


class ProSDK(BaseSDK):
    r"""Base class for all Pro API (pro.nfl.com) endpoint sub-SDKs.

    Sets ``server_type`` to ``"pro"`` so that requests are routed to the
    Pro NFL API server instead of the default public API.
    """

    def __init__(self, sdk_config: SDKConfiguration, parent_ref: Optional[object]):
        """Initialise the Pro SDK and set the server type to ``"pro"``."""
        super().__init__(sdk_config=sdk_config, parent_ref=parent_ref)
        self.sdk_configuration.server_type = "pro"
