from __future__ import annotations

from typing import Literal, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.enums.position_enums import (
    DefenseNGSPositionEnum,
    DefenseNGSPositionGroupEnum,
    DefensePositionEnum,
    DefensePositionGroupEnum,
)

from ...types import BaseModel


class DefensivePlayerOverviewStatsTypedDict(TypedDict):
    display_name: str
    r"""Player's full name"""
    gp: int
    r"""Games played"""
    gs: int
    r"""Games started"""
    nfl_id: str
    r"""NFL player identifier"""
    position: DefensePositionEnum
    r"""Player position"""
    snap: int
    r"""Total defensive snaps played"""
    team_id: str
    r"""Team identifier"""
    game_snap: NotRequired[int]
    r"""Defensive snaps played in games"""
    h_stop: NotRequired[int]
    r"""Hard stops (tackles for loss or no gain)"""
    headshot: NotRequired[str]
    r"""URL to player headshot image (contains formatInstructions placeholder)"""
    int_: NotRequired[int]
    r"""Interceptions"""
    jersey_number: NotRequired[int]
    r"""Player's jersey number"""
    ngs_position: NotRequired[DefenseNGSPositionEnum]
    r"""Next Gen Stats position"""
    ngs_position_group: NotRequired[DefenseNGSPositionGroupEnum]
    r"""Defensive position group"""
    pass_rating_nd: NotRequired[float]
    r"""Passer rating allowed when targeted (no data excluded)"""
    position_group: NotRequired[DefensePositionGroupEnum]
    r"""Defensive position group"""
    pr: NotRequired[int]
    r"""Pass rush snaps"""
    qbp: NotRequired[int]
    r"""Quarterback pressures"""
    qbp_r: NotRequired[float]
    r"""Quarterback pressure rate (0-1)"""
    qd: NotRequired[bool]
    r"""Qualified defender status"""
    rd: NotRequired[int]
    r"""Run defense snaps"""
    rec_nd: NotRequired[int]
    r"""Receptions allowed (no data excluded)"""
    rec_td_nd: NotRequired[int]
    r"""Receiving touchdowns allowed (no data excluded)"""
    rec_yds_nd: NotRequired[int]
    r"""Receiving yards allowed (no data excluded)"""
    sack: NotRequired[float]
    r"""Sacks"""
    short_name: NotRequired[str]
    r"""Abbreviated player name"""
    snap_pct: NotRequired[float]
    r"""Percentage of team snaps played (0-1)"""
    t_stop: NotRequired[int]
    r"""Tackle stops (successful tackles)"""
    tck: NotRequired[int]
    r"""Total tackles"""
    team_snap: NotRequired[int]
    r"""Total team defensive snaps"""
    tg: NotRequired[int]
    r"""Team games for player"""
    tgt_nd: NotRequired[int]
    r"""Times targeted in coverage (no data excluded)"""
    total_tg: NotRequired[int]
    r"""Total team games in period"""


class DefensivePlayerOverviewStats(BaseModel):
    display_name: Annotated[str, pydantic.Field(alias="displayName")]
    r"""Player's full name"""

    gp: int
    r"""Games played"""

    gs: int
    r"""Games started"""

    nfl_id: Annotated[str, pydantic.Field(alias="nflId")]
    r"""NFL player identifier"""

    position: DefensePositionEnum
    r"""Player position"""

    snap: int
    r"""Total defensive snaps played"""

    team_id: Annotated[str, pydantic.Field(alias="teamId")]
    r"""Team identifier"""

    game_snap: Annotated[Optional[int], pydantic.Field(alias="gameSnap")] = None
    r"""Defensive snaps played in games"""

    h_stop: Annotated[Optional[int], pydantic.Field(alias="hStop")] = None
    r"""Hard stops (tackles for loss or no gain)"""

    headshot: Optional[str] = None
    r"""URL to player headshot image (contains formatInstructions placeholder)"""

    int_: Annotated[Optional[int], pydantic.Field(alias="int")] = None
    r"""Interceptions"""

    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    r"""Player's jersey number"""

    ngs_position: Annotated[
        Optional[DefenseNGSPositionEnum],
        pydantic.Field(alias="ngsPosition"),
    ] = None
    r"""Next Gen Stats position"""

    ngs_position_group: Annotated[
        Optional[DefenseNGSPositionGroupEnum], pydantic.Field(alias="ngsPositionGroup")
    ] = None
    r"""Defensive position group"""

    pass_rating_nd: Annotated[Optional[float], pydantic.Field(alias="passRatingNd")] = (
        None
    )
    r"""Passer rating allowed when targeted (no data excluded)"""

    position_group: Annotated[
        Optional[DefensePositionGroupEnum], pydantic.Field(alias="positionGroup")
    ] = None
    r"""Defensive position group"""

    pr: Optional[int] = None
    r"""Pass rush snaps"""

    qbp: Optional[int] = None
    r"""Quarterback pressures"""

    qbp_r: Annotated[Optional[float], pydantic.Field(alias="qbpR")] = None
    r"""Quarterback pressure rate (0-1)"""

    qd: Optional[bool] = None
    r"""Qualified defender status"""

    rd: Optional[int] = None
    r"""Run defense snaps"""

    rec_nd: Annotated[Optional[int], pydantic.Field(alias="recNd")] = None
    r"""Receptions allowed (no data excluded)"""

    rec_td_nd: Annotated[Optional[int], pydantic.Field(alias="recTdNd")] = None
    r"""Receiving touchdowns allowed (no data excluded)"""

    rec_yds_nd: Annotated[Optional[int], pydantic.Field(alias="recYdsNd")] = None
    r"""Receiving yards allowed (no data excluded)"""

    sack: Optional[float] = None
    r"""Sacks"""

    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    r"""Abbreviated player name"""

    snap_pct: Annotated[Optional[float], pydantic.Field(alias="snapPct")] = None
    r"""Percentage of team snaps played (0-1)"""

    t_stop: Annotated[Optional[int], pydantic.Field(alias="tStop")] = None
    r"""Tackle stops (successful tackles)"""

    tck: Optional[int] = None
    r"""Total tackles"""

    team_snap: Annotated[Optional[int], pydantic.Field(alias="teamSnap")] = None
    r"""Total team defensive snaps"""

    tg: Optional[int] = None
    r"""Team games for player"""

    tgt_nd: Annotated[Optional[int], pydantic.Field(alias="tgtNd")] = None
    r"""Times targeted in coverage (no data excluded)"""

    total_tg: Annotated[Optional[int], pydantic.Field(alias="totalTg")] = None
    r"""Total team games in period"""
