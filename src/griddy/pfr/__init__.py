from ._version import __title__, __user_agent__, __version__
from .sdk import *  # noqa: F401,F403
from .sdkconfiguration import *  # noqa: F401,F403

VERSION: str = __version__
USER_AGENT: str = __user_agent__
