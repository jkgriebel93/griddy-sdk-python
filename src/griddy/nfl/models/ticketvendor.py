from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel


class TicketVendorTypedDict(TypedDict):
    ticket_url: NotRequired[str]
    r"""Vendor-specific ticket URL"""
    vendor_name: NotRequired[str]
    r"""Vendor identifier"""


class TicketVendor(BaseModel):
    ticket_url: Annotated[Optional[str], pydantic.Field(alias="ticketUrl")] = None
    r"""Vendor-specific ticket URL"""

    vendor_name: Annotated[Optional[str], pydantic.Field(alias="vendorName")] = None
    r"""Vendor identifier"""
