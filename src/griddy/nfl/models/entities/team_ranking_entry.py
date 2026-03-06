from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class TeamRankingEntry(BaseModel):
    """Team ranking entry for a statistical category."""

    rank: Optional[int] = None
    r"""Team's rank (1-32)"""

    stats: Optional[float] = None
    r"""Statistical value"""

    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
