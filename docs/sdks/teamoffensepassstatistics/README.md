# TeamOffensePassStatistics
(*team_offense_pass_statistics*)

## Overview

Comprehensive team offensive pass statistics and situational analytics

### Available Operations

* [get_team_offense_pass_stats_by_season](#get_team_offense_pass_stats_by_season) - Get Team Offense Pass Statistics by Season

## get_team_offense_pass_stats_by_season

Retrieves comprehensive pass offense statistics for NFL teams during a specified season.
Returns detailed metrics including traditional offensive stats, advanced analytics like EPA
and YACOE (Yards After Catch Over Expected), Next Gen Stats data, and situational performance
breakdowns. Supports various sorting options and includes pressure rates, quarterback metrics,
completion rates, and receiver separation data.


### Example Usage

<!-- UsageSnippet language="python" operationID="getTeamOffensePassStatsBySeason" method="get" path="/api/secured/stats/team-offense/pass/season" -->
```python
from griddy.nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.team_offense_pass_statistics.get_team_offense_pass_stats_by_season(season=2025, season_type=models.SeasonTypeEnum.REG, limit=35, offset=0, page=1, sort_key=models.GetTeamOffensePassStatsBySeasonQueryParamSortKey.PASS_YPG, sort_value=models.SortOrderEnum.DESC, team_defense="2250")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                             | Type                                                                                                                                  | Required                                                                                                                              | Description                                                                                                                           | Example                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `season`                                                                                                                              | *int*                                                                                                                                 | :heavy_check_mark:                                                                                                                    | Season year                                                                                                                           | 2025                                                                                                                                  |
| `season_type`                                                                                                                         | [models.SeasonTypeEnum](../../models/seasontypeenum.md)                                                                               | :heavy_check_mark:                                                                                                                    | Type of season                                                                                                                        | REG                                                                                                                                   |
| `limit`                                                                                                                               | *Optional[int]*                                                                                                                       | :heavy_minus_sign:                                                                                                                    | Maximum number of teams to return                                                                                                     | 35                                                                                                                                    |
| `offset`                                                                                                                              | *Optional[int]*                                                                                                                       | :heavy_minus_sign:                                                                                                                    | Number of records to skip for pagination                                                                                              | 0                                                                                                                                     |
| `page`                                                                                                                                | *Optional[int]*                                                                                                                       | :heavy_minus_sign:                                                                                                                    | Page number for pagination                                                                                                            | 1                                                                                                                                     |
| `sort_key`                                                                                                                            | [Optional[models.GetTeamOffensePassStatsBySeasonQueryParamSortKey]](../../models/getteamoffensepassstatsbyseasonqueryparamsortkey.md) | :heavy_minus_sign:                                                                                                                    | Field to sort by                                                                                                                      | passYpg                                                                                                                               |
| `sort_value`                                                                                                                          | [Optional[models.SortOrderEnum]](../../models/sortorderenum.md)                                                                       | :heavy_minus_sign:                                                                                                                    | Sort direction                                                                                                                        | DESC                                                                                                                                  |
| `team_defense`                                                                                                                        | *Optional[str]*                                                                                                                       | :heavy_minus_sign:                                                                                                                    | Filter by specific team ID                                                                                                            | 2250                                                                                                                                  |
| `retries`                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                      | :heavy_minus_sign:                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                   |                                                                                                                                       |
| `server_url`                                                                                                                          | *Optional[str]*                                                                                                                       | :heavy_minus_sign:                                                                                                                    | An optional server URL to use.                                                                                                        | http://localhost:8080                                                                                                                 |

### Response

**[models.TeamOffensePassStatsResponse](../../models/teamoffensepassstatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |