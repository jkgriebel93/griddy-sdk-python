from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from ...types import UNSET, BaseModel, OptionalNullable
from .team_ranking_entry import TeamRankingEntry


class MultipleRankingsCategoryPagination(BaseModel):
    """Pagination details for multiple rankings queries."""

    limit: Optional[int] = None

    token: OptionalNullable[str] = UNSET


class MultipleRankingsCategory(BaseModel):
    """Category grouping for multiple team or player rankings."""

    pagination: Optional[MultipleRankingsCategoryPagination] = None

    stat_category: Annotated[Optional[str], pydantic.Field(alias="statCategory")] = None
    r"""Category of statistic"""

    stat_name: Annotated[Optional[str], pydantic.Field(alias="statName")] = None
    r"""Name of specific statistic"""

    teams: Optional[List[TeamRankingEntry]] = None
