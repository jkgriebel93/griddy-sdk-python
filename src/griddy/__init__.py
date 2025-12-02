"""
Griddy SDK - Python SDK for sports data sources.

This SDK provides access to multiple sports data sources including:
- NFL.com
- Pro Football Reference
- ESPN

Usage:
    from griddy import nfl

    # NFL data
    nfl_client = nfl.Client()
    games = nfl_client.get_games(season=2024, week=1)

"""

from . import core

# Version
__version__ = "0.1.0"

# Main exports
__all__ = [
    "__version__",
    "core",
    "nfl",
]

# Convenience imports for common exceptions
from .core.exceptions import (
    APIError,
    AuthenticationError,
    GriddyError,
    NotFoundError,
    RateLimitError,
    ValidationError,
)

# Add exceptions to __all__
__all__.extend(
    [
        "GriddyError",
        "APIError",
        "RateLimitError",
        "NotFoundError",
        "AuthenticationError",
        "ValidationError",
    ]
)
