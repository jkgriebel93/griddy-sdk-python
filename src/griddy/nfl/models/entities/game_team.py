from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class Score(BaseModel):
    """Quarterly score breakdown for a team."""

    total: Optional[str] = None
    r"""Total score (empty string for future games)"""


class GameTeam(BaseModel):
    """Team entry within a game with score and record."""

    current_logo: Annotated[Optional[str], pydantic.Field(alias="currentLogo")] = None
    r"""URL to team logo (may contain formatInstructions placeholder)"""

    full_name: Annotated[Optional[str], pydantic.Field(alias="fullName")] = None

    id: Optional[str] = None

    score: Optional[Score] = None

    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
