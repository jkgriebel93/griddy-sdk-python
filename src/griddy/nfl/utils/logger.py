from griddy.core.utils.logger import Logger, NoOpLogger, get_body_content  # noqa: F401
from griddy.core.utils.logger import get_default_logger as _core_get_default_logger


def get_default_logger() -> Logger:
    """Get default logger with NFL-specific env var."""
    return _core_get_default_logger(env_var="GRIDDY_NFL_DEBUG")
