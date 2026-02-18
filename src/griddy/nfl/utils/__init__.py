"""NFL utils — re-exports everything from griddy.core.utils.

NFL-specific overrides:
- get_security_from_env: Uses GRIDDY_NFL_NFL_AUTH env var
- get_default_logger: Uses GRIDDY_NFL_DEBUG env var
- unmarshal_json_response: Passes NFL error class
"""

import builtins
import sys
from importlib import import_module
from typing import TYPE_CHECKING

# Re-export everything from core
from griddy.core.utils import *  # noqa: F401,F403
from griddy.core.utils import __all__ as _core_all

from .logger import Logger, get_body_content, get_default_logger  # noqa: F401

# Override with NFL-specific versions
from .security import get_security, get_security_from_env  # noqa: F401

__all__ = list(_core_all)
