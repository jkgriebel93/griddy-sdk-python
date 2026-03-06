from __future__ import annotations

from typing import Optional

from ...types import BaseModel


class Record(BaseModel):
    """Win-loss-tie record."""

    losses: Optional[int] = None

    ties: Optional[int] = None

    wins: Optional[int] = None
