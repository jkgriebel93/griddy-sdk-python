from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.enums.position_enums import (
    DefenseNGSPositionEnum,
    DefenseNGSPositionGroupEnum,
    DefensePositionEnum,
    DefensePositionGroupEnum,
)

from ..types import BaseModel


class DefensiveNearestDefenderStatsTypedDict(TypedDict):
    cov: int
    r"""Total coverage snaps"""
    cov_nd: int
    r"""Coverage snaps (no data excluded)"""
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
    team_id: str
    r"""Team identifier"""
    bh_pct: NotRequired[float]
    r"""Burn percentage (deep completions allowed rate)"""
    catch_nd: NotRequired[float]
    r"""Catch rate allowed (0-1)"""
    croe_nd: NotRequired[float]
    r"""Completion Rate Over Expected allowed"""
    game_snap: NotRequired[int]
    r"""Defensive snaps played"""
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
    r"""Passer rating allowed when targeted"""
    position_group: NotRequired[DefensePositionGroupEnum]
    r"""Defensive position group"""
    qd: NotRequired[bool]
    r"""Qualified defender status"""
    rec_nd: NotRequired[int]
    r"""Receptions allowed"""
    rec_td_nd: NotRequired[int]
    r"""Receiving touchdowns allowed"""
    rec_yds_nd: NotRequired[int]
    r"""Receiving yards allowed"""
    sep: NotRequired[float]
    r"""Average separation allowed at target (yards)"""
    short_name: NotRequired[str]
    r"""Abbreviated player name"""
    team_snap: NotRequired[int]
    r"""Total team defensive snaps"""
    tg: NotRequired[int]
    r"""Team games for player"""
    tgt_epa_nd: NotRequired[float]
    r"""Target EPA (Expected Points Added) allowed"""
    tgt_nd: NotRequired[int]
    r"""Times targeted in coverage"""
    tgt_r_nd: NotRequired[float]
    r"""Target rate (targets per coverage snap)"""
    total_tg: NotRequired[int]
    r"""Total team games in period"""
    twf_pct: NotRequired[float]
    r"""Tight window frequency (percentage of targets in tight windows)"""
    yacpr_nd: NotRequired[float]
    r"""Yards After Catch allowed per reception"""


class DefensiveNearestDefenderStats(BaseModel):
    cov: int
    r"""Total coverage snaps"""

    cov_nd: Annotated[int, pydantic.Field(alias="covNd")]
    r"""Coverage snaps (no data excluded)"""

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

    team_id: Annotated[str, pydantic.Field(alias="teamId")]
    r"""Team identifier"""

    bh_pct: Annotated[Optional[float], pydantic.Field(alias="bhPct")] = None
    r"""Burn percentage (deep completions allowed rate)"""

    catch_nd: Annotated[Optional[float], pydantic.Field(alias="catchNd")] = None
    r"""Catch rate allowed (0-1)"""

    croe_nd: Annotated[Optional[float], pydantic.Field(alias="croeNd")] = None
    r"""Completion Rate Over Expected allowed"""

    game_snap: Annotated[Optional[int], pydantic.Field(alias="gameSnap")] = None
    r"""Defensive snaps played"""

    headshot: Optional[str] = None
    r"""URL to player headshot image (contains formatInstructions placeholder)"""

    int_: Annotated[Optional[int], pydantic.Field(alias="int")] = None
    r"""Interceptions"""

    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    r"""Player's jersey number"""

    ngs_position: Annotated[
        Optional[DefenseNGSPositionEnum], pydantic.Field(alias="ngsPosition")
    ] = None
    r"""Next Gen Stats position"""

    ngs_position_group: Annotated[
        Optional[DefensePositionGroupEnum], pydantic.Field(alias="ngsPositionGroup")
    ] = None
    r"""Defensive position group"""

    pass_rating_nd: Annotated[Optional[float], pydantic.Field(alias="passRatingNd")] = (
        None
    )
    r"""Passer rating allowed when targeted"""

    position_group: Annotated[
        Optional[DefensePositionGroupEnum], pydantic.Field(alias="positionGroup")
    ] = None
    r"""Defensive position group"""

    qd: Optional[bool] = None
    r"""Qualified defender status"""

    rec_nd: Annotated[Optional[int], pydantic.Field(alias="recNd")] = None
    r"""Receptions allowed"""

    rec_td_nd: Annotated[Optional[int], pydantic.Field(alias="recTdNd")] = None
    r"""Receiving touchdowns allowed"""

    rec_yds_nd: Annotated[Optional[int], pydantic.Field(alias="recYdsNd")] = None
    r"""Receiving yards allowed"""

    sep: Optional[float] = None
    r"""Average separation allowed at target (yards)"""

    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    r"""Abbreviated player name"""

    team_snap: Annotated[Optional[int], pydantic.Field(alias="teamSnap")] = None
    r"""Total team defensive snaps"""

    tg: Optional[int] = None
    r"""Team games for player"""

    tgt_epa_nd: Annotated[Optional[float], pydantic.Field(alias="tgtEpaNd")] = None
    r"""Target EPA (Expected Points Added) allowed"""

    tgt_nd: Annotated[Optional[int], pydantic.Field(alias="tgtNd")] = None
    r"""Times targeted in coverage"""

    tgt_r_nd: Annotated[Optional[float], pydantic.Field(alias="tgtRNd")] = None
    r"""Target rate (targets per coverage snap)"""

    total_tg: Annotated[Optional[int], pydantic.Field(alias="totalTg")] = None
    r"""Total team games in period"""

    twf_pct: Annotated[Optional[float], pydantic.Field(alias="twfPct")] = None
    r"""Tight window frequency (percentage of targets in tight windows)"""

    yacpr_nd: Annotated[Optional[float], pydantic.Field(alias="yacprNd")] = None
    r"""Yards After Catch allowed per reception"""
