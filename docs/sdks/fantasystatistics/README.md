# FantasyStatistics
(*fantasy_statistics*)

## Overview

Fantasy football player statistics and scoring metrics

### Available Operations

* [get_fantasy_stats_by_season](#get_fantasy_stats_by_season) - Get Fantasy Football Statistics by Season

## get_fantasy_stats_by_season

Retrieves comprehensive fantasy football statistics for NFL players during a specified season.
Returns fantasy-relevant metrics including standard scoring, PPR scoring, snap counts, and
target share data. Supports filtering by position groups (QB, RB, WR, TE, SPEC), teams,
minimum offensive snap thresholds, and rolling N-week windows for recent performance analysis.
Data includes traditional fantasy categories and advanced metrics for lineup optimization.


### Example Usage

<!-- UsageSnippet language="python" operationID="getFantasyStatsBySeason" method="get" path="/api/secured/stats/fantasy/season" -->
```python
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.fantasy_statistics.get_fantasy_stats_by_season(season=2025, season_type="REG", limit=35, offset=0, page=1, sort_key="fpStd", sort_value="DESC", position_group=[
        "QB",
    ], team_offense="3900", team_defense="4600", min_offensive_snaps=75, last_n_weeks=3)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       | Example                                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `season`                                                                                          | *int*                                                                                             | :heavy_check_mark:                                                                                | Season year                                                                                       | 2025                                                                                              |
| `season_type`                                                                                     | [models.SeasonTypeEnum](../../models/seasontypeenum.md)                                           | :heavy_check_mark:                                                                                | Type of season                                                                                    | REG                                                                                               |
| `limit`                                                                                           | *Optional[int]*                                                                                   | :heavy_minus_sign:                                                                                | Maximum number of players to return                                                               | 35                                                                                                |
| `offset`                                                                                          | *Optional[int]*                                                                                   | :heavy_minus_sign:                                                                                | Number of records to skip for pagination                                                          | 0                                                                                                 |
| `page`                                                                                            | *Optional[int]*                                                                                   | :heavy_minus_sign:                                                                                | Page number for pagination                                                                        | 1                                                                                                 |
| `sort_key`                                                                                        | [Optional[models.GetFantasyStatsBySeasonSortKey]](../../models/getfantasystatsbyseasonsortkey.md) | :heavy_minus_sign:                                                                                | Field to sort by                                                                                  | fpStd                                                                                             |
| `sort_value`                                                                                      | [Optional[models.SortOrderEnum]](../../models/sortorderenum.md)                                   | :heavy_minus_sign:                                                                                | Sort direction                                                                                    | DESC                                                                                              |
| `position_group`                                                                                  | List[[models.PositionGroup](../../models/positiongroup.md)]                                       | :heavy_minus_sign:                                                                                | Filter by position groups (supports multiple positions)                                           | [<br/>"QB"<br/>]                                                                                  |
| `team_offense`                                                                                    | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | Filter by specific offensive team ID                                                              | 3900                                                                                              |
| `team_defense`                                                                                    | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | Filter by specific defensive team ID (opponent analysis)                                          | 4600                                                                                              |
| `min_offensive_snaps`                                                                             | *Optional[int]*                                                                                   | :heavy_minus_sign:                                                                                | Minimum offensive snaps threshold for inclusion                                                   | 75                                                                                                |
| `last_n_weeks`                                                                                    | *Optional[int]*                                                                                   | :heavy_minus_sign:                                                                                | Number of recent weeks to analyze (rolling window)                                                | 3                                                                                                 |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |                                                                                                   |
| `server_url`                                                                                      | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | An optional server URL to use.                                                                    | http://localhost:8080                                                                             |

### Response

**[models.FantasyStatsResponse](../../models/fantasystatsresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |