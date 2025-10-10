# TeamDefenseRushStatistics
(*team_defense_rush_statistics*)

## Overview

Comprehensive team defensive rush statistics and situational analytics

### Available Operations

* [get_team_defense_rush_stats_by_season](#get_team_defense_rush_stats_by_season) - Get Team Defense Rush Statistics by Season

## get_team_defense_rush_stats_by_season

Retrieves comprehensive rush defense statistics for NFL teams during a specified season.
Returns detailed metrics including traditional run defense stats, advanced analytics like EPA
and RYOE (Rush Yards Over Expected), Next Gen Stats data, and situational performance
breakdowns. Supports various sorting options and includes stuff rates, gap analysis,
box count distributions, and directional rush defense metrics.


### Example Usage

<!-- UsageSnippet language="python" operationID="getTeamDefenseRushStatsBySeason" method="get" path="/api/secured/stats/team-defense/rush/season" -->
```python
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.team_defense_rush_statistics.get_team_defense_rush_stats_by_season(request={
        "season": 2025,
        "season_type": models.SeasonTypeEnum.REG,
        "sort_value": models.SortOrderEnum.DESC,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `request`                                                                                               | [models.GetTeamDefenseRushStatsBySeasonRequest](../../models/getteamdefenserushstatsbyseasonrequest.md) | :heavy_check_mark:                                                                                      | The request object to use for the request.                                                              |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.TeamDefenseRushStatsResponse](../../models/teamdefenserushstatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |