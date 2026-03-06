from __future__ import annotations

from typing import Optional

from ...types import BaseModel


class Statistic(BaseModel):
    """Named statistic with its value."""

    type: Optional[str] = None
    r"""Statistical category name"""

    value: Optional[float] = None
    r"""Statistical value"""


class StatisticRanking(BaseModel):
    """Player or team ranking for a specific statistic."""

    rank: Optional[int] = None
    r"""Team's rank in this category (1-32)"""

    statistic: Optional[Statistic] = None
