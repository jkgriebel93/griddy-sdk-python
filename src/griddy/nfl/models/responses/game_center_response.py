from __future__ import annotations

from typing import Any, Dict, List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.game_center_schedule import GamecenterSchedule
from griddy.nfl.models.entities.passer_stats import PasserStats
from griddy.nfl.types import BaseModel


class PassDistanceLeaders(BaseModel):
    """Next Gen Stats pass distance leaders."""

    pass


class SpeedLeaders(BaseModel):
    """Next Gen Stats speed leaders."""

    pass


class TimeToSackLeaders(BaseModel):
    """Next Gen Stats time-to-sack leaders."""

    pass


class Leaders(BaseModel):
    """Aggregated NGS leaders across categories."""

    pass_distance_leaders: Annotated[
        Optional[PassDistanceLeaders], pydantic.Field(alias="passDistanceLeaders")
    ] = None

    speed_leaders: Annotated[
        Optional[SpeedLeaders], pydantic.Field(alias="speedLeaders")
    ] = None

    time_to_sack_leaders: Annotated[
        Optional[TimeToSackLeaders], pydantic.Field(alias="timeToSackLeaders")
    ] = None


class LeagueAverageSeparationToQb(BaseModel):
    """League-average separation to quarterback metrics."""

    avg: Optional[float] = None


class PassRushers(BaseModel):
    """NGS pass rusher statistics for a game."""

    home: Optional[List[Dict[str, Any]]] = None

    league_average_separation_to_qb: Annotated[
        Optional[LeagueAverageSeparationToQb],
        pydantic.Field(alias="leagueAverageSeparationToQb"),
    ] = None

    visitor: Optional[List[Dict[str, Any]]] = None


class Passers(BaseModel):
    """NGS passer statistics for a game."""

    home: Optional[PasserStats] = None

    visitor: Optional[PasserStats] = None


class LeagueAverageReceiverSeparation(BaseModel):
    """League-average receiver separation metrics."""

    avg: Optional[float] = None


class Receivers(BaseModel):
    """NGS receiver statistics for a game."""

    home: Optional[List[Dict[str, Any]]] = None

    league_average_receiver_separation: Annotated[
        Optional[LeagueAverageReceiverSeparation],
        pydantic.Field(alias="leagueAverageReceiverSeparation"),
    ] = None

    visitor: Optional[List[Dict[str, Any]]] = None


class Rushers(BaseModel):
    """NGS rusher statistics for a game."""

    home: Optional[List[Dict[str, Any]]] = None

    visitor: Optional[List[Dict[str, Any]]] = None


class GamecenterResponse(BaseModel):
    """Response containing Game Center data with NGS stats."""

    leaders: Optional[Leaders] = None

    pass_rushers: Annotated[
        Optional[PassRushers], pydantic.Field(alias="passRushers")
    ] = None

    passers: Optional[Passers] = None

    receivers: Optional[Receivers] = None

    rushers: Optional[Rushers] = None

    schedule: Optional[GamecenterSchedule] = None
