# PlayerStatistics
(*player_statistics*)

## Overview

Individual player passing statistics and analytics

### Available Operations

* [get_player_passing_stats_by_season](#get_player_passing_stats_by_season) - Get Player Passing Statistics by Season

## get_player_passing_stats_by_season

Retrieves comprehensive passing statistics for NFL players during a specified season.
Returns detailed metrics including traditional stats, advanced analytics, and Next Gen Stats
data. Supports filtering by teams, qualified passers only, and various sorting options.
Data includes completion percentage, yards per attempt, passer rating, EPA (Expected Points Added),
CPOE (Completion Percentage Over Expected), time to throw metrics, and situational statistics.


### Example Usage

<!-- UsageSnippet language="python" operationID="getPlayerPassingStatsBySeason" method="get" path="/api/secured/stats/players-offense/passing/season" -->
```python
from griddy.nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.player_statistics.get_player_passing_stats_by_season(season=2025, season_type=models.SeasonTypeEnum.REG, limit=35, offset=0, page=1, sort_value=models.SortOrderEnum.DESC, qualified_passer=True, team_offense=[
        "3000",
        "3900",
    ])

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           | Example                                                                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `season`                                                                              | *int*                                                                                 | :heavy_check_mark:                                                                    | Season year                                                                           | 2025                                                                                  |
| `season_type`                                                                         | [models.SeasonTypeEnum](../../models/seasontypeenum.md)                               | :heavy_check_mark:                                                                    | Type of season                                                                        | REG                                                                                   |
| `limit`                                                                               | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | Maximum number of players to return                                                   | 35                                                                                    |
| `offset`                                                                              | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | Number of records to skip for pagination                                              | 0                                                                                     |
| `page`                                                                                | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | Page number for pagination                                                            | 1                                                                                     |
| `sort_key`                                                                            | [Optional[models.PassingStatsCategoryEnum]](../../models/passingstatscategoryenum.md) | :heavy_minus_sign:                                                                    | Field to sort by                                                                      |                                                                                       |
| `sort_value`                                                                          | [Optional[models.SortOrderEnum]](../../models/sortorderenum.md)                       | :heavy_minus_sign:                                                                    | Sort direction                                                                        | DESC                                                                                  |
| `qualified_passer`                                                                    | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | Filter to only qualified passers (minimum attempts threshold)                         | true                                                                                  |
| `team_offense`                                                                        | List[*str*]                                                                           | :heavy_minus_sign:                                                                    | Filter by specific team IDs (supports multiple teams)                                 | [<br/>"3000",<br/>"3900"<br/>]                                                        |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |                                                                                       |
| `server_url`                                                                          | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | An optional server URL to use.                                                        | http://localhost:8080                                                                 |

### Response

**[models.PassingStatsResponse](../../models/passingstatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |