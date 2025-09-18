"""
Griddy SDK - Python SDK for sports data sources.

This SDK provides access to multiple sports data sources including:
- NFL.com
- Pro Football Reference
- ESPN

Usage:
    from griddy import nfl, pfr, espn

    # NFL data
    nfl_client = nfl.Client()
    games = nfl_client.get_games(season=2024, week=1)

    # Pro Football Reference data
    pfr_client = pfr.Client()
    player = pfr_client.get_player("player_id")

    # ESPN data
    espn_client = espn.Client()
    scoreboard = espn_client.get_scoreboard()
"""

from . import core
from . import nfl
from . import pfr
from . import espn
from . import pff

# Version
__version__ = "0.1.0"

# Main exports
__all__ = [
    "__version__",
    "core",
    "nfl",
    "pfr",
    "espn",
    "pff",
]

# Convenience imports for common exceptions
from .core.exceptions import (
    GriddyError,
    APIError,
    RateLimitError,
    NotFoundError,
    AuthenticationError,
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
