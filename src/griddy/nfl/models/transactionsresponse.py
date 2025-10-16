from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ..types import BaseModel
from .pagination import Pagination, PaginationTypedDict
from .transaction import Transaction, TransactionTypedDict


class TransactionsResponseTypedDict(TypedDict):
    pagination: NotRequired[PaginationTypedDict]
    transactions: NotRequired[List[TransactionTypedDict]]


class TransactionsResponse(BaseModel):
    pagination: Optional[Pagination] = None

    transactions: Optional[List[Transaction]] = None
