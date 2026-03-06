"""Tests verifying docstrings and type annotations for the nfl module (TGF-160)."""

import inspect

import pytest

from griddy.nfl.basesdk import BaseSDK
from griddy.nfl.sdk import GriddyNFL
from griddy.nfl.sdkconfiguration import SDKConfiguration
from griddy.nfl.utils.retries import (
    BackoffStrategy,
    PermanentError,
    Retries,
    RetryConfig,
    TemporaryError,
    retry,
    retry_async,
    retry_with_backoff,
    retry_with_backoff_async,
)
from griddy.nfl.utils.security import do_browser_auth
from griddy.nfl.utils.serializers import (
    _contains_pydantic_model,
    get_pydantic_model,
    is_nullable,
    marshal_json,
    serialize_decimal,
    serialize_float,
    serialize_int,
    stream_to_bytes,
    stream_to_bytes_async,
    stream_to_text,
    stream_to_text_async,
    unmarshal,
    unmarshal_json,
    validate_const,
    validate_decimal,
    validate_float,
    validate_int,
    validate_open_enum,
)
from griddy.nfl.utils.unmarshal_json_response import int_to_str, unmarshal_json_response
from griddy.nfl.utils.url import (
    _populate_path_params,
    generate_url,
    is_optional,
    remove_suffix,
    template_url,
)
from griddy.nfl.utils.values import (
    _get_serialized_params,
    _is_set,
    _populate_from_globals,
    _val_to_string,
    cast_partial,
    get_global_from_env,
    match_content_type,
    match_response,
    match_status_codes,
)

# Collect all items from the ticket that need docstrings
_ITEMS_NEEDING_DOCSTRINGS = [
    # nfl/basesdk.py
    (BaseSDK._default_error_cls.fget, "BaseSDK._default_error_cls"),
    (BaseSDK._no_response_error_cls.fget, "BaseSDK._no_response_error_cls"),
    (BaseSDK._security_model_cls.fget, "BaseSDK._security_model_cls"),
    (BaseSDK._security_env_mapping.fget, "BaseSDK._security_env_mapping"),
    # nfl/sdk.py
    (GriddyNFL._get_debug_logger_env_var, "GriddyNFL._get_debug_logger_env_var"),
    (GriddyNFL._create_security, "GriddyNFL._create_security"),
    (GriddyNFL._create_sdk_configuration, "GriddyNFL._create_sdk_configuration"),
    (GriddyNFL._create_hooks, "GriddyNFL._create_hooks"),
    # nfl/sdkconfiguration.py
    (SDKConfiguration, "SDKConfiguration"),
    (SDKConfiguration.__post_init__, "SDKConfiguration.__post_init__"),
    (SDKConfiguration.get_server_details, "SDKConfiguration.get_server_details"),
    # nfl/utils/retries.py
    (BackoffStrategy, "BackoffStrategy"),
    (BackoffStrategy.__init__, "BackoffStrategy.__init__"),
    (RetryConfig, "RetryConfig"),
    (RetryConfig.__init__, "RetryConfig.__init__"),
    (Retries, "Retries"),
    (Retries.__init__, "Retries.__init__"),
    (TemporaryError, "TemporaryError"),
    (TemporaryError.__init__, "TemporaryError.__init__"),
    (PermanentError, "PermanentError"),
    (PermanentError.__init__, "PermanentError.__init__"),
    (retry, "retry"),
    (retry_async, "retry_async"),
    (retry_with_backoff, "retry_with_backoff"),
    (retry_with_backoff_async, "retry_with_backoff_async"),
    # nfl/utils/security.py
    (do_browser_auth, "do_browser_auth"),
    # nfl/utils/serializers.py
    (serialize_decimal, "serialize_decimal"),
    (validate_decimal, "validate_decimal"),
    (serialize_float, "serialize_float"),
    (validate_float, "validate_float"),
    (serialize_int, "serialize_int"),
    (validate_int, "validate_int"),
    (validate_open_enum, "validate_open_enum"),
    (validate_const, "validate_const"),
    (unmarshal_json, "unmarshal_json"),
    (unmarshal, "unmarshal"),
    (marshal_json, "marshal_json"),
    (is_nullable, "is_nullable"),
    (stream_to_text, "stream_to_text"),
    (stream_to_text_async, "stream_to_text_async"),
    (stream_to_bytes, "stream_to_bytes"),
    (stream_to_bytes_async, "stream_to_bytes_async"),
    (get_pydantic_model, "get_pydantic_model"),
    (_contains_pydantic_model, "_contains_pydantic_model"),
    # nfl/utils/unmarshal_json_response.py
    (int_to_str, "int_to_str"),
    (unmarshal_json_response, "unmarshal_json_response"),
    # nfl/utils/url.py
    (generate_url, "generate_url"),
    (_populate_path_params, "_populate_path_params"),
    (is_optional, "is_optional"),
    (template_url, "template_url"),
    (remove_suffix, "remove_suffix"),
    # nfl/utils/values.py
    (match_content_type, "match_content_type"),
    (match_status_codes, "match_status_codes"),
    (cast_partial, "cast_partial"),
    (get_global_from_env, "get_global_from_env"),
    (match_response, "match_response"),
    (_populate_from_globals, "_populate_from_globals"),
    (_val_to_string, "_val_to_string"),
    (_get_serialized_params, "_get_serialized_params"),
    (_is_set, "_is_set"),
]


@pytest.mark.unit
class TestDocstringsExist:
    @pytest.mark.parametrize(
        "obj,name",
        [pytest.param(obj, name, id=name) for obj, name in _ITEMS_NEEDING_DOCSTRINGS],
    )
    def test_has_docstring(self, obj, name):
        assert obj.__doc__ is not None, f"{name} is missing a docstring"
        assert len(obj.__doc__.strip()) > 0, f"{name} has an empty docstring"


# Items that the ticket flagged as missing type annotations
_ITEMS_NEEDING_RETURN_TYPES = [
    # retries.py
    (retry, "retry"),
    (retry_async, "retry_async"),
    (retry_with_backoff, "retry_with_backoff"),
    (retry_with_backoff_async, "retry_with_backoff_async"),
    # serializers.py
    (serialize_decimal, "serialize_decimal"),
    (validate_decimal, "validate_decimal"),
    (serialize_float, "serialize_float"),
    (validate_float, "validate_float"),
    (serialize_int, "serialize_int"),
    (validate_int, "validate_int"),
    (validate_open_enum, "validate_open_enum"),
    (validate_const, "validate_const"),
    (marshal_json, "marshal_json"),
    (is_nullable, "is_nullable"),
    # unmarshal_json_response.py
    (int_to_str, "int_to_str"),
    # url.py
    (is_optional, "is_optional"),
    (remove_suffix, "remove_suffix"),
    # values.py
    (cast_partial, "cast_partial"),
]


@pytest.mark.unit
class TestReturnTypeAnnotations:
    @pytest.mark.parametrize(
        "func,name",
        [pytest.param(f, n, id=n) for f, n in _ITEMS_NEEDING_RETURN_TYPES],
    )
    def test_has_return_annotation(self, func, name):
        hints = inspect.get_annotations(func)
        assert "return" in hints, f"{name} is missing a return type annotation"


_ITEMS_NEEDING_PARAM_TYPES = [
    # retries.py - func param
    (retry, "retry", "func"),
    (retry_async, "retry_async", "func"),
    (retry_with_backoff, "retry_with_backoff", "func"),
    (retry_with_backoff, "retry_with_backoff", "initial_interval"),
    (retry_with_backoff, "retry_with_backoff", "max_interval"),
    (retry_with_backoff, "retry_with_backoff", "exponent"),
    (retry_with_backoff, "retry_with_backoff", "max_elapsed_time"),
    (retry_with_backoff_async, "retry_with_backoff_async", "func"),
    (retry_with_backoff_async, "retry_with_backoff_async", "initial_interval"),
    (retry_with_backoff_async, "retry_with_backoff_async", "max_interval"),
    (retry_with_backoff_async, "retry_with_backoff_async", "exponent"),
    (retry_with_backoff_async, "retry_with_backoff_async", "max_elapsed_time"),
    # serializers.py
    (validate_decimal, "validate_decimal", "d"),
    (validate_float, "validate_float", "f"),
    (validate_int, "validate_int", "b"),
    (validate_const, "validate_const", "v"),
    (unmarshal_json, "unmarshal_json", "raw"),
    (unmarshal, "unmarshal", "val"),
    (marshal_json, "marshal_json", "val"),
    (marshal_json, "marshal_json", "typ"),
    (is_nullable, "is_nullable", "field"),
    # unmarshal_json_response.py
    (int_to_str, "int_to_str", "value"),
    # url.py
    (is_optional, "is_optional", "field"),
    (remove_suffix, "remove_suffix", "input_string"),
    (remove_suffix, "remove_suffix", "suffix"),
    # values.py
    (cast_partial, "cast_partial", "typ"),
    (_val_to_string, "_val_to_string", "val"),
]


@pytest.mark.unit
class TestParamTypeAnnotations:
    @pytest.mark.parametrize(
        "func,name,param",
        [
            pytest.param(f, n, p, id=f"{n}.{p}")
            for f, n, p in _ITEMS_NEEDING_PARAM_TYPES
        ],
    )
    def test_has_param_annotation(self, func, name, param):
        hints = inspect.get_annotations(func)
        assert param in hints, f"{name} is missing type annotation for param '{param}'"
