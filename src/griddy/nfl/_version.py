
import importlib.metadata

__title__: str = "griddy-nfl"
__version__: str = "0.1.3"
__openapi_doc_version__: str = "1.0.0"
__gen_version__: str = "2.721.3"
__user_agent__: str = "speakeasy-sdk/python 0.1.3 2.721.3 1.0.0 griddy-nfl"

try:
    if __package__ is not None:
        __version__ = importlib.metadata.version(__package__)
except importlib.metadata.PackageNotFoundError:
    pass
