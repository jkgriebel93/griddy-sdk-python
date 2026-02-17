import builtins
from typing import TYPE_CHECKING

from griddy_nfl._import import dynamic_import

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
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(
            f"No {attr_name} found in _dynamic_imports for module name -> {__name__} "
        )

    try:
        module = dynamic_import(module_name, __package__)
        result = getattr(module, attr_name)
        return result
    except ImportError as e:
        raise ImportError(
            f"Failed to import {attr_name} from {module_name}: {e}"
        ) from e
    except AttributeError as e:
        raise AttributeError(
            f"Failed to get {attr_name} from {module_name}: {e}"
        ) from e


def __dir__():
    lazy_attrs = builtins.list(_dynamic_imports.keys())
    return builtins.sorted(lazy_attrs)
