from __future__ import annotations

from datetime import datetime
from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel
from .moneyline import MoneyLine
from .point_spread import PointSpread
from .totals import Totals


class GameOdds(BaseModel):
    """Betting odds for a game including spread and over/under."""

    game_id: Annotated[Optional[int], pydantic.Field(alias="gameId")] = None
    r"""Game identifier (10-digit format YYYYMMDDNN)"""

    game_key: Annotated[Optional[int], pydantic.Field(alias="gameKey")] = None
    r"""Unique game key identifier"""

    home_team_abbr: Annotated[Optional[str], pydantic.Field(alias="homeTeamAbbr")] = (
        None
    )
    r"""Home team abbreviation"""

    home_team_id: Annotated[Optional[str], pydantic.Field(alias="homeTeamId")] = None
    r"""Home team identifier"""

    moneyline: Optional[MoneyLine] = None
    r"""Money line betting odds"""

    spread: Optional[PointSpread] = None
    r"""Point spread betting odds"""

    totals: Optional[Totals] = None
    r"""Over/Under (totals) betting odds"""

    updated_at: Annotated[Optional[datetime], pydantic.Field(alias="updatedAt")] = None
    r"""Timestamp of last odds update"""

    visitor_team_abbr: Annotated[
        Optional[str], pydantic.Field(alias="visitorTeamAbbr")
    ] = None
    r"""Visitor team abbreviation"""

    visitor_team_id: Annotated[Optional[str], pydantic.Field(alias="visitorTeamId")] = (
        None
    )
    r"""Visitor team identifier"""
