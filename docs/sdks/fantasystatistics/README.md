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
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.fantasy_statistics.get_fantasy_stats_by_season(request={
        "season": 2025,
        "season_type": models.SeasonTypeEnum.REG,
        "sort_value": models.SortOrderEnum.DESC,
        "position_group": [
            models.PositionGroup.QB,
        ],
        "team_offense": "3900",
        "team_defense": "4600",
        "min_offensive_snaps": 75,
        "last_n_weeks": 3,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.GetFantasyStatsBySeasonRequest](../../models/getfantasystatsbyseasonrequest.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.FantasyStatsResponse](../../models/fantasystatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |