"""Pro Football Focus (PFF) data source module."""

from .client import PFFClient
from .models import (
    PFFDefensiveGrades,
    PFFPassingGrades,
    PFFPlayer,
    PFFPlayerGrades,
    PFFPlayerMetrics,
    PFFReceivingGrades,
    PFFRushingGrades,
    PFFSeasonSummary,
    PFFSpecialTeamsGrades,
    PFFTeamGrades,
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
