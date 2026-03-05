from ._version import (
    __user_agent__,
    __version__,
)
from .sdk import GriddyNFL
from .sdkconfiguration import SERVERS, SDKConfiguration

__all__ = [
    "GriddyNFL",
    "SDKConfiguration",
    "SERVERS",
    "VERSION",
    "USER_AGENT",
]

VERSION: str = __version__
USER_AGENT = __user_agent__
