from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class PlayStat(BaseModel):
    """Individual statistic recorded on a play."""

    club_code: Annotated[str, pydantic.Field(alias="clubCode")]
    r"""Team abbreviation"""

    play_id: Annotated[int, pydantic.Field(alias="playId")]

    stat_id: Annotated[int, pydantic.Field(alias="statId")]
    r"""Type of statistic"""

    yards: int
    r"""Yards gained/lost"""

    gsis_id: Annotated[Optional[str], pydantic.Field(alias="gsisId")] = None
    r"""Player GSIS ID. Absent on team-level stats."""

    player_name: Annotated[Optional[str], pydantic.Field(alias="playerName")] = None
    r"""Player name. Absent on team-level stats."""
