import logging
import os
from typing import Any, Protocol

import httpx


class Logger(Protocol):
    """Protocol for SDK debug loggers."""

    def debug(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """Log a debug-level message."""
        pass

    def warning(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """Log a warning-level message."""
        pass


class NoOpLogger:
    """Logger implementation that discards all messages."""

    def debug(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """Discard the debug message."""
        pass

    def warning(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """Discard the warning message."""
        pass


def get_body_content(req: httpx.Request) -> str:
    """Return the request body content as a string, or a placeholder for streaming."""
    return "<streaming body>" if not hasattr(req, "_content") else str(req.content)


def get_default_logger(env_var: str = "GRIDDY_DEBUG") -> Logger:
    """Get a default logger, optionally enabled via an environment variable.

    Args:
        env_var: Environment variable name to check for debug logging.
    """
    if os.getenv(env_var):
        logging.basicConfig(level=logging.DEBUG)
        return logging.getLogger("griddy")
    return NoOpLogger()
