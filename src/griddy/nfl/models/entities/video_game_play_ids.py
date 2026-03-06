from __future__ import annotations

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class VideoGamePlayIds(BaseModel):
    """Game and play identifiers for a video replay."""

    away_team_id: Annotated[str, pydantic.Field(alias="awayTeamId")]
    r"""Away team UUID"""

    game_id: Annotated[str, pydantic.Field(alias="gameId")]
    r"""Game UUID"""

    home_team_id: Annotated[str, pydantic.Field(alias="homeTeamId")]
    r"""Home team UUID"""

    play_id: Annotated[str, pydantic.Field(alias="playId")]
    r"""Play identifier"""
