import functools
import json
import typing
from datetime import date, datetime, time
from decimal import Decimal
from typing import Any, Callable, Dict, List, Tuple, Union, get_args

import httpx
import typing_extensions
from pydantic import ConfigDict, create_model
from pydantic_core import from_json
from typing_extensions import get_origin

from griddy.core.types.basemodel import BaseModel, Nullable, OptionalNullable, Unset


def serialize_decimal(as_str: bool) -> Callable:
    """Return a Pydantic serializer for Decimal values."""

    def serialize(d):
        # Optional[T] is a Union[T, None]
        if is_union(type(d)) and type(None) in get_args(type(d)) and d is None:
            return None
        if isinstance(d, Unset):
            return d

        if not isinstance(d, Decimal):
            raise ValueError("Expected Decimal object")

        return str(d) if as_str else float(d)

    return serialize


def validate_decimal(d: Any) -> Decimal | None:
    """Validate and coerce a value to Decimal."""
    if d is None:
        return None

    if isinstance(d, (Decimal, Unset)):
        return d

    if not isinstance(d, (str, int, float)):
        raise ValueError("Expected string, int or float")

    return Decimal(str(d))


def serialize_float(as_str: bool) -> Callable:
    """Return a Pydantic serializer for float values."""

    def serialize(f):
        # Optional[T] is a Union[T, None]
        if is_union(type(f)) and type(None) in get_args(type(f)) and f is None:
            return None
        if isinstance(f, Unset):
            return f

        if not isinstance(f, float):
            raise ValueError("Expected float")

        return str(f) if as_str else f

    return serialize


def validate_float(f: Any) -> float | None:
    """Validate and coerce a value to float."""
    if f is None:
        return None

    if isinstance(f, (float, Unset)):
        return f

    if not isinstance(f, str):
        raise ValueError("Expected string")

    return float(f)


def serialize_int(as_str: bool) -> Callable:
    """Return a Pydantic serializer for int values."""

    def serialize(i):
        # Optional[T] is a Union[T, None]
        if is_union(type(i)) and type(None) in get_args(type(i)) and i is None:
            return None
        if isinstance(i, Unset):
            return i

        if not isinstance(i, int):
            raise ValueError("Expected int")

        return str(i) if as_str else i

    return serialize


def validate_int(b: Any) -> int | None:
    """Validate and coerce a value to int."""
    if b is None:
        return None

    if isinstance(b, (int, Unset)):
        return b

    if not isinstance(b, str):
        raise ValueError("Expected string")

    return int(b)


def validate_open_enum(is_int: bool) -> Callable:
    """Return a validator that accepts int or str enum values."""

    def validate(e):
        if e is None:
            return None

        if isinstance(e, Unset):
            return e

        if is_int:
            if not isinstance(e, int):
                raise ValueError("Expected int")
        else:
            if not isinstance(e, str):
                raise ValueError("Expected string")

        return e

    return validate


def validate_const(v: Any) -> Callable:
    """Return a validator that enforces a constant value."""

    def validate(c):
        # Optional[T] is a Union[T, None]
        if is_union(type(c)) and type(None) in get_args(type(c)) and c is None:
            return None

        if v != c:
            raise ValueError(f"Expected {v}")

        return c

    return validate


def unmarshal_json(raw: bytes | str, typ: Any) -> Any:
    """Deserialize a raw JSON bytes/string into the given type."""
    return unmarshal(from_json(raw), typ)


def unmarshal(val: Any, typ: Any) -> Any:
    """Coerce a parsed value into the given Pydantic-compatible type."""
    unmarshaller = create_model(
        "Unmarshaller",
        body=(typ, ...),
        __config__=ConfigDict(populate_by_name=True, arbitrary_types_allowed=True),
    )

    m = unmarshaller(body=val)

    # pyright: ignore[reportAttributeAccessIssue]
    return m.body  # type: ignore


def marshal_json(val: Any, typ: Any) -> str:
    """Serialize a value to a JSON string using a Pydantic model wrapper."""
    if is_nullable(typ) and val is None:
        return "null"

    marshaller = create_model(
        "Marshaller",
        body=(typ, ...),
        __config__=ConfigDict(populate_by_name=True, arbitrary_types_allowed=True),
    )

    m = marshaller(body=val)

    d = m.model_dump(by_alias=True, mode="json", exclude_none=True)

    if len(d) == 0:
        return ""

    return json.dumps(d[next(iter(d))], separators=(",", ":"))


def is_nullable(field: Any) -> bool:
    """Check if a type annotation represents a nullable type."""
    origin = get_origin(field)
    if origin is Nullable or origin is OptionalNullable:
        return True

    if not origin is Union or type(None) not in get_args(field):
        return False

    for arg in get_args(field):
        if get_origin(arg) is Nullable or get_origin(arg) is OptionalNullable:
            return True

    return False


def is_union(obj: object) -> bool:
    """
    Returns True if the given object is a typing.Union or typing_extensions.Union.
    """
    return any(
        obj is typing_obj for typing_obj in _get_typing_objects_by_name_of("Union")
    )


def stream_to_text(stream: httpx.Response) -> str:
    """Read a streaming HTTP response into a single text string."""
    return "".join(stream.iter_text())


async def stream_to_text_async(stream: httpx.Response) -> str:
    """Async read a streaming HTTP response into a single text string."""
    return "".join([chunk async for chunk in stream.aiter_text()])


def stream_to_bytes(stream: httpx.Response) -> bytes:
    """Read a streaming HTTP response into bytes."""
    return stream.content


async def stream_to_bytes_async(stream: httpx.Response) -> bytes:
    """Async read a streaming HTTP response into bytes."""
    return await stream.aread()


def get_pydantic_model(data: Any, typ: Any) -> Any:
    """Return data as-is if it already contains Pydantic models, otherwise unmarshal."""
    if not _contains_pydantic_model(data):
        return unmarshal(data, typ)

    return data


def _contains_pydantic_model(data: Any) -> bool:
    """Recursively check if data contains any Pydantic model instances."""
    if isinstance(data, BaseModel):
        return True
    if isinstance(data, List):
        return any(_contains_pydantic_model(item) for item in data)
    if isinstance(data, Dict):
        return any(_contains_pydantic_model(value) for value in data.values())

    return False


@functools.cache
def _get_typing_objects_by_name_of(name: str) -> Tuple[Any, ...]:
    """
    Get typing objects by name from typing and typing_extensions.
    Reference: https://typing-extensions.readthedocs.io/en/latest/#runtime-use-of-types
    """
    result = tuple(
        getattr(module, name)
        for module in (typing, typing_extensions)
        if hasattr(module, name)
    )
    if not result:
        raise ValueError(
            f"Neither typing nor typing_extensions has an object called {name!r}"
        )
    return result


class DateTimeEncoder(json.JSONEncoder):
    """JSON encoder that serializes datetime, date, and time objects to ISO format."""

    def default(self, o: Any) -> Any:
        """Return ISO format for datetime objects, delegate otherwise."""
        if isinstance(o, (datetime, date, time)):
            return o.isoformat()
        return super().default(o=o)
