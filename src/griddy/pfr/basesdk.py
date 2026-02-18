from typing import Any, Dict, Optional, Type

from griddy.core.basesdk import BaseSDK as CoreBaseSDK
from griddy.core.basesdk import EndpointConfig  # noqa: F401

from . import errors, models


class BaseSDK(CoreBaseSDK):
    """PFR-specific BaseSDK with PFR error classes and security model."""

    @property
    def _default_error_cls(self) -> Type[Exception]:
        return errors.GriddyPFRDefaultError

    @property
    def _no_response_error_cls(self) -> Type[Exception]:
        return errors.NoResponseError

    @property
    def _security_model_cls(self) -> Any:
        return models.Security

    @property
    def _security_env_mapping(self) -> Optional[Dict[str, str]]:
        return {"pfr_auth": "GRIDDY_PFR_AUTH"}
