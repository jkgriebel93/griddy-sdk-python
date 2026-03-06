from typing import Any, Dict, Optional, Type

from griddy.core.basesdk import (
    BaseEndpointConfig,  # noqa: F401
    EndpointConfig,  # noqa: F401
)
from griddy.core.basesdk import BaseSDK as CoreBaseSDK

from . import errors, models
from .sdkconfiguration import SDKConfiguration


class BaseSDK(CoreBaseSDK[SDKConfiguration]):
    """NFL-specific BaseSDK with NFL error classes and security model."""

    @property
    def _default_error_cls(self) -> Type[Exception]:
        """Return the default error class for NFL API response errors."""
        return errors.GriddyNFLDefaultError

    @property
    def _no_response_error_cls(self) -> Type[Exception]:
        """Return the error class raised when the NFL API returns no response body."""
        return errors.NoResponseError

    @property
    def _security_model_cls(self) -> Any:
        """Return the Pydantic security model class for NFL authentication."""
        return models.Security

    @property
    def _security_env_mapping(self) -> Optional[Dict[str, str]]:
        """Return the mapping of security fields to environment variable names."""
        return {"nfl_auth": "GRIDDY_NFL_NFL_AUTH"}

    def _get_security_from_env(self, security: Any) -> Any:
        """NFL uses its own get_security_from_env with hardcoded env var."""
        from .utils.security import get_security_from_env

        return get_security_from_env(security, models.Security)
