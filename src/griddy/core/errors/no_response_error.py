from dataclasses import dataclass

from griddy.core.exceptions import GriddyError


@dataclass(frozen=True)
class NoResponseError(GriddyError):
    """Error raised when no HTTP response is received from the server.

    Inherits from GriddyError so that catching GriddyError will also
    catch no-response errors.
    """

    message: str

    def __init__(self, message: str = "No response received"):
        object.__setattr__(self, "message", message)
        object.__setattr__(self, "status_code", None)
        object.__setattr__(self, "response_data", {})
        Exception.__init__(self, message)

    def __str__(self):
        return self.message
