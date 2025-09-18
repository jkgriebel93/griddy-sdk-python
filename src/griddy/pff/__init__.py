"""Pro Football Focus (PFF) data source module."""

from .client import PFFClient
from .models import (
    PFFPlayer, PFFPlayerGrades, PFFPlayerMetrics, PFFTeamGrades,
    PFFPassingGrades, PFFRushingGrades, PFFReceivingGrades,
    PFFDefensiveGrades, PFFSpecialTeamsGrades, PFFSeasonSummary
)

__all__ = [
    "PFFClient",
    "PFFPlayer",
    "PFFPlayerGrades",
    "PFFPlayerMetrics",
    "PFFTeamGrades",
    "PFFPassingGrades",
    "PFFRushingGrades",
    "PFFReceivingGrades",
    "PFFDefensiveGrades",
    "PFFSpecialTeamsGrades",
    "PFFSeasonSummary",
]

# Convenience alias
Client = PFFClient