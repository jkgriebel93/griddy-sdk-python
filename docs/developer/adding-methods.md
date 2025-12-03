# Developer Guide: Adding Endpoints to the NFL SDK

This guide outlines the complete process for adding new endpoints to the Griddy NFL SDK, including creating request/response models, implementing endpoint methods, and integrating new sub-SDKs.

## Table of Contents

1. [Overview](#overview)
2. [Directory Structure](#directory-structure)
3. [Decision Tree: Methods vs New Sub-SDK](#decision-tree)
4. [Part A: Adding Methods to Existing Sub-SDKs](#part-a-adding-methods-to-existing-sub-sdks)
5. [Part B: Creating New Sub-SDKs](#part-b-creating-new-sub-sdks)
6. [Part C: Request and Response Models](#part-c-request-and-response-models)
7. [Testing](#testing)
8. [Common Patterns](#common-patterns)

---

## Overview

The Griddy NFL SDK follows a layered architecture:

```
GriddyNFL (sdk.py)
├── Sub-SDKs (e.g., players, games, teams)
│   └── Methods (e.g., get_player, get_season_stats)
│       └── Request Models
│       └── Response Models
```

**Key Components:**
- **Sub-SDKs**: Classes that group related endpoints (e.g., `Players`, `TeamOffenseOverviewStats`)
- **Methods**: Individual API endpoint functions (sync and async versions)
- **Request Models**: Pydantic models for API request parameters
- **Response Models**: Pydantic models for API response data

---

## Directory Structure

```
src/griddy/nfl/
├── sdk.py                          # Main SDK class with sub-SDK registry
├── basesdk.py                      # Base class for all SDKs
├── models/                         # Request/Response models
│   ├── __init__.py                # Model exports
│   ├── get{endpoint}op.py         # Request models
│   └── {endpoint}response.py      # Response models
└── endpoints/
    ├── pro/                        # Pro API endpoints
    │   ├── __init__.py            # ProSDK base class
    │   ├── content.py             # Content sub-SDK
    │   ├── games.py               # Games sub-SDK
    │   ├── players.py             # Players sub-SDK
    │   ├── schedules.py           # Schedules sub-SDK
    │   ├── teams.py               # Teams sub-SDK
    │   └── stats/                 # Stats sub-category
    │       ├── defense.py
    │       ├── passing.py
    │       ├── receiving.py
    │       ├── rushing.py
    │       └── team_offense.py
    └── regular/                    # Regular API endpoints
```

---

## Decision Tree

### Should I Add Methods or Create a New Sub-SDK?

**Add methods to existing sub-SDK when:**
- The endpoint logically belongs to an existing category
- Example: Adding `get_weekly_rush_stats()` to existing `TeamOffenseOverviewStats` class

**Create a new sub-SDK when:**
- Introducing a new resource category (e.g., Coaches, Stadiums)
- The functionality is distinct and deserves its own namespace
- You'll have multiple related methods (3+)

---

## Part A: Adding Methods to Existing Sub-SDKs

Use this approach when adding endpoints to existing classes like `TeamOffenseOverviewStats`, `Players`, etc.

### Step 1: Create Request Models

#### 1.1 Create Season Request Model

**File**: `griddy/nfl/models/get{resource}{action}byseasonop.py`

**Example**: `getteamoffenserushstatsbyseasonop.py`

```python
from __future__ import annotations

from typing import Literal, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from ..utils import FieldMetadata, QueryParamMetadata
from .seasontypeenum import SeasonTypeEnum
from .sortorderenum import SortOrderEnum

# Define sort keys specific to this endpoint
Get{Resource}{Action}BySeasonSortKey = Literal[
    "field1",
    "field2",
    # Add all sortable fields
]
r"""Field to sort by"""


class Get{Resource}{Action}BySeasonRequestTypedDict(TypedDict):
    season: int
    r"""Season year"""
    season_type: SeasonTypeEnum
    r"""Type of season"""
    # Add endpoint-specific required parameters
    limit: NotRequired[int]
    r"""Maximum number of records to return"""
    # Add endpoint-specific optional parameters


class Get{Resource}{Action}BySeasonRequest(BaseModel):
    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Season year"""

    season_type: Annotated[
        SeasonTypeEnum,
        pydantic.Field(alias="seasonType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Type of season"""

    # Add all fields with proper annotations
    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 35
    r"""Maximum number of records to return"""
```

**Key Points:**
- Use `Annotated` with `FieldMetadata` for all fields
- Add `pydantic.Field(alias="...")` for camelCase conversion
- Optional fields use `Optional[Type]` with default values
- Required fields have no default value

#### 1.2 Create Weekly Request Model (if applicable)

**File**: `griddy/nfl/models/get{resource}{action}byweekop.py`

Copy the season version and add the `week` field after `season_type`:

```python
from .weekslugenum import WeekSlugEnum

class Get{Resource}{Action}ByWeekRequest(BaseModel):
    season: Annotated[...]
    r"""Season year"""

    season_type: Annotated[...]
    r"""Type of season"""

    week: Annotated[
        WeekSlugEnum,
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Week identifier"""

    # ... rest of fields (same as season version)
```

### Step 2: Register Models in `models/__init__.py`

Add in **three locations**:

#### 2.1 TYPE_CHECKING Block

```python
if TYPE_CHECKING:
    from .get{resource}{action}byseasonop import (
        Get{Resource}{Action}BySeasonRequest,
        Get{Resource}{Action}BySeasonRequestTypedDict,
        Get{Resource}{Action}BySeasonSortKey,
    )
    from .get{resource}{action}byweekop import (
        Get{Resource}{Action}ByWeekRequest,
        Get{Resource}{Action}ByWeekRequestTypedDict,
        Get{Resource}{Action}ByWeekSortKey,
    )
```

#### 2.2 `__all__` List (alphabetically)

```python
__all__ = [
    # ...
    "Get{Resource}{Action}BySeasonRequest",
    "Get{Resource}{Action}BySeasonRequestTypedDict",
    "Get{Resource}{Action}BySeasonSortKey",
    "Get{Resource}{Action}ByWeekRequest",
    "Get{Resource}{Action}ByWeekRequestTypedDict",
    "Get{Resource}{Action}ByWeekSortKey",
    # ...
]
```

#### 2.3 Module Mapping Dictionary

```python
_MODULE_MAP = {
    # ...
    "Get{Resource}{Action}BySeasonRequest": ".get{resource}{action}byseasonop",
    "Get{Resource}{Action}BySeasonRequestTypedDict": ".get{resource}{action}byseasonop",
    "Get{Resource}{Action}BySeasonSortKey": ".get{resource}{action}byseasonop",
    "Get{Resource}{Action}ByWeekRequest": ".get{resource}{action}byweekop",
    "Get{Resource}{Action}ByWeekRequestTypedDict": ".get{resource}{action}byweekop",
    "Get{Resource}{Action}ByWeekSortKey": ".get{resource}{action}byweekop",
    # ...
}
```

### Step 3: Create Response Model (if needed)

**File**: `griddy/nfl/models/{resource}{action}response.py`

```python
from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from ..types import BaseModel

class {Resource}{Action}ResponseTypedDict(TypedDict):
    # Define response structure based on API

class {Resource}{Action}Response(BaseModel):
    # Define response fields with proper types
```

Add to `models/__init__.py` following the same pattern as request models.

### Step 4: Implement Endpoint Methods

**File**: Find the appropriate sub-SDK class (e.g., `endpoints/pro/stats/team_offense.py`)

Implement **4 methods** for each endpoint:
1. Sync season method
2. Async season method
3. Sync weekly method (if applicable)
4. Async weekly method (if applicable)

#### 4.1 Sync Season Method Template

```python
def get_{action}(
    self,
    *,
    season: int,
    season_type: models.SeasonTypeEnum,
    # Add endpoint-specific parameters
    limit: Optional[int] = 35,
    offset: Optional[int] = 0,
    page: Optional[int] = 1,
    sort_key: Optional[models.Get{Resource}{Action}BySeasonSortKey] = "default",
    sort_value: Optional[models.SortOrderEnum] = None,
    retries: OptionalNullable[utils.RetryConfig] = UNSET,
    server_url: Optional[str] = None,
    timeout_ms: Optional[int] = None,
    http_headers: Optional[Mapping[str, str]] = None,
) -> models.{Resource}{Action}Response:
    r"""Brief description of endpoint

    Detailed description of what this endpoint returns and its purpose.

    :param season: Season year
    :param season_type: Type of season
    # Document all parameters
    :param retries: Override the default retry configuration
    :param server_url: Override the default server URL
    :param timeout_ms: Override the default request timeout in milliseconds
    :param http_headers: Additional headers to set or replace
    """
    base_url = None
    url_variables = None
    if timeout_ms is None:
        timeout_ms = self.sdk_configuration.timeout_ms

    if server_url is not None:
        base_url = server_url
    else:
        base_url = self._get_url(base_url, url_variables)

    request = models.Get{Resource}{Action}BySeasonRequest(
        season=season,
        season_type=season_type,
        # Pass all parameters
    )

    req = self._build_request(
        method="GET",  # or POST, PUT, etc.
        path="/api/path/to/endpoint",
        base_url=base_url,
        url_variables=url_variables,
        request=request,
        request_body_required=False,
        request_has_path_params=False,
        request_has_query_params=True,
        user_agent_header="user-agent",
        accept_header_value="application/json",
        http_headers=http_headers,
        security=self.sdk_configuration.security,
        timeout_ms=timeout_ms,
    )

    if retries == UNSET:
        if self.sdk_configuration.retry_config is not UNSET:
            retries = self.sdk_configuration.retry_config

    retry_config = None
    if isinstance(retries, utils.RetryConfig):
        retry_config = (retries, ["429", "500", "502", "503", "504"])

    http_res = self.do_request(
        hook_ctx=HookContext(
            config=self.sdk_configuration,
            base_url=base_url or "",
            operation_id="get{Resource}{Action}BySeason",
            oauth2_scopes=[],
            security_source=get_security_from_env(
                self.sdk_configuration.security, models.Security
            ),
        ),
        request=req,
        error_status_codes=["400", "401", "403", "4XX", "500", "5XX"],
        retry_config=retry_config,
    )

    if utils.match_response(http_res, "200", "application/json"):
        return http_res.json()
        # Or: return unmarshal_json_response(models.{Resource}{Action}Response, http_res)
    if utils.match_response(http_res, ["400", "401", "403", "4XX"], "*"):
        http_res_text = utils.stream_to_text(http_res)
        raise errors.GriddyNFLDefaultError(
            "API error occurred", http_res, http_res_text
        )
    if utils.match_response(http_res, ["500", "5XX"], "*"):
        http_res_text = utils.stream_to_text(http_res)
        raise errors.GriddyNFLDefaultError(
            "API error occurred", http_res, http_res_text
        )

    raise errors.GriddyNFLDefaultError("Unexpected response received", http_res)
```

#### 4.2 Async Version Changes

```python
async def get_{action}_async(
    self,
    # ... same parameters ...
) -> models.{Resource}{Action}Response:
    # ... same setup ...

    req = self._build_request_async(  # <- async builder
        # ... same configuration ...
    )

    # ... same retry setup ...

    http_res = await self.do_request_async(  # <- await async request
        # ... same hook context ...
    )

    if utils.match_response(http_res, "200", "application/json"):
        return http_res.json()
    if utils.match_response(http_res, ["400", "401", "403", "4XX"], "*"):
        http_res_text = await utils.stream_to_text_async(http_res)  # <- await
        raise errors.GriddyNFLDefaultError(
            "API error occurred", http_res, http_res_text
        )
    if utils.match_response(http_res, ["500", "5XX"], "*"):
        http_res_text = await utils.stream_to_text_async(http_res)  # <- await
        raise errors.GriddyNFLDefaultError(
            "API error occurred", http_res, http_res_text
        )

    raise errors.GriddyNFLDefaultError("Unexpected response received", http_res)
```

---

## Part B: Creating New Sub-SDKs

Use this approach when adding entirely new resource categories.

### Step 1: Create the Sub-SDK Class

**File**: `griddy/nfl/endpoints/pro/{subsdk_name}.py` or `griddy/nfl/{subsdk_name}.py`

**For Pro API endpoints:**

```python
from typing import Mapping, Optional

from griddy.nfl import errors, models, utils
from griddy.nfl._hooks import HookContext
from griddy.nfl.endpoints.pro import ProSDK
from griddy.nfl.types import UNSET, OptionalNullable
from griddy.nfl.utils import get_security_from_env


class {SubSDKName}(ProSDK):
    r"""Brief description of this sub-SDK's purpose"""

    def get_{resource}(
        self,
        *,
        # Add parameters
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.{Response}:
        r"""Method documentation"""
        # Implement method (follow template from Step 4)

    async def get_{resource}_async(
        self,
        # ... async version
    ) -> models.{Response}:
        r"""Async method documentation"""
        # Implement async method
```

**For Regular API endpoints:**

```python
from griddy.nfl.endpoints.basesdk import BaseSDK


class {SubSDKName}(BaseSDK):
    r"""Brief description"""
    # Same structure as above
```

**Key Differences:**
- **ProSDK**: Inherits from `ProSDK`, sets `is_pro = True` flag
- **BaseSDK**: Inherits from `BaseSDK`, for regular NFL API

### Step 2: Register Sub-SDK in `sdk.py`

#### 2.1 Add Type Hint

In the `TYPE_CHECKING` block:

```python
if TYPE_CHECKING:
    # ... existing imports ...
    from griddy.nfl.endpoints.pro.{subsdk_file} import {SubSDKName}
```

#### 2.2 Add Property Declaration

In the `GriddyNFL` class:

```python
class GriddyNFL(BaseSDK):
    # ... existing properties ...

    {subsdk_attribute}: "{SubSDKName}"
    r"""Brief description of what this sub-SDK provides"""
```

#### 2.3 Register in `_sub_sdk_map`

```python
_sub_sdk_map = {
    # ... existing mappings ...
    "{subsdk_attribute}": ("griddy.nfl.endpoints.pro.{subsdk_file}", "{SubSDKName}"),
}
```

**Example**:
```python
# Type hint
from griddy.nfl.endpoints.pro.coaches import Coaches

# Property
coaches: "Coaches"
r"""NFL coaching staff information and statistics"""

# Registry
_sub_sdk_map = {
    "coaches": ("griddy.nfl.endpoints.pro.coaches", "Coaches"),
}
```

### Step 3: Test Sub-SDK Registration

```python
from griddy import GriddyNFL

sdk = GriddyNFL(nfl_auth={...})

# Access should trigger lazy loading
result = sdk.{subsdk_attribute}.get_{method}(...)
```

---

## Part C: Request and Response Models

### Request Model Guidelines

**Naming Convention**: `Get{Resource}{Action}By{Timeframe}Request`

**Required Components**:
1. `TypedDict` version (for type checking)
2. `BaseModel` version (for runtime validation)
3. Sort key `Literal` (if sorting is supported)

**Field Annotations**:
```python
# Required field (no default)
field: Annotated[
    Type,
    pydantic.Field(alias="fieldName"),  # if camelCase conversion needed
    FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
]

# Optional field (with default)
field: Annotated[
    Optional[Type],
    FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
] = default_value

# List field
field: Annotated[
    Optional[List[Type]],
    FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
] = None
```

### Response Model Guidelines

**Naming Convention**: `{Resource}{Action}Response`

**Structure**:
```python
class {Resource}{Action}Response(BaseModel):
    data: Optional[List[{DataModel}]] = None
    pagination: Optional[PaginationModel] = None
    # Other top-level fields
```

**Best Practices**:
- Create nested models for complex objects
- Use `Optional` for fields that might not be present
- Add docstrings for non-obvious fields

---

## Testing

### Unit Testing Models

```python
from griddy.nfl.models import (
    Get{Resource}{Action}BySeasonRequest,
    Get{Resource}{Action}ByWeekRequest,
)

def test_season_request():
    request = Get{Resource}{Action}BySeasonRequest(
        season=2024,
        seasonType='REG'
    )
    assert request.season == 2024
    assert request.season_type == 'REG'
    assert request.limit == 35  # default

def test_weekly_request():
    request = Get{Resource}{Action}ByWeekRequest(
        season=2024,
        seasonType='REG',
        week='WEEK_1'
    )
    assert request.week == 'WEEK_1'
```

### Integration Testing Methods

```python
from griddy import GriddyNFL

def test_endpoint_call():
    sdk = GriddyNFL(nfl_auth={...})

    # Test sync method
    result = sdk.{subsdk}.get_{action}(
        season=2024,
        season_type='REG'
    )
    assert result is not None

    # Test async method
    async def test_async():
        result = await sdk.{subsdk}.get_{action}_async(
            season=2024,
            season_type='REG'
        )
        assert result is not None
```

---

## Common Patterns

### Pattern 1: Season vs Weekly Endpoints

**Season**: Aggregates data across entire season
- No `week` parameter
- File: `get{resource}byseasonop.py`

**Weekly**: Data for specific week
- Requires `week: WeekSlugEnum` parameter
- File: `get{resource}byweekop.py`

### Pattern 2: Pagination Parameters

Standard pagination fields:
```python
limit: Optional[int] = 35
offset: Optional[int] = 0
page: Optional[int] = 1
```

### Pattern 3: Sorting Parameters

```python
sort_key: Optional[{Resource}SortKey] = "default_field"
sort_value: Optional[SortOrderEnum] = None  # ASC/DESC
```

### Pattern 4: Filtering Parameters

Common filters:
- `team_id` / `team_defense` / `team_offense`
- `player_id`
- `game_id`
- `split` (situational filters)

---

## Summary Checklist

### For Adding Methods to Existing Sub-SDK:

- [ ] Create season request model (`get{resource}{action}byseasonop.py`)
- [ ] Create weekly request model (`get{resource}{action}byweekop.py`) (if applicable)
- [ ] Add models to `models/__init__.py` (3 locations)
- [ ] Create/verify response model
- [ ] Implement sync season method
- [ ] Implement async season method
- [ ] Implement sync weekly method (if applicable)
- [ ] Implement async weekly method (if applicable)
- [ ] Write unit tests
- [ ] Write integration tests

### For Creating New Sub-SDK:

- [ ] Create sub-SDK class file
- [ ] Implement all methods (sync and async)
- [ ] Create request models
- [ ] Create response models
- [ ] Register models in `models/__init__.py`
- [ ] Add type hint in `sdk.py`
- [ ] Add property declaration in `sdk.py`
- [ ] Add to `_sub_sdk_map` in `sdk.py`
- [ ] Write unit tests
- [ ] Write integration tests
- [ ] Update documentation

---

## References

### Code Examples
- **Existing Sub-SDK**: `griddy/nfl/endpoints/pro/players.py`
- **Request Models**: `griddy/nfl/models/getteamoffensepassstatsbyseasonop.py`
- **Response Models**: `griddy/nfl/models/teamoffensepassstatsresponse.py`
- **SDK Registration**: `griddy/nfl/sdk.py` (lines 100-155)

### Key Base Classes
- `BaseSDK`: `griddy/nfl/basesdk.py`
- `ProSDK`: `griddy/nfl/endpoints/pro/__init__.py`

### Utilities
- `FieldMetadata`: Request parameter metadata
- `QueryParamMetadata`: Query parameter serialization config
- `HookContext`: Request hook context for logging/monitoring
