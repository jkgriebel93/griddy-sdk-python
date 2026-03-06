from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class ContractInfo(BaseModel):
    """Player contract details."""

    expiration_year: Annotated[
        Optional[int], pydantic.Field(alias="expirationYear")
    ] = None
    r"""Contract expiration year"""

    guaranteed: Optional[float] = None
    r"""Guaranteed money"""

    signing_bonus: Annotated[Optional[float], pydantic.Field(alias="signingBonus")] = (
        None
    )
    r"""Signing bonus"""

    total_value: Annotated[Optional[float], pydantic.Field(alias="totalValue")] = None
    r"""Total contract value"""

    years: Optional[int] = None
    r"""Contract length in years"""
