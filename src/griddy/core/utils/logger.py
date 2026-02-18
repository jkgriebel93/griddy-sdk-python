import logging
import os
from typing import Any, Protocol

import httpx


class Logger(Protocol):
    def debug(self, msg: str, *args: Any, **kwargs: Any) -> None:
        pass


class NoOpLogger:
    def debug(self, msg: str, *args: Any, **kwargs: Any) -> None:
        pass


def get_body_content(req: httpx.Request) -> str:
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
