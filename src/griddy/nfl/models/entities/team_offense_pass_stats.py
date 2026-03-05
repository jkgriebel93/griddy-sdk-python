from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class TeamOffensePassStats(BaseModel):
    gp: int
    r"""Games played"""

    pass_: Annotated[int, pydantic.Field(alias="pass")]
    r"""Pass attempts (including sacks)"""

    pass_pct: Annotated[float, pydantic.Field(alias="passPct")]
    r"""Percentage of plays that were passes (0-1)"""

    pass_yds: Annotated[int, pydantic.Field(alias="passYds")]
    r"""Passing yards"""

    pass_ypp: Annotated[float, pydantic.Field(alias="passYpp")]
    r"""Passing yards per pass attempt"""

    team_id: Annotated[str, pydantic.Field(alias="teamId")]
    r"""Team identifier"""

    total: int
    r"""Total offensive plays"""

    att: Optional[int] = None
    r"""Pass attempts (not including sacks)"""

    blitz_pct: Annotated[Optional[float], pydantic.Field(alias="blitzPct")] = None
    r"""Blitz percentage faced (0-1)"""

    epa_pass: Annotated[Optional[float], pydantic.Field(alias="epaPass")] = None
    r"""EPA on passing plays (positive is better for offense)"""

    epa_pass_pp: Annotated[Optional[float], pydantic.Field(alias="epaPassPP")] = None
    r"""EPA per pass play"""

    pa_pct: Annotated[Optional[float], pydantic.Field(alias="paPct")] = None
    r"""Play action percentage (0-1)"""

    pass_td: Annotated[Optional[int], pydantic.Field(alias="passTd")] = None
    r"""Passing touchdowns"""

    pass_ypg: Annotated[Optional[float], pydantic.Field(alias="passYpg")] = None
    r"""Pass yards per game"""

    qbp: Optional[int] = None
    r"""Times quarterback was pressured"""

    qbp_pct: Annotated[Optional[float], pydantic.Field(alias="qbpPct")] = None
    r"""Quarterback pressure rate (0-1)"""

    sack: Optional[int] = None
    r"""Sacks taken"""

    sack_pct: Annotated[Optional[float], pydantic.Field(alias="sackPct")] = None
    r"""Sack rate (0-1)"""

    sacked_yds: Annotated[Optional[int], pydantic.Field(alias="sackedYds")] = None
    r"""Sack yards lost"""

    sacked_ypg: Annotated[Optional[float], pydantic.Field(alias="sackedYpg")] = None
    r"""Sack yards lost per game"""

    sep: Optional[float] = None
    r"""Average receiver separation at target (yards)"""

    ttp: Optional[float] = None
    r"""Time to pressure (seconds)"""

    ttt: Optional[float] = None
    r"""Average time to throw (seconds)"""

    yac: Optional[int] = None
    r"""Yards after catch"""

    yacoe: Optional[int] = None
    r"""Yards after catch over expected (positive is better)"""
