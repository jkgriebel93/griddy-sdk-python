from typing import TYPE_CHECKING

from griddy.core._lazy import dynamic_dir, dynamic_getattr

from .sdkerror import SDKError

if TYPE_CHECKING:
    from .defaultsdkerror import DefaultSDKError
    from .no_response_error import NoResponseError
    from .responsevalidationerror import ResponseValidationError

__all__ = [
    "DefaultSDKError",
    "NoResponseError",
    "ResponseValidationError",
    "SDKError",
]

_dynamic_imports: dict[str, str] = {
    "DefaultSDKError": ".defaultsdkerror",
    "NoResponseError": ".no_response_error",
    "ResponseValidationError": ".responsevalidationerror",
}


def __getattr__(attr_name: str) -> object:
    """Lazily import error classes on first access."""
    return dynamic_getattr(attr_name, _dynamic_imports, __package__, __name__)


def __dir__() -> list[str]:
    """List all exportable error class names."""
    return dynamic_dir(_dynamic_imports)
