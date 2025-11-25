# Implementation Plan: Split Large Files

## Priority: 5
## Estimated Effort: Medium
## Impact: Medium - Improves maintainability and code navigation

---

## Problem Statement

Several files in the codebase have grown too large, making them difficult to navigate, maintain, and review:

| File | Lines | Issue |
|------|-------|-------|
| `endpoints/regular/football/games.py` | 887 | Multiple game-related concerns |
| `endpoints/pro/mixins.py` | 1,917 | Multiple unrelated mixins |
| `models/__init__.py` | ~2,600 | Massive dynamic import registry |

---

## File 1: `endpoints/pro/mixins.py` (1,917 lines)

### Current Structure

The file contains multiple unrelated mixins:
- `GameScheduleMixin` - Game schedule operations
- `GameContentMixin` - Film room and content operations
- `GameResultsDataMixin` - Game results and statistics
- Possibly others

### Proposed Split

**New Directory Structure:**
```
endpoints/pro/mixins/
├── __init__.py              # Re-exports all mixins
├── game_schedule.py         # GameScheduleMixin
├── game_content.py          # GameContentMixin
├── game_results.py          # GameResultsDataMixin
└── base.py                  # Any shared utilities
```

### Implementation Steps

#### Step 1: Create mixins directory

```bash
mkdir -p src/griddy/nfl/endpoints/pro/mixins
```

#### Step 2: Split GameScheduleMixin

**File:** `src/griddy/nfl/endpoints/pro/mixins/game_schedule.py`

```python
"""Game schedule mixin for Pro API endpoints."""

from typing import List, Mapping, Optional

from griddy.nfl import errors, models, utils
from griddy.nfl._hooks import HookContext
from griddy.nfl.types import UNSET, OptionalNullable
from griddy.nfl.utils import get_security_from_env
from griddy.nfl.utils.unmarshal_json_response import unmarshal_json_response


class GameScheduleMixin:
    """Mixin providing game schedule operations."""

    def get_scheduled_game(
        self,
        *,
        game_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GameDetail:
        # ... implementation
        pass

    async def get_scheduled_game_async(self, ...) -> models.GameDetail:
        # ... implementation
        pass

    # ... other schedule methods
```

#### Step 3: Split GameContentMixin

**File:** `src/griddy/nfl/endpoints/pro/mixins/game_content.py`

```python
"""Game content mixin for Pro API endpoints."""

from typing import List, Mapping, Optional

from griddy.nfl import errors, models, utils
from griddy.nfl._hooks import HookContext
from griddy.nfl.types import UNSET, OptionalNullable
from griddy.nfl.utils import get_security_from_env
from griddy.nfl.utils.unmarshal_json_response import unmarshal_json_response


class GameContentMixin:
    """Mixin providing game content and film room operations."""

    def get_film_room(self, ...) -> models.FilmRoomResponse:
        # ... implementation
        pass

    async def get_film_room_async(self, ...) -> models.FilmRoomResponse:
        # ... implementation
        pass

    # ... other content methods
```

#### Step 4: Split GameResultsDataMixin

**File:** `src/griddy/nfl/endpoints/pro/mixins/game_results.py`

```python
"""Game results data mixin for Pro API endpoints."""

from typing import List, Mapping, Optional

from griddy.nfl import errors, models, utils
from griddy.nfl._hooks import HookContext
from griddy.nfl.types import UNSET, OptionalNullable
from griddy.nfl.utils import get_security_from_env
from griddy.nfl.utils.unmarshal_json_response import unmarshal_json_response


class GameResultsDataMixin:
    """Mixin providing game results and statistics operations."""

    def get_game_stats(self, ...) -> models.GameStatsResponse:
        # ... implementation
        pass

    async def get_game_stats_async(self, ...) -> models.GameStatsResponse:
        # ... implementation
        pass

    # ... other results methods
```

#### Step 5: Create package __init__.py

**File:** `src/griddy/nfl/endpoints/pro/mixins/__init__.py`

```python
"""Pro API mixins for shared endpoint functionality."""

from .game_schedule import GameScheduleMixin
from .game_content import GameContentMixin
from .game_results import GameResultsDataMixin

__all__ = [
    "GameScheduleMixin",
    "GameContentMixin",
    "GameResultsDataMixin",
]
```

#### Step 6: Update imports in dependent files

**File:** `src/griddy/nfl/endpoints/pro/games.py`

```python
# Before
from griddy.nfl.endpoints.pro.mixins import GameScheduleMixin, GameContentMixin

# After (same, but now imports from package)
from griddy.nfl.endpoints.pro.mixins import GameScheduleMixin, GameContentMixin
```

---

## File 2: `endpoints/regular/football/games.py` (887 lines)

### Current Structure

Single file with multiple game-related endpoints:
- Basic game info
- Game details
- Weekly games
- Live scores
- Historical games

### Proposed Split

**New Directory Structure:**
```
endpoints/regular/football/games/
├── __init__.py              # Games class re-exporting all methods
├── base.py                  # Base games operations
├── details.py               # Detailed game information
├── live.py                  # Live game data and scores
└── historical.py            # Historical game queries
```

### Implementation Steps

#### Step 1: Analyze method groupings

Review the file to identify logical groupings:
- `get_games()`, `get_game()` → base.py
- `get_game_details()`, `get_weekly_game_details()` → details.py
- `get_live_scores()`, `get_current_games()` → live.py
- `get_historical_games()` → historical.py

#### Step 2: Create games directory

```bash
mkdir -p src/griddy/nfl/endpoints/regular/football/games
```

#### Step 3: Split into focused modules

Each module should contain related methods and their async counterparts.

#### Step 4: Use composition in main Games class

**File:** `src/griddy/nfl/endpoints/regular/football/games/__init__.py`

```python
"""Football games endpoints."""

from griddy.nfl.basesdk import BaseSDK
from griddy.nfl.sdkconfiguration import SDKConfiguration

from .base import GameBaseMixin
from .details import GameDetailsMixin
from .live import GameLiveMixin
from .historical import GameHistoricalMixin


class Games(
    GameBaseMixin,
    GameDetailsMixin,
    GameLiveMixin,
    GameHistoricalMixin,
    BaseSDK,
):
    """Football games API providing access to game information and scores."""

    def __init__(self, sdk_config: SDKConfiguration, parent_ref=None):
        super().__init__(sdk_config, parent_ref)
```

---

## File 3: `models/__init__.py` (~2,600 lines)

### Current Structure

Massive file containing:
- TYPE_CHECKING imports (~1,000 lines)
- `__all__` list (~800 lines)
- `_dynamic_imports` dict (~800 lines)
- `__getattr__` and `__dir__` functions

### Proposed Approach

**Option A: Generate dynamically**

Create a script to generate the `__init__.py` from the actual model files:

**File:** `scripts/generate_models_init.py`

```python
#!/usr/bin/env python3
"""Generate models/__init__.py from existing model files."""

import os
from pathlib import Path

MODELS_DIR = Path("src/griddy/nfl/models")

def find_model_classes(directory: Path) -> dict:
    """Find all model classes in a directory."""
    # Implementation to scan .py files and extract class names
    pass

def generate_init_content(classes: dict) -> str:
    """Generate the __init__.py content."""
    # Generate TYPE_CHECKING block
    # Generate __all__ list
    # Generate _dynamic_imports dict
    pass

def main():
    classes = find_model_classes(MODELS_DIR)
    content = generate_init_content(classes)

    init_path = MODELS_DIR / "__init__.py"
    init_path.write_text(content)
    print(f"Generated {init_path}")

if __name__ == "__main__":
    main()
```

**Option B: Split by category**

Create separate registry files:

```
models/
├── __init__.py              # Main entry, imports from registries
├── _registry/
│   ├── __init__.py
│   ├── entities.py          # Entity model registry
│   ├── requests.py          # Request model registry
│   ├── responses.py         # Response model registry
│   └── enums.py             # Enum registry
├── entities/
├── requests/
├── responses/
└── enums/
```

**File:** `models/_registry/entities.py`

```python
"""Registry for entity models."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..entities.person import Person, PersonTypedDict
    from ..entities.player import Player, PlayerTypedDict
    # ... etc

ENTITY_IMPORTS = {
    "Person": ".entities.person",
    "PersonTypedDict": ".entities.person",
    "Player": ".entities.player",
    "PlayerTypedDict": ".entities.player",
    # ... etc
}

ENTITY_EXPORTS = list(ENTITY_IMPORTS.keys())
```

**File:** `models/__init__.py` (simplified)

```python
"""NFL SDK models."""

from ._registry.entities import ENTITY_IMPORTS, ENTITY_EXPORTS
from ._registry.requests import REQUEST_IMPORTS, REQUEST_EXPORTS
from ._registry.responses import RESPONSE_IMPORTS, RESPONSE_EXPORTS
from ._registry.enums import ENUM_IMPORTS, ENUM_EXPORTS

_dynamic_imports = {
    **ENTITY_IMPORTS,
    **REQUEST_IMPORTS,
    **RESPONSE_IMPORTS,
    **ENUM_IMPORTS,
}

__all__ = [
    *ENTITY_EXPORTS,
    *REQUEST_EXPORTS,
    *RESPONSE_EXPORTS,
    *ENUM_EXPORTS,
]

def __getattr__(attr_name: str):
    # ... existing lazy loading logic
    pass

def __dir__():
    return __all__
```

---

## Validation Checklist

### Mixins Split
- [ ] `mixins/` directory created
- [ ] `GameScheduleMixin` extracted
- [ ] `GameContentMixin` extracted
- [ ] `GameResultsDataMixin` extracted
- [ ] Package `__init__.py` created
- [ ] Dependent files updated
- [ ] All imports work correctly
- [ ] Tests pass

### Games Split
- [ ] `games/` directory created
- [ ] Base methods extracted
- [ ] Details methods extracted
- [ ] Live methods extracted
- [ ] Historical methods extracted
- [ ] Package `__init__.py` created
- [ ] SDK registration updated
- [ ] Tests pass

### Models Init
- [ ] Approach decided (generate vs split)
- [ ] Registry files created (if splitting)
- [ ] Generation script created (if generating)
- [ ] Main `__init__.py` simplified
- [ ] All model imports work
- [ ] Tests pass

---

## Files Modified/Created

| File | Change Type |
|------|-------------|
| `endpoints/pro/mixins/` | New directory |
| `endpoints/pro/mixins/__init__.py` | New file |
| `endpoints/pro/mixins/game_schedule.py` | New file (from mixins.py) |
| `endpoints/pro/mixins/game_content.py` | New file (from mixins.py) |
| `endpoints/pro/mixins/game_results.py` | New file (from mixins.py) |
| `endpoints/pro/mixins.py` | Delete |
| `endpoints/regular/football/games/` | New directory |
| `endpoints/regular/football/games/__init__.py` | New file |
| `endpoints/regular/football/games/base.py` | New file |
| `endpoints/regular/football/games/details.py` | New file |
| `endpoints/regular/football/games/live.py` | New file |
| `endpoints/regular/football/games/historical.py` | New file |
| `endpoints/regular/football/games.py` | Delete |
| `models/_registry/` | New directory (if splitting) |
| `models/__init__.py` | Simplify |
| `scripts/generate_models_init.py` | New file (if generating) |

---

## Benefits

1. **Navigability**: Smaller files are easier to navigate
2. **Reviews**: Smaller files are easier to code review
3. **Maintainability**: Changes isolated to specific modules
4. **Testing**: Can test modules independently
5. **IDE Performance**: Large files can slow down IDEs
