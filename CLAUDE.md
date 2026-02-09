# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build and Test Commands

```bash
pip install -e ".[dev]"                        # Install with dev dependencies
pytest                                          # Run all tests (includes coverage)
pytest tests/test_nfl/unit/test_sdk.py          # Run a single test file
pytest tests/test_nfl/unit/test_sdk.py::TestClass::test_name  # Run a single test
pytest -m "not integration"                     # Skip integration tests (hit real APIs)
pytest -m integration                           # Run only integration tests
black src/ tests/                               # Format code
isort src/ tests/                               # Sort imports
mypy src/                                       # Type checking (strict mode)
flake8 src/ tests/                              # Linting
mkdocs serve                                    # Serve docs locally
```

Coverage is enabled by default in pyproject.toml (`--cov=src/griddy`). Test markers: `unit`, `integration`, `slow`.

## Architecture

### Entry Point and Lazy Loading

`GriddyNFL` (in `nfl/sdk.py`) is the main client. It uses `__getattr__` with a `_sub_sdk_map` dict to lazily instantiate sub-SDKs on first attribute access. Each sub-SDK maps an attribute name to a `(module_path, class_name)` tuple. On first access, the module is dynamically imported, the class is instantiated with the shared `SDKConfiguration`, and cached via `setattr`. This same pattern is repeated in `NextGenStats` and `StatsSDK` for their own nested sub-SDKs.

### Three API Tiers with Different Base URLs

The SDK talks to three different NFL API servers, configured in `sdkconfiguration.py:SERVERS`:
- **regular** (`api.nfl.com`) - Public endpoints. Endpoint classes extend `BaseSDK` directly.
- **pro** (`pro.nfl.com`) - Advanced stats. Endpoint classes extend `ProSDK`, which sets `server_type = "pro"` on init.
- **ngs** (`nextgenstats.nfl.com`) - Next Gen Stats. Endpoint classes extend `NgsBaseSDK`, which overrides `_resolve_base_url`.

The `server_type` field on `SDKConfiguration` determines which base URL is used via `get_server_details()`.

### Endpoint Implementation Pattern

Every endpoint follows a three-method pattern (see `endpoints/pro/stats/passing.py` for a complete example):
1. `_get_<name>_config()` - Builds an `EndpointConfig` dataclass with method, path, request model, response type, and error codes.
2. `get_<name>()` - Sync version: calls `_get_<name>_config()` then `self._execute_endpoint(config)`.
3. `get_<name>_async()` - Async version: calls `_get_<name>_config()` then `await self._execute_endpoint_async(config)`.

`_execute_endpoint` / `_execute_endpoint_async` in `basesdk.py` handle URL resolution, request building, hooks, retries, and response unmarshalling. New endpoints only need to define the config and the two thin wrappers.

### Request/Response Hooks

The `_hooks/` system provides lifecycle hooks (SDKInit, BeforeRequest, AfterSuccess, AfterError). Hooks are registered in `_hooks/registration.py`. Currently `HackAuthHook` is the only registered hook - it runs before every request to add required headers (referer, sec-fetch-*) and auto-refreshes expired auth tokens using the refresh token.

### Models

All request/response models are Pydantic v2 models in `nfl/models/`. Request models use `Annotated` types with `Field` for query parameter metadata. Response models map NFL API JSON structures. Shared error code constants live in `_constants.py` (COLLECTION_ERROR_CODES, RESOURCE_ERROR_CODES, STATS_ERROR_CODES, SECURED_RESOURCE_ERROR_CODES).

### Authentication

Two auth methods: pass `nfl_auth={"accessToken": ..., "refreshToken": ..., "expiresIn": ...}` directly, or provide `login_email`/`login_password` for Playwright-based browser auth. The `HackAuthHook` handles token refresh automatically when the token is within 30 seconds of expiring.

### Error Hierarchy

`core/exceptions.py` defines: `GriddyError` (base) -> `APIError`, `RateLimitError`, `NotFoundError`, `AuthenticationError`, `ValidationError`. The NFL SDK also has `errors.GriddyNFLDefaultError` used by `basesdk.py` for API response errors.

## Code Style

- Black (line-length 88), isort (black profile), mypy strict (`disallow_untyped_defs`)
- `Annotated` types with Pydantic `Field` for model metadata
- Tests in `tests/` mirror `src/` structure; fixtures in `tests/conftest.py`

## Environment Variables

- `NFL_API_KEY`, `NFL_CLIENT_KEY`, `NFL_CLIENT_SECRET` - API credentials (loaded in `settings.py`)
- `NFL_LOGIN_EMAIL`, `NFL_LOGIN_PASSWORD` - For browser-based auth
