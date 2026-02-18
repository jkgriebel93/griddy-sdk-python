from dataclasses import dataclass
from typing import Optional

import httpx

from griddy.core.errors.sdkerror import SDKError


@dataclass(frozen=True)
class GriddyPFRError(SDKError):
    """The base class for all PFR SDK HTTP error responses."""

    def __init__(
        self, message: str, raw_response: httpx.Response, body: Optional[str] = None
    ):
        super().__init__(message, raw_response, body)
