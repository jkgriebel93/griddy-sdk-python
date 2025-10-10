# DefensiveStatistics
(*defensive_statistics*)

## Overview

Individual defensive player statistics and coverage analytics

### Available Operations

* [get_defensive_stats_by_season](#get_defensive_stats_by_season) - Get Defensive Player Statistics by Season

## get_defensive_stats_by_season

Retrieves comprehensive defensive statistics for NFL players during a specified season. Returns detailed coverage metrics including targets allowed, completion rates, pass rating allowed, yards after catch prevention, and advanced Next Gen Stats data. Supports filtering by qualified defenders, teams, and various sorting options. Data includes traditional defensive stats and advanced analytics like EPA (Expected Points Added), CROE (Completion Rate Over Expected), receiver separation allowed, and coverage snap counts.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDefensiveStatsBySeason" method="get" path="/api/secured/stats/defense/nearest/season" -->
```python
from griddy.nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.defensive_statistics.get_defensive_stats_by_season(season=2025, season_type=models.SeasonTypeEnum.REG, limit=35, offset=0, page=1, sort_key=models.SortKey.COV, sort_value=models.SortOrderEnum.DESC, qualified_defender=False, team_defense=[
        "3800",
        "1800",
    ])

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `season_type`                                                       | [models.SeasonTypeEnum](../../models/seasontypeenum.md)             | :heavy_check_mark:                                                  | Type of season                                                      | REG                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum number of players to return                                 | 35                                                                  |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of records to skip for pagination                            | 0                                                                   |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number for pagination                                          | 1                                                                   |
| `sort_key`                                                          | [Optional[models.SortKey]](../../models/sortkey.md)                 | :heavy_minus_sign:                                                  | Field to sort by                                                    | cov                                                                 |
| `sort_value`                                                        | [Optional[models.SortOrderEnum]](../../models/sortorderenum.md)     | :heavy_minus_sign:                                                  | Sort direction                                                      | DESC                                                                |
| `qualified_defender`                                                | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Filter to only qualified defenders (minimum snap threshold)         | false                                                               |
| `team_defense`                                                      | List[*str*]                                                         | :heavy_minus_sign:                                                  | Filter by specific team IDs (supports multiple teams)               | [<br/>"3800",<br/>"1800"<br/>]                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.DefensiveStatsResponse](../../models/defensivestatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |