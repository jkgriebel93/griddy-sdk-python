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
- All files now use the factory pattern with `return_raw_json=True`

## Affected Files and Methods

### Pro API - Games (`endpoints/pro/games.py`)

| Fixed | Method | Async Method | Response Model |
|:-----:|--------|--------------|----------------|
| [x] | `get_gamecenter` | `get_gamecenter_async` | `GamecenterResponse` |
| [x] | `get_live_game_scores` | `get_live_game_scores_async` | `LiveScoresResponse` |

### Pro API - Players (`endpoints/pro/players.py`)

| Fixed | Method | Async Method | Response Model |
|:-----:|--------|--------------|----------------|
| [x] | `get_player` | `get_player_async` | `PlayerDetail` |

### Pro API - Content (`endpoints/pro/content.py`)

| Fixed | Method | Async Method | Response Model |
|:-----:|--------|--------------|----------------|
| [x] | `get_season_insights` | `get_season_insights_async` | `List[Insight]` |

### Pro API - Transactions (`endpoints/pro/transactions.py`)

| Fixed | Method | Async Method | Response Model |
|:-----:|--------|--------------|----------------|
| [x] | `get_transactions` | `get_transactions_async` | `TransactionsResponse` |

### Pro API - Mixins

#### game_results.py
| Fixed | Method | Async Method | Response Model |
|:-----:|--------|--------------|----------------|
| [x] | `get_stats_boxscore` | *(sync only)* | `BoxscoreResponse` |
| [x] | `get_playlist` | *(sync only)* | `PlaylistResponse` |
| [x] | `get_plays_win_probability` | `get_plays_win_probability_async` | `GetPlaysWinProbabilityResponse` |

### Pro API - Stats

#### passing.py
| Fixed | Method | Async Method | Response Model |
|:-----:|--------|--------------|----------------|
|  [x]  | `get_weekly_summary` | `get_weekly_summary_async` | `WeeklyPassingStatsResponse` |
|  [x]  | `get_season_summary` | `get_season_summary_async` | `PassingStatsResponse` |

#### receiving.py
| Fixed | Method | Async Method | Response Model |
|:-----:|--------|--------------|----------------|
|  [x]  | `get_weekly_summary` | `get_weekly_summary_async` | `WeeklyReceivingStatsResponse` |
|  [x]  | `get_season_summary` | `get_season_summary_async` | `ReceivingStatsResponse` |

#### rushing.py
| Fixed | Method | Async Method | Response Model |
|:-----:|--------|--------------|----------------|
|  [x]  | `get_weekly_summary` | `get_weekly_summary_async` | `WeeklyRushingStatsResponse` |
|  [x]  | `get_season_summary` | `get_season_summary_async` | `RushingStatsResponse` |

#### fantasy.py
| Fixed | Method | Async Method | Response Model |
|:-----:|--------|--------------|----------------|
|  [x]  | `get_fantasy_stats_by_season` | `get_fantasy_stats_by_season_async` | `FantasyStatsResponse` |

#### defense.py
| Fixed | Method | Async Method | Response Model |
|:-----:|--------|--------------|----------------|
|  [x]  | `get_season_summary` | `get_season_summary_async` | `DefensiveOverviewStatsResponse` |
|  [x]  | `get_weekly_summary` | `get_weekly_summary_async` | `DefensiveOverviewStatsResponse` |
|  [x]  | `get_season_pass_rush_summary` | `get_season_pass_rush_summary_async` | `PassRushStatsResponse` |
|  [x]  | `get_weekly_pass_rush_summary` | `get_weekly_pass_rush_summary_async` | `PassRushStatsResponse` |
|  [x]  | `get_season_nearest_defender_summary` | `get_season_nearest_defender_summary_async` | `dict` (no model) |
|  [x]  | `get_weekly_nearest_defender_summary` | `get_weekly_nearest_defender_summary_async` | `dict` (no model) |

#### team_offense.py
| Fixed | Method | Async Method | Response Model |
|:-----:|--------|--------------|----------------|
|  [x]  | `get_season_overview` | `get_season_overview_async` | `TeamOffenseStatsResponse` |
|  [x]  | `get_weekly_overview` | `get_weekly_overview_async` | `TeamOffenseStatsResponse` |
|  [x]  | `get_season_pass_stats` | `get_season_pass_stats_async` | `TeamOffensePassStatsResponse` |
|  [x]  | `get_weekly_pass_stats` | `get_weekly_pass_stats_async` | `TeamOffensePassStatsResponse` |
|  [x]  | `get_season_rush_stats` | `get_season_rush_stats_async` | `TeamOffensePassStatsResponse` |
|  [x]  | `get_weekly_rush_stats` | `get_weekly_rush_stats_async` | `TeamOffensePassStatsResponse` |

#### team_defense.py
| Fixed | Method | Async Method | Response Model |
|:-----:|--------|--------------|----------------|
|  [X]  | `get_season_overview` | `get_season_overview_async` | `TeamDefenseStatsResponse` |
|  [X]  | `get_weekly_overview` | `get_weekly_overview_async` | `TeamDefenseStatsResponse` |
|  [x]  | `get_season_pass_stats` | `get_season_pass_stats_async` | `TeamDefensePassStatsResponse` |
|  [x]  | `get_weekly_pass_stats` | `get_weekly_pass_stats_async` | `TeamDefensePassStatsResponse` |
|  [x]  | `get_season_rush_stats` | `get_season_rush_stats_async` | `TeamDefenseRushStatsResponse` |
|  [x]  | `get_weekly_rush_stats` | `get_weekly_rush_stats_async` | `TeamDefenseRushStatsResponse` |

### Regular API - Football

#### rosters.py
| Fixed | Method | Async Method | Response Model |
|:-----:|--------|--------------|----------------|
|  [x]  | `get_rosters` | `get_rosters_async` | `FootballRostersResponse` |

#### combine.py
| Fixed | Method | Async Method | Response Model |
|:-----:|--------|--------------|----------------|
|  [x]  | `get_profiles` | `get_profiles_async` | `CombineProfilesResponse` |
|  [x]  | `get_rankings` | `get_rankings_async` | `CombineRankingsResponse` |

#### draft.py
| Fixed | Method | Async Method | Response Model |
|:-----:|--------|--------------|----------------|
|  [x]  | `get_picks_report` | `get_picks_report_async` | `DraftResponse` |

#### games.py
| Fixed | Method | Async Method | Response Model |
|:-----:|--------|--------------|----------------|
| [ ] | `get_weekly_game_details` | `get_weekly_game_details_async` | `List[WeeklyGameDetail]` |

## Summary by Category

| Category | Unique Methods | Fixed |
|----------|---------------|-------|
| Pro API - Games | 2 | 2 |
| Pro API - Players | 1 | 1 |
| Pro API - Content | 1 | 1 |
| Pro API - Transactions | 1 | 1 |
| Pro API - Mixins | 3 | 3 |
| Pro API - Stats | 25 | 0 |
| Regular API - Football | 6 | 0 |
| **Total** | **39** | **8** |

## Implementation Notes

### Factory Pattern

All endpoint files now use the `EndpointConfig` factory pattern with `return_raw_json=True`:

```python
def _get_example_config(self, ...) -> EndpointConfig:
    return EndpointConfig(
        method="GET",
        path="/api/example",
        operation_id="getExample",
        request=models.ExampleRequest(...),
        response_type=models.ExampleResponse,
        error_status_codes=STATS_ERROR_CODES,
        return_raw_json=True,  # TODO: Fix Pydantic model
        ...
    )
```

## How to Fix

For each affected method:

1. **Capture actual API response** - Call the endpoint and save the raw JSON response
2. **Compare with model schema** - Identify discrepancies between response and Pydantic model
3. **Update model definition** - Fix field names, types, optional fields, etc.
4. **Test unmarshaling** - Verify the model correctly parses the response
5. **Remove raw JSON return** - Set `return_raw_json=False` (or remove the parameter) from `EndpointConfig`
6. **Mark as fixed** - Check the box in this document

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
