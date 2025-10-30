
from __future__ import annotations
from ..types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TeamDefensePassStatsTypedDict(TypedDict):
    gp: int
    r"""Games played"""
    pass_: int
    r"""Pass attempts faced"""
    pass_pct: float
    r"""Percentage of plays that were passes (0-1)"""
    pass_yds: int
    r"""Passing yards allowed"""
    pass_ypp: float
    r"""Passing yards allowed per pass attempt"""
    team_id: str
    r"""Team identifier"""
    total: int
    r"""Total defensive plays"""
    blitz_pct: NotRequired[float]
    r"""Blitz percentage (0-1)"""
    epa_pass: NotRequired[float]
    r"""EPA allowed on passing plays (negative is better for defense)"""
    epa_pass_pp: NotRequired[float]
    r"""EPA allowed per pass play"""
    go: NotRequired[float]
    r"""Get-off metric (coverage disruption)"""
    pass_td: NotRequired[int]
    r"""Passing touchdowns allowed"""
    pass_ypg: NotRequired[float]
    r"""Pass yards allowed per game"""
    qbp: NotRequired[int]
    r"""Quarterback pressures generated"""
    qbp_pct: NotRequired[float]
    r"""Quarterback pressure rate (0-1)"""
    sack: NotRequired[int]
    r"""Sacks"""
    sack_pct: NotRequired[float]
    r"""Sack rate (0-1)"""
    sacked_yds: NotRequired[int]
    r"""Sack yards generated"""
    sacked_ypg: NotRequired[float]
    r"""Sack yards generated per game"""
    sep: NotRequired[float]
    r"""Average receiver separation allowed at target (yards)"""
    ttp: NotRequired[float]
    r"""Time to pressure (seconds)"""
    ttt: NotRequired[float]
    r"""Average time to throw allowed (seconds)"""
    yac: NotRequired[int]
    r"""Yards after catch allowed"""
    yacoe: NotRequired[int]
    r"""Yards after catch over expected allowed (negative is better)"""


class TeamDefensePassStats(BaseModel):
    gp: int
    r"""Games played"""

    pass_: Annotated[int, pydantic.Field(alias="pass")]
    r"""Pass attempts faced"""

    pass_pct: Annotated[float, pydantic.Field(alias="passPct")]
    r"""Percentage of plays that were passes (0-1)"""

    pass_yds: Annotated[int, pydantic.Field(alias="passYds")]
    r"""Passing yards allowed"""

    pass_ypp: Annotated[float, pydantic.Field(alias="passYpp")]
    r"""Passing yards allowed per pass attempt"""

    team_id: Annotated[str, pydantic.Field(alias="teamId")]
    r"""Team identifier"""

    total: int
    r"""Total defensive plays"""

    blitz_pct: Annotated[Optional[float], pydantic.Field(alias="blitzPct")] = None
    r"""Blitz percentage (0-1)"""

    epa_pass: Annotated[Optional[float], pydantic.Field(alias="epaPass")] = None
    r"""EPA allowed on passing plays (negative is better for defense)"""

    epa_pass_pp: Annotated[Optional[float], pydantic.Field(alias="epaPassPP")] = None
    r"""EPA allowed per pass play"""

    go: Optional[float] = None
    r"""Get-off metric (coverage disruption)"""

    pass_td: Annotated[Optional[int], pydantic.Field(alias="passTd")] = None
    r"""Passing touchdowns allowed"""

    pass_ypg: Annotated[Optional[float], pydantic.Field(alias="passYpg")] = None
    r"""Pass yards allowed per game"""

    qbp: Optional[int] = None
    r"""Quarterback pressures generated"""

    qbp_pct: Annotated[Optional[float], pydantic.Field(alias="qbpPct")] = None
    r"""Quarterback pressure rate (0-1)"""

    sack: Optional[int] = None
    r"""Sacks"""

    sack_pct: Annotated[Optional[float], pydantic.Field(alias="sackPct")] = None
    r"""Sack rate (0-1)"""

    sacked_yds: Annotated[Optional[int], pydantic.Field(alias="sackedYds")] = None
    r"""Sack yards generated"""

    sacked_ypg: Annotated[Optional[float], pydantic.Field(alias="sackedYpg")] = None
    r"""Sack yards generated per game"""

    sep: Optional[float] = None
    r"""Average receiver separation allowed at target (yards)"""

    ttp: Optional[float] = None
    r"""Time to pressure (seconds)"""

    ttt: Optional[float] = None
    r"""Average time to throw allowed (seconds)"""

    yac: Optional[int] = None
    r"""Yards after catch allowed"""

    yacoe: Optional[int] = None
    r"""Yards after catch over expected allowed (negative is better)"""
