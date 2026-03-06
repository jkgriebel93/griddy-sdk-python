from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class Content(BaseModel):
    r"""Insight content and analysis"""


class GameInsight(BaseModel):
    """Pre-game or in-game insight and analysis."""

    content: Optional[Content] = None
    r"""Insight content and analysis"""

    game_id: Annotated[Optional[str], pydantic.Field(alias="gameId")] = None
    r"""Game identifier"""

    id: Optional[str] = None
    r"""Insight identifier"""

    type: Optional[str] = None
    r"""Type of insight"""
