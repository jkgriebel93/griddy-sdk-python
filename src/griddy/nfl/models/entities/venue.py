from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import UNSET, BaseModel, OptionalNullable


class Venue(BaseModel):
    address: OptionalNullable[str] = UNSET
    r"""Street address"""

    city: Optional[str] = None
    r"""City name"""

    country: Optional[str] = None
    r"""Country name"""

    id: Optional[str] = None
    r"""Unique venue identifier"""

    name: Optional[str] = None
    r"""Venue name"""

    postal_code: Annotated[
        OptionalNullable[str], pydantic.Field(alias="postalCode")
    ] = UNSET
    r"""Postal/ZIP code"""

    territory: OptionalNullable[str] = UNSET
    r"""State or territory code"""
