from __future__ import annotations

from typing import Any, Dict, List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from .game_center_schedule import GamecenterSchedule, GamecenterScheduleTypedDict
from .passer_stats import PasserStats, PasserStatsTypedDict


class PassDistanceLeadersTypedDict(TypedDict):
    pass


class PassDistanceLeaders(BaseModel):
    pass


class SpeedLeadersTypedDict(TypedDict):
    pass


class SpeedLeaders(BaseModel):
    pass


class TimeToSackLeadersTypedDict(TypedDict):
    pass


class TimeToSackLeaders(BaseModel):
    pass


class LeadersTypedDict(TypedDict):
    pass_distance_leaders: NotRequired[PassDistanceLeadersTypedDict]
    speed_leaders: NotRequired[SpeedLeadersTypedDict]
    time_to_sack_leaders: NotRequired[TimeToSackLeadersTypedDict]


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


class LeagueAverageSeparationToQbTypedDict(TypedDict):
    avg: NotRequired[float]


class LeagueAverageSeparationToQb(BaseModel):
    avg: Optional[float] = None


class PassRushersTypedDict(TypedDict):
    home: NotRequired[List[Dict[str, Any]]]
    league_average_separation_to_qb: NotRequired[LeagueAverageSeparationToQbTypedDict]
    visitor: NotRequired[List[Dict[str, Any]]]


class PassRushers(BaseModel):
    home: Optional[List[Dict[str, Any]]] = None

    league_average_separation_to_qb: Annotated[
        Optional[LeagueAverageSeparationToQb],
        pydantic.Field(alias="leagueAverageSeparationToQb"),
    ] = None

    visitor: Optional[List[Dict[str, Any]]] = None


class PassersTypedDict(TypedDict):
    home: NotRequired[PasserStatsTypedDict]
    visitor: NotRequired[PasserStatsTypedDict]


class Passers(BaseModel):
    home: Optional[PasserStats] = None

    visitor: Optional[PasserStats] = None


class LeagueAverageReceiverSeparationTypedDict(TypedDict):
    avg: NotRequired[float]


class LeagueAverageReceiverSeparation(BaseModel):
    avg: Optional[float] = None


class ReceiversTypedDict(TypedDict):
    home: NotRequired[List[Dict[str, Any]]]
    league_average_receiver_separation: NotRequired[
        LeagueAverageReceiverSeparationTypedDict
    ]
    visitor: NotRequired[List[Dict[str, Any]]]


class Receivers(BaseModel):
    home: Optional[List[Dict[str, Any]]] = None

    league_average_receiver_separation: Annotated[
        Optional[LeagueAverageReceiverSeparation],
        pydantic.Field(alias="leagueAverageReceiverSeparation"),
    ] = None

    visitor: Optional[List[Dict[str, Any]]] = None


class RushersTypedDict(TypedDict):
    home: NotRequired[List[Dict[str, Any]]]
    visitor: NotRequired[List[Dict[str, Any]]]


class Rushers(BaseModel):
    home: Optional[List[Dict[str, Any]]] = None

    visitor: Optional[List[Dict[str, Any]]] = None


class GamecenterResponseTypedDict(TypedDict):
    leaders: NotRequired[LeadersTypedDict]
    pass_rushers: NotRequired[PassRushersTypedDict]
    passers: NotRequired[PassersTypedDict]
    receivers: NotRequired[ReceiversTypedDict]
    rushers: NotRequired[RushersTypedDict]
    schedule: NotRequired[GamecenterScheduleTypedDict]


class GamecenterResponse(BaseModel):
    leaders: Optional[Leaders] = None

    pass_rushers: Annotated[
        Optional[PassRushers], pydantic.Field(alias="passRushers")
    ] = None

    passers: Optional[Passers] = None

    receivers: Optional[Receivers] = None

    rushers: Optional[Rushers] = None

    schedule: Optional[GamecenterSchedule] = None
