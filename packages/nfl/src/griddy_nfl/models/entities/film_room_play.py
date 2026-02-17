from __future__ import annotations

from typing import Any, Dict, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.enums.play_type_enum import PlayTypeEnum
from griddy_nfl.models.enums.season_type_enum import SeasonTypeEnum

from ...types import BaseModel


class FilmroomPlayTypedDict(TypedDict):
    defense_team_id: str
    r"""Defensive team identifier"""
    down: int
    r"""Down number"""
    fapi_game_id: str
    r"""Football API game identifier"""
    game_clock: str
    r"""Game clock time when play occurred"""
    game_id: int
    r"""Game identifier (10-digit format YYYYMMDDNN)"""
    home_team_abbr: str
    r"""Home team abbreviation"""
    home_team_id: str
    r"""Home team identifier"""
    play_description: str
    r"""Detailed description of the play"""
    play_id: int
    r"""Unique play identifier within the game"""
    play_type: PlayTypeEnum
    r"""Enumeration of all possible play types"""
    possession_team_id: str
    r"""Team with possession of the ball"""
    quarter: int
    r"""Quarter of the play"""
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of NFL season"""
    sequence: int
    r"""Play sequence number"""
    visitor_team_abbr: str
    r"""Visiting team abbreviation"""
    visitor_team_id: str
    r"""Visiting team identifier"""
    week: int
    r"""Week number"""
    week_slug: str
    r"""Week identifier slug"""
    yardline: str
    r"""Field position where play occurred"""
    yards_to_go: int
    r"""Yards needed for first down"""
    selected_param_values: NotRequired[Dict[str, Any]]
    r"""Selected parameter values for the play filter"""


class FilmroomPlay(BaseModel):
    defense_team_id: Annotated[str, pydantic.Field(alias="defenseTeamId")]
    r"""Defensive team identifier"""

    down: int
    r"""Down number"""

    fapi_game_id: Annotated[str, pydantic.Field(alias="fapiGameId")]
    r"""Football API game identifier"""

    game_clock: Annotated[str, pydantic.Field(alias="gameClock")]
    r"""Game clock time when play occurred"""

    game_id: Annotated[int, pydantic.Field(alias="gameId")]
    r"""Game identifier (10-digit format YYYYMMDDNN)"""

    home_team_abbr: Annotated[str, pydantic.Field(alias="homeTeamAbbr")]
    r"""Home team abbreviation"""

    home_team_id: Annotated[str, pydantic.Field(alias="homeTeamId")]
    r"""Home team identifier"""

    play_description: Annotated[str, pydantic.Field(alias="playDescription")]
    r"""Detailed description of the play"""

    play_id: Annotated[int, pydantic.Field(alias="playId")]
    r"""Unique play identifier within the game"""

    play_type: Annotated[PlayTypeEnum, pydantic.Field(alias="playType")]
    r"""Enumeration of all possible play types"""

    possession_team_id: Annotated[str, pydantic.Field(alias="possessionTeamId")]
    r"""Team with possession of the ball"""

    quarter: int
    r"""Quarter of the play"""

    season: int
    r"""Season year"""

    season_type: Annotated[SeasonTypeEnum, pydantic.Field(alias="seasonType")]
    r"""Type of NFL season"""

    sequence: int
    r"""Play sequence number"""

    visitor_team_abbr: Annotated[str, pydantic.Field(alias="visitorTeamAbbr")]
    r"""Visiting team abbreviation"""

    visitor_team_id: Annotated[str, pydantic.Field(alias="visitorTeamId")]
    r"""Visiting team identifier"""

    week: int
    r"""Week number"""

    week_slug: Annotated[str, pydantic.Field(alias="weekSlug")]
    r"""Week identifier slug"""

    yardline: str
    r"""Field position where play occurred"""

    yards_to_go: Annotated[int, pydantic.Field(alias="yardsToGo")]
    r"""Yards needed for first down"""

    selected_param_values: Annotated[
        Optional[Dict[str, Any]], pydantic.Field(alias="selectedParamValues")
    ] = None
    r"""Selected parameter values for the play filter"""
