"""Pro Football Reference data source module."""

from .client import PFRClient
from .models import PFRPlayer, PFRPlayerStats, PFRTeamStats, PFRGame

__all__ = [
    "PFRClient",
    "PFRPlayer",
    "PFRPlayerStats",
    "PFRTeamStats",
    "PFRGame",
]

# Convenience alias
Client = PFRClient
