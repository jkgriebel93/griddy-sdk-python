from typing import Any, Dict, Optional, Type

from griddy.core.basesdk import BaseSDK as CoreBaseSDK
from griddy.core.basesdk import EndpointConfig  # noqa: F401

from . import errors, models


class BaseSDK(CoreBaseSDK):
    """NFL-specific BaseSDK with NFL error classes and security model."""

    @property
    def _default_error_cls(self) -> Type[Exception]:
        return errors.GriddyNFLDefaultError

    @property
    def _no_response_error_cls(self) -> Type[Exception]:
        return errors.NoResponseError

    @property
    def _security_model_cls(self) -> Any:
        return models.Security

    @property
    def _security_env_mapping(self) -> Optional[Dict[str, str]]:
        return {"nfl_auth": "GRIDDY_NFL_NFL_AUTH"}

    def _get_security_from_env(self, security: Any) -> Any:
        """NFL uses its own get_security_from_env with hardcoded env var."""
        from .utils.security import get_security_from_env

        return get_security_from_env(security, models.Security)
