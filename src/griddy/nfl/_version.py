import importlib.metadata

from griddy.settings import *

__title__: str = "griddy-nfl"
__version__: str = "0.1.3"
__openapi_doc_version__: str = "1.0.0"
__user_agent__: str = NFL.get("user_agent")

try:
    if __package__ is not None:
        __version__ = importlib.metadata.version(__package__)
except importlib.metadata.PackageNotFoundError:
    pass
