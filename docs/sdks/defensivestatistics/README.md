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
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.defensive_statistics.get_defensive_stats_by_season(request={
        "season": 2025,
        "season_type": models.SeasonTypeEnum.REG,
        "sort_value": models.SortOrderEnum.DESC,
        "team_defense": [
            "3800",
            "1800",
        ],
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.GetDefensiveStatsBySeasonRequest](../../models/getdefensivestatsbyseasonrequest.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.DefensiveStatsResponse](../../models/defensivestatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |