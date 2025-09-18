"""ESPN data source module."""

from .client import ESPNClient
from .models import ESPNGame, ESPNTeam, ESPNPlayer, ESPNPlayerStats, ESPNScoreboard

__all__ = [
    "ESPNClient",
    "ESPNGame",
    "ESPNTeam",
    "ESPNPlayer",
    "ESPNPlayerStats",
    "ESPNScoreboard",
]

# Convenience alias
Client = ESPNClient