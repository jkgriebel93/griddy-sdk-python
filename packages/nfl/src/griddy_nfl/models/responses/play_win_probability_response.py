from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.entities.play_win_probability import (
    PlayWinProbability,
    PlayWinProbabilityTypedDict,
)
from griddy_nfl.types import BaseModel
from griddy_nfl.utils.unmarshal_json_response import int_to_str


class PlayWinProbabilityResponseTypedDict(TypedDict):
    game_id: str
    r"""Ten digit game ID"""
    game_key: int
    r"""Another ID looking value, not sure what it is."""
    pregame_away_team_win_probability: float
    r"""As determined before kickoff, the probability (0 < p < 1), the away team wins"""
    pregame_home_team_wint_probability: float
    r"""As determined before kickoff, the probability (0 < p < 1), the home team wins"""
    plays: List[PlayWinProbabilityTypedDict]


class PlayWinProbabilityResponse(BaseModel):
    game_id: Annotated[
        Optional[str],
        pydantic.Field(alias="gameId"),
        pydantic.BeforeValidator(int_to_str),
    ] = None
    game_key: Annotated[Optional[int], pydantic.Field(alias="gameKey")] = None
    pregame_away_team_win_probability: Annotated[
        float, pydantic.Field(alias="pregameAwayTeamWinProbability")
    ]
    pregame_home_team_win_probability: Annotated[
        float, pydantic.Field(alias="pregameHomeTeamWinProbability")
    ]
    plays: List[PlayWinProbability]
