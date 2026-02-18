from typing import Any, Optional, Type

import httpx

from .serializers import unmarshal_json


def unmarshal_json_response(
    typ: Any,
    http_res: httpx.Response,
    validation_error_cls: Optional[Type[Exception]] = None,
    body: Optional[str] = None,
) -> Any:
    """Unmarshal a JSON HTTP response into the given type.

    Args:
        typ: The Pydantic model type to unmarshal into.
        http_res: The HTTP response.
        validation_error_cls: Optional error class to raise on validation failure.
            Must accept (message, raw_response, cause, body) constructor args.
            If None, the raw Pydantic ValidationError is re-raised.
        body: Optional pre-read body text.
    """
    if body is None:
        body = http_res.text
    try:
        return unmarshal_json(body, typ)
    except Exception as e:
        if validation_error_cls is not None:
            raise validation_error_cls(
                "Response validation failed",
                http_res,
                e,
                body,
            ) from e
        raise
