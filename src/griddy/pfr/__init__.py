from ._version import __user_agent__, __version__
from .sdk import GriddyPFR
from .sdkconfiguration import SERVERS, SDKConfiguration

__all__ = [
    "GriddyPFR",
    "SDKConfiguration",
    "SERVERS",
    "VERSION",
    "USER_AGENT",
]

VERSION: str = __version__
USER_AGENT: str = __user_agent__
