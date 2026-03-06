from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class TicketVendor(BaseModel):
    """Ticket vendor information for a game."""

    ticket_url: Annotated[Optional[str], pydantic.Field(alias="ticketUrl")] = None
    r"""Vendor-specific ticket URL"""

    vendor_name: Annotated[Optional[str], pydantic.Field(alias="vendorName")] = None
    r"""Vendor identifier"""
