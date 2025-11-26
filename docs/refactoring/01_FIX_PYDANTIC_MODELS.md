# Fix Pydantic Models

This document tracks all endpoint methods that currently return raw JSON (`http_res.json()`) instead of properly unmarshaled Pydantic models. These methods need their Pydantic models fixed to enable proper type safety.

## Overview

When a Pydantic model has schema issues (missing fields, incorrect types, etc.), the `unmarshal_json_response` function fails. As a workaround, these endpoints return raw JSON dictionaries instead of typed model instances.

**Impact:**
- Loss of type safety for consumers
- No IDE autocompletion for response fields
- No Pydantic validation of response data

**Statistics:**
- **40 unique methods** affected (each has both sync and async versions = 80 implementations)
- **38 direct `http_res.json()` calls** in the codebase

## Affected Files and Methods

### Pro API - Games (`endpoints/pro/games.py`)

| Method                     | Async Method                     | Response Model           |
|----------------------------|----------------------------------|--------------------------|
| ~~`get_gamecenter`~~       | ~~`get_gamecenter_async`~~       | ~~`GamecenterResponse`~~ |
| ~~`get_live_game_scores`~~ | ~~`get_live_game_scores_async`~~ | ~~`LiveScoresResponse`~~ |

### Pro API - Players (`endpoints/pro/players.py`)

| Method           | Async Method           | Response Model     |
|------------------|------------------------|--------------------|
| ~~`get_player`~~ | ~~`get_player_async`~~ | ~~`PlayerDetail`~~ |

### Pro API - Content (`endpoints/pro/content.py`)

| Method                    | Async Method                    | Response Model      |
|---------------------------|---------------------------------|---------------------|
| ~~`get_season_insights`~~ | ~~`get_season_insights_async`~~ | ~~`List[Insight]`~~ |

### Pro API - Transactions (`endpoints/pro/transactions.py`)

| Method                 | Async Method                 | Response Model             |
|------------------------|------------------------------|----------------------------|
| ~~`get_transactions`~~ | ~~`get_transactions_async`~~ | ~~`TransactionsResponse`~~ |

### Pro API - Mixins

#### game_results.py
| Method | Async Method | Response Model |
|--------|--------------|----------------|
| `get_stats_boxscore` | *(sync only)* | `BoxscoreResponse` |
| `get_playlist` | *(sync only)* | `dict` (no model) |
| `get_plays_win_probability` | `get_plays_win_probability_async` | `GetPlaysWinProbabilityResponse` |

### Pro API - Stats (Factory Pattern)

#### passing.py
| Method | Async Method | Response Model |
|--------|--------------|----------------|
| `get_weekly_passing_stats` | `get_weekly_passing_stats_async` | `WeeklyPassingStatsResponse` |
| `get_passing_stats_by_season` | `get_passing_stats_by_season_async` | `PassingStatsResponse` |

#### receiving.py
| Method | Async Method | Response Model |
|--------|--------------|----------------|
| `get_weekly_receiving_stats` | `get_weekly_receiving_stats_async` | `WeeklyReceivingStatsResponse` |
| `get_receiving_stats_by_season` | `get_receiving_stats_by_season_async` | `ReceivingStatsResponse` |

#### rushing.py
| Method | Async Method | Response Model |
|--------|--------------|----------------|
| `get_weekly_rushing_stats` | `get_weekly_rushing_stats_async` | `WeeklyRushingStatsResponse` |
| `get_rushing_stats_by_season` | `get_rushing_stats_by_season_async` | `RushingStatsResponse` |

#### fantasy.py
| Method | Async Method | Response Model |
|--------|--------------|----------------|
| `get_fantasy_stats_by_season` | `get_fantasy_stats_by_season_async` | `FantasyStatsResponse` |

### Pro API - Stats (Old Pattern - Not Yet Refactored)

#### defense.py
| Method | Async Method | Response Model |
|--------|--------------|----------------|
| `get_season_summary` | `get_season_summary_async` | `DefensiveOverviewStatsResponse` |
| `get_weekly_summary` | `get_weekly_summary_async` | `DefensiveOverviewStatsResponse` |
| `get_season_pass_rush_summary` | `get_season_pass_rush_summary_async` | `PassRushStatsResponse` |
| `get_weekly_pass_rush_summary` | `get_weekly_pass_rush_summary_async` | `PassRushStatsResponse` |
| `get_season_nearest_defender_summary` | `get_season_nearest_defender_summary_async` | `dict` (no model) |
| `get_weekly_nearest_defender_summary` | `get_weekly_nearest_defender_summary_async` | `dict` (no model) |

#### team_offense.py
| Method | Async Method | Response Model |
|--------|--------------|----------------|
| `get_season_overview` | `get_season_overview_async` | `TeamOffenseStatsResponse` |
| `get_weekly_overview` | `get_weekly_overview_async` | `TeamOffenseStatsResponse` |
| `get_season_pass_stats` | `get_season_pass_stats_async` | `TeamOffensePassStatsResponse` |
| `get_weekly_pass_stats` | `get_weekly_pass_stats_async` | `TeamOffensePassStatsResponse` |
| `get_season_rush_stats` | `get_season_rush_stats_async` | `TeamOffensePassStatsResponse` |
| `get_weekly_rush_stats` | `get_weekly_rush_stats_async` | `TeamOffensePassStatsResponse` |

#### team_defense.py
| Method | Async Method | Response Model |
|--------|--------------|----------------|
| `get_season_overview` | `get_season_overview_async` | `TeamDefenseStatsResponse` |
| `get_weekly_overview` | `get_weekly_overview_async` | `TeamDefenseStatsResponse` |
| `get_season_pass_stats` | `get_season_pass_stats_async` | `TeamDefensePassStatsResponse` |
| `get_weekly_pass_stats` | `get_weekly_pass_stats_async` | `TeamDefensePassStatsResponse` |
| `get_season_rush_stats` | `get_season_rush_stats_async` | `TeamDefenseRushStatsResponse` |
| `get_weekly_rush_stats` | `get_weekly_rush_stats_async` | `TeamDefenseRushStatsResponse` |

### Regular API - Football

#### injuries.py
| Method | Async Method | Response Model |
|--------|--------------|----------------|
| `get_injury_reports` | `get_injury_reports_async` | `InjuryReportResponse` |

#### rosters.py
| Method | Async Method | Response Model |
|--------|--------------|----------------|
| `get_rosters` | `get_rosters_async` | `FootballRostersResponse` |

#### combine.py
| Method | Async Method | Response Model |
|--------|--------------|----------------|
| `get_profiles` | `get_profiles_async` | `CombineProfilesResponse` |
| `get_rankings` | `get_rankings_async` | `CombineRankingsResponse` |

#### draft.py
| Method | Async Method | Response Model |
|--------|--------------|----------------|
| `get_picks_report` | `get_picks_report_async` | `DraftResponse` |

#### games.py
| Method | Async Method | Response Model |
|--------|--------------|----------------|
| `get_weekly_game_details` | `get_weekly_game_details_async` | `List[WeeklyGameDetail]` |

## Summary by Category

| Category | Unique Methods | Implementations |
|----------|---------------|-----------------|
| Pro API - Games | 2 | 4 |
| Pro API - Players | 1 | 2 |
| Pro API - Content | 1 | 2 |
| Pro API - Transactions | 1 | 2 |
| Pro API - Mixins | 4 | 7 |
| Pro API - Stats (factory pattern) | 7 | 14 |
| Pro API - Stats (old pattern) | 18 | 36 |
| Regular API - Football | 6 | 12 |
| **Total** | **40** | **79** |

## Implementation Notes

### Files Using Factory Pattern (`return_raw_json=True`)
These files use `EndpointConfig` with `return_raw_json=True`, which delegates to `basesdk.py`:
- `endpoints/pro/games.py`
- `endpoints/pro/players.py`
- `endpoints/pro/content.py`
- `endpoints/pro/transactions.py`
- `endpoints/pro/mixins/game_schedule.py`
- `endpoints/pro/mixins/game_results.py`
- `endpoints/pro/stats/passing.py`
- `endpoints/pro/stats/receiving.py`
- `endpoints/pro/stats/rushing.py`
- `endpoints/pro/stats/fantasy.py`
- `endpoints/regular/football/*.py`

### Files Using Old Pattern (Direct `http_res.json()`)
These files still use the old boilerplate pattern with direct `http_res.json()` calls:
- `endpoints/pro/stats/defense.py` (12 occurrences)
- `endpoints/pro/stats/team_offense.py` (12 occurrences)
- `endpoints/pro/stats/team_defense.py` (12 occurrences)

**TODO:** Refactor these 3 files to use the factory pattern.

## How to Fix

For each affected method:

1. **Capture actual API response** - Call the endpoint and save the raw JSON response
2. **Compare with model schema** - Identify discrepancies between response and Pydantic model
3. **Update model definition** - Fix field names, types, optional fields, etc.
4. **Test unmarshaling** - Verify the model correctly parses the response
5. **Remove raw JSON return**:
   - For factory pattern: Remove `return_raw_json=True` from `EndpointConfig`
   - For old pattern: Remove the `if utils.match_response...` block

### Common Issues

- **Missing fields** - Response has fields not defined in model
- **Incorrect types** - Field defined as `str` but API returns `int`
- **Optional vs Required** - Field marked required but sometimes missing
- **Nested models** - Child model has schema issues
- **Enum mismatches** - API returns values not in enum definition

### Testing

After fixing a model, run the specific test:
```bash
pytest tests/test_nfl/unit/test_models/ -k "<model_name>" -v
```

And verify the endpoint works:
```bash
pytest tests/test_nfl/integration/ -k "<method_name>" -v
```
