from dataclasses import dataclass, field
from typing import Callable, Dict, Optional, Tuple, Union

from griddy.core.sdkconfiguration import SDKConfiguration as CoreSDKConfiguration

from ..nfl import models
from ._version import (
    __user_agent__,
    __version__,
)
from .httpclient import AsyncHttpClient, HttpClient
from .types import UNSET, OptionalNullable
from .utils import Logger, RetryConfig, remove_suffix

SERVERS = {
    "regular": "https://api.nfl.com",
    "pro": "https://pro.nfl.com",
    "ngs": "https://nextgenstats.nfl.com",
}


@dataclass
class SDKConfiguration(CoreSDKConfiguration):
    security: Optional[Union[models.Security, Callable[[], models.Security]]] = None
    sdk_version: str = __version__
    user_agent: str = __user_agent__
    server_type: str = "regular"
    custom_auth_info: Optional[dict] = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url is not None and self.server_url:
            return remove_suffix(self.server_url, "/"), {}
        if self.server_idx is None:
            self.server_idx = 0

        server_url = SERVERS.get(self.server_type, SERVERS["regular"])
        return server_url, {}
