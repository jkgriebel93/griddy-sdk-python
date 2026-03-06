"""Class decorators for SDK endpoint boilerplate reduction."""

import functools
from typing import Callable


def sdk_endpoints(cls: type) -> type:
    """Auto-generate sync/async endpoint wrappers from config methods.

    Scans the class for methods matching the pattern ``_<name>_config`` and
    generates two public methods for each:

    - ``<name>(self, ...)`` — calls the config method then ``_execute_endpoint``
    - ``<name>_async(self, ...)`` — calls the config method then
      ``_execute_endpoint_async``

    The generated methods inherit the parameter signature and docstring from
    the config method via ``functools.wraps``.  If a method with the target
    name already exists on the class it is **not** overwritten, allowing
    manual overrides.

    Example::

        @sdk_endpoints
        class Passing(ProSDK):
            def _get_weekly_summary_config(self, *, season: int) -> EndpointConfig:
                \"\"\"Get weekly passing stats.\"\"\"
                return EndpointConfig(...)

            # get_weekly_summary() and get_weekly_summary_async() are
            # auto-generated at class-creation time.
    """
    for name in list(vars(cls)):
        if not (name.startswith("_") and name.endswith("_config")):
            continue

        config_method = vars(cls)[name]
        if not callable(config_method):
            continue

        # _get_foo_config -> get_foo / get_foo_async
        # _refresh_token_config -> refresh_token / refresh_token_async
        public_name = name[1:-7]  # strip leading '_' and trailing '_config'
        async_name = f"{public_name}_async"

        if public_name not in vars(cls):
            setattr(cls, public_name, _make_sync(config_method, cls, public_name))

        if async_name not in vars(cls):
            setattr(cls, async_name, _make_async(config_method, cls, async_name))

    return cls


def _make_sync(cfg_fn: Callable, cls: type, method_name: str) -> Callable:
    """Create a sync wrapper that calls the config method then _execute_endpoint."""

    @functools.wraps(cfg_fn)
    def wrapper(self, *args, **kwargs):
        config = cfg_fn(self, *args, **kwargs)
        return self._execute_endpoint(config)

    wrapper.__name__ = method_name
    wrapper.__qualname__ = f"{cls.__qualname__}.{method_name}"
    return wrapper


def _make_async(cfg_fn: Callable, cls: type, method_name: str) -> Callable:
    """Create an async wrapper that calls the config method then _execute_endpoint_async."""

    @functools.wraps(cfg_fn)
    async def wrapper(self, *args, **kwargs):
        config = cfg_fn(self, *args, **kwargs)
        return await self._execute_endpoint_async(config)

    wrapper.__name__ = method_name
    wrapper.__qualname__ = f"{cls.__qualname__}.{method_name}"
    return wrapper
