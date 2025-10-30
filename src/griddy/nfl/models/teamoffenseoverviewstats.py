
from __future__ import annotations
from ..types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TeamOffenseOverviewStatsTypedDict(TypedDict):
    gp: int
    r"""Games played"""
    pass_: int
    r"""Pass attempts (including sacks)"""
    run: int
    r"""Rush attempts"""
    team_id: str
    r"""Team identifier"""
    total: int
    r"""Total offensive plays"""
    yds: int
    r"""Total offensive yards"""
    epa: NotRequired[float]
    r"""Total EPA (positive is better for offense)"""
    epa_pp: NotRequired[float]
    r"""EPA per play"""
    epa_pass: NotRequired[float]
    r"""EPA on passing plays"""
    epa_pass_pp: NotRequired[float]
    r"""EPA per pass play"""
    epa_rush: NotRequired[float]
    r"""EPA on rushing plays"""
    epa_rush_pp: NotRequired[float]
    r"""EPA per rush play"""
    pass_pct: NotRequired[float]
    r"""Percentage of plays that were passes (0-1)"""
    pass_td: NotRequired[int]
    r"""Passing touchdowns"""
    pass_yds: NotRequired[int]
    r"""Passing yards"""
    pass_ypg: NotRequired[float]
    r"""Pass yards per game"""
    pass_ypp: NotRequired[float]
    r"""Passing yards per pass attempt"""
    ppg: NotRequired[float]
    r"""Points per game"""
    red_zone_pct: NotRequired[float]
    r"""Red zone touchdown percentage (0-1)"""
    rush_td: NotRequired[int]
    r"""Rushing touchdowns"""
    rush_yds: NotRequired[int]
    r"""Rushing yards"""
    rush_ypg: NotRequired[float]
    r"""Rush yards per game"""
    rush_ypp: NotRequired[float]
    r"""Rushing yards per rush attempt"""
    td: NotRequired[int]
    r"""Total touchdowns"""
    third_down_pct: NotRequired[float]
    r"""Third down conversion percentage (0-1)"""
    to: NotRequired[int]
    r"""Turnovers"""
    ypg: NotRequired[float]
    r"""Yards per game"""
    ypp: NotRequired[float]
    r"""Yards per play"""


class TeamOffenseOverviewStats(BaseModel):
    gp: int
    r"""Games played"""

    pass_: Annotated[int, pydantic.Field(alias="pass")]
    r"""Pass attempts (including sacks)"""

    run: int
    r"""Rush attempts"""

    team_id: Annotated[str, pydantic.Field(alias="teamId")]
    r"""Team identifier"""

    total: int
    r"""Total offensive plays"""

    yds: int
    r"""Total offensive yards"""

    epa: Optional[float] = None
    r"""Total EPA (positive is better for offense)"""

    epa_pp: Annotated[Optional[float], pydantic.Field(alias="epaPP")] = None
    r"""EPA per play"""

    epa_pass: Annotated[Optional[float], pydantic.Field(alias="epaPass")] = None
    r"""EPA on passing plays"""

    epa_pass_pp: Annotated[Optional[float], pydantic.Field(alias="epaPassPP")] = None
    r"""EPA per pass play"""

    epa_rush: Annotated[Optional[float], pydantic.Field(alias="epaRush")] = None
    r"""EPA on rushing plays"""

    epa_rush_pp: Annotated[Optional[float], pydantic.Field(alias="epaRushPP")] = None
    r"""EPA per rush play"""

    pass_pct: Annotated[Optional[float], pydantic.Field(alias="passPct")] = None
    r"""Percentage of plays that were passes (0-1)"""

    pass_td: Annotated[Optional[int], pydantic.Field(alias="passTd")] = None
    r"""Passing touchdowns"""

    pass_yds: Annotated[Optional[int], pydantic.Field(alias="passYds")] = None
    r"""Passing yards"""

    pass_ypg: Annotated[Optional[float], pydantic.Field(alias="passYpg")] = None
    r"""Pass yards per game"""

    pass_ypp: Annotated[Optional[float], pydantic.Field(alias="passYpp")] = None
    r"""Passing yards per pass attempt"""

    ppg: Optional[float] = None
    r"""Points per game"""

    red_zone_pct: Annotated[Optional[float], pydantic.Field(alias="redZonePct")] = None
    r"""Red zone touchdown percentage (0-1)"""

    rush_td: Annotated[Optional[int], pydantic.Field(alias="rushTd")] = None
    r"""Rushing touchdowns"""

    rush_yds: Annotated[Optional[int], pydantic.Field(alias="rushYds")] = None
    r"""Rushing yards"""

    rush_ypg: Annotated[Optional[float], pydantic.Field(alias="rushYpg")] = None
    r"""Rush yards per game"""

    rush_ypp: Annotated[Optional[float], pydantic.Field(alias="rushYpp")] = None
    r"""Rushing yards per rush attempt"""

    td: Optional[int] = None
    r"""Total touchdowns"""

    third_down_pct: Annotated[Optional[float], pydantic.Field(alias="thirdDownPct")] = (
        None
    )
    r"""Third down conversion percentage (0-1)"""

    to: Optional[int] = None
    r"""Turnovers"""

    ypg: Optional[float] = None
    r"""Yards per game"""

    ypp: Optional[float] = None
    r"""Yards per play"""
