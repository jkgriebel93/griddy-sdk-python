from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ...types import BaseModel


class TeamDefenseRushStatsTypedDict(TypedDict):
    gp: int
    r"""Games played"""
    run: int
    r"""Rush attempts faced"""
    run_pct: float
    r"""Percentage of plays that were rushes (0-1)"""
    rush_yds: int
    r"""Rushing yards allowed"""
    rush_ypp: float
    r"""Rushing yards allowed per rush attempt"""
    team_id: str
    r"""Team identifier"""
    total: int
    r"""Total defensive plays"""
    epa_rush: NotRequired[float]
    r"""EPA allowed on rushing plays (negative is better for defense)"""
    epa_rush_pp: NotRequired[float]
    r"""EPA allowed per rush play"""
    in_pct: NotRequired[float]
    r"""Percentage of rushes between tackles (inside)"""
    light_pct: NotRequired[float]
    r"""Percentage of rushes against light box (6 or fewer defenders)"""
    out_pct: NotRequired[float]
    r"""Percentage of rushes outside tackles"""
    rush10_p_yds: NotRequired[int]
    r"""Rush attempts of 10+ yards allowed"""
    rush_td: NotRequired[int]
    r"""Rushing touchdowns allowed"""
    rush_ypg: NotRequired[float]
    r"""Rush yards allowed per game"""
    ryoe: NotRequired[float]
    r"""Rush Yards Over Expected allowed (negative is better)"""
    ryoe_att: NotRequired[float]
    r"""RYOE per rush attempt"""
    stacked_pct: NotRequired[float]
    r"""Percentage of rushes against stacked box (8+ defenders)"""
    stuff_pct: NotRequired[float]
    r"""Stuff rate - percentage of rushes stopped for 0 or negative yards"""
    yaco_att: NotRequired[float]
    r"""Yards after contact per attempt allowed"""
    ybco_att: NotRequired[float]
    r"""Yards before contact per attempt allowed"""


class TeamDefenseRushStats(BaseModel):
    gp: int
    r"""Games played"""

    run: int
    r"""Rush attempts faced"""

    run_pct: Annotated[float, pydantic.Field(alias="runPct")]
    r"""Percentage of plays that were rushes (0-1)"""

    rush_yds: Annotated[int, pydantic.Field(alias="rushYds")]
    r"""Rushing yards allowed"""

    rush_ypp: Annotated[float, pydantic.Field(alias="rushYpp")]
    r"""Rushing yards allowed per rush attempt"""

    team_id: Annotated[str, pydantic.Field(alias="teamId")]
    r"""Team identifier"""

    total: int
    r"""Total defensive plays"""

    epa_rush: Annotated[Optional[float], pydantic.Field(alias="epaRush")] = None
    r"""EPA allowed on rushing plays (negative is better for defense)"""

    epa_rush_pp: Annotated[Optional[float], pydantic.Field(alias="epaRushPP")] = None
    r"""EPA allowed per rush play"""

    in_pct: Annotated[Optional[float], pydantic.Field(alias="inPct")] = None
    r"""Percentage of rushes between tackles (inside)"""

    light_pct: Annotated[Optional[float], pydantic.Field(alias="lightPct")] = None
    r"""Percentage of rushes against light box (6 or fewer defenders)"""

    out_pct: Annotated[Optional[float], pydantic.Field(alias="outPct")] = None
    r"""Percentage of rushes outside tackles"""

    rush10_p_yds: Annotated[Optional[int], pydantic.Field(alias="rush10PYds")] = None
    r"""Rush attempts of 10+ yards allowed"""

    rush_td: Annotated[Optional[int], pydantic.Field(alias="rushTd")] = None
    r"""Rushing touchdowns allowed"""

    rush_ypg: Annotated[Optional[float], pydantic.Field(alias="rushYpg")] = None
    r"""Rush yards allowed per game"""

    ryoe: Optional[float] = None
    r"""Rush Yards Over Expected allowed (negative is better)"""

    ryoe_att: Annotated[Optional[float], pydantic.Field(alias="ryoeAtt")] = None
    r"""RYOE per rush attempt"""

    stacked_pct: Annotated[Optional[float], pydantic.Field(alias="stackedPct")] = None
    r"""Percentage of rushes against stacked box (8+ defenders)"""

    stuff_pct: Annotated[Optional[float], pydantic.Field(alias="stuffPct")] = None
    r"""Stuff rate - percentage of rushes stopped for 0 or negative yards"""

    yaco_att: Annotated[Optional[float], pydantic.Field(alias="yacoAtt")] = None
    r"""Yards after contact per attempt allowed"""

    ybco_att: Annotated[Optional[float], pydantic.Field(alias="ybcoAtt")] = None
    r"""Yards before contact per attempt allowed"""
