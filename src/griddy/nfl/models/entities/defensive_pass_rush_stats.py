from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.enums.position_enums import (
    DefenseNGSPositionEnum,
    DefenseNGSPositionGroupEnum,
    DefensePositionEnum,
    DefensePositionGroupEnum,
)
from griddy.nfl.types import BaseModel


class DefensivePassRushStats(BaseModel):
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

    pr: int
    r"""Pass rush grade/rating"""

    pr_r: Annotated[float, pydantic.Field(alias="prR")]
    r"""Pass rush rate (0-1)"""

    qbp: int
    r"""Quarterback pressures"""

    qbp_r: Annotated[float, pydantic.Field(alias="qbpR")]
    r"""Quarterback pressure rate (0-1)"""

    sack: float
    r"""Sacks (can be fractional for shared sacks)"""

    sack_r: Annotated[float, pydantic.Field(alias="sackR")]
    r"""Sack rate (0-1)"""

    team_id: Annotated[str, pydantic.Field(alias="teamId")]
    r"""Team identifier"""

    game_snap: Annotated[Optional[int], pydantic.Field(alias="gameSnap")] = None
    r"""Defensive snaps played"""

    headshot: Optional[str] = None
    r"""URL to player headshot image (contains formatInstructions placeholder)"""

    jersey_number: Annotated[Optional[int], pydantic.Field(alias="jerseyNumber")] = None
    r"""Player's jersey number"""

    ngs_position: Annotated[
        Optional[DefenseNGSPositionEnum], pydantic.Field(alias="ngsPosition")
    ] = None
    r"""Next Gen Stats position"""

    ngs_position_group: Annotated[
        Optional[DefenseNGSPositionGroupEnum], pydantic.Field(alias="ngsPositionGroup")
    ] = None
    r"""Defensive position group"""

    position_group: Annotated[
        Optional[DefensePositionGroupEnum], pydantic.Field(alias="positionGroup")
    ] = None
    r"""Defensive position group"""

    pr_go: Annotated[Optional[float], pydantic.Field(alias="prGo")] = None
    r"""Pass rush get-off metric"""

    qd: Optional[bool] = None
    r"""Qualified defender status"""

    qp: Optional[int] = None
    r"""Quarterback hits"""

    short_name: Annotated[Optional[str], pydantic.Field(alias="shortName")] = None
    r"""Abbreviated player name"""

    team_snap: Annotated[Optional[int], pydantic.Field(alias="teamSnap")] = None
    r"""Total team defensive snaps"""

    tg: Optional[int] = None
    r"""Team games for player"""

    total_tg: Annotated[Optional[int], pydantic.Field(alias="totalTg")] = None
    r"""Total team games in period"""

    ttp: Optional[float] = None
    r"""Time to pressure (seconds)"""

    tts: Optional[float] = None
    r"""Time to sack (seconds)"""

    turn_qbp: Annotated[Optional[int], pydantic.Field(alias="turnQbp")] = None
    r"""Quarterback pressures that resulted in turnovers"""
