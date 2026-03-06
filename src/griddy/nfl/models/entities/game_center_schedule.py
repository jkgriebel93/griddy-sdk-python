from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.utils.unmarshal_json_response import int_to_str

from ...types import BaseModel


class GamecenterSchedule(BaseModel):
    """Game schedule entry for the NFL Game Center."""

    game_date: Annotated[Optional[str], pydantic.Field(alias="gameDate")] = None

    game_id: Annotated[
        Optional[str],
        pydantic.Field(alias="gameId"),
        pydantic.BeforeValidator(int_to_str),
    ] = None

    game_key: Annotated[Optional[int], pydantic.Field(alias="gameKey")] = None

    game_time_eastern: Annotated[
        Optional[str], pydantic.Field(alias="gameTimeEastern")
    ] = None

    home_team_abbr: Annotated[Optional[str], pydantic.Field(alias="homeTeamAbbr")] = (
        None
    )

    home_team_id: Annotated[Optional[str], pydantic.Field(alias="homeTeamId")] = None

    season: Optional[int] = None

    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None

    visitor_team_abbr: Annotated[
        Optional[str], pydantic.Field(alias="visitorTeamAbbr")
    ] = None

    visitor_team_id: Annotated[Optional[str], pydantic.Field(alias="visitorTeamId")] = (
        None
    )

    week: Optional[int] = None
