from __future__ import annotations
from .binaryflagenum import BinaryFlagEnum
from .playtypeenum import PlayTypeEnum
from .seasontypeenum import SeasonTypeEnum
from .weekslugenum import WeekSlugEnum
from ..types import BaseModel
from ..utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


YardsToGoType = Literal[
    "SHORT",
    "MID",
    "LONG",
]


QbAlignment = Literal[
    "PISTOL",
    "UNDER_CENTER",
    "SHOTGUN",
]


TargetLocation = Literal[
    "DOWN_SEAMS",
    "BETWEEN_HASHES",
    "OUTSIDE_NUMBERS",
]


AirYardType = Literal[
    "INTERMEDIATE",
    "SHORT",
    "DEEP",
]


DropbackTimeType = Literal[
    "QUICK",
    "LONG",
]


RushDirection = Literal[
    "INSIDE",
    "OUTSIDE",
]


ReceiverAlignment = Literal[
    "SLOT",
    "BACKFIELD",
    "TIGHT",
    "WIDE",
]


SeparationType = Literal[
    "OPEN",
    "TIGHT",
]


Personnel = Literal[
    "NICKEL",
    "BASE",
    "DIME",
]


DefendersInTheBoxType = Literal[
    "LIGHT",
    "STACKED",
    "NEUTRAL",
]


DefCoverageType = Literal[
    "PRESS",
    "MAN",
    "ZONE",
]


class GetFilmroomPlaysRequestTypedDict(TypedDict):
    game_id: NotRequired[List[str]]
    r"""Filter by specific game IDs (supports multiple values)"""
    week_slug: NotRequired[List[WeekSlugEnum]]
    r"""Filter by week identifier (supports multiple values)"""
    season: NotRequired[List[int]]
    r"""Filter by season year (supports multiple values)"""
    season_type: NotRequired[List[SeasonTypeEnum]]
    r"""Filter by season type"""
    nfl_id: NotRequired[List[str]]
    r"""Filter by player NFL ID"""
    quarter: NotRequired[List[int]]
    r"""Filter by quarter"""
    down: NotRequired[List[int]]
    r"""Filter by down"""
    yards_to_go_type: NotRequired[List[YardsToGoType]]
    r"""Filter by yards to go category"""
    touchdown: NotRequired[List[BinaryFlagEnum]]
    r"""Filter for touchdown plays (1 = yes, 0 = no)"""
    rush10_plus_yards: NotRequired[List[BinaryFlagEnum]]
    r"""Filter for rushing plays of 10+ yards"""
    fumble_lost: NotRequired[List[BinaryFlagEnum]]
    r"""Filter for plays with fumbles lost"""
    fumble: NotRequired[List[BinaryFlagEnum]]
    r"""Filter for plays with fumbles"""
    qb_alignment: NotRequired[List[QbAlignment]]
    r"""Filter by quarterback alignment"""
    redzone: NotRequired[List[BinaryFlagEnum]]
    r"""Filter for red zone plays"""
    goal_to_go: NotRequired[List[BinaryFlagEnum]]
    r"""Filter for goal-to-go situations"""
    pass_play: NotRequired[List[BinaryFlagEnum]]
    r"""Filter for passing plays"""
    run_play: NotRequired[List[BinaryFlagEnum]]
    r"""Filter for running plays"""
    play_type: NotRequired[List[PlayTypeEnum]]
    r"""Filter by specific play types"""
    attempt: NotRequired[List[BinaryFlagEnum]]
    r"""Filter for passing attempts"""
    completion: NotRequired[List[BinaryFlagEnum]]
    r"""Filter for completed passes"""
    interception: NotRequired[List[BinaryFlagEnum]]
    r"""Filter for interceptions"""
    reception: NotRequired[List[BinaryFlagEnum]]
    r"""Filter for receptions"""
    sack: NotRequired[List[BinaryFlagEnum]]
    r"""Filter for sacks"""
    rec_motion: NotRequired[List[BinaryFlagEnum]]
    r"""Filter by receiver motion"""
    target_location: NotRequired[List[TargetLocation]]
    r"""Filter by target location on field"""
    air_yard_type: NotRequired[List[AirYardType]]
    r"""Filter by air yards category"""
    dropback_time_type: NotRequired[List[DropbackTimeType]]
    r"""Filter by dropback time"""
    pressure: NotRequired[List[BinaryFlagEnum]]
    r"""Filter by quarterback pressure"""
    blitz: NotRequired[List[BinaryFlagEnum]]
    r"""Filter by defensive blitz"""
    play_action: NotRequired[List[BinaryFlagEnum]]
    r"""Filter by play action usage"""
    rush_direction: NotRequired[List[RushDirection]]
    r"""Filter by rush direction"""
    run_stuff: NotRequired[List[BinaryFlagEnum]]
    r"""Filter for stuffed runs"""
    receiver_alignment: NotRequired[List[ReceiverAlignment]]
    r"""Filter by receiver alignment"""
    separation_type: NotRequired[List[SeparationType]]
    r"""Filter by receiver separation"""
    personnel: NotRequired[List[Personnel]]
    r"""Filter by defensive personnel package"""
    defenders_in_the_box_type: NotRequired[List[DefendersInTheBoxType]]
    r"""Filter by defenders in the box"""
    def_coverage_type: NotRequired[List[DefCoverageType]]
    r"""Filter by defensive coverage type"""


class GetFilmroomPlaysRequest(BaseModel):
    game_id: Annotated[
        Optional[List[str]],
        pydantic.Field(alias="gameId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by specific game IDs (supports multiple values)"""

    week_slug: Annotated[
        Optional[List[WeekSlugEnum]],
        pydantic.Field(alias="weekSlug"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by week identifier (supports multiple values)"""

    season: Annotated[
        Optional[List[int]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by season year (supports multiple values)"""

    season_type: Annotated[
        Optional[List[SeasonTypeEnum]],
        pydantic.Field(alias="seasonType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by season type"""

    nfl_id: Annotated[
        Optional[List[str]],
        pydantic.Field(alias="nflId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by player NFL ID"""

    quarter: Annotated[
        Optional[List[int]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by quarter"""

    down: Annotated[
        Optional[List[int]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by down"""

    yards_to_go_type: Annotated[
        Optional[List[YardsToGoType]],
        pydantic.Field(alias="yardsToGoType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by yards to go category"""

    touchdown: Annotated[
        Optional[List[BinaryFlagEnum]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter for touchdown plays (1 = yes, 0 = no)"""

    rush10_plus_yards: Annotated[
        Optional[List[BinaryFlagEnum]],
        pydantic.Field(alias="rush10PlusYards"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter for rushing plays of 10+ yards"""

    fumble_lost: Annotated[
        Optional[List[BinaryFlagEnum]],
        pydantic.Field(alias="fumbleLost"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter for plays with fumbles lost"""

    fumble: Annotated[
        Optional[List[BinaryFlagEnum]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter for plays with fumbles"""

    qb_alignment: Annotated[
        Optional[List[QbAlignment]],
        pydantic.Field(alias="qbAlignment"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by quarterback alignment"""

    redzone: Annotated[
        Optional[List[BinaryFlagEnum]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter for red zone plays"""

    goal_to_go: Annotated[
        Optional[List[BinaryFlagEnum]],
        pydantic.Field(alias="goalToGo"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter for goal-to-go situations"""

    pass_play: Annotated[
        Optional[List[BinaryFlagEnum]],
        pydantic.Field(alias="passPlay"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter for passing plays"""

    run_play: Annotated[
        Optional[List[BinaryFlagEnum]],
        pydantic.Field(alias="runPlay"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter for running plays"""

    play_type: Annotated[
        Optional[List[PlayTypeEnum]],
        pydantic.Field(alias="playType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by specific play types"""

    attempt: Annotated[
        Optional[List[BinaryFlagEnum]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter for passing attempts"""

    completion: Annotated[
        Optional[List[BinaryFlagEnum]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter for completed passes"""

    interception: Annotated[
        Optional[List[BinaryFlagEnum]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter for interceptions"""

    reception: Annotated[
        Optional[List[BinaryFlagEnum]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter for receptions"""

    sack: Annotated[
        Optional[List[BinaryFlagEnum]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter for sacks"""

    rec_motion: Annotated[
        Optional[List[BinaryFlagEnum]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by receiver motion"""

    target_location: Annotated[
        Optional[List[TargetLocation]],
        pydantic.Field(alias="targetLocation"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by target location on field"""

    air_yard_type: Annotated[
        Optional[List[AirYardType]],
        pydantic.Field(alias="airYardType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by air yards category"""

    dropback_time_type: Annotated[
        Optional[List[DropbackTimeType]],
        pydantic.Field(alias="dropbackTimeType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by dropback time"""

    pressure: Annotated[
        Optional[List[BinaryFlagEnum]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by quarterback pressure"""

    blitz: Annotated[
        Optional[List[BinaryFlagEnum]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by defensive blitz"""

    play_action: Annotated[
        Optional[List[BinaryFlagEnum]],
        pydantic.Field(alias="playAction"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by play action usage"""

    rush_direction: Annotated[
        Optional[List[RushDirection]],
        pydantic.Field(alias="rushDirection"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by rush direction"""

    run_stuff: Annotated[
        Optional[List[BinaryFlagEnum]],
        pydantic.Field(alias="runStuff"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter for stuffed runs"""

    receiver_alignment: Annotated[
        Optional[List[ReceiverAlignment]],
        pydantic.Field(alias="receiverAlignment"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by receiver alignment"""

    separation_type: Annotated[
        Optional[List[SeparationType]],
        pydantic.Field(alias="separationType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by receiver separation"""

    personnel: Annotated[
        Optional[List[Personnel]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by defensive personnel package"""

    defenders_in_the_box_type: Annotated[
        Optional[List[DefendersInTheBoxType]],
        pydantic.Field(alias="defendersInTheBoxType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by defenders in the box"""

    def_coverage_type: Annotated[
        Optional[List[DefCoverageType]],
        pydantic.Field(alias="def_coverageType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by defensive coverage type"""
