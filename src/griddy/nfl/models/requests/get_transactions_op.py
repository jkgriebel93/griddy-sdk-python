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
    start_date: NotRequired[date]
    r"""Start date for transactions (ISO 8601)"""
    end_date: NotRequired[date]
    r"""End date for transactions (ISO 8601)"""
    team_id: NotRequired[str]
    r"""Filter by team"""
    transaction_type: NotRequired[GetTransactionsTransactionType]
    r"""Type of transaction"""
    limit: NotRequired[int]
    r"""Maximum number of results"""


class GetTransactionsRequest(BaseModel):
    start_date: Annotated[
        Optional[date],
        pydantic.Field(alias="startDate"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Start date for transactions (ISO 8601)"""

    end_date: Annotated[
        Optional[date],
        pydantic.Field(alias="endDate"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""End date for transactions (ISO 8601)"""

    team_id: Annotated[
        Optional[str],
        pydantic.Field(alias="teamId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by team"""

    transaction_type: Annotated[
        Optional[GetTransactionsTransactionType],
        pydantic.Field(alias="transactionType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Type of transaction"""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 20
    r"""Maximum number of results"""
