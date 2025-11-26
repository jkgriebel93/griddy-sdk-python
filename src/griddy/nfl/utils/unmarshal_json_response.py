from typing import Any, Optional

import httpx

from .. import errors
from .serializers import unmarshal_json


def int_to_str(value):
    if isinstance(value, int):
        return str(value)
    return value


def unmarshal_json_response(
    typ: Any, http_res: httpx.Response, body: Optional[str] = None
) -> Any:
    print("ARMADILLO", typ)
    if body is None:
        body = http_res.text
    try:
        return unmarshal_json(body, typ)
    except Exception as e:
        entries = http_res.json()
        busted = []
        for e in entries.get("plays", []):
            for key in ["homeTimeoutsLeft", "visitorTimeoutsLeft"]:
                if not e.get(key):
                    busted.append(e)
                    break
        import json

        with open("busted.json", "w") as outfile:
            json.dump(busted, outfile, indent=4)

        raise errors.ResponseValidationError(
            "Response validation failed",
            http_res,
            e,
            body,
        ) from e
