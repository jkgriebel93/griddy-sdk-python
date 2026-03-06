import json
import re
from typing import (
    Any,
    AsyncGenerator,
    Callable,
    Generator,
    Generic,
    Optional,
    Tuple,
    TypeVar,
)

import httpx

T = TypeVar("T")


class EventStream(Generic[T]):
    """Synchronous iterator over server-sent events from a streaming HTTP response."""

    # Holds a reference to the SDK client to avoid it being garbage collected
    # and cause termination of the underlying httpx client.
    client_ref: Optional[object]
    response: httpx.Response
    generator: Generator[T, None, None]

    def __init__(
        self,
        response: httpx.Response,
        decoder: Callable[[str], T],
        sentinel: Optional[str] = None,
        client_ref: Optional[object] = None,
    ):
        """Initialize with an HTTP response, decoder, optional sentinel, and client ref."""
        self.response = response
        self.generator = stream_events(response, decoder, sentinel)
        self.client_ref = client_ref

    def __iter__(self) -> "EventStream[T]":
        """Return self as the iterator."""
        return self

    def __next__(self) -> T:
        """Return the next decoded event."""
        return next(self.generator)

    def __enter__(self) -> "EventStream[T]":
        """Enter the event stream context."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: Any,
    ) -> None:
        """Close the underlying HTTP response."""
        self.response.close()


class EventStreamAsync(Generic[T]):
    """Asynchronous iterator over server-sent events from a streaming HTTP response."""

    # Holds a reference to the SDK client to avoid it being garbage collected
    # and cause termination of the underlying httpx client.
    client_ref: Optional[object]
    response: httpx.Response
    generator: AsyncGenerator[T, None]

    def __init__(
        self,
        response: httpx.Response,
        decoder: Callable[[str], T],
        sentinel: Optional[str] = None,
        client_ref: Optional[object] = None,
    ):
        """Initialize with an HTTP response, decoder, optional sentinel, and client ref."""
        self.response = response
        self.generator = stream_events_async(response, decoder, sentinel)
        self.client_ref = client_ref

    def __aiter__(self) -> "EventStreamAsync[T]":
        """Return self as the async iterator."""
        return self

    async def __anext__(self) -> T:
        """Return the next decoded event asynchronously."""
        return await self.generator.__anext__()

    async def __aenter__(self) -> "EventStreamAsync[T]":
        """Enter the async event stream context."""
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: Any,
    ) -> None:
        """Close the underlying HTTP response asynchronously."""
        await self.response.aclose()


class ServerEvent:
    """Parsed server-sent event with id, event type, data, and retry fields."""

    id: Optional[str] = None
    event: Optional[str] = None
    data: Optional[str] = None
    retry: Optional[int] = None


MESSAGE_BOUNDARIES = [
    b"\r\n\r\n",
    b"\n\n",
    b"\r\r",
]


async def stream_events_async(
    response: httpx.Response,
    decoder: Callable[[str], T],
    sentinel: Optional[str] = None,
) -> AsyncGenerator[T, None]:
    """Async generator yielding decoded events from a streaming HTTP response."""
    buffer = bytearray()
    position = 0
    discard = False
    async for chunk in response.aiter_bytes():
        # We've encountered the sentinel value and should no longer process
        # incoming data. Instead we throw new data away until the server closes
        # the connection.
        if discard:
            continue

        buffer += chunk
        for i in range(position, len(buffer)):
            char = buffer[i : i + 1]
            seq: Optional[bytes] = None
            if char in [b"\r", b"\n"]:
                for boundary in MESSAGE_BOUNDARIES:
                    seq = _peek_sequence(i, buffer, boundary)
                    if seq is not None:
                        break
            if seq is None:
                continue

            block = buffer[position:i]
            position = i + len(seq)
            event, discard = _parse_event(block, decoder, sentinel)
            if event is not None:
                yield event

        if position > 0:
            buffer = buffer[position:]
            position = 0

    event, discard = _parse_event(buffer, decoder, sentinel)
    if event is not None:
        yield event


def stream_events(
    response: httpx.Response,
    decoder: Callable[[str], T],
    sentinel: Optional[str] = None,
) -> Generator[T, None, None]:
    """Generator yielding decoded events from a streaming HTTP response."""
    buffer = bytearray()
    position = 0
    discard = False
    for chunk in response.iter_bytes():
        # We've encountered the sentinel value and should no longer process
        # incoming data. Instead we throw new data away until the server closes
        # the connection.
        if discard:
            continue

        buffer += chunk
        for i in range(position, len(buffer)):
            char = buffer[i : i + 1]
            seq: Optional[bytes] = None
            if char in [b"\r", b"\n"]:
                for boundary in MESSAGE_BOUNDARIES:
                    seq = _peek_sequence(i, buffer, boundary)
                    if seq is not None:
                        break
            if seq is None:
                continue

            block = buffer[position:i]
            position = i + len(seq)
            event, discard = _parse_event(block, decoder, sentinel)
            if event is not None:
                yield event

        if position > 0:
            buffer = buffer[position:]
            position = 0

    event, discard = _parse_event(buffer, decoder, sentinel)
    if event is not None:
        yield event


def _parse_event(
    raw: bytearray, decoder: Callable[[str], T], sentinel: Optional[str] = None
) -> Tuple[Optional[T], bool]:
    """Parse a raw SSE message block into a decoded event."""
    block = raw.decode()
    lines = re.split(r"\r?\n|\r", block)
    publish = False
    event = ServerEvent()
    data = ""
    for line in lines:
        if not line:
            continue

        delim = line.find(":")
        if delim <= 0:
            continue

        field = line[0:delim]
        value = line[delim + 1 :] if delim < len(line) - 1 else ""
        if len(value) and value[0] == " ":
            value = value[1:]

        if field == "event":
            event.event = value
            publish = True
        elif field == "data":
            data += value + "\n"
            publish = True
        elif field == "id":
            event.id = value
            publish = True
        elif field == "retry":
            event.retry = int(value) if value.isdigit() else None
            publish = True

    if sentinel and data == f"{sentinel}\n":
        return None, True

    if data:
        data = data[:-1]
        event.data = data

        data_is_primitive = (
            data.isnumeric() or data == "true" or data == "false" or data == "null"
        )
        data_is_json = (
            data.startswith("{") or data.startswith("[") or data.startswith('"')
        )

        if data_is_primitive or data_is_json:
            try:
                event.data = json.loads(data)
            except Exception:
                pass

    out = None
    if publish:
        out = decoder(json.dumps(event.__dict__))

    return out, False


def _peek_sequence(
    position: int, buffer: bytearray, sequence: bytes
) -> Optional[bytes]:
    """Check if buffer at position starts with the given byte sequence."""
    if len(sequence) > (len(buffer) - position):
        return None

    for i, seq in enumerate(sequence):
        if buffer[position + i] != seq:
            return None

    return sequence
