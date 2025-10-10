# PlayerRushingStatistics
(*player_rushing_statistics*)

## Overview

Individual player rushing statistics and analytics

### Available Operations

* [get_player_rushing_stats_by_season](#get_player_rushing_stats_by_season) - Get Player Rushing Statistics by Season
* [get_player_rushing_stats_by_week](#get_player_rushing_stats_by_week) - Get Player Rushing Statistics by Week

## get_player_rushing_stats_by_season

Retrieves comprehensive rushing statistics for NFL players during a specified season.
Returns detailed metrics including traditional stats, advanced analytics, and Next Gen Stats
data. Supports filtering by teams, qualified rushers, and various sorting options.
Data includes yards per carry, EPA (Expected Points Added), RYOE (Rush Yards Over Expected),
efficiency metrics, yards before/after contact, and situational breakdowns.


### Example Usage

<!-- UsageSnippet language="python" operationID="getPlayerRushingStatsBySeason" method="get" path="/api/secured/stats/players-offense/rushing/season" -->
```python
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.player_rushing_statistics.get_player_rushing_stats_by_season(season=2025, season_type="REG", limit=3, offset=0, page=1, sort_key="yds", sort_value="DESC", qualified_rusher=False, team_offense=[
        "3000",
        "3900",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   | Example                                                                                                       |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `season`                                                                                                      | *int*                                                                                                         | :heavy_check_mark:                                                                                            | Season year                                                                                                   | 2025                                                                                                          |
| `season_type`                                                                                                 | [models.SeasonTypeEnum](../../models/seasontypeenum.md)                                                       | :heavy_check_mark:                                                                                            | Type of season                                                                                                | REG                                                                                                           |
| `limit`                                                                                                       | *Optional[int]*                                                                                               | :heavy_minus_sign:                                                                                            | Maximum number of players to return                                                                           | 3                                                                                                             |
| `offset`                                                                                                      | *Optional[int]*                                                                                               | :heavy_minus_sign:                                                                                            | Number of records to skip for pagination                                                                      | 0                                                                                                             |
| `page`                                                                                                        | *Optional[int]*                                                                                               | :heavy_minus_sign:                                                                                            | Page number for pagination                                                                                    | 1                                                                                                             |
| `sort_key`                                                                                                    | [Optional[models.GetPlayerRushingStatsBySeasonSortKey]](../../models/getplayerrushingstatsbyseasonsortkey.md) | :heavy_minus_sign:                                                                                            | Field to sort by                                                                                              | yds                                                                                                           |
| `sort_value`                                                                                                  | [Optional[models.SortOrderEnum]](../../models/sortorderenum.md)                                               | :heavy_minus_sign:                                                                                            | Sort direction                                                                                                | DESC                                                                                                          |
| `qualified_rusher`                                                                                            | *Optional[bool]*                                                                                              | :heavy_minus_sign:                                                                                            | Filter to only qualified rushers (minimum attempts threshold)                                                 | false                                                                                                         |
| `team_offense`                                                                                                | List[*str*]                                                                                                   | :heavy_minus_sign:                                                                                            | Filter by specific team IDs (supports multiple teams)                                                         | [<br/>"3000",<br/>"3900"<br/>]                                                                                |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |                                                                                                               |
| `server_url`                                                                                                  | *Optional[str]*                                                                                               | :heavy_minus_sign:                                                                                            | An optional server URL to use.                                                                                | http://localhost:8080                                                                                         |

### Response

**[models.RushingStatsResponse](../../models/rushingstatsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |

## get_player_rushing_stats_by_week

Retrieves comprehensive rushing statistics for NFL players during a specified week and season.
Returns detailed metrics including traditional stats, advanced analytics, and Next Gen Stats
data. Supports filtering by teams, qualified rushers, and various sorting options.
Data includes yards per carry, EPA (Expected Points Added), RYOE (Rush Yards Over Expected),
efficiency metrics, yards before/after contact, and game-specific context.


### Example Usage

<!-- UsageSnippet language="python" operationID="getPlayerRushingStatsByWeek" method="get" path="/api/secured/stats/players-offense/rushing/week" -->
```python
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.player_rushing_statistics.get_player_rushing_stats_by_week(season=2025, season_type="REG", week="WEEK_4", limit=50, offset=0, page=1, sort_key="yds", sort_value="DESC", qualified_rusher=False, team_offense=[
        "3900",
        "3200",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               | Example                                                                                                   |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `season`                                                                                                  | *int*                                                                                                     | :heavy_check_mark:                                                                                        | Season year                                                                                               | 2025                                                                                                      |
| `season_type`                                                                                             | [models.SeasonTypeEnum](../../models/seasontypeenum.md)                                                   | :heavy_check_mark:                                                                                        | Type of season                                                                                            | REG                                                                                                       |
| `week`                                                                                                    | [models.WeekSlugEnum](../../models/weekslugenum.md)                                                       | :heavy_check_mark:                                                                                        | Week identifier                                                                                           |                                                                                                           |
| `limit`                                                                                                   | *Optional[int]*                                                                                           | :heavy_minus_sign:                                                                                        | Maximum number of players to return                                                                       | 50                                                                                                        |
| `offset`                                                                                                  | *Optional[int]*                                                                                           | :heavy_minus_sign:                                                                                        | Number of records to skip for pagination                                                                  | 0                                                                                                         |
| `page`                                                                                                    | *Optional[int]*                                                                                           | :heavy_minus_sign:                                                                                        | Page number for pagination                                                                                | 1                                                                                                         |
| `sort_key`                                                                                                | [Optional[models.GetPlayerRushingStatsByWeekSortKey]](../../models/getplayerrushingstatsbyweeksortkey.md) | :heavy_minus_sign:                                                                                        | Field to sort by                                                                                          | yds                                                                                                       |
| `sort_value`                                                                                              | [Optional[models.SortOrderEnum]](../../models/sortorderenum.md)                                           | :heavy_minus_sign:                                                                                        | Sort direction                                                                                            | DESC                                                                                                      |
| `qualified_rusher`                                                                                        | *Optional[bool]*                                                                                          | :heavy_minus_sign:                                                                                        | Filter to only qualified rushers (minimum attempts threshold)                                             | false                                                                                                     |
| `team_offense`                                                                                            | List[*str*]                                                                                               | :heavy_minus_sign:                                                                                        | Filter by specific team IDs (supports multiple teams)                                                     | [<br/>"3900",<br/>"3200"<br/>]                                                                            |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |                                                                                                           |
| `server_url`                                                                                              | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | An optional server URL to use.                                                                            | http://localhost:8080                                                                                     |

### Response

**[models.WeeklyRushingStatsResponse](../../models/weeklyrushingstatsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |