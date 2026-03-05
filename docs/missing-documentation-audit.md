# Missing Documentation Audit

Auto-generated analysis of `src/griddy/` for missing docstrings and type annotations.

## Summary

| Metric | Count |
|---|---|
| Total items with gaps | 885 |
| Missing docstrings | 872 |
| Missing type annotations | 131 |
| Files affected | 381 |

## By Module

| Module | Items | Missing Docstrings | Missing Types |
|---|---|---|---|
| `core` | 227 | 221 | 90 |
| `nfl` | 60 | 60 | 21 |
| `nfl/hooks` | 5 | 4 | 2 |
| `nfl/errors` | 6 | 5 | 2 |
| `nfl/endpoints/regular` | 13 | 13 | 0 |
| `nfl/endpoints/pro` | 14 | 13 | 1 |
| `nfl/models` | 342 | 342 | 1 |
| `pfr` | 16 | 15 | 1 |
| `pfr/endpoints` | 35 | 35 | 0 |
| `pfr/models` | 124 | 124 | 1 |
| `pfr/parsers` | 22 | 22 | 4 |
| `pfr/errors` | 8 | 7 | 2 |
| `pfr/utils` | 9 | 7 | 6 |
| `root` | 4 | 4 | 0 |

## By Kind

| Kind | Items | Missing Docstrings | Missing Types |
|---|---|---|---|
| class | 537 | 537 | 0 |
| method | 209 | 202 | 54 |
| async method | 12 | 10 | 9 |
| function | 118 | 114 | 64 |
| async function | 9 | 9 | 4 |

---

## `core` (227 items)

### `core/_import.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | function | `dynamic_import` | return type |

### `core/_lazy_load.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 27 | method | `LazySubSDKMixin.__getattr__` | docstring |
| 49 | method | `LazySubSDKMixin.__dir__` | docstring |

### `core/base_griddy_sdk.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 131 | method | `BaseGriddySDK.__enter__` | docstring, return type |
| 134 | async method | `BaseGriddySDK.__aenter__` | docstring, return type |
| 137 | method | `BaseGriddySDK.__exit__` | docstring, return type, param types: `exc_type`, `exc_val`, `exc_tb` |
| 140 | async method | `BaseGriddySDK.__aexit__` | docstring, return type, param types: `exc_type`, `exc_val`, `exc_tb` |
| 194 | method | `BaseGriddySDK.__del__` | docstring |

### `core/basesdk.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 94 | class | `BaseSDK` | docstring |
| 101 | method | `BaseSDK._default_error_cls` | docstring |
| 107 | method | `BaseSDK._no_response_error_cls` | docstring |
| 113 | method | `BaseSDK._security_model_cls` | docstring |
| 121 | method | `BaseSDK.__init__` | docstring |
| 130 | method | `BaseSDK._get_url` | docstring, return type, param types: `base_url`, `url_variables` |
| 141 | method | `BaseSDK._resolve_base_url` | docstring |
| 150 | method | `BaseSDK._resolve_timeout` | docstring |
| 155 | method | `BaseSDK._resolve_retry_config` | docstring |
| 198 | method | `BaseSDK._create_hook_context` | docstring |
| 211 | method | `BaseSDK._process_json_error_response` | docstring |
| 283 | method | `BaseSDK._execute_endpoint` | docstring |
| 320 | async method | `BaseSDK._execute_endpoint_async` | docstring |
| 358 | method | `BaseSDK._build_request_async` | docstring, param types: `method`, `path`, `base_url`, `url_variables`, `request`, `request_body_required`, `request_has_path_params`, `request_has_query_params`, `user_agent_header`, `accept_header_value`, `_globals`, `security` |
| 400 | method | `BaseSDK._build_request` | docstring, param types: `method`, `path`, `base_url`, `url_variables`, `request`, `request_body_required`, `request_has_path_params`, `request_has_query_params`, `user_agent_header`, `accept_header_value`, `_globals`, `security` |
| 442 | method | `BaseSDK._build_request_with_client` | param types: `client`, `method`, `path`, `base_url`, `url_variables`, `request`, `request_body_required`, `request_has_path_params`, `request_has_query_params`, `user_agent_header`, `accept_header_value`, `_globals`, `security` |
| 573 | method | `BaseSDK.do_request` | param types: `hook_ctx`, `request`, `error_status_codes`, `stream` |
| 680 | async method | `BaseSDK.do_request_async` | param types: `hook_ctx`, `request`, `error_status_codes`, `stream` |

### `core/decorators.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 6 | function | `sdk_endpoints` | return type |
| 54 | function | `_make_sync` | docstring, return type, param types: `cfg_fn`, `method_name` |
| 65 | function | `_make_async` | docstring, return type, param types: `cfg_fn`, `method_name` |

### `core/errors/__init__.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 26 | function | `__getattr__` | docstring |
| 30 | function | `__dir__` | docstring, return type |

### `core/errors/defaultsdkerror.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 14 | method | `DefaultSDKError.__init__` | docstring |

### `core/errors/no_response_error.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | method | `NoResponseError.__init__` | docstring |
| 22 | method | `NoResponseError.__str__` | docstring, return type |

### `core/errors/responsevalidationerror.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | method | `ResponseValidationError.__init__` | docstring |
| 24 | method | `ResponseValidationError.cause` | return type |

### `core/errors/sdkerror.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 23 | method | `SDKError.__init__` | docstring |
| 36 | method | `SDKError.__str__` | docstring, return type |

### `core/hooks/sdkhooks.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 25 | method | `SDKHooks.__init__` | docstring |
| 35 | method | `SDKHooks.register_sdk_init_hook` | docstring |
| 38 | method | `SDKHooks.register_before_request_hook` | docstring |
| 41 | method | `SDKHooks.register_after_success_hook` | docstring |
| 44 | method | `SDKHooks.register_after_error_hook` | docstring |
| 47 | method | `SDKHooks.sdk_init` | docstring |
| 52 | method | `SDKHooks.before_request` | docstring |
| 63 | method | `SDKHooks.after_success` | docstring |
| 73 | method | `SDKHooks.after_error` | docstring |

### `core/hooks/types.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 7 | class | `HookContext` | docstring |
| 14 | method | `HookContext.__init__` | docstring |
| 29 | class | `BeforeRequestContext` | docstring |
| 30 | method | `BeforeRequestContext.__init__` | docstring |
| 40 | class | `AfterSuccessContext` | docstring |
| 41 | method | `AfterSuccessContext.__init__` | docstring |
| 51 | class | `AfterErrorContext` | docstring |
| 52 | method | `AfterErrorContext.__init__` | docstring |
| 62 | class | `SDKInitHook` | docstring |
| 64 | method | `SDKInitHook.sdk_init` | docstring |
| 68 | class | `BeforeRequestHook` | docstring |
| 70 | method | `BeforeRequestHook.before_request` | docstring |
| 76 | class | `AfterSuccessHook` | docstring |
| 78 | method | `AfterSuccessHook.after_success` | docstring |
| 84 | class | `AfterErrorHook` | docstring |
| 86 | method | `AfterErrorHook.after_error` | docstring |
| 95 | class | `Hooks` | docstring |
| 97 | method | `Hooks.register_sdk_init_hook` | docstring, return type |
| 101 | method | `Hooks.register_before_request_hook` | docstring, return type |
| 105 | method | `Hooks.register_after_success_hook` | docstring, return type |
| 109 | method | `Hooks.register_after_error_hook` | docstring, return type |

### `core/httpclient.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `HttpClient` | docstring |
| 11 | method | `HttpClient.send` | docstring |
| 25 | method | `HttpClient.build_request` | docstring |
| 44 | method | `HttpClient.close` | docstring |
| 49 | class | `AsyncHttpClient` | docstring |
| 50 | async method | `AsyncHttpClient.send` | docstring |
| 64 | method | `AsyncHttpClient.build_request` | docstring |
| 83 | async method | `AsyncHttpClient.aclose` | docstring |
| 87 | class | `ClientOwner` | docstring |

### `core/types/basemodel.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `BaseModel` | docstring |
| 16 | method | `BaseModel.serialize_model` | docstring, return type, param types: `handler` |
| 43 | class | `Unset` | docstring |
| 45 | method | `Unset.serialize_model` | docstring, return type |
| 48 | method | `Unset.__bool__` | docstring |

### `core/utils/__init__.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 230 | function | `__getattr__` | docstring |
| 234 | function | `__dir__` | docstring, return type |

### `core/utils/converters.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 27 | function | `multi_replace` | docstring |
| 40 | function | `snakify` | docstring |

### `core/utils/cookies.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | method | `Cookie.__init__` | docstring |

### `core/utils/enums.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 5 | class | `OpenEnumMeta` | docstring |

### `core/utils/eventstreaming.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 18 | class | `EventStream` | docstring |
| 25 | method | `EventStream.__init__` | docstring |
| 36 | method | `EventStream.__iter__` | docstring, return type |
| 39 | method | `EventStream.__next__` | docstring, return type |
| 42 | method | `EventStream.__enter__` | docstring, return type |
| 45 | method | `EventStream.__exit__` | docstring, return type, param types: `exc_type`, `exc_val`, `exc_tb` |
| 49 | class | `EventStreamAsync` | docstring |
| 56 | method | `EventStreamAsync.__init__` | docstring |
| 67 | method | `EventStreamAsync.__aiter__` | docstring, return type |
| 70 | async method | `EventStreamAsync.__anext__` | docstring, return type |
| 73 | async method | `EventStreamAsync.__aenter__` | docstring, return type |
| 76 | async method | `EventStreamAsync.__aexit__` | docstring, return type, param types: `exc_type`, `exc_val`, `exc_tb` |
| 80 | class | `ServerEvent` | docstring |
| 94 | async function | `stream_events_async` | docstring |
| 136 | function | `stream_events` | docstring |
| 178 | function | `_parse_event` | docstring |
| 239 | function | `_peek_sequence` | docstring, return type |

### `core/utils/forms.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 21 | function | `_populate_form` | docstring, return type |
| 115 | function | `serialize_multipart_form` | docstring |
| 191 | function | `serialize_form_data` | docstring |

### `core/utils/har.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 26 | function | `extract_minified_har_entry` | docstring, return type |
| 43 | class | `HarEntryPathManager` | docstring |
| 44 | method | `HarEntryPathManager.__init__` | docstring |
| 57 | method | `HarEntryPathManager.filename` | docstring, return type |
| 67 | method | `HarEntryPathManager.as_dict` | docstring |
| 83 | method | `HarEntryPathManager.add_entry` | docstring, return type |
| 104 | function | `consolidate_minified_entries` | docstring |
| 119 | function | `write_consolidated_to_files` | docstring, return type |
| 128 | function | `minify_har` | docstring, return type |

### `core/utils/headers.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 19 | function | `get_headers` | docstring |
| 31 | function | `_populate_headers` | docstring |
| 67 | function | `_serialize_header` | docstring |
| 127 | function | `get_response_headers` | docstring |

### `core/utils/logger.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 8 | class | `Logger` | docstring |
| 9 | method | `Logger.debug` | docstring |
| 12 | method | `Logger.warning` | docstring |
| 16 | class | `NoOpLogger` | docstring |
| 17 | method | `NoOpLogger.debug` | docstring |
| 20 | method | `NoOpLogger.warning` | docstring |
| 24 | function | `get_body_content` | docstring |

### `core/utils/metadata.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `SecurityMetadata` | docstring |
| 17 | method | `SecurityMetadata.get_field_name` | docstring |
| 22 | class | `ParamMetadata` | docstring |
| 29 | class | `PathParamMetadata` | docstring |
| 34 | class | `QueryParamMetadata` | docstring |
| 40 | class | `HeaderMetadata` | docstring |
| 45 | class | `RequestMetadata` | docstring |
| 50 | class | `MultipartFormMetadata` | docstring |
| 57 | class | `FormMetadata` | docstring |
| 63 | class | `FieldMetadata` | docstring |
| 72 | method | `FieldMetadata.__init__` | docstring |
| 93 | function | `find_field_metadata` | docstring |
| 107 | function | `find_metadata` | docstring |

### `core/utils/queryparams.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 25 | function | `get_query_params` | docstring |
| 38 | function | `_populate_query_params` | docstring |
| 100 | function | `_populate_deep_object_query_params` | docstring, return type |
| 114 | function | `_populate_deep_object_query_params_basemodel` | docstring, return type |
| 148 | function | `_populate_deep_object_query_params_dict` | docstring, return type |
| 172 | function | `_populate_deep_object_query_params_list` | docstring, return type |
| 190 | function | `_populate_delimited_query_params` | docstring, return type |

### `core/utils/requestbodies.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 22 | class | `SerializedRequestBody` | docstring |
| 29 | function | `serialize_request_body` | docstring, param types: `request_body_type` |

### `core/utils/retries.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 47 | class | `BackoffStrategy` | docstring |
| 53 | method | `BackoffStrategy.__init__` | docstring |
| 66 | class | `RetryConfig` | docstring |
| 71 | method | `RetryConfig.__init__` | docstring |
| 79 | class | `Retries` | docstring |
| 83 | method | `Retries.__init__` | docstring |
| 88 | class | `TemporaryError` | docstring |
| 91 | method | `TemporaryError.__init__` | docstring |
| 95 | class | `PermanentError` | docstring |
| 98 | method | `PermanentError.__init__` | docstring |
| 102 | function | `retry` | docstring, return type, param types: `func` |
| 151 | async function | `retry_async` | docstring, return type, param types: `func` |
| 200 | function | `retry_with_backoff` | docstring, return type, param types: `func`, `initial_interval`, `max_interval`, `exponent`, `max_elapsed_time` |
| 228 | async function | `retry_with_backoff_async` | docstring, return type, param types: `func`, `initial_interval`, `max_interval`, `exponent`, `max_elapsed_time` |

### `core/utils/security.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | function | `get_security` | docstring |
| 79 | function | `_parse_security_option` | docstring, return type |
| 97 | function | `_parse_security_scheme` | docstring, return type |
| 134 | function | `_parse_security_scheme_value` | docstring, return type |
| 170 | function | `_apply_bearer` | docstring |
| 174 | function | `_parse_basic_auth_scheme` | docstring, return type |

### `core/utils/serializers.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 17 | function | `serialize_decimal` | docstring, return type |
| 33 | function | `validate_decimal` | docstring, return type, param types: `d` |
| 46 | function | `serialize_float` | docstring, return type |
| 62 | function | `validate_float` | docstring, return type, param types: `f` |
| 75 | function | `serialize_int` | docstring, return type |
| 91 | function | `validate_int` | docstring, return type, param types: `b` |
| 104 | function | `validate_open_enum` | docstring, return type |
| 124 | function | `validate_const` | docstring, return type, param types: `v` |
| 138 | function | `unmarshal_json` | docstring, param types: `raw` |
| 142 | function | `unmarshal` | docstring, param types: `val` |
| 155 | function | `marshal_json` | docstring, return type, param types: `val`, `typ` |
| 175 | function | `is_nullable` | docstring, return type, param types: `field` |
| 199 | function | `stream_to_text` | docstring |
| 203 | async function | `stream_to_text_async` | docstring |
| 207 | function | `stream_to_bytes` | docstring |
| 211 | async function | `stream_to_bytes_async` | docstring |
| 215 | function | `get_pydantic_model` | docstring |
| 222 | function | `_contains_pydantic_model` | docstring |
| 251 | class | `DateTimeEncoder` | docstring |
| 252 | method | `DateTimeEncoder.default` | docstring, return type, param types: `o` |

### `core/utils/url.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 28 | function | `generate_url` | docstring |
| 48 | function | `_populate_path_params` | docstring |
| 140 | function | `is_optional` | docstring, return type, param types: `field` |
| 144 | function | `template_url` | docstring |
| 151 | function | `remove_suffix` | docstring, return type, param types: `input_string`, `suffix` |

### `core/utils/values.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 18 | function | `match_content_type` | docstring |
| 37 | function | `match_status_codes` | docstring |
| 53 | function | `cast_partial` | docstring, return type, param types: `typ` |
| 57 | function | `get_global_from_env` | docstring |
| 71 | function | `match_response` | docstring |
| 80 | function | `_populate_from_globals` | docstring |
| 112 | function | `_val_to_string` | docstring, param types: `val` |
| 123 | function | `_get_serialized_params` | docstring |
| 135 | function | `_is_set` | docstring |

### `core/utils/yaml_consolidator.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 15 | class | `YAMLConsolidator` | docstring |
| 27 | method | `YAMLConsolidator.__init__` | docstring |
| 53 | method | `YAMLConsolidator._set_openapi_attr` | docstring, return type |
| 60 | method | `YAMLConsolidator.add_diff_entry` | docstring, return type, param types: `attr`, `key`, `old`, `new` |
| 71 | method | `YAMLConsolidator.add_spec` | docstring, return type |
| 82 | method | `YAMLConsolidator.combine_all_specs` | docstring, return type |
| 98 | method | `YAMLConsolidator.compute_diff_info` | docstring, return type |
| 114 | method | `YAMLConsolidator.create_full_html_string` | docstring, return type, param types: `diffs_list` |
| 128 | method | `YAMLConsolidator.get_open_api_attr` | docstring, return type |
| 134 | method | `YAMLConsolidator.get_sorted_spec` | docstring |
| 144 | method | `YAMLConsolidator.handle_component_diffs` | docstring, return type |
| 152 | method | `YAMLConsolidator.integrate_attr` | docstring, return type, param types: `spec`, `attr` |
| 177 | method | `YAMLConsolidator.integrate_components` | docstring, return type, param types: `components` |
| 212 | method | `YAMLConsolidator.integrate_spec` | docstring, return type, param types: `spec` |
| 216 | method | `YAMLConsolidator.integrate_tags` | docstring, return type, param types: `tags` |
| 241 | method | `YAMLConsolidator.load_specs` | docstring, return type |
| 248 | method | `YAMLConsolidator.output_diff` | docstring, return type |
| 268 | method | `YAMLConsolidator.set_common_info` | docstring, return type, param types: `*args`, `**kwargs` |
| 272 | method | `YAMLConsolidator.sort_all_specs` | docstring, return type |
| 276 | method | `YAMLConsolidator.sort_entries_for_attr` | docstring |
| 298 | method | `YAMLConsolidator.write_spec_to_disk` | docstring, return type, param types: `spec` |
| 305 | method | `YAMLConsolidator.write_to_disk` | docstring, return type |
| 314 | method | `YAMLConsolidator.write_to_html` | docstring, return type, param types: `file_name`, `html_text` |

---

## `nfl` (60 items)

### `nfl/basesdk.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 15 | method | `BaseSDK._default_error_cls` | docstring |
| 19 | method | `BaseSDK._no_response_error_cls` | docstring |
| 23 | method | `BaseSDK._security_model_cls` | docstring |
| 27 | method | `BaseSDK._security_env_mapping` | docstring |

### `nfl/sdk.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 256 | method | `GriddyNFL._get_debug_logger_env_var` | docstring |
| 259 | method | `GriddyNFL._create_security` | docstring |
| 262 | method | `GriddyNFL._create_sdk_configuration` | docstring |
| 265 | method | `GriddyNFL._create_hooks` | docstring |

### `nfl/sdkconfiguration.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 21 | class | `SDKConfiguration` | docstring |
| 28 | method | `SDKConfiguration.__post_init__` | docstring |
| 32 | method | `SDKConfiguration.get_server_details` | docstring |

### `nfl/utils/retries.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 9 | class | `BackoffStrategy` | docstring |
| 15 | method | `BackoffStrategy.__init__` | docstring |
| 28 | class | `RetryConfig` | docstring |
| 33 | method | `RetryConfig.__init__` | docstring |
| 41 | class | `Retries` | docstring |
| 45 | method | `Retries.__init__` | docstring |
| 50 | class | `TemporaryError` | docstring |
| 53 | method | `TemporaryError.__init__` | docstring |
| 57 | class | `PermanentError` | docstring |
| 60 | method | `PermanentError.__init__` | docstring |
| 64 | function | `retry` | docstring, return type, param types: `func` |
| 113 | async function | `retry_async` | docstring, return type, param types: `func` |
| 162 | function | `retry_with_backoff` | docstring, return type, param types: `func`, `initial_interval`, `max_interval`, `exponent`, `max_elapsed_time` |
| 190 | async function | `retry_with_backoff_async` | docstring, return type, param types: `func`, `initial_interval`, `max_interval`, `exponent`, `max_elapsed_time` |

### `nfl/utils/security.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 38 | function | `do_browser_auth` | docstring |

### `nfl/utils/serializers.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | function | `serialize_decimal` | docstring, return type |
| 32 | function | `validate_decimal` | docstring, return type, param types: `d` |
| 45 | function | `serialize_float` | docstring, return type |
| 61 | function | `validate_float` | docstring, return type, param types: `f` |
| 74 | function | `serialize_int` | docstring, return type |
| 90 | function | `validate_int` | docstring, return type, param types: `b` |
| 103 | function | `validate_open_enum` | docstring, return type |
| 123 | function | `validate_const` | docstring, return type, param types: `v` |
| 137 | function | `unmarshal_json` | docstring, param types: `raw` |
| 141 | function | `unmarshal` | docstring, param types: `val` |
| 154 | function | `marshal_json` | docstring, return type, param types: `val`, `typ` |
| 174 | function | `is_nullable` | docstring, return type, param types: `field` |
| 198 | function | `stream_to_text` | docstring |
| 202 | async function | `stream_to_text_async` | docstring |
| 206 | function | `stream_to_bytes` | docstring |
| 210 | async function | `stream_to_bytes_async` | docstring |
| 214 | function | `get_pydantic_model` | docstring |
| 221 | function | `_contains_pydantic_model` | docstring |

### `nfl/utils/unmarshal_json_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | function | `int_to_str` | docstring, return type, param types: `value` |
| 18 | function | `unmarshal_json_response` | docstring |

### `nfl/utils/url.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 28 | function | `generate_url` | docstring |
| 48 | function | `_populate_path_params` | docstring |
| 140 | function | `is_optional` | docstring, return type, param types: `field` |
| 144 | function | `template_url` | docstring |
| 151 | function | `remove_suffix` | docstring, return type, param types: `input_string`, `suffix` |

### `nfl/utils/values.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 17 | function | `match_content_type` | docstring |
| 36 | function | `match_status_codes` | docstring |
| 52 | function | `cast_partial` | docstring, return type, param types: `typ` |
| 56 | function | `get_global_from_env` | docstring |
| 70 | function | `match_response` | docstring |
| 79 | function | `_populate_from_globals` | docstring |
| 111 | function | `_val_to_string` | docstring, param types: `val` |
| 122 | function | `_get_serialized_params` | docstring |
| 134 | function | `_is_set` | docstring |

---

## `nfl/hooks` (5 items)

### `nfl/_hooks/hack_auth.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 14 | class | `HackAuthHook` | docstring |
| 34 | method | `HackAuthHook._do_refresh_token` | docstring, return type, param types: `refresh_token` |
| 41 | method | `HackAuthHook.before_request` | docstring |

### `nfl/_hooks/registration.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | function | `init_hooks` | return type |

### `nfl/_hooks/sdkhooks.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 9 | method | `SDKHooks.__init__` | docstring |

---

## `nfl/errors` (6 items)

### `nfl/errors/__init__.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 26 | function | `__getattr__` | docstring |
| 30 | function | `__dir__` | docstring, return type |

### `nfl/errors/griddynfldefaulterror.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 15 | method | `GriddyNFLDefaultError.__init__` | docstring |

### `nfl/errors/griddynflerror.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | method | `GriddyNFLError.__init__` | docstring |

### `nfl/errors/responsevalidationerror.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | method | `ResponseValidationError.__init__` | docstring |
| 24 | method | `ResponseValidationError.cause` | return type |

---

## `nfl/endpoints/regular` (13 items)

### `nfl/endpoints/regular/content/__init__.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `VideoContent` | docstring |

### `nfl/endpoints/regular/experience/__init__.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `Experience` | docstring |

### `nfl/endpoints/regular/football/combine.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `Combine` | docstring |

### `nfl/endpoints/regular/football/draft.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `Draft` | docstring |

### `nfl/endpoints/regular/football/games.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `Games` | docstring |

### `nfl/endpoints/regular/football/rosters.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `Rosters` | docstring |

### `nfl/endpoints/regular/football/standings.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `Standings` | docstring |

### `nfl/endpoints/regular/football/stats/__init__.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 31 | method | `FootballStatsSDK.__init__` | docstring |

### `nfl/endpoints/regular/football/stats/historical.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `HistoricalStats` | docstring |

### `nfl/endpoints/regular/football/stats/live.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `LiveStats` | docstring |

### `nfl/endpoints/regular/football/teams.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `Teams` | docstring |

### `nfl/endpoints/regular/football/venues.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `Venues` | docstring |

### `nfl/endpoints/regular/football/weeks.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `Weeks` | docstring |

---

## `nfl/endpoints/pro` (14 items)

### `nfl/endpoints/pro/__init__.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 7 | class | `ProSDK` | docstring |
| 8 | method | `ProSDK.__init__` | docstring |

### `nfl/endpoints/pro/content.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 18 | class | `Content` | docstring |

### `nfl/endpoints/pro/games.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 17 | class | `ProGames` | docstring |

### `nfl/endpoints/pro/players.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `Players` | docstring |

### `nfl/endpoints/pro/stats/__init__.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 66 | method | `StatsSDK.__init__` | docstring |

### `nfl/endpoints/pro/stats/base.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 19 | method | `PlayerStatsBase._make_stats_config` | param types: `**kwargs` |

### `nfl/endpoints/pro/stats/defense.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `PlayerDefenseStats` | docstring |

### `nfl/endpoints/pro/stats/passing.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `PlayerPassingStats` | docstring |

### `nfl/endpoints/pro/stats/receiving.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `PlayerReceivingStats` | docstring |

### `nfl/endpoints/pro/stats/rushing.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `PlayerRushingStats` | docstring |

### `nfl/endpoints/pro/stats/team_defense.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `TeamDefenseStats` | docstring |

### `nfl/endpoints/pro/teams.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `Teams` | docstring |

### `nfl/endpoints/pro/transactions.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `Transactions` | docstring |

---

## `nfl/models` (342 items)

### `nfl/models/__init__.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 2068 | function | `__getattr__` | docstring |
| 2072 | function | `__dir__` | docstring, return type |

### `nfl/models/entities/award.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 22 | class | `Award` | docstring |

### `nfl/models/entities/boxscore_schedule.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 18 | class | `BoxscoreSchedule` | docstring |

### `nfl/models/entities/boxscore_score.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `BoxscoreScore` | docstring |

### `nfl/models/entities/boxscore_site.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `BoxscoreSite` | docstring |

### `nfl/models/entities/boxscore_team.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 14 | class | `BoxscoreTeam` | docstring |

### `nfl/models/entities/broadcast_info.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `InternationalWatchOption` | docstring |
| 17 | class | `StreamingNetwork` | docstring |
| 32 | class | `BroadcastInfo` | docstring |

### `nfl/models/entities/career_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `CareerStats` | docstring |

### `nfl/models/entities/clinched.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `Clinched` | docstring |

### `nfl/models/entities/coaches_film_video.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 28 | class | `Cta` | docstring |
| 32 | class | `Image` | docstring |
| 36 | class | `PromoAsset` | docstring |
| 51 | class | `Video` | docstring |
| 55 | class | `CoachesFilmVideo` | docstring |

### `nfl/models/entities/combine_events.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 5 | class | `HasDesignation` | docstring |
| 10 | class | `BenchPress` | docstring |
| 15 | class | `BroadJump` | docstring |
| 20 | class | `FortyYardDash` | docstring |
| 25 | class | `TenYardSplit` | docstring |
| 30 | class | `ThreeConeDrill` | docstring |
| 35 | class | `TwentyYardShuffle` | docstring |
| 40 | class | `VerticalJump` | docstring |

### `nfl/models/entities/combine_profile.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 19 | class | `CombinePerson` | docstring |
| 36 | class | `CombineProfile` | docstring |

### `nfl/models/entities/conference.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `Conference` | docstring |

### `nfl/models/entities/contract_info.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `ContractInfo` | docstring |

### `nfl/models/entities/current_game.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 24 | class | `CurrentGameExtension` | docstring |
| 28 | class | `CurrentGame` | docstring |

### `nfl/models/entities/defensive_nearest_defender_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 17 | class | `DefensiveNearestDefenderStats` | docstring |

### `nfl/models/entities/defensive_pass_rush_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 17 | class | `DefensivePassRushStats` | docstring |

### `nfl/models/entities/defensive_player_overview_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 18 | class | `DefensivePlayerOverviewStats` | docstring |

### `nfl/models/entities/defensive_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `DefensiveStats` | docstring |

### `nfl/models/entities/division.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `Division` | docstring |

### `nfl/models/entities/draft_day.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 7 | class | `DraftDay` | docstring |

### `nfl/models/entities/draft_pick.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 9 | class | `Tweet` | docstring |
| 14 | class | `DraftPick` | docstring |

### `nfl/models/entities/drive.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 25 | class | `Drive` | docstring |

### `nfl/models/entities/external_id.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 8 | class | `ExternalID` | docstring |

### `nfl/models/entities/fantasy_player_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 31 | class | `FantasyPlayerStats` | docstring |

### `nfl/models/entities/film_card.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 36 | class | `FilmCard` | docstring |

### `nfl/models/entities/film_room_play.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 14 | class | `FilmroomPlay` | docstring |

### `nfl/models/entities/football_roster.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `FootballRoster` | docstring |

### `nfl/models/entities/futures_market.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `FuturesMarket` | docstring |

### `nfl/models/entities/game.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 23 | class | `GameExtension` | docstring |
| 33 | class | `Game` | docstring |

### `nfl/models/entities/game_center_schedule.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `GamecenterSchedule` | docstring |

### `nfl/models/entities/game_detail.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 17 | class | `GameDetail` | docstring |

### `nfl/models/entities/game_odds.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 15 | class | `GameOdds` | docstring |

### `nfl/models/entities/game_schedule.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 17 | class | `GameSchedule` | docstring |

### `nfl/models/entities/game_score.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `GameScore` | docstring |

### `nfl/models/entities/game_site.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `GameSite` | docstring |

### `nfl/models/entities/game_team.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `Score` | docstring |
| 16 | class | `GameTeam` | docstring |

### `nfl/models/entities/historical_stat_categories.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 15 | class | `HistoricalDefenseStats` | docstring |
| 96 | class | `HistoricalPassingStats` | docstring |
| 183 | class | `HistoricalRushingStats` | docstring |
| 242 | class | `HistoricalReceivingStats` | docstring |
| 307 | class | `HistoricalKickReturnsStats` | docstring |
| 342 | class | `HistoricalPuntReturnsStats` | docstring |
| 381 | class | `KickingDetails` | docstring |
| 398 | class | `HistoricalKickingStats` | docstring |
| 437 | class | `HistoricalKickoffsStats` | docstring |
| 482 | class | `HistoricalPuntingStats` | docstring |
| 529 | class | `HistoricalPenaltiesStats` | docstring |
| 540 | class | `HistoricalScoringStats` | docstring |
| 579 | class | `HistoricalDownAndDistanceStats` | docstring |
| 626 | class | `HistoricalRedzoneStats` | docstring |
| 639 | class | `HistoricalGoalToGoStats` | docstring |
| 650 | class | `HistoricalTimeOfPossessionStats` | docstring |
| 669 | class | `HistoricalStatCategories` | docstring |

### `nfl/models/entities/injury_entry.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 22 | class | `PracticeStatus` | docstring |
| 33 | class | `InjuryEntry` | docstring |

### `nfl/models/entities/insight.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 35 | class | `Insight` | docstring |

### `nfl/models/entities/kicking_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `KickingStats` | docstring |

### `nfl/models/entities/live_game.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `AwayTeam` | docstring |
| 20 | class | `HomeTeam` | docstring |

### `nfl/models/entities/multiple_rankings_category.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `MultipleRankingsCategoryPagination` | docstring |
| 18 | class | `MultipleRankingsCategory` | docstring |

### `nfl/models/entities/nfl_auth.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `NFLAuth` | docstring |

### `nfl/models/entities/odds_selection.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `OddsSelection` | docstring |

### `nfl/models/entities/overall_record.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `OverallRecordPoints` | docstring |
| 28 | class | `Streak` | docstring |
| 36 | class | `OverallRecord` | docstring |

### `nfl/models/entities/pagination.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 8 | class | `Pagination` | docstring |

### `nfl/models/entities/passer_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `Zone` | docstring |
| 17 | class | `PasserStats` | docstring |

### `nfl/models/entities/passing_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `PassingStats` | docstring |

### `nfl/models/entities/penalty.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `Penalty` | docstring |

### `nfl/models/entities/person.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `Person` | docstring |

### `nfl/models/entities/play.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `Play` | docstring |

### `nfl/models/entities/play_detail.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 28 | class | `PlayDetail` | docstring |

### `nfl/models/entities/play_participant.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 23 | class | `PlayParticipant` | docstring |

### `nfl/models/entities/play_player.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `PlayPlayer` | docstring |

### `nfl/models/entities/play_stat.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `PlayStat` | docstring |

### `nfl/models/entities/play_win_probability.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `PlayWinProbability` | docstring |

### `nfl/models/entities/player.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `Player` | docstring |

### `nfl/models/entities/player_detail.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 14 | class | `PlayerDetail` | docstring |

### `nfl/models/entities/player_game_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 14 | class | `PlayerGameStats` | docstring |

### `nfl/models/entities/player_passing_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `PlayerPassingStats` | docstring |

### `nfl/models/entities/player_projection.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `WeekPoint` | docstring |
| 23 | class | `WeekStat` | docstring |
| 30 | class | `Relationships` | docstring |
| 44 | class | `PlayerProjection` | docstring |

### `nfl/models/entities/player_receiving_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 15 | class | `PlayerReceivingStats` | docstring |

### `nfl/models/entities/player_rushing_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 15 | class | `PlayerRushingStats` | docstring |

### `nfl/models/entities/player_week_projected_points.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `PlayerWeekProjectedPointsAttributes` | docstring |
| 31 | class | `PlayerWeekProjectedPoints` | docstring |

### `nfl/models/entities/player_week_projected_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `PlayerWeekProjectedStatsAttributes` | docstring |
| 174 | class | `PlayerWeekProjectedStats` | docstring |

### `nfl/models/entities/points_record.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `PointsRecordPoints` | docstring |
| 17 | class | `PointsRecord` | docstring |

### `nfl/models/entities/pro_game.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 23 | class | `ProGameExtension` | docstring |
| 33 | class | `ProGame` | docstring |

### `nfl/models/entities/pro_play.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `UnofficialPlay` | docstring |
| 18 | class | `OffenseInfo` | docstring |
| 25 | class | `DefenseInfo` | docstring |
| 37 | class | `PassInfo` | docstring |
| 45 | class | `RecInfo` | docstring |
| 52 | class | `ProPlay` | docstring |

### `nfl/models/entities/pro_team.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 26 | class | `ProTeam` | docstring |

### `nfl/models/entities/pro_week.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 22 | class | `ProWeek` | docstring |

### `nfl/models/entities/receiving_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `ReceivingStats` | docstring |

### `nfl/models/entities/record.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 8 | class | `Record` | docstring |

### `nfl/models/entities/response_metadata.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `ResponseMetadata` | docstring |

### `nfl/models/entities/rushing_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `RushingStats` | docstring |

### `nfl/models/entities/schedule_team.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 14 | class | `ScheduleTeam` | docstring |

### `nfl/models/entities/scheduled_game.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 17 | class | `ScheduledGame` | docstring |

### `nfl/models/entities/scoring_play.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 20 | class | `ScoringPlay` | docstring |

### `nfl/models/entities/search_players_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 9 | class | `SearchPlayersRequest` | docstring |

### `nfl/models/entities/season_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 18 | class | `SeasonStats` | docstring |

### `nfl/models/entities/security.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `Security` | docstring |

### `nfl/models/entities/site.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `Site` | docstring |

### `nfl/models/entities/social_media.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 8 | class | `SocialMedia` | docstring |

### `nfl/models/entities/standings.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `StandingsTeam` | docstring |
| 24 | class | `Standings` | docstring |

### `nfl/models/entities/standings_record.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `StandingsRecordPoints` | docstring |
| 19 | class | `StandingsRecord` | docstring |

### `nfl/models/entities/statistic_ranking.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 8 | class | `Statistic` | docstring |
| 16 | class | `StatisticRanking` | docstring |

### `nfl/models/entities/team.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 26 | class | `Team` | docstring |

### `nfl/models/entities/team_boxscore.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `TeamBoxscore` | docstring |

### `nfl/models/entities/team_defense_pass_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `TeamDefensePassStats` | docstring |

### `nfl/models/entities/team_defense_rush_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `TeamDefenseRushStats` | docstring |

### `nfl/models/entities/team_defense_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `TeamDefenseStats` | docstring |

### `nfl/models/entities/team_game_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `TeamGameStats` | docstring |

### `nfl/models/entities/team_injury_report.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 14 | class | `TeamInjuryReport` | docstring |

### `nfl/models/entities/team_needs.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `TeamNeeds` | docstring |

### `nfl/models/entities/team_offense_overview_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `TeamOffenseStats` | docstring |

### `nfl/models/entities/team_offense_pass_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `TeamOffensePassStats` | docstring |

### `nfl/models/entities/team_offense_rush_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 7 | class | `TeamOffenseRushStats` | docstring |

### `nfl/models/entities/team_ranking_entry.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `TeamRankingEntry` | docstring |

### `nfl/models/entities/team_rankings.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 14 | class | `TeamRankings` | docstring |

### `nfl/models/entities/team_score.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `TeamScore` | docstring |

### `nfl/models/entities/team_venue.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 8 | class | `TeamVenue` | docstring |

### `nfl/models/entities/ticket_vendor.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `TicketVendor` | docstring |

### `nfl/models/entities/transaction.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 25 | class | `Transaction` | docstring |

### `nfl/models/entities/venue.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `Venue` | docstring |

### `nfl/models/entities/venue_info.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `VenueInfo` | docstring |

### `nfl/models/entities/video_authorizations.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `NflPlusPlusRequirements` | docstring |
| 17 | class | `NFLPLUSPLUSNFLPLUSCOACHESFILM` | docstring |
| 21 | class | `NflPlusPlus` | docstring |
| 28 | class | `NflPlusPremiumRequirements` | docstring |
| 34 | class | `NFLPLUSPremiumNFLPLUSCOACHESFILM` | docstring |
| 38 | class | `NflPlusPremium` | docstring |
| 45 | class | `ProPremiumRequirements` | docstring |
| 51 | class | `ProPremiumNFLPLUSCOACHESFILM` | docstring |
| 55 | class | `ProPremium` | docstring |

### `nfl/models/entities/video_game_play_ids.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 9 | class | `VideoGamePlayIds` | docstring |

### `nfl/models/entities/video_thumbnail.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 9 | class | `VideoThumbnail` | docstring |

### `nfl/models/entities/week.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 22 | class | `Week` | docstring |

### `nfl/models/entities/weekly_game_detail.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 23 | class | `WeeklyGameDetailExtension` | docstring |
| 33 | class | `DriveChartPlayStat` | docstring |
| 50 | class | `DriveChartPlay` | docstring |
| 115 | class | `Drive` | docstring |
| 178 | class | `Replay` | docstring |
| 206 | class | `WeeklyGameDetail` | docstring |

### `nfl/models/entities/weekly_player_passing_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `WeeklyPlayerPassingStats` | docstring |

### `nfl/models/entities/weekly_player_rushing_stats.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `WeeklyPlayerRushingStats` | docstring |

### `nfl/models/requests/get_coaches_film_videos_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `GetCoachesFilmVideosRequest` | docstring |

### `nfl/models/requests/get_combine_profiles_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 9 | class | `GetCombineProfilesRequest` | docstring |

### `nfl/models/requests/get_combine_rankings_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `GetCombineRankingsRequest` | docstring |

### `nfl/models/requests/get_defensive_nearest_defender_stats_by_season_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 19 | class | `GetDefensiveNearestDefenderStatsBySeasonRequest` | docstring |

### `nfl/models/requests/get_defensive_nearest_defender_stats_by_week_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 20 | class | `GetDefensiveNearestDefenderStatsByWeekRequest` | docstring |

### `nfl/models/requests/get_defensive_overview_stats_by_season_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 35 | class | `GetDefensiveOverviewStatsBySeasonRequest` | docstring |

### `nfl/models/requests/get_defensive_overview_stats_by_week_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 36 | class | `GetDefensiveOverviewStatsByWeekRequest` | docstring |

### `nfl/models/requests/get_defensive_passrush_stats_by_season_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 30 | class | `GetDefensivePassRushStatsBySeasonRequest` | docstring |

### `nfl/models/requests/get_defensive_passrush_stats_by_week_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 31 | class | `GetDefensivePassRushStatsByWeekRequest` | docstring |

### `nfl/models/requests/get_defensive_stats_by_season_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 34 | class | `GetDefensiveStatsBySeasonRequest` | docstring |

### `nfl/models/requests/get_draft_info_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `GetDraftInfoRequest` | docstring |

### `nfl/models/requests/get_draft_picks_report_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 9 | class | `GetDraftPicksReportRequest` | docstring |

### `nfl/models/requests/get_fantasy_stats_by_season_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 42 | class | `GetFantasyStatsBySeasonRequest` | docstring |

### `nfl/models/requests/get_film_room_plays_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 90 | class | `GetFilmroomPlaysRequest` | docstring |

### `nfl/models/requests/get_football_boxscore_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `GetFootballBoxScoreRequest` | docstring |

### `nfl/models/requests/get_football_games_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `GetFootballGamesRequest` | docstring |

### `nfl/models/requests/get_football_rosters_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 7 | class | `GetFootballRostersRequest` | docstring |

### `nfl/models/requests/get_football_teams_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 7 | class | `GetFootballTeamsRequest` | docstring |

### `nfl/models/requests/get_game_center_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `GetGamecenterRequest` | docstring |

### `nfl/models/requests/get_game_details_by_slug_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `GetGameDetailsBySlugRequest` | docstring |

### `nfl/models/requests/get_game_details_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `GetGameDetailsRequest` | docstring |

### `nfl/models/requests/get_game_insights_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `GetGameInsightsRequest` | docstring |

### `nfl/models/requests/get_game_matchup_rankings_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `GetGameMatchupRankingsRequest` | docstring |

### `nfl/models/requests/get_game_preview_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `GetGamePreviewRequest` | docstring |

### `nfl/models/requests/get_game_team_rankings_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `GetGameTeamRankingsRequest` | docstring |

### `nfl/models/requests/get_historical_player_stats_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `GetHistoricalPlayerStatsRequest` | docstring |

### `nfl/models/requests/get_historical_team_stats_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `GetHistoricalTeamStatsRequest` | docstring |

### `nfl/models/requests/get_injury_reports_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `GetInjuryReportsRequest` | docstring |

### `nfl/models/requests/get_live_game_scores_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `GetLiveGameScoresRequest` | docstring |

### `nfl/models/requests/get_live_game_stats_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `GetLiveGameStatsRequest` | docstring |

### `nfl/models/requests/get_live_player_statistics_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `GetLivePlayerStatisticsRequest` | docstring |

### `nfl/models/requests/get_live_team_statistics_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `GetLiveTeamStatisticsRequest` | docstring |

### `nfl/models/requests/get_multiple_rankings_all_teams_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `GetMultipleRankingsAllTeamsRequest` | docstring |

### `nfl/models/requests/get_play_by_play_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `GetPlayByPlayRequest` | docstring |

### `nfl/models/requests/get_play_list.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `GetPlayListRequest` | docstring |

### `nfl/models/requests/get_player_details_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `GetPlayerDetailsRequest` | docstring |

### `nfl/models/requests/get_player_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `GetPlayerRequest` | docstring |

### `nfl/models/requests/get_player_passing_stats_by_season_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 15 | class | `GetPlayerPassingStatsBySeasonRequest` | docstring |

### `nfl/models/requests/get_player_passing_stats_by_week_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `GetPlayerPassingStatsByWeekRequest` | docstring |

### `nfl/models/requests/get_player_receiving_stats_by_season_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 17 | class | `GetPlayerReceivingStatsBySeasonRequest` | docstring |

### `nfl/models/requests/get_player_receiving_stats_by_week_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 18 | class | `GetPlayerReceivingStatsByWeekRequest` | docstring |

### `nfl/models/requests/get_player_rushing_stats_by_season_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 41 | class | `GetPlayerRushingStatsBySeasonRequest` | docstring |

### `nfl/models/requests/get_player_rushing_stats_by_week_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 42 | class | `GetPlayerRushingStatsByWeekRequest` | docstring |

### `nfl/models/requests/get_players_team_roster_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `GetPlayersTeamRosterRequest` | docstring |

### `nfl/models/requests/get_plays_win_probability_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 18 | class | `GetPlaysWinProbabilityRequest` | docstring |

### `nfl/models/requests/get_projected_stats_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `GetProjectedStatsRequest` | docstring |

### `nfl/models/requests/get_schedule_season_weeks_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 9 | class | `GetScheduleSeasonWeeksRequest` | docstring |

### `nfl/models/requests/get_scheduled_game_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `GetScheduledGameRequest` | docstring |

### `nfl/models/requests/get_scheduled_games_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `GetScheduledGamesRequest` | docstring |

### `nfl/models/requests/get_season_content_insights_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 24 | class | `GetSeasonContentInsightsRequest` | docstring |

### `nfl/models/requests/get_season_player_stats_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 40 | class | `GetSeasonPlayerStatsRequest` | docstring |

### `nfl/models/requests/get_season_weeks_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `GetSeasonWeeksRequest` | docstring |

### `nfl/models/requests/get_standings_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `GetStandingsRequest` | docstring |

### `nfl/models/requests/get_stats_boxscore_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `GetStatsBoxscoreRequest` | docstring |

### `nfl/models/requests/get_summary_play_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `GetSummaryPlayRequest` | docstring |

### `nfl/models/requests/get_team_defense_pass_stats_by_season_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 40 | class | `GetTeamDefensePassStatsBySeasonRequest` | docstring |

### `nfl/models/requests/get_team_defense_pass_stats_by_week_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 41 | class | `GetTeamDefensePassStatsByWeekRequest` | docstring |

### `nfl/models/requests/get_team_defense_rush_stats_by_season_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 37 | class | `GetTeamDefenseRushStatsBySeasonRequest` | docstring |

### `nfl/models/requests/get_team_defense_rush_stats_by_week_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 38 | class | `GetTeamDefenseRushStatsByWeekRequest` | docstring |

### `nfl/models/requests/get_team_defense_stats_by_season_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 68 | class | `GetTeamDefenseStatsBySeasonRequest` | docstring |

### `nfl/models/requests/get_team_defense_stats_by_week_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 69 | class | `GetTeamDefenseStatsByWeekRequest` | docstring |

### `nfl/models/requests/get_team_injuries_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `GetTeamInjuriesRequest` | docstring |

### `nfl/models/requests/get_team_needs_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 9 | class | `GetTeamNeedsRequest` | docstring |

### `nfl/models/requests/get_team_offense_overview_stats_by_season_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 56 | class | `GetTeamOffenseStatsBySeasonRequest` | docstring |

### `nfl/models/requests/get_team_offense_overview_stats_by_week_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 57 | class | `GetTeamOffenseStatsByWeekRequest` | docstring |

### `nfl/models/requests/get_team_offense_pass_stats_by_season_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 41 | class | `GetTeamOffensePassStatsBySeasonRequest` | docstring |

### `nfl/models/requests/get_team_offense_pass_stats_by_week_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 42 | class | `GetTeamOffensePassStatsByWeekRequest` | docstring |

### `nfl/models/requests/get_team_offense_rush_stats_by_season_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 15 | class | `GetTeamOffenseRushStatsBySeasonRequest` | docstring |

### `nfl/models/requests/get_team_offense_rush_stats_by_week_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `GetTeamOffenseRushStatsByWeekRequest` | docstring |

### `nfl/models/requests/get_team_roster_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `GetTeamRosterRequest` | docstring |

### `nfl/models/requests/get_team_schedule_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `GetTeamScheduleRequest` | docstring |

### `nfl/models/requests/get_team_standings_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `GetTeamStandingsRequest` | docstring |

### `nfl/models/requests/get_transactions_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 23 | class | `GetTransactionsRequest` | docstring |

### `nfl/models/requests/get_venues_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `GetVenuesRequest` | docstring |

### `nfl/models/requests/get_video_replays_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `GetVideoReplaysRequest` | docstring |

### `nfl/models/requests/get_week_of_date_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 7 | class | `GetWeekOfDateRequest` | docstring |

### `nfl/models/requests/get_weekly_betting_odds_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `GetWeeklyBettingOddsRequest` | docstring |

### `nfl/models/requests/get_weekly_game_details_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `GetWeeklyGameDetailsRequest` | docstring |

### `nfl/models/requests/get_weekly_team_roster_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `GetWeeklyTeamRosterRequest` | docstring |

### `nfl/models/requests/get_win_probability_min_op.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `GetWinProbabilityMinRequest` | docstring |

### `nfl/models/requests/refresh_token_request.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 19 | class | `RefreshTokenRequest` | docstring |

### `nfl/models/requests/token_request.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 19 | class | `TokenRequest` | docstring |

### `nfl/models/responses/boxscore_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `BoxscoreResponse` | docstring |

### `nfl/models/responses/boxscore_response_2.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 19 | class | `Away` | docstring |
| 25 | class | `Home` | docstring |
| 31 | class | `PlayerStats` | docstring |
| 37 | class | `TeamStats` | docstring |
| 43 | class | `BoxScoreResponse2` | docstring |

### `nfl/models/responses/coaches_film_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 14 | class | `CoachesFilmResponse` | docstring |

### `nfl/models/responses/combine_profiles_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `CombineProfilesResponse` | docstring |

### `nfl/models/responses/combine_rankings_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `CombineRankingsResponse` | docstring |

### `nfl/models/responses/current_games_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `CurrentGamesResponse` | docstring |

### `nfl/models/responses/defensive_overview_stats_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `DefensiveOverviewStatsResponse` | docstring |

### `nfl/models/responses/draft_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 14 | class | `DraftResponse` | docstring |

### `nfl/models/responses/fantasy_stats_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `FantasyStatsResponse` | docstring |

### `nfl/models/responses/film_room_plays_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `FilmroomPlaysResponse` | docstring |

### `nfl/models/responses/football_games_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `FootballGamesResponse` | docstring |

### `nfl/models/responses/football_rosters_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 7 | class | `FootballRostersResponse` | docstring |

### `nfl/models/responses/football_teams_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 8 | class | `FootballTeamsResponse` | docstring |

### `nfl/models/responses/futures_odds_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 14 | class | `FuturesOddsResponseData` | docstring |
| 24 | class | `FuturesOddsResponse` | docstring |

### `nfl/models/responses/game_center_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 15 | class | `PassDistanceLeaders` | docstring |
| 19 | class | `SpeedLeaders` | docstring |
| 23 | class | `TimeToSackLeaders` | docstring |
| 27 | class | `Leaders` | docstring |
| 41 | class | `LeagueAverageSeparationToQb` | docstring |
| 45 | class | `PassRushers` | docstring |
| 56 | class | `Passers` | docstring |
| 62 | class | `LeagueAverageReceiverSeparation` | docstring |
| 66 | class | `Receivers` | docstring |
| 77 | class | `Rushers` | docstring |
| 83 | class | `GamecenterResponse` | docstring |

### `nfl/models/responses/game_stats_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `GameStatsResponse` | docstring |

### `nfl/models/responses/games_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `GamesResponse` | docstring |

### `nfl/models/responses/historical_player_stats_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `PersonStatLineup` | docstring |

### `nfl/models/responses/historical_team_stats_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `HistoricalGameInfo` | docstring |

### `nfl/models/responses/home_filmcards_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 9 | class | `HomeFilmCardsResponse` | docstring |

### `nfl/models/responses/injury_report_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `InjuryReportResponse` | docstring |

### `nfl/models/responses/lives_cores_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `LiveScoresResponse` | docstring |

### `nfl/models/responses/matchup_rankings_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 15 | class | `MatchupRankingsResponse` | docstring |

### `nfl/models/responses/nearest_defender_stats_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `NearestDefenderStatsResponse` | docstring |

### `nfl/models/responses/pass_rush_stats_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `PassRushStatsResponse` | docstring |

### `nfl/models/responses/passing_stats_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `PassingStatsResponse` | docstring |

### `nfl/models/responses/play_by_play_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 15 | class | `PlayByPlayResponse` | docstring |

### `nfl/models/responses/play_summary_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 14 | class | `PlaySummaryResponse` | docstring |

### `nfl/models/responses/play_win_probability_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `PlayWinProbabilityResponse` | docstring |

### `nfl/models/responses/player_search_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `PlayerSearchResponse` | docstring |

### `nfl/models/responses/player_stats_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `PlayerStatsResponsePagination` | docstring |
| 25 | class | `PlayerStatsResponsePlayer` | docstring |
| 34 | class | `PlayerStatsResponse` | docstring |

### `nfl/models/responses/playlist_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `PlaylistResponse` | docstring |

### `nfl/models/responses/projected_stats_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 23 | class | `Page` | docstring |
| 31 | class | `Meta` | docstring |
| 35 | class | `ProjectedStatsResponsePagination` | docstring |

### `nfl/models/responses/receiving_stats_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `ReceivingStatsResponse` | docstring |

### `nfl/models/responses/roster_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `Roster` | docstring |
| 31 | class | `RosterResponse` | docstring |

### `nfl/models/responses/rushing_stats_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `RushingStatsResponse` | docstring |

### `nfl/models/responses/season_weeks_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `SeasonWeeksResponse` | docstring |

### `nfl/models/responses/standings_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 14 | class | `StandingsResponseWeek` | docstring |
| 20 | class | `StandingsResponse` | docstring |

### `nfl/models/responses/team_defense_pass_stats_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `TeamDefensePassStatsResponse` | docstring |

### `nfl/models/responses/team_defense_rush_stats_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `TeamDefenseRushStatsResponse` | docstring |

### `nfl/models/responses/team_defense_stats_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `TeamDefenseStatsResponse` | docstring |

### `nfl/models/responses/team_needs_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 8 | class | `TeamNeedsResponse` | docstring |

### `nfl/models/responses/team_offense_overview_stats_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `TeamOffenseStatsResponse` | docstring |

### `nfl/models/responses/team_offense_pass_stats_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `TeamOffensePassStatsResponse` | docstring |

### `nfl/models/responses/team_offense_rush_stats_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `TeamOffenseRushStatsResponse` | docstring |

### `nfl/models/responses/team_rankings_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `TeamRankingsResponse` | docstring |

### `nfl/models/responses/team_roster_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `TeamRosterResponse` | docstring |

### `nfl/models/responses/token_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 9 | class | `TokenResponse` | docstring |

### `nfl/models/responses/transactions_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `TransactionsResponse` | docstring |

### `nfl/models/responses/venues_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `VenuesResponse` | docstring |

### `nfl/models/responses/video_replays_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 14 | class | `VideoReplaysMetadata` | docstring |
| 18 | class | `VideoReplaysPagination` | docstring |

### `nfl/models/responses/weekly_odds_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | class | `WeeklyOddsResponse` | docstring |

### `nfl/models/responses/weekly_passing_stats_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `WeeklyPassingStatsResponse` | docstring |

### `nfl/models/responses/weekly_roster_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 14 | class | `WeeklyRosterResponse` | docstring |

### `nfl/models/responses/weekly_rushing_stats_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `WeeklyRushingStatsResponse` | docstring |

### `nfl/models/responses/weeks_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `WeeksResponse` | docstring |

### `nfl/models/responses/win_probability_response.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 14 | class | `WinProbabilityResponse` | docstring |

---

## `pfr` (16 items)

### `pfr/_hooks/registration.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 4 | function | `init_hooks` | return type |

### `pfr/basesdk.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 25 | method | `PfrParser.__call__` | docstring |
| 42 | method | `BaseSDK.__init__` | docstring |
| 58 | method | `BaseSDK._default_error_cls` | docstring |
| 62 | method | `BaseSDK._no_response_error_cls` | docstring |
| 66 | method | `BaseSDK._security_model_cls` | docstring |
| 70 | method | `BaseSDK._security_env_mapping` | docstring |
| 73 | method | `BaseSDK._build_url` | docstring |
| 92 | method | `BaseSDK._parse_and_validate` | docstring |

### `pfr/sdk.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 147 | method | `GriddyPFR._get_debug_logger_env_var` | docstring |
| 150 | method | `GriddyPFR._create_security` | docstring |
| 157 | method | `GriddyPFR._create_sdk_configuration` | docstring |
| 160 | method | `GriddyPFR._create_hooks` | docstring |

### `pfr/sdkconfiguration.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 15 | class | `SDKConfiguration` | docstring |
| 20 | method | `SDKConfiguration.__post_init__` | docstring |
| 24 | method | `SDKConfiguration.get_server_details` | docstring |

---

## `pfr/endpoints` (35 items)

### `pfr/endpoints/awards.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 21 | method | `Awards._parser` | docstring |

### `pfr/endpoints/coaches.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 22 | method | `Coaches._parser` | docstring |

### `pfr/endpoints/draft.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 22 | method | `Draft._parser` | docstring |

### `pfr/endpoints/executives.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 22 | method | `Executives._parser` | docstring |

### `pfr/endpoints/fantasy.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 41 | method | `Fantasy._parser` | docstring |

### `pfr/endpoints/frivolities.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 92 | method | `Frivolities._multi_team_parser` | docstring |
| 96 | method | `Frivolities._milestones_parser` | docstring |
| 100 | method | `Frivolities._upcoming_parser` | docstring |
| 104 | method | `Frivolities._birthdays_parser` | docstring |
| 108 | method | `Frivolities._birthplaces_parser` | docstring |
| 112 | method | `Frivolities._born_before_parser` | docstring |
| 116 | method | `Frivolities._uniform_numbers_parser` | docstring |
| 120 | method | `Frivolities._qb_wins_parser` | docstring |
| 124 | method | `Frivolities._non_qb_passers_parser` | docstring |
| 128 | method | `Frivolities._non_skill_pos_td_parser` | docstring |
| 132 | method | `Frivolities._octopus_tracker_parser` | docstring |
| 136 | method | `Frivolities._overtime_ties_parser` | docstring |
| 140 | method | `Frivolities._cups_of_coffee_parser` | docstring |
| 144 | method | `Frivolities._multi_sport_players_parser` | docstring |
| 148 | method | `Frivolities._pronunciation_guide_parser` | docstring |
| 152 | method | `Frivolities._last_undefeated_parser` | docstring |
| 156 | method | `Frivolities._standings_on_date_parser` | docstring |

### `pfr/endpoints/games.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 22 | method | `Games._parser` | docstring |

### `pfr/endpoints/hof.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 21 | method | `Hof._parser` | docstring |

### `pfr/endpoints/leaders.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 22 | method | `Leaders._parser` | docstring |

### `pfr/endpoints/officials.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 22 | method | `Officials._parser` | docstring |

### `pfr/endpoints/players.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 22 | method | `Players._parser` | docstring |

### `pfr/endpoints/probowl.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 21 | method | `ProBowl._parser` | docstring |

### `pfr/endpoints/schedule.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 22 | method | `Schedule._parser` | docstring |

### `pfr/endpoints/schools.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 21 | method | `Schools._parser` | docstring |

### `pfr/endpoints/seasons.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 23 | method | `Seasons._parser` | docstring |

### `pfr/endpoints/stadiums.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 22 | method | `Stadiums._parser` | docstring |

### `pfr/endpoints/superbowl.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 22 | method | `SuperBowl._parser` | docstring |

### `pfr/endpoints/teams.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 23 | method | `Teams._team_season_parser` | docstring |
| 27 | method | `Teams._franchise_parser` | docstring |

---

## `pfr/models` (124 items)

### `pfr/models/__init__.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 508 | function | `__getattr__` | docstring |
| 512 | function | `__dir__` | docstring, return type |

### `pfr/models/entities/awards.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 20 | class | `AwardWinner` | docstring |
| 38 | class | `AwardHistory` | docstring |
| 48 | class | `HofPlayer` | docstring |
| 91 | class | `HallOfFame` | docstring |
| 100 | class | `ProBowlPlayer` | docstring |
| 137 | class | `ProBowlRoster` | docstring |

### `pfr/models/entities/birthdays.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 8 | class | `BirthdayPlayer` | docstring |
| 40 | class | `Birthdays` | docstring |

### `pfr/models/entities/birthplaces.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 19 | class | `BirthplaceLocation` | docstring |
| 39 | class | `BirthplaceLanding` | docstring |
| 47 | class | `BirthplacePlayer` | docstring |
| 79 | class | `BirthplaceFiltered` | docstring |

### `pfr/models/entities/coach_profile.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 17 | class | `CoachBio` | docstring |
| 38 | class | `CoachingResult` | docstring |
| 67 | class | `CoachingResultTotal` | docstring |
| 87 | class | `CoachingRank` | docstring |
| 127 | class | `CoachingHistoryEntry` | docstring |
| 139 | class | `CoachingTreeEntry` | docstring |
| 148 | class | `ChallengeResult` | docstring |
| 161 | class | `CoachProfile` | docstring |

### `pfr/models/entities/draft.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 20 | class | `DraftPick` | docstring |
| 61 | class | `YearDraft` | docstring |
| 71 | class | `CombineEntry` | docstring |
| 99 | class | `CombineResults` | docstring |
| 109 | class | `TeamDraftPick` | docstring |
| 146 | class | `TeamDraft` | docstring |

### `pfr/models/entities/executive_profile.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `ExecutiveBio` | docstring |
| 23 | class | `ExecutiveResult` | docstring |
| 43 | class | `ExecutiveResultsTotal` | docstring |
| 56 | class | `ExecutiveProfile` | docstring |

### `pfr/models/entities/fantasy.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 28 | class | `FantasyPlayer` | docstring |
| 79 | class | `TopFantasyPlayers` | docstring |
| 88 | class | `FantasyMatchupPlayer` | docstring |
| 139 | class | `FantasyMatchups` | docstring |
| 149 | class | `FantasyPointsAllowedTeam` | docstring |
| 190 | class | `FantasyPointsAllowed` | docstring |
| 199 | class | `RedZonePassingPlayer` | docstring |
| 228 | class | `RedZonePassing` | docstring |
| 237 | class | `RedZoneReceivingPlayer` | docstring |
| 266 | class | `RedZoneReceiving` | docstring |
| 275 | class | `RedZoneRushingPlayer` | docstring |
| 305 | class | `RedZoneRushing` | docstring |

### `pfr/models/entities/game_details.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 12 | class | `ScoreboxTeam` | docstring |
| 21 | class | `ScoreboxMeta` | docstring |
| 29 | class | `Scorebox` | docstring |
| 38 | class | `LinescoreEntry` | docstring |
| 47 | class | `ScoringPlay` | docstring |
| 60 | class | `ExpectedPoints` | docstring |
| 82 | class | `PlayerOffense` | docstring |
| 112 | class | `PlayerDefense` | docstring |
| 137 | class | `PlayerReturn` | docstring |
| 157 | class | `PlayerKicking` | docstring |
| 175 | class | `Starter` | docstring |
| 185 | class | `SnapCount` | docstring |
| 201 | class | `Drive` | docstring |
| 215 | class | `GameDetails` | docstring |

### `pfr/models/entities/leaders.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `LeaderEntry` | docstring |
| 34 | class | `Leaderboard` | docstring |

### `pfr/models/entities/multi_team_players.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 8 | class | `TopPlayerSummary` | docstring |
| 15 | class | `MultiTeamPlayerStats` | docstring |
| 22 | class | `StatsTable` | docstring |
| 28 | class | `MultiTeamPlayers` | docstring |

### `pfr/models/entities/official_profile.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `OfficialBio` | docstring |
| 24 | class | `OfficialSeasonStat` | docstring |
| 50 | class | `OfficialGame` | docstring |
| 69 | class | `OfficialProfile` | docstring |

### `pfr/models/entities/player_profile.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `PlayerNames` | docstring |
| 23 | class | `BirthPlace` | docstring |
| 31 | class | `RoundAndOverall` | docstring |
| 36 | class | `DraftInfo` | docstring |
| 45 | class | `PlayerBio` | docstring |
| 62 | class | `JerseyNumber` | docstring |
| 72 | class | `Transaction` | docstring |
| 80 | class | `PlayerStatistics` | docstring |
| 88 | class | `PlayerProfile` | docstring |

### `pfr/models/entities/players_born_before.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 14 | class | `PlayerBornBefore` | docstring |
| 47 | class | `PlayersBornBefore` | docstring |

### `pfr/models/entities/qb_wins.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `QBWinEntry` | docstring |
| 18 | class | `QBWins` | docstring |

### `pfr/models/entities/schedule_game.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 8 | class | `ScheduleGame` | docstring |

### `pfr/models/entities/schools.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 19 | class | `College` | docstring |
| 46 | class | `CollegeList` | docstring |
| 55 | class | `HighSchool` | docstring |
| 69 | class | `HighSchoolList` | docstring |

### `pfr/models/entities/season.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `ConferenceStanding` | docstring |
| 36 | class | `PlayoffGame` | docstring |
| 54 | class | `PlayoffStanding` | docstring |
| 67 | class | `SeasonOverview` | docstring |
| 87 | class | `SeasonStats` | docstring |
| 95 | class | `WeekGame` | docstring |
| 119 | class | `WeekSummary` | docstring |

### `pfr/models/entities/security.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 11 | class | `Security` | docstring |

### `pfr/models/entities/stadium.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 16 | class | `StadiumTeam` | docstring |
| 29 | class | `StadiumBio` | docstring |
| 41 | class | `StadiumLeader` | docstring |
| 52 | class | `StadiumBestGame` | docstring |
| 66 | class | `StadiumGameLeader` | docstring |
| 76 | class | `StadiumGameSummary` | docstring |
| 92 | class | `StadiumProfile` | docstring |

### `pfr/models/entities/statistical_milestones.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 8 | class | `MilestoneEntry` | docstring |
| 17 | class | `CareerLeader` | docstring |
| 27 | class | `StatisticalMilestones` | docstring |

### `pfr/models/entities/superbowl.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 20 | class | `SuperBowlGame` | docstring |
| 44 | class | `SuperBowlHistory` | docstring |
| 53 | class | `SuperBowlLeaderEntry` | docstring |
| 66 | class | `SuperBowlLeaderTable` | docstring |
| 76 | class | `SuperBowlLeaders` | docstring |
| 85 | class | `SuperBowlQB` | docstring |
| 96 | class | `SuperBowlStanding` | docstring |
| 115 | class | `SuperBowlStandings` | docstring |

### `pfr/models/entities/team_franchise.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `FranchiseLeader` | docstring |
| 16 | class | `FranchiseMeta` | docstring |
| 34 | class | `FranchiseSeasonRecord` | docstring |
| 82 | class | `Franchise` | docstring |

### `pfr/models/entities/team_season.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 10 | class | `TeamSeasonMeta` | docstring |
| 37 | class | `SeasonGame` | docstring |
| 70 | class | `TeamSeason` | docstring |

### `pfr/models/entities/uniform_numbers.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 8 | class | `UniformNumberPlayer` | docstring |
| 17 | class | `UniformNumbers` | docstring |

### `pfr/models/entities/upcoming_milestones.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 8 | class | `UpcomingMilestoneEntry` | docstring |
| 17 | class | `UpcomingLeaderboardEntry` | docstring |
| 27 | class | `UpcomingMilestones` | docstring |

---

## `pfr/parsers` (22 items)

### `pfr/parsers/player_profile.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 15 | class | `PlayerProfileParser` | docstring |
| 16 | method | `PlayerProfileParser.__init__` | docstring |
| 19 | method | `PlayerProfileParser._extract_names` | docstring |
| 56 | method | `PlayerProfileParser._extract_pos` | docstring |
| 76 | method | `PlayerProfileParser._extract_height_weight` | docstring |
| 84 | method | `PlayerProfileParser._extract_birth_info` | docstring, return type |
| 98 | method | `PlayerProfileParser._parse_draft_info` | docstring |
| 103 | method | `PlayerProfileParser._extract_pre_nfl` | docstring |
| 136 | method | `PlayerProfileParser._extract_bio_info` | docstring, return type |
| 166 | method | `PlayerProfileParser._parse_meta_panel` | docstring |
| 175 | method | `PlayerProfileParser._parse_bling` | docstring |
| 178 | method | `PlayerProfileParser._extract_team_and_years_jersey_num` | docstring |
| 192 | method | `PlayerProfileParser._parse_jersey_numbers` | docstring |
| 209 | method | `PlayerProfileParser._parse_stats_summary` | docstring |
| 229 | method | `PlayerProfileParser._extract_overheader_indices` | docstring, return type |
| 246 | method | `PlayerProfileParser._group_by_over_header` | docstring, return type |
| 260 | method | `PlayerProfileParser._parse_stats_table` | docstring |
| 309 | method | `PlayerProfileParser._extract_all_stats` | docstring |
| 325 | method | `PlayerProfileParser._parse_transactions` | docstring |
| 344 | method | `PlayerProfileParser._parse_bottom_nav` | docstring |
| 379 | method | `PlayerProfileParser._parse_leader_boards` | docstring |
| 390 | method | `PlayerProfileParser.parse` | docstring |

---

## `pfr/errors` (8 items)

### `pfr/errors/__init__.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 28 | function | `__getattr__` | docstring |
| 32 | function | `__dir__` | docstring, return type |

### `pfr/errors/griddypfrdefaulterror.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 15 | method | `GriddyPFRDefaultError.__init__` | docstring |

### `pfr/errors/griddypfrerror.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | method | `GriddyPFRError.__init__` | docstring |

### `pfr/errors/parsing_error.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 18 | method | `ParsingError.__init__` | docstring |
| 31 | method | `ParsingError.__str__` | docstring |

### `pfr/errors/responsevalidationerror.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 13 | method | `ResponseValidationError.__init__` | docstring |
| 24 | method | `ResponseValidationError.cause` | return type |

---

## `pfr/utils` (9 items)

### `pfr/utils/browserless.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 41 | class | `Browserless` | docstring |
| 42 | method | `Browserless.__init__` | docstring |
| 53 | method | `Browserless.fetch_data` | docstring, return type |
| 84 | method | `Browserless._handle_page_navigation` | docstring, return type, param types: `browser` |
| 106 | method | `Browserless.get_page_content` | return type |
| 153 | method | `AsyncBrowserless.__init__` | docstring |
| 164 | async method | `AsyncBrowserless.fetch_data` | docstring, return type |
| 196 | async method | `AsyncBrowserless._handle_page_navigation` | docstring, return type, param types: `browser` |
| 219 | async method | `AsyncBrowserless.get_page_content` | return type |

---

## `root` (4 items)

### `settings.py`

| Line | Kind | Name | Missing |
|---|---|---|---|
| 8 | class | `NFLSettings` | docstring |
| 24 | class | `BrowserlessSettings` | docstring |
| 31 | class | `GriddySettings` | docstring |
| 36 | method | `GriddySettings.fixture_dir` | docstring |

