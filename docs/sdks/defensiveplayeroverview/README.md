# DefensivePlayerOverview
(*defensive_player_overview*)

## Overview

Comprehensive individual defensive player statistics and analytics

### Available Operations

* [get_defensive_overview_stats_by_season](#get_defensive_overview_stats_by_season) - Get Defensive Player Overview Statistics by Season

## get_defensive_overview_stats_by_season

Retrieves comprehensive defensive overview statistics for NFL players during a specified season. Returns detailed metrics including traditional defensive stats (tackles, stops, sacks), coverage metrics (targets, completions allowed, pass rating allowed), pass rush data, and advanced analytics. Supports filtering by qualified defenders, teams, and various sorting options. Data includes snap counts, tackle efficiency, coverage effectiveness, and situational performance.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDefensiveOverviewStatsBySeason" method="get" path="/api/secured/stats/defense/overview/season" -->
```python
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.defensive_player_overview.get_defensive_overview_stats_by_season(season=2025, season_type="REG", limit=3, offset=0, page=1, sort_key="sack", sort_value="DESC", qualified_defender=False, team_defense=[
        "3000",
        "3900",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           | Example                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `season`                                                                                                              | *int*                                                                                                                 | :heavy_check_mark:                                                                                                    | Season year                                                                                                           | 2025                                                                                                                  |
| `season_type`                                                                                                         | [models.SeasonTypeEnum](../../models/seasontypeenum.md)                                                               | :heavy_check_mark:                                                                                                    | Type of season                                                                                                        | REG                                                                                                                   |
| `limit`                                                                                                               | *Optional[int]*                                                                                                       | :heavy_minus_sign:                                                                                                    | Maximum number of players to return                                                                                   | 3                                                                                                                     |
| `offset`                                                                                                              | *Optional[int]*                                                                                                       | :heavy_minus_sign:                                                                                                    | Number of records to skip for pagination                                                                              | 0                                                                                                                     |
| `page`                                                                                                                | *Optional[int]*                                                                                                       | :heavy_minus_sign:                                                                                                    | Page number for pagination                                                                                            | 1                                                                                                                     |
| `sort_key`                                                                                                            | [Optional[models.GetDefensiveOverviewStatsBySeasonSortKey]](../../models/getdefensiveoverviewstatsbyseasonsortkey.md) | :heavy_minus_sign:                                                                                                    | Field to sort by                                                                                                      | sack                                                                                                                  |
| `sort_value`                                                                                                          | [Optional[models.SortOrderEnum]](../../models/sortorderenum.md)                                                       | :heavy_minus_sign:                                                                                                    | Sort direction                                                                                                        | DESC                                                                                                                  |
| `qualified_defender`                                                                                                  | *Optional[bool]*                                                                                                      | :heavy_minus_sign:                                                                                                    | Filter to only qualified defenders (minimum snap threshold)                                                           | false                                                                                                                 |
| `team_defense`                                                                                                        | List[*str*]                                                                                                           | :heavy_minus_sign:                                                                                                    | Filter by specific team IDs (supports multiple teams)                                                                 | [<br/>"3000",<br/>"3900"<br/>]                                                                                        |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |                                                                                                                       |
| `server_url`                                                                                                          | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | An optional server URL to use.                                                                                        | http://localhost:8080                                                                                                 |

### Response

**[models.DefensiveOverviewStatsResponse](../../models/defensiveoverviewstatsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |