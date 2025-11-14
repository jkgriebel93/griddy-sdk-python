# NFL SDK Endpoint Migration Status

**Date**: 2025-11-14
**Purpose**: Document which API endpoints exist in direct child modules of `griddy.nfl` but have not been migrated to the `griddy.nfl.endpoints` directory structure.

## Executive Summary

This report identifies **~13 unique API endpoints** that are implemented in direct child modules of `griddy.nfl` (e.g., `win_probability.py`, `scores.py`, `football.py`) but are NOT found in the refactored `griddy.nfl.endpoints/` directory structure.

The unmigrated endpoints fall into two main categories:
1. **Pro API secured endpoints** - Win probability, fantasy stats, experience API
2. **Football API v2 endpoints** - Injuries, player details, live stats, transactions, venues

## Endpoints Not Yet Migrated

### 1. Win Probability (`src/griddy/nfl/win_probability.py`)

| Method | Path | Status |
|--------|------|--------|
| `get_plays_win_probability()` | `/api/secured/plays/winProbability` | ❌ Not in endpoints/ |
| `get_win_probability_min()` | `/api/secured/plays/winProbabilityMin` | ❌ Not in endpoints/ |

### 2. Live Scores (`src/griddy/nfl/scores.py`)

| Method | Path | Status |
|--------|------|--------|
| `get_live_game_scores()` | `/api/scores/live/games` | ❌ Not in endpoints/ |

### 3. Fantasy Statistics (`src/griddy/nfl/fantasy_statistics.py`)

| Method | Path | Status |
|--------|------|--------|
| `get_fantasy_stats_by_season()` | `/api/secured/stats/fantasy/season` | ❌ Not in endpoints/ |

### 4. Experience API (`src/griddy/nfl/experience.py`)

| Method | Path | Status |
|--------|------|--------|
| `get_experience_games()` | `/experience/v1/games` | ❌ Not in endpoints/ |
| `get_experience_teams()` | `/experience/v1/teams` | ❌ Not in endpoints/ |

**Note**: There is an `endpoints/regular/football/experience.py` but it contains different methods (`get_weekly_game_details()`).

### 5. Football API v2 (`src/griddy/nfl/football.py`)

| Method | Path | Status | Notes |
|--------|------|--------|-------|
| `get_injury_reports()` | `/football/v2/injuries/...` | ❌ Not in endpoints/ | Empty placeholder at `endpoints/regular/football/injuries.py` |
| `get_player_details()` | `/football/v2/players/{playerId}/profile` | ❌ Not in endpoints/ | Empty placeholder at `endpoints/regular/football/players.py` |
| `get_live_game_stats()` | `/football/v2/stats/live/games` | ❌ Not in endpoints/ | Empty placeholder at `endpoints/regular/football/stats.py` |
| `get_season_player_stats()` | `/football/v2/stats/season/.../player/position/{position}` | ❌ Not in endpoints/ | Empty placeholder at `endpoints/regular/football/stats.py` |
| `get_transactions()` | `/football/v2/transactions/date/{date}` | ❌ Not in endpoints/ | Empty placeholder at `endpoints/regular/football/transactions.py` |
| `get_venues()` | `/football/v2/venues` | ❌ Not in endpoints/ | Empty placeholder at `endpoints/regular/football/venues.py` |

**Other Football API v2 endpoints** (already migrated):
- ✅ `get_draft_info()` → `endpoints/regular/football/draft.py::get_picks_report()`
- ✅ `get_weekly_game_details()` → `endpoints/regular/football/experience.py`
- ✅ `get_football_games()` → `endpoints/regular/football/games.py::get_games()`
- ✅ `get_football_box_score()` → `endpoints/regular/football/games.py::get_box_score()`
- ✅ `get_play_by_play()` → `endpoints/regular/football/games.py`
- ✅ `get_players_team_roster()` → `endpoints/regular/football/rosters.py::get_rosters()`
- ✅ `get_standings()` → `endpoints/regular/football/standings.py`
- ✅ `get_season_weeks()` → `endpoints/regular/football/weeks.py`

## Modules Marked for Cleanup/Deletion

### 1. `team_offense_pass_statistics.py`
- **Status**: Contains "TODO: DELETE" comment
- **Reason**: Functionality replaced by `endpoints/pro/stats/team_offense.py::get_season_pass_stats()`
- **Action**: Can be removed after verifying all references are updated

### 2. `betting.py`
- **Status**: Contains "TODO: Not sure where to put this module" comment
- **Endpoint**: `get_weekly_betting_odds()` - `/api/schedules/week/odds`
- **Note**: Similar endpoint `get_future_betting_odds()` exists in `endpoints/pro/schedules.py`

## Empty Placeholder Files

The following files exist in `endpoints/regular/football/` but are currently empty, suggesting planned but incomplete migration:

- `injuries.py`
- `players.py`
- `stats.py`
- `transactions.py`
- `venues.py`

## Partial Duplicates/Overlaps

Some endpoints exist in BOTH direct child modules and endpoints directory:

| Original Location | Migrated Location | Status |
|-------------------|-------------------|--------|
| `secured_videos.py::get_coaches_film_videos()` | `endpoints/pro/content.py::get_coaches_film_videos()` | ⚠️ Duplicate |
| `filmroom.py::get_filmroom_plays()` | `endpoints/pro/content.py::get_filmroom_plays()` | ⚠️ Duplicate |
| `player_statistics.py` (all methods) | `endpoints/pro/stats/passing.py` (and similar) | ⚠️ Deprecated |

## Patterns and Observations

1. **Pro API Migration**: Most Pro API secured endpoints (`/api/secured/*`) have been successfully migrated to `endpoints/pro/`, with notable exceptions being win probability, fantasy stats, and experience endpoints.

2. **Football API v2 Partial Migration**: Basic game/schedule endpoints are migrated, but player-specific and stats endpoints remain in `football.py`.

3. **Empty Placeholders**: The presence of empty files suggests migration was planned but not completed for injuries, players, stats, transactions, and venues.

4. **Module Organization**: The new `endpoints/` structure separates Pro API (`endpoints/pro/`) from Regular API (`endpoints/regular/football/`), which is cleaner than the flat structure in direct child modules.

## Recommendations

### High Priority
1. **Complete Football API v2 migration** by implementing the 6 empty placeholder files
2. **Migrate Win Probability endpoints** to `endpoints/pro/plays.py` or similar
3. **Migrate Fantasy Statistics** to `endpoints/pro/stats/fantasy.py`

### Medium Priority
4. **Consolidate Experience endpoints** - decide whether to keep in root `experience.py` or migrate to endpoints structure
5. **Resolve betting.py** - determine proper location for betting endpoints
6. **Delete deprecated modules** - Remove `team_offense_pass_statistics.py` after verification

### Low Priority
7. **Remove duplicate implementations** once migration is verified complete
8. **Update SDK registration** in `sdk.py` to use new endpoint locations

## Migration Checklist Template

For each unmigrated endpoint:

- [ ] Create/update target file in `endpoints/` directory
- [ ] Implement sync and async methods following patterns in existing endpoint files
- [ ] Create request/response models in `models/`
- [ ] Register models in `models/__init__.py`
- [ ] Add tests in `tests/test_nfl/test_endpoints/`
- [ ] Update SDK registration in `sdk.py` if needed
- [ ] Verify old implementation is no longer referenced
- [ ] Remove old implementation file
- [ ] Update documentation

## See Also

- `ADDING_METHODS_TO_NFL_SDK.md` - Guide for adding new methods to the NFL SDK
- `TESTING_STRATEGY.md` - Testing approach for endpoints
