# DefensivePassRushStatistics
(*defensive_pass_rush_statistics*)

## Overview

Individual defensive player pass rush statistics and analytics

### Available Operations

* [get_defensive_pass_rush_stats_by_season](#get_defensive_pass_rush_stats_by_season) - Get Defensive Pass Rush Statistics by Season

## get_defensive_pass_rush_stats_by_season

Retrieves comprehensive pass rush statistics for NFL defensive players during a specified season.
Returns detailed metrics including pressures, sacks, quarterback hits, time to throw allowed,
pass rush productivity, and Next Gen Stats data. Supports filtering by qualified defenders,
teams, and various sorting options. Data includes traditional pass rush stats and advanced
analytics like pass rush grade, pressure rate, and time to sack metrics.


### Example Usage

<!-- UsageSnippet language="python" operationID="getDefensivePassRushStatsBySeason" method="get" path="/api/secured/stats/defense/passRush/season" -->
```python
from griddy.nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.defensive_pass_rush_statistics.get_defensive_pass_rush_stats_by_season(season=2025, season_type=models.SeasonTypeEnum.REG, limit=35, offset=0, page=1, sort_key=models.GetDefensivePassRushStatsBySeasonQueryParamSortKey.PR, sort_value=models.SortOrderEnum.DESC, qualified_defender=False)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `season`                                                                                                                                  | *int*                                                                                                                                     | :heavy_check_mark:                                                                                                                        | Season year                                                                                                                               | 2025                                                                                                                                      |
| `season_type`                                                                                                                             | [models.SeasonTypeEnum](../../models/seasontypeenum.md)                                                                                   | :heavy_check_mark:                                                                                                                        | Type of season                                                                                                                            | REG                                                                                                                                       |
| `limit`                                                                                                                                   | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Maximum number of players to return                                                                                                       | 35                                                                                                                                        |
| `offset`                                                                                                                                  | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Number of records to skip for pagination                                                                                                  | 0                                                                                                                                         |
| `page`                                                                                                                                    | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Page number for pagination                                                                                                                | 1                                                                                                                                         |
| `sort_key`                                                                                                                                | [Optional[models.GetDefensivePassRushStatsBySeasonQueryParamSortKey]](../../models/getdefensivepassrushstatsbyseasonqueryparamsortkey.md) | :heavy_minus_sign:                                                                                                                        | Field to sort by                                                                                                                          | pr                                                                                                                                        |
| `sort_value`                                                                                                                              | [Optional[models.SortOrderEnum]](../../models/sortorderenum.md)                                                                           | :heavy_minus_sign:                                                                                                                        | Sort direction                                                                                                                            | DESC                                                                                                                                      |
| `qualified_defender`                                                                                                                      | *Optional[bool]*                                                                                                                          | :heavy_minus_sign:                                                                                                                        | Filter to only qualified defenders (minimum snap threshold)                                                                               | false                                                                                                                                     |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |
| `server_url`                                                                                                                              | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | An optional server URL to use.                                                                                                            | http://localhost:8080                                                                                                                     |

### Response

**[models.PassRushStatsResponse](../../models/passrushstatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |