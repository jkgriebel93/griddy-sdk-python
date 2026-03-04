"""Shared error-message formatting utilities."""

import httpx

MAX_MESSAGE_LEN = 10_000


def format_error_message(
    message: str, raw_response: httpx.Response, body: str | None = None
) -> str:
    """Build a human-readable error message from an HTTP response.

    Handles status code insertion, content-type annotation for non-JSON
    responses, and body truncation for very long payloads.
    """
    body_display = body or raw_response.text or '""'

    if message:
        message += ": "
    message += f"Status {raw_response.status_code}"

    headers = raw_response.headers
    content_type = headers.get("content-type", '""')
    if content_type != "application/json":
        if " " in content_type:
            content_type = f'"{content_type}"'
        message += f" Content-Type {content_type}"

    if len(body_display) > MAX_MESSAGE_LEN:
        truncated = body_display[:MAX_MESSAGE_LEN]
        remaining = len(body_display) - MAX_MESSAGE_LEN
        body_display = f"{truncated}...and {remaining} more chars"

    message += f". Body: {body_display}"
    return message.strip()
