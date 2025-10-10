# PlayerPassingStatistics
(*player_passing_statistics*)

## Overview

Individual player passing statistics and analytics by week

### Available Operations

* [get_player_passing_stats_by_week](#get_player_passing_stats_by_week) - Get Player Passing Statistics by Week

## get_player_passing_stats_by_week

Retrieves comprehensive passing statistics for NFL players during a specified week and season.
Returns detailed metrics including traditional stats, advanced analytics, and Next Gen Stats
data. Supports filtering by teams, qualified passers, and various sorting options.
Data includes completion percentage, yards per attempt, passer rating, EPA (Expected Points Added),
CPOE (Completion Percentage Over Expected), time to throw metrics, and game-specific context.


### Example Usage

<!-- UsageSnippet language="python" operationID="getPlayerPassingStatsByWeek" method="get" path="/api/secured/stats/players-offense/passing/week" -->
```python
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.player_passing_statistics.get_player_passing_stats_by_week(season=2025, season_type="REG", week="WEEK_10", limit=50, offset=0, page=1, sort_value="DESC", qualified_passer=False, team_offense=[
        "3900",
        "3200",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           | Example                                                                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `season`                                                                              | *int*                                                                                 | :heavy_check_mark:                                                                    | Season year                                                                           | 2025                                                                                  |
| `season_type`                                                                         | [models.SeasonTypeEnum](../../models/seasontypeenum.md)                               | :heavy_check_mark:                                                                    | Type of season                                                                        | REG                                                                                   |
| `week`                                                                                | [models.WeekSlugEnum](../../models/weekslugenum.md)                                   | :heavy_check_mark:                                                                    | Week identifier                                                                       |                                                                                       |
| `limit`                                                                               | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | Maximum number of players to return                                                   | 50                                                                                    |
| `offset`                                                                              | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | Number of records to skip for pagination                                              | 0                                                                                     |
| `page`                                                                                | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | Page number for pagination                                                            | 1                                                                                     |
| `sort_key`                                                                            | [Optional[models.PassingStatsCategoryEnum]](../../models/passingstatscategoryenum.md) | :heavy_minus_sign:                                                                    | Field to sort by                                                                      |                                                                                       |
| `sort_value`                                                                          | [Optional[models.SortOrderEnum]](../../models/sortorderenum.md)                       | :heavy_minus_sign:                                                                    | Sort direction                                                                        | DESC                                                                                  |
| `qualified_passer`                                                                    | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | Filter to only qualified passers (minimum attempts threshold)                         | false                                                                                 |
| `team_offense`                                                                        | List[*str*]                                                                           | :heavy_minus_sign:                                                                    | Filter by specific team IDs (supports multiple teams)                                 | [<br/>"3900",<br/>"3200"<br/>]                                                        |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |                                                                                       |
| `server_url`                                                                          | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | An optional server URL to use.                                                        | http://localhost:8080                                                                 |

### Response

**[models.WeeklyPassingStatsResponse](../../models/weeklypassingstatsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |