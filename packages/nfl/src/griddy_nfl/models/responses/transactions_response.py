from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from griddy_nfl.models.entities.pagination import Pagination, PaginationTypedDict
from griddy_nfl.models.entities.transaction import Transaction, TransactionTypedDict
from griddy_nfl.types import BaseModel


class TransactionsResponseTypedDict(TypedDict):
    pagination: NotRequired[PaginationTypedDict]
    transactions: NotRequired[List[TransactionTypedDict]]


class TransactionsResponse(BaseModel):
    pagination: Optional[Pagination] = None

    transactions: Optional[List[Transaction]] = None
