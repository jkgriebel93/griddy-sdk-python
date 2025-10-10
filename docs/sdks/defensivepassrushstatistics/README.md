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
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.defensive_pass_rush_statistics.get_defensive_pass_rush_stats_by_season(request={
        "season": 2025,
        "season_type": models.SeasonTypeEnum.REG,
        "sort_value": models.SortOrderEnum.DESC,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                   | [models.GetDefensivePassRushStatsBySeasonRequest](../../models/getdefensivepassrushstatsbyseasonrequest.md) | :heavy_check_mark:                                                                                          | The request object to use for the request.                                                                  |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.PassRushStatsResponse](../../models/passrushstatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |