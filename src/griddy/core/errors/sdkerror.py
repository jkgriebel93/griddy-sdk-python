from dataclasses import dataclass, field
from typing import Optional

import httpx

from griddy.core.exceptions import APIError


@dataclass(frozen=True)
class SDKError(APIError):
    """The base class for all SDK HTTP error responses.

    Inherits from APIError so that catching GriddyError or APIError
    will also catch internal SDK errors.
    """

    message: str
    status_code: int
    body: str
    headers: httpx.Headers = field(hash=False)
    raw_response: httpx.Response = field(hash=False)

    def __init__(
        self, message: str, raw_response: httpx.Response, body: Optional[str] = None
    ):
        object.__setattr__(self, "message", message)
        object.__setattr__(self, "status_code", raw_response.status_code)
        object.__setattr__(
            self, "body", body if body is not None else raw_response.text
        )
        object.__setattr__(self, "headers", raw_response.headers)
        object.__setattr__(self, "raw_response", raw_response)
        object.__setattr__(self, "response_data", {})
        Exception.__init__(self, message)

    def __str__(self):
        return self.message
