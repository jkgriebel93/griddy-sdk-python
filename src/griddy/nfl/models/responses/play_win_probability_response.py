from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.play_win_probability import PlayWinProbability
from griddy.nfl.types import BaseModel
from griddy.nfl.utils.unmarshal_json_response import int_to_str


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
