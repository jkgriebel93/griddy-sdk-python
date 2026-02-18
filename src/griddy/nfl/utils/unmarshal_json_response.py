from typing import Any, Optional

import httpx

from griddy.core.utils.unmarshal_json_response import (
    unmarshal_json_response as _core_unmarshal,
)

from .. import errors


def int_to_str(value):
    if isinstance(value, int):
        return str(value)
    return value


def unmarshal_json_response(
    typ: Any, http_res: httpx.Response, body: Optional[str] = None
) -> Any:
    return _core_unmarshal(
        typ, http_res, validation_error_cls=errors.ResponseValidationError, body=body
    )
