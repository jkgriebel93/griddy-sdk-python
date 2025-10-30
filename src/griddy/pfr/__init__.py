"""Pro Football Reference data source module."""

from .client import PFRClient
from .models import PFRGame, PFRPlayer, PFRPlayerStats, PFRTeamStats

__all__ = [
    "PFRClient",
    "PFRPlayer",
    "PFRPlayerStats",
    "PFRTeamStats",
    "PFRGame",
]

# Convenience alias
Client = PFRClient
