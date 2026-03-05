from typing import TYPE_CHECKING

from griddy.core._lazy import dynamic_dir, dynamic_getattr

from .griddynflerror import GriddyNFLError

if TYPE_CHECKING:
    from .griddynfldefaulterror import GriddyNFLDefaultError
    from .no_response_error import NoResponseError
    from .responsevalidationerror import ResponseValidationError

__all__ = [
    "GriddyNFLDefaultError",
    "GriddyNFLError",
    "NoResponseError",
    "ResponseValidationError",
]

_dynamic_imports: dict[str, str] = {
    "GriddyNFLDefaultError": ".griddynfldefaulterror",
    "NoResponseError": ".no_response_error",
    "ResponseValidationError": ".responsevalidationerror",
}


def __getattr__(attr_name: str) -> object:
    return dynamic_getattr(attr_name, _dynamic_imports, __package__, __name__)


def __dir__():
    return dynamic_dir(_dynamic_imports)
