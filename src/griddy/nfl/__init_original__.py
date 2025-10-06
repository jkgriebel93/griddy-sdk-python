"""NFL.com data source module."""

from .client import NFLClient
from .models import NFLGame, NFLTeam, NFLPlayer, NFLPlayerStats

__all__ = [
    "NFLClient",
    "NFLGame",
    "NFLTeam",
    "NFLPlayer",
    "NFLPlayerStats",
]

# Convenience alias
Client = NFLClient
