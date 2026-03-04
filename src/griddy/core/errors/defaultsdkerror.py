from dataclasses import dataclass
from typing import Optional

import httpx

from ._formatting import format_error_message
from .sdkerror import SDKError


@dataclass(frozen=True)
class DefaultSDKError(SDKError):
    """The fallback error class if no more specific error class is matched."""

    def __init__(
        self, message: str, raw_response: httpx.Response, body: Optional[str] = None
    ):
        message = format_error_message(message, raw_response, body)
        super().__init__(message, raw_response, body)
