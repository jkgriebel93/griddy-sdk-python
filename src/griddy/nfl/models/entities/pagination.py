from __future__ import annotations

from typing import Optional

from ...types import UNSET, BaseModel, OptionalNullable


class Pagination(BaseModel):
    limit: Optional[int] = None
    r"""Maximum items per page"""

    token: OptionalNullable[str] = UNSET
    r"""Token for next page of results"""
