# TeamDefenseStatistics
(*team_defense_statistics*)

## Overview

Comprehensive team defensive statistics and situational analytics

### Available Operations

* [get_team_defense_stats_by_season](#get_team_defense_stats_by_season) - Get Team Defense Statistics by Season

## get_team_defense_stats_by_season

Retrieves comprehensive defensive statistics for NFL teams during a specified season. Returns detailed metrics including traditional defensive stats, advanced analytics like EPA and RYOE, Next Gen Stats data, and situational performance breakdowns. Supports filtering by various defensive situations including personnel packages (Base, Nickel, Dime), game situations (leading, trailing, tied), field positions (red zone, goal-to-go), and offensive formations faced (shotgun, under center, pistol, motion).

### Example Usage

<!-- UsageSnippet language="python" operationID="getTeamDefenseStatsBySeason" method="get" path="/api/secured/stats/team-defense/overview/season" -->
```python
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.team_defense_statistics.get_team_defense_stats_by_season(season=2025, season_type="REG", limit=35, offset=0, page=1, sort_key="ypg", sort_value="DESC", split=[
        "TEAM_DEFENSE_NICKEL",
        "TEAM_DEFENSE_RED_ZONE",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               | Example                                                                                                   |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `season`                                                                                                  | *int*                                                                                                     | :heavy_check_mark:                                                                                        | Season year                                                                                               | 2025                                                                                                      |
| `season_type`                                                                                             | [models.SeasonTypeEnum](../../models/seasontypeenum.md)                                                   | :heavy_check_mark:                                                                                        | Type of season                                                                                            | REG                                                                                                       |
| `limit`                                                                                                   | *Optional[int]*                                                                                           | :heavy_minus_sign:                                                                                        | Maximum number of teams to return                                                                         | 35                                                                                                        |
| `offset`                                                                                                  | *Optional[int]*                                                                                           | :heavy_minus_sign:                                                                                        | Number of records to skip for pagination                                                                  | 0                                                                                                         |
| `page`                                                                                                    | *Optional[int]*                                                                                           | :heavy_minus_sign:                                                                                        | Page number for pagination                                                                                | 1                                                                                                         |
| `sort_key`                                                                                                | [Optional[models.GetTeamDefenseStatsBySeasonSortKey]](../../models/getteamdefensestatsbyseasonsortkey.md) | :heavy_minus_sign:                                                                                        | Field to sort by                                                                                          | ypg                                                                                                       |
| `sort_value`                                                                                              | [Optional[models.SortOrderEnum]](../../models/sortorderenum.md)                                           | :heavy_minus_sign:                                                                                        | Sort direction                                                                                            | DESC                                                                                                      |
| `split`                                                                                                   | List[[models.GetTeamDefenseStatsBySeasonSplit](../../models/getteamdefensestatsbyseasonsplit.md)]         | :heavy_minus_sign:                                                                                        | Defensive situation splits to filter by (supports multiple values)                                        | [<br/>"TEAM_DEFENSE_NICKEL",<br/>"TEAM_DEFENSE_RED_ZONE"<br/>]                                            |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |                                                                                                           |
| `server_url`                                                                                              | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | An optional server URL to use.                                                                            | http://localhost:8080                                                                                     |

### Response

**[models.TeamDefenseStatsResponse](../../models/teamdefensestatsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |