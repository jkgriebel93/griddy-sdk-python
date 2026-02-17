from typing import Optional

from griddy_nfl.basesdk import BaseSDK
from griddy_nfl.sdkconfiguration import SDKConfiguration


class ProSDK(BaseSDK):
    def __init__(self, sdk_config: SDKConfiguration, parent_ref: Optional[object]):
        super().__init__(sdk_config=sdk_config, parent_ref=parent_ref)
        self.sdk_configuration.server_type = "pro"
