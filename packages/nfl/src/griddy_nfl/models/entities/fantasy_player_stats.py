from __future__ import annotations

from typing import Literal, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ...types import BaseModel

FantasyPlayerStatsPosition = Literal[
    "QB",
    "RB",
    "WR",
    "TE",
    "K",
    "DST",
]
r"""Player position"""


PositionGroup = Literal[
    "QB",
    "RB",
    "WR",
    "TE",
    "SPEC",
]
r"""Position group"""


class FantasyPlayerStatsTypedDict(TypedDict):
    display_name: str
    r"""Player's full name"""
    fp_std: float
    r"""Fantasy points (standard scoring)"""
    gp: int
    r"""Games played"""
    nfl_id: str
    r"""NFL player identifier"""
    position: FantasyPlayerStatsPosition
    r"""Player position"""
    team_id: str
    r"""Team identifier"""
    fp_half_ppr: NotRequired[float]
    r"""Fantasy points (half-PPR scoring)"""
    fp_ppr: NotRequired[float]
    r"""Fantasy points (PPR scoring)"""
    fp_ppr_pg: NotRequired[float]
    r"""Fantasy points per game (PPR)"""
    fp_std_pg: NotRequired[float]
    r"""Fantasy points per game (standard)"""
    gs: NotRequired[int]
    r"""Games started"""
    headshot: NotRequired[str]
    r"""URL to player headshot image"""
    jersey_number: NotRequired[int]
    r"""Player's jersey number"""
    pass_int: NotRequired[int]
    r"""Passing interceptions"""
    pass_td: NotRequired[int]
    r"""Passing touchdowns"""
    pass_yds: NotRequired[int]
    r"""Passing yards"""
    pass_yds_pg: NotRequired[float]
    r"""Passing yards per game"""
    position_group: NotRequired[PositionGroup]
    r"""Position group"""
    rec: NotRequired[int]
    r"""Receptions"""
    rec_pg: NotRequired[float]
    r"""Receptions per game"""
    rec_td: NotRequired[int]
    r"""Receiving touchdowns"""
    rec_yds: NotRequired[int]
    r"""Receiving yards"""
    red_zone_targets: NotRequired[int]
    r"""Targets inside the red zone"""
    rush_td: NotRequired[int]
    r"""Rushing touchdowns"""
    rush_yds: NotRequired[int]
    r"""Rushing yards"""
    rush_yds_pg: NotRequired[float]
    r"""Rushing yards per game"""
    short_name: NotRequired[str]
    r"""Abbreviated player name"""
    snap_pct: NotRequired[float]
    r"""Percentage of offensive snaps played (0-1)"""
    target_share: NotRequired[float]
    r"""Percentage of team targets (0-1)"""
    tgt: NotRequired[int]
    r"""Targets"""


class FantasyPlayerStats(BaseModel):
    display_name: Annotated[str, pydantic.Field(alias="displayName")]
    r"""Player's full name"""

    fp_std: Annotated[float, pydantic.Field(alias="fpStd")]
    r"""Fantasy points (standard scoring)"""

    gp: int
    r"""Games played"""

    nfl_id: Annotated[str, pydantic.Field(alias="nflId")]
    r"""NFL player identifier"""

    position: FantasyPlayerStatsPosition
    r"""Player position"""

    team_id: Annotated[str, pydantic.Field(alias="teamId")]
    r"""Team identifier"""

    fp_half_ppr: Annotated[Optional[float], pydantic.Field(alias="fpHalfPpr")] = None
    r"""Fantasy points (half-PPR scoring)"""

    fp_ppr: Annotated[Optional[float], pydantic.Field(alias="fpPpr")] = None
    r"""Fantasy points (PPR scoring)"""

    fp_ppr_pg: Annotated[Optional[float], pydantic.Field(alias="fpPprPG")] = None
    r"""Fantasy points per game (PPR)"""

    fp_std_pg: Annotated[Optional[float], pydantic.Field(alias="fpStdPG")] = None
    r"""Fantasy points per game (standard)"""

    gs: Optional[int] = None
    r"""Games started"""

    headshot: Optional[str] = None
    r"""URL to player headshot image"""

    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    r"""Player's jersey number"""

    pass_int: Annotated[Optional[int], pydantic.Field(alias="passInt")] = None
    r"""Passing interceptions"""

    pass_td: Annotated[Optional[int], pydantic.Field(alias="passTd")] = None
    r"""Passing touchdowns"""

    pass_yds: Annotated[Optional[int], pydantic.Field(alias="passYds")] = None
    r"""Passing yards"""

    pass_yds_pg: Annotated[Optional[float], pydantic.Field(alias="passYdsPG")] = None
    r"""Passing yards per game"""

    position_group: Annotated[
        Optional[PositionGroup], pydantic.Field(alias="positionGroup")
    ] = None
    r"""Position group"""

    rec: Optional[int] = None
    r"""Receptions"""

    rec_pg: Annotated[Optional[float], pydantic.Field(alias="recPG")] = None
    r"""Receptions per game"""

    rec_td: Annotated[Optional[int], pydantic.Field(alias="recTd")] = None
    r"""Receiving touchdowns"""

    rec_yds: Annotated[Optional[int], pydantic.Field(alias="recYds")] = None
    r"""Receiving yards"""

    red_zone_targets: Annotated[
        Optional[int], pydantic.Field(alias="redZoneTargets")
    ] = None
    r"""Targets inside the red zone"""

    rush_td: Annotated[Optional[int], pydantic.Field(alias="rushTd")] = None
    r"""Rushing touchdowns"""

    rush_yds: Annotated[Optional[int], pydantic.Field(alias="rushYds")] = None
    r"""Rushing yards"""

    rush_yds_pg: Annotated[Optional[float], pydantic.Field(alias="rushYdsPG")] = None
    r"""Rushing yards per game"""

    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    r"""Abbreviated player name"""

    snap_pct: Annotated[Optional[float], pydantic.Field(alias="snapPct")] = None
    r"""Percentage of offensive snaps played (0-1)"""

    target_share: Annotated[Optional[float], pydantic.Field(alias="targetShare")] = None
    r"""Percentage of team targets (0-1)"""

    tgt: Optional[int] = None
    r"""Targets"""
