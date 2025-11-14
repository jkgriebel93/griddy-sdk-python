from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel


class TeamOffenseRushStatsTypedDict(TypedDict):
    gp: int
    r"""Games played"""
    total: int
    r"""Total offensive plays"""
    run: int
    r"""Count of run plays"""
    run_pct: float
    r"""Percentage of all plays that are runs"""
    rush_td: int
    r"""Rushing touchdowns"""
    rush_yds: int
    r"""Total rushing yards"""
    rush_yds_per_play: float
    r"""Rush yards per play"""
    rush_epa_total: float
    r"""Total expected points added by rushing"""
    rush_epa_per_play: float
    r"""Expected points added per rushing play"""
    rush_ten_yds_plus: int
    r"""Rushing plays of 10+ yards"""
    rush_success_pct: float
    r"""Team rushing success rate"""
    stuff_pct: float
    r"""Team rushing stuff rate"""
    ryoe: float
    r"""Rushing yards over expected"""
    ryoe_att: float
    r"""Rushing yards over expected per rush"""
    ybco_att: float
    r"""Rush yards before contact per attempt"""
    yaco_att: float
    r"""Rush yards after contact per play"""
    in_pct: float
    r"""Inside tackles rush pct"""
    out_pct: float
    r"""Outside tackles rush pct"""
    light_pct: float
    r"""Opponent light box pct"""
    stacked_pct: float
    r"""Opponent stacked box pct"""
    rush_ypg: float
    r"""Team rushing yards per game"""
    team_id: str
    r"""Team identifier"""


class TeamOffenseRushStats(BaseModel):
    gp: int
    r"""Games played"""
    total: int
    r"""Total offensive plays"""
    run: int
    r"""Count of run plays"""
    run_pct: Annotated[float, pydantic.Field(alias="runPct")]
    r"""Percentage of all plays that are runs"""
    rush_td: Annotated[int, pydantic.Field(alias="rushTd")]
    r"""Rushing touchdowns"""
    rush_yds: Annotated[int, pydantic.Field(alias="rushYds")]
    r"""Total rushing yards"""
    rush_yds_per_play: Annotated[float, pydantic.Field(alias="rushYpp")]
    r"""Rush yards per play"""
    rush_epa_total: Annotated[float, pydantic.Field(alias="epaRush")]
    r"""Total expected points added by rushing"""
    rush_epa_per_play: Annotated[float, pydantic.Field(alias="epaRushPP")]
    r"""Expected points added per rushing play"""
    rush_ten_yds_plus: Annotated[int, pydantic.Field(alias="rush10PYds")]
    r"""Rushing plays of 10+ yards"""
    rush_success_pct: Annotated[float, pydantic.Field(alias="rushSuccessPct")]
    r"""Team rushing success rate"""
    stuff_pct: Annotated[float, pydantic.Field(alias="stuffPct")]
    r"""Team rushing stuff rate"""
    ryoe: Annotated[float, pydantic.Field(alias="ryoe")]
    r"""Rushing yards over expected"""
    ryoe_att: Annotated[float, pydantic.Field(alias="ryoeAtt")]
    r"""Rushing yards over expected per rush"""
    ybco_att: Annotated[float, pydantic.Field(alias="ybcoAtt")]
    r"""Rush yards before contact per attempt"""
    yaco_att: Annotated[float, pydantic.Field(alias="yacoAtt")]
    r"""Rush yards after contact per play"""
    in_pct: Annotated[float, pydantic.Field(alias="inPct")]
    r"""Inside tackles rush pct"""
    out_pct: Annotated[float, pydantic.Field(alias="outPct")]
    r"""Outside tackles rush pct"""
    light_pct: Annotated[float, pydantic.Field(alias="lightPct")]
    r"""Opponent light box pct"""
    stacked_pct: Annotated[float, pydantic.Field(alias="stackedPct")]
    r"""Opponent stacked box pct"""
    rush_ypg: Annotated[float, pydantic.Field(alias="rushYpg")]
    r"""Team rushing yards per game"""
    team_id: Annotated[str, pydantic.Field(alias="teamId")]
    r"""Team identifier"""
