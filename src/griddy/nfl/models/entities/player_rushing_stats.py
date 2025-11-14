from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.enums.offensive_player_position_enum import (
    OffensivePlayerPositionEnum,
)

from ...types import BaseModel


class PlayerRushingStatsTypedDict(TypedDict):
    att: int
    r"""Rushing attempts"""
    display_name: str
    r"""Player's full name"""
    gp: int
    r"""Games played"""
    gs: int
    r"""Games started"""
    nfl_id: str
    r"""NFL player identifier"""
    position: OffensivePlayerPositionEnum
    r"""Offensive player position"""
    td: int
    r"""Rushing touchdowns"""
    team_id: str
    r"""Team identifier"""
    yds: int
    r"""Rushing yards"""
    ypc: float
    r"""Yards per carry"""
    att_pg: NotRequired[float]
    r"""Attempts per game"""
    eff: NotRequired[float]
    r"""Efficiency rating"""
    epa: NotRequired[float]
    r"""Expected Points Added"""
    epa_att: NotRequired[float]
    r"""EPA per attempt"""
    epa_pg: NotRequired[float]
    r"""EPA per game"""
    fum: NotRequired[int]
    r"""Fumbles"""
    fum_pg: NotRequired[float]
    r"""Fumbles per game"""
    headshot: NotRequired[str]
    r"""URL to player headshot image (contains formatInstructions placeholder)"""
    in_t_pct: NotRequired[float]
    r"""Inside tackles percentage (0-1)"""
    jersey_number: NotRequired[int]
    r"""Player's jersey number"""
    lost: NotRequired[int]
    r"""Fumbles lost"""
    lost_pg: NotRequired[float]
    r"""Fumbles lost per game"""
    ngs_position: NotRequired[OffensivePlayerPositionEnum]
    r"""Offensive player position"""
    ngs_position_group: NotRequired[OffensivePlayerPositionEnum]
    r"""Offensive player position"""
    position_group: NotRequired[OffensivePlayerPositionEnum]
    r"""Offensive player position"""
    qr: NotRequired[bool]
    r"""Qualified rusher status"""
    rush10_p_yds: NotRequired[int]
    r"""Rushes of 10+ yards"""
    rush10_p_yds_pg: NotRequired[float]
    r"""10+ yard rushes per game"""
    rush15_p_mph: NotRequired[int]
    r"""Rushes of 15+ mph"""
    rush15_p_mph_pg: NotRequired[float]
    r"""15+ mph rushes per game"""
    rush20_p_mph: NotRequired[int]
    r"""Rushes of 20+ mph"""
    rush20_p_mph_pg: NotRequired[float]
    r"""20+ mph rushes per game"""
    ryoe: NotRequired[float]
    r"""Rush Yards Over Expected"""
    ryoe_att: NotRequired[float]
    r"""RYOE per attempt"""
    ryoe_pg: NotRequired[float]
    r"""RYOE per game"""
    short_name: NotRequired[str]
    r"""Abbreviated player name"""
    st_box_pct: NotRequired[float]
    r"""Stacked box percentage (0-1)"""
    success: NotRequired[float]
    r"""Success rate (0-1)"""
    td_pg: NotRequired[float]
    r"""Touchdowns per game"""
    tg: NotRequired[int]
    r"""Team games for player"""
    total_tg: NotRequired[int]
    r"""Total team games in period"""
    under_pct: NotRequired[float]
    r"""Under center percentage (0-1)"""
    x_ry: NotRequired[float]
    r"""Expected rushing yards"""
    x_ry_pg: NotRequired[float]
    r"""Expected rushing yards per game"""
    x_ypc: NotRequired[float]
    r"""Expected yards per carry"""
    yaco: NotRequired[float]
    r"""Yards after contact"""
    yaco_att: NotRequired[float]
    r"""Yards after contact per attempt"""
    yaco_pg: NotRequired[float]
    r"""Yards after contact per game"""
    ybco: NotRequired[float]
    r"""Yards before contact"""
    ybco_pg: NotRequired[float]
    r"""Yards before contact per game"""
    yds_pg: NotRequired[float]
    r"""Yards per game"""


class PlayerRushingStats(BaseModel):
    att: int
    r"""Rushing attempts"""

    display_name: Annotated[str, pydantic.Field(alias="displayName")]
    r"""Player's full name"""

    gp: int
    r"""Games played"""

    gs: int
    r"""Games started"""

    nfl_id: Annotated[str, pydantic.Field(alias="nflId")]
    r"""NFL player identifier"""

    position: OffensivePlayerPositionEnum
    r"""Offensive player position"""

    td: int
    r"""Rushing touchdowns"""

    team_id: Annotated[str, pydantic.Field(alias="teamId")]
    r"""Team identifier"""

    yds: int
    r"""Rushing yards"""

    ypc: float
    r"""Yards per carry"""

    att_pg: Annotated[Optional[float], pydantic.Field(alias="attPG")] = None
    r"""Attempts per game"""

    eff: Optional[float] = None
    r"""Efficiency rating"""

    epa: Optional[float] = None
    r"""Expected Points Added"""

    epa_att: Annotated[Optional[float], pydantic.Field(alias="epaAtt")] = None
    r"""EPA per attempt"""

    epa_pg: Annotated[Optional[float], pydantic.Field(alias="epaPG")] = None
    r"""EPA per game"""

    fum: Optional[int] = None
    r"""Fumbles"""

    fum_pg: Annotated[Optional[float], pydantic.Field(alias="fumPG")] = None
    r"""Fumbles per game"""

    headshot: Optional[str] = None
    r"""URL to player headshot image (contains formatInstructions placeholder)"""

    in_t_pct: Annotated[Optional[float], pydantic.Field(alias="inTPct")] = None
    r"""Inside tackles percentage (0-1)"""

    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    r"""Player's jersey number"""

    lost: Optional[int] = None
    r"""Fumbles lost"""

    lost_pg: Annotated[Optional[float], pydantic.Field(alias="lostPG")] = None
    r"""Fumbles lost per game"""

    ngs_position: Annotated[
        Optional[OffensivePlayerPositionEnum], pydantic.Field(alias="ngsPosition")
    ] = None
    r"""Offensive player position"""

    ngs_position_group: Annotated[
        Optional[OffensivePlayerPositionEnum], pydantic.Field(alias="ngsPositionGroup")
    ] = None
    r"""Offensive player position"""

    position_group: Annotated[
        Optional[OffensivePlayerPositionEnum], pydantic.Field(alias="positionGroup")
    ] = None
    r"""Offensive player position"""

    qr: Optional[bool] = None
    r"""Qualified rusher status"""

    rush10_p_yds: Annotated[Optional[int], pydantic.Field(alias="rush10PYds")] = None
    r"""Rushes of 10+ yards"""

    rush10_p_yds_pg: Annotated[
        Optional[float], pydantic.Field(alias="rush10PYdsPG")
    ] = None
    r"""10+ yard rushes per game"""

    rush15_p_mph: Annotated[Optional[int], pydantic.Field(alias="rush15PMph")] = None
    r"""Rushes of 15+ mph"""

    rush15_p_mph_pg: Annotated[
        Optional[float], pydantic.Field(alias="rush15PMphPG")
    ] = None
    r"""15+ mph rushes per game"""

    rush20_p_mph: Annotated[Optional[int], pydantic.Field(alias="rush20PMph")] = None
    r"""Rushes of 20+ mph"""

    rush20_p_mph_pg: Annotated[
        Optional[float], pydantic.Field(alias="rush20PMphPG")
    ] = None
    r"""20+ mph rushes per game"""

    ryoe: Optional[float] = None
    r"""Rush Yards Over Expected"""

    ryoe_att: Annotated[Optional[float], pydantic.Field(alias="ryoeAtt")] = None
    r"""RYOE per attempt"""

    ryoe_pg: Annotated[Optional[float], pydantic.Field(alias="ryoePG")] = None
    r"""RYOE per game"""

    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    r"""Abbreviated player name"""

    st_box_pct: Annotated[Optional[float], pydantic.Field(alias="stBoxPct")] = None
    r"""Stacked box percentage (0-1)"""

    success: Optional[float] = None
    r"""Success rate (0-1)"""

    td_pg: Annotated[Optional[float], pydantic.Field(alias="tdPG")] = None
    r"""Touchdowns per game"""

    tg: Optional[int] = None
    r"""Team games for player"""

    total_tg: Annotated[Optional[int], pydantic.Field(alias="totalTg")] = None
    r"""Total team games in period"""

    under_pct: Annotated[Optional[float], pydantic.Field(alias="underPct")] = None
    r"""Under center percentage (0-1)"""

    x_ry: Annotated[Optional[float], pydantic.Field(alias="xRy")] = None
    r"""Expected rushing yards"""

    x_ry_pg: Annotated[Optional[float], pydantic.Field(alias="xRyPG")] = None
    r"""Expected rushing yards per game"""

    x_ypc: Annotated[Optional[float], pydantic.Field(alias="xYpc")] = None
    r"""Expected yards per carry"""

    yaco: Optional[float] = None
    r"""Yards after contact"""

    yaco_att: Annotated[Optional[float], pydantic.Field(alias="yacoAtt")] = None
    r"""Yards after contact per attempt"""

    yaco_pg: Annotated[Optional[float], pydantic.Field(alias="yacoPG")] = None
    r"""Yards after contact per game"""

    ybco: Optional[float] = None
    r"""Yards before contact"""

    ybco_pg: Annotated[Optional[float], pydantic.Field(alias="ybcoPG")] = None
    r"""Yards before contact per game"""

    yds_pg: Annotated[Optional[float], pydantic.Field(alias="ydsPG")] = None
    r"""Yards per game"""
