from typing import Optional

from griddy.nfl.basesdk import BaseSDK
from griddy.nfl.sdkconfiguration import SDKConfiguration

class ProSDK(BaseSDK):
    def __init__(self, sdk_config: SDKConfiguration, parent_ref: Optional[object]):
        super().__init__(sdk_config=sdk_config,
                         parent_ref=parent_ref)
        self.sdk_configuration.is_pro = True
