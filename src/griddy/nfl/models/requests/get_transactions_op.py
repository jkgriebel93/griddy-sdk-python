from __future__ import annotations

from datetime import date
from typing import Literal, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

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


class GetTransactionsRequestTypedDict(TypedDict):
    month: int
    r"""Month (number) to fetch transactions for"""
    year: int
    r"""Year (all four digits, as int) to fetch transactions for"""
    team_id: str
    r"""Team UUID string"""
    limit: NotRequired[int]
    r"""Maximum number of results"""


class GetTransactionsRequest(BaseModel):
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
