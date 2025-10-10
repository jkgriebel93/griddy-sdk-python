# TeamDefenseRushStatistics
(*team_defense_rush_statistics*)

## Overview

Comprehensive team defensive rush statistics and situational analytics

### Available Operations

* [get_team_defense_rush_stats_by_season](#get_team_defense_rush_stats_by_season) - Get Team Defense Rush Statistics by Season

## get_team_defense_rush_stats_by_season

Retrieves comprehensive rush defense statistics for NFL teams during a specified season.
Returns detailed metrics including traditional run defense stats, advanced analytics like EPA
and RYOE (Rush Yards Over Expected), Next Gen Stats data, and situational performance
breakdowns. Supports various sorting options and includes stuff rates, gap analysis,
box count distributions, and directional rush defense metrics.


### Example Usage

<!-- UsageSnippet language="python" operationID="getTeamDefenseRushStatsBySeason" method="get" path="/api/secured/stats/team-defense/rush/season" -->
```python
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.team_defense_rush_statistics.get_team_defense_rush_stats_by_season(season=2025, season_type="REG", limit=35, offset=0, page=1, sort_key="rushYpg", sort_value="DESC")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       | Example                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `season`                                                                                                          | *int*                                                                                                             | :heavy_check_mark:                                                                                                | Season year                                                                                                       | 2025                                                                                                              |
| `season_type`                                                                                                     | [models.SeasonTypeEnum](../../models/seasontypeenum.md)                                                           | :heavy_check_mark:                                                                                                | Type of season                                                                                                    | REG                                                                                                               |
| `limit`                                                                                                           | *Optional[int]*                                                                                                   | :heavy_minus_sign:                                                                                                | Maximum number of teams to return                                                                                 | 35                                                                                                                |
| `offset`                                                                                                          | *Optional[int]*                                                                                                   | :heavy_minus_sign:                                                                                                | Number of records to skip for pagination                                                                          | 0                                                                                                                 |
| `page`                                                                                                            | *Optional[int]*                                                                                                   | :heavy_minus_sign:                                                                                                | Page number for pagination                                                                                        | 1                                                                                                                 |
| `sort_key`                                                                                                        | [Optional[models.GetTeamDefenseRushStatsBySeasonSortKey]](../../models/getteamdefenserushstatsbyseasonsortkey.md) | :heavy_minus_sign:                                                                                                | Field to sort by                                                                                                  | rushYpg                                                                                                           |
| `sort_value`                                                                                                      | [Optional[models.SortOrderEnum]](../../models/sortorderenum.md)                                                   | :heavy_minus_sign:                                                                                                | Sort direction                                                                                                    | DESC                                                                                                              |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |                                                                                                                   |
| `server_url`                                                                                                      | *Optional[str]*                                                                                                   | :heavy_minus_sign:                                                                                                | An optional server URL to use.                                                                                    | http://localhost:8080                                                                                             |

### Response

**[models.TeamDefenseRushStatsResponse](../../models/teamdefenserushstatsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |