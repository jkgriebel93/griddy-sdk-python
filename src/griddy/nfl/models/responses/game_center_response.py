from __future__ import annotations

from typing import Any, Dict, List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.game_center_schedule import (
    GamecenterSchedule,
)
from griddy.nfl.models.entities.passer_stats import PasserStats
from griddy.nfl.types import BaseModel


class PassDistanceLeaders(BaseModel):
    pass


class SpeedLeaders(BaseModel):
    pass


class TimeToSackLeaders(BaseModel):
    pass


class Leaders(BaseModel):
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
    avg: Optional[float] = None


class PassRushers(BaseModel):
    home: Optional[List[Dict[str, Any]]] = None

    league_average_separation_to_qb: Annotated[
        Optional[LeagueAverageSeparationToQb],
        pydantic.Field(alias="leagueAverageSeparationToQb"),
    ] = None

    visitor: Optional[List[Dict[str, Any]]] = None


class Passers(BaseModel):
    home: Optional[PasserStats] = None

    visitor: Optional[PasserStats] = None


class LeagueAverageReceiverSeparation(BaseModel):
    avg: Optional[float] = None


class Receivers(BaseModel):
    home: Optional[List[Dict[str, Any]]] = None

    league_average_receiver_separation: Annotated[
        Optional[LeagueAverageReceiverSeparation],
        pydantic.Field(alias="leagueAverageReceiverSeparation"),
    ] = None

    visitor: Optional[List[Dict[str, Any]]] = None


class Rushers(BaseModel):
    home: Optional[List[Dict[str, Any]]] = None

    visitor: Optional[List[Dict[str, Any]]] = None


class GamecenterResponse(BaseModel):
    leaders: Optional[Leaders] = None

    pass_rushers: Annotated[
        Optional[PassRushers], pydantic.Field(alias="passRushers")
    ] = None

    passers: Optional[Passers] = None

    receivers: Optional[Receivers] = None

    rushers: Optional[Rushers] = None

    schedule: Optional[GamecenterSchedule] = None
