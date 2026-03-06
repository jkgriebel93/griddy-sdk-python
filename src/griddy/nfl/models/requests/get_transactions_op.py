from __future__ import annotations

from typing import Literal, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata

GetTransactionsTransactionType = Literal[
    "TRADE",
    "SIGNED",
    "RELEASED",
    "WAIVED",
    "PRACTICE_SQUAD",
    "IR",
    "SUSPENDED",
]
r"""Type of transaction"""


class GetTransactionsRequest(BaseModel):
    """Request parameters for fetching player transactions."""

    month: Annotated[
        int,
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Month (number) to fetch transactions for"""
    year: Annotated[
        int,
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Year (all four digits, as int) to fetch transactions for"""
    team_id: Annotated[
        str,
        pydantic.Field(alias="teamId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Team UUID string"""
    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 20
    r"""Maximum number of results"""
