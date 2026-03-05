from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class TeamDefenseStats(BaseModel):
    gp: int
    r"""Games played"""

    pass_: Annotated[int, pydantic.Field(alias="pass")]
    r"""Pass attempts faced"""

    run: int
    r"""Rush attempts faced"""

    team_id: Annotated[str, pydantic.Field(alias="teamId")]
    r"""Team identifier"""

    total: int
    r"""Total defensive plays"""

    yds: int
    r"""Total yards allowed"""

    defensive_touchdown: Annotated[
        Optional[int], pydantic.Field(alias="defensiveTouchdown")
    ] = None
    r"""Defensive touchdowns scored"""

    epa: Optional[float] = None
    r"""Total EPA allowed (negative is better for defense)"""

    epa_pp: Annotated[Optional[float], pydantic.Field(alias="epaPP")] = None
    r"""EPA allowed per play"""

    epa_pass: Annotated[Optional[float], pydantic.Field(alias="epaPass")] = None
    r"""EPA allowed on passing plays"""

    epa_pass_pp: Annotated[Optional[float], pydantic.Field(alias="epaPassPP")] = None
    r"""EPA allowed per pass play"""

    epa_rush: Annotated[Optional[float], pydantic.Field(alias="epaRush")] = None
    r"""EPA allowed on rushing plays"""

    epa_rush_pp: Annotated[Optional[float], pydantic.Field(alias="epaRushPP")] = None
    r"""EPA allowed per rush play"""

    forced_fumble: Annotated[Optional[int], pydantic.Field(alias="forcedFumble")] = None
    r"""Forced fumbles"""

    fumble_recovered: Annotated[
        Optional[int], pydantic.Field(alias="fumbleRecovered")
    ] = None
    r"""Fumble recoveries"""

    interception: Optional[int] = None
    r"""Interceptions"""

    pass_pct: Annotated[Optional[float], pydantic.Field(alias="passPct")] = None
    r"""Percentage of plays that were passes (0-1)"""

    pass_td: Annotated[Optional[int], pydantic.Field(alias="passTd")] = None
    r"""Passing touchdowns allowed"""

    pass_yds: Annotated[Optional[int], pydantic.Field(alias="passYds")] = None
    r"""Passing yards allowed"""

    pass_ypg: Annotated[Optional[float], pydantic.Field(alias="passYpg")] = None
    r"""Pass yards allowed per game"""

    pass_ypp: Annotated[Optional[float], pydantic.Field(alias="passYpp")] = None
    r"""Passing yards allowed per pass attempt"""

    ppg: Optional[float] = None
    r"""Points allowed per game"""

    qbp: Optional[int] = None
    r"""Quarterback pressures generated"""

    qbp_pct: Annotated[Optional[float], pydantic.Field(alias="qbpPct")] = None
    r"""Quarterback pressure rate (0-1)"""

    rush_td: Annotated[Optional[int], pydantic.Field(alias="rushTd")] = None
    r"""Rushing touchdowns allowed"""

    rush_yds: Annotated[Optional[int], pydantic.Field(alias="rushYds")] = None
    r"""Rushing yards allowed"""

    rush_ypg: Annotated[Optional[float], pydantic.Field(alias="rushYpg")] = None
    r"""Rush yards allowed per game"""

    rush_ypp: Annotated[Optional[float], pydantic.Field(alias="rushYpp")] = None
    r"""Rushing yards allowed per rush attempt"""

    ryoe: Optional[float] = None
    r"""Rush Yards Over Expected allowed (negative is better for defense)"""

    sacked_yds: Annotated[Optional[int], pydantic.Field(alias="sackedYds")] = None
    r"""Sack yards generated"""

    sacked_ypg: Annotated[Optional[float], pydantic.Field(alias="sackedYpg")] = None
    r"""Sack yards generated per game"""

    td: Optional[int] = None
    r"""Total touchdowns allowed"""

    total_takeaways: Annotated[
        Optional[int], pydantic.Field(alias="totalTakeaways")
    ] = None
    r"""Total takeaways (interceptions + fumble recoveries)"""

    ttt: Optional[float] = None
    r"""Average time to throw allowed (seconds)"""

    ypg: Optional[float] = None
    r"""Yards allowed per game"""

    ypp: Optional[float] = None
    r"""Yards allowed per play"""
