from __future__ import annotations

from typing import List, Optional

from griddy.nfl.models.entities.pagination import Pagination
from griddy.nfl.models.entities.transaction import Transaction
from griddy.nfl.types import BaseModel


class TransactionsResponse(BaseModel):
    pagination: Optional[Pagination] = None

    transactions: Optional[List[Transaction]] = None
