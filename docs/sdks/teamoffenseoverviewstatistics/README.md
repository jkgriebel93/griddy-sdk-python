# TeamOffenseOverviewStatistics
(*team_offense_overview_statistics*)

## Overview

Comprehensive team offensive overview statistics and situational analytics

### Available Operations

* [get_team_offense_overview_stats_by_season](#get_team_offense_overview_stats_by_season) - Get Team Offense Overview Statistics by Season

## get_team_offense_overview_stats_by_season

Retrieves comprehensive offensive overview statistics for NFL teams during a specified season. Returns detailed metrics including traditional offensive stats, advanced analytics like EPA and efficiency ratings, Next Gen Stats data, and situational performance breakdowns. Supports filtering by various offensive situations including formations (shotgun, under center, pistol), game situations (leading, trailing, tied), and field positions (red zone, goal-to-go). Includes total offense, passing offense, rushing offense, and scoring metrics.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTeamOffenseOverviewStatsBySeason" method="get" path="/api/secured/stats/team-offense/overview/season" -->
```python
from griddy.nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.team_offense_overview_statistics.get_team_offense_overview_stats_by_season(season=2025, season_type=models.SeasonTypeEnum.REG, limit=35, offset=0, page=1, sort_key=models.GetTeamOffenseOverviewStatsBySeasonQueryParamSortKey.YPG, sort_value=models.SortOrderEnum.DESC, team_defense="2250", split=[
        models.QueryParamSplit.TEAM_WHEN_LEADING,
    ])

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `season`                                                                                                                                      | *int*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | Season year                                                                                                                                   | 2025                                                                                                                                          |
| `season_type`                                                                                                                                 | [models.SeasonTypeEnum](../../models/seasontypeenum.md)                                                                                       | :heavy_check_mark:                                                                                                                            | Type of season                                                                                                                                | REG                                                                                                                                           |
| `limit`                                                                                                                                       | *Optional[int]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Maximum number of teams to return                                                                                                             | 35                                                                                                                                            |
| `offset`                                                                                                                                      | *Optional[int]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Number of records to skip for pagination                                                                                                      | 0                                                                                                                                             |
| `page`                                                                                                                                        | *Optional[int]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Page number for pagination                                                                                                                    | 1                                                                                                                                             |
| `sort_key`                                                                                                                                    | [Optional[models.GetTeamOffenseOverviewStatsBySeasonQueryParamSortKey]](../../models/getteamoffenseoverviewstatsbyseasonqueryparamsortkey.md) | :heavy_minus_sign:                                                                                                                            | Field to sort by                                                                                                                              | ypg                                                                                                                                           |
| `sort_value`                                                                                                                                  | [Optional[models.SortOrderEnum]](../../models/sortorderenum.md)                                                                               | :heavy_minus_sign:                                                                                                                            | Sort direction                                                                                                                                | DESC                                                                                                                                          |
| `team_defense`                                                                                                                                | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | Filter by specific team identifier                                                                                                            | 2250                                                                                                                                          |
| `split`                                                                                                                                       | List[[models.QueryParamSplit](../../models/queryparamsplit.md)]                                                                               | :heavy_minus_sign:                                                                                                                            | Offensive situation splits to filter by (supports multiple values)                                                                            | [<br/>"TEAM_WHEN_LEADING"<br/>]                                                                                                               |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |
| `server_url`                                                                                                                                  | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | An optional server URL to use.                                                                                                                | http://localhost:8080                                                                                                                         |

### Response

**[models.TeamOffenseOverviewStatsResponse](../../models/teamoffenseoverviewstatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |