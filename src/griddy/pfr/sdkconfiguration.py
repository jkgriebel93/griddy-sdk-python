from dataclasses import dataclass
from typing import Dict, Optional, Tuple

from griddy.core.sdkconfiguration import SDKConfiguration as CoreSDKConfiguration

from ._version import __user_agent__, __version__
from .utils import remove_suffix

SERVERS = {
    "default": "https://www.pro-football-reference.com",
}


@dataclass
class SDKConfiguration(CoreSDKConfiguration):
    sdk_version: str = __version__
    user_agent: str = __user_agent__
    server_type: str = "default"

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url is not None and self.server_url:
            return remove_suffix(self.server_url, "/"), {}
        if self.server_idx is None:
            self.server_idx = 0

        server_url = SERVERS.get(self.server_type, SERVERS["default"])
        return server_url, {}
