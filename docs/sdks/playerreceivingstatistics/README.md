# PlayerReceivingStatistics
(*player_receiving_statistics*)

## Overview

Individual player receiving statistics and analytics

### Available Operations

* [get_player_receiving_stats_by_season](#get_player_receiving_stats_by_season) - Get Player Receiving Statistics by Season
* [get_player_receiving_stats_by_week](#get_player_receiving_stats_by_week) - Get Player Receiving Statistics by Week

## get_player_receiving_stats_by_season

Retrieves comprehensive receiving statistics for NFL players during a specified season.
Returns detailed metrics including traditional stats, advanced analytics, and Next Gen Stats
data. Supports filtering by teams, qualified receivers, and various sorting options.
Data includes catch percentage, yards per reception, EPA (Expected Points Added), CROE
(Catch Rate Over Expected), target share, route depth, separation metrics, and YAC analytics.


### Example Usage

<!-- UsageSnippet language="python" operationID="getPlayerReceivingStatsBySeason" method="get" path="/api/secured/stats/players-offense/receiving/season" -->
```python
from griddy.nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.player_receiving_statistics.get_player_receiving_stats_by_season(request={
        "season": 2025,
        "season_type": models.SeasonTypeEnum.REG,
        "limit": 3,
        "sort_value": models.SortOrderEnum.DESC,
        "team_offense": [
            "3000",
            "3900",
        ],
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `request`                                                                                               | [models.GetPlayerReceivingStatsBySeasonRequest](../../models/getplayerreceivingstatsbyseasonrequest.md) | :heavy_check_mark:                                                                                      | The request object to use for the request.                                                              |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |
| `server_url`                                                                                            | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | An optional server URL to use.                                                                          |

### Response

**[models.ReceivingStatsResponse](../../models/receivingstatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_player_receiving_stats_by_week

Retrieves comprehensive receiving statistics for NFL players during a specified week and season.
Returns detailed metrics including traditional stats, advanced analytics, and Next Gen Stats
data. Supports filtering by teams, qualified receivers, and various sorting options.
Data includes catch percentage, yards per reception, EPA (Expected Points Added), CROE
(Catch Rate Over Expected), target share, route depth, separation metrics, and YAC analytics.


### Example Usage

<!-- UsageSnippet language="python" operationID="getPlayerReceivingStatsByWeek" method="get" path="/api/secured/stats/players-offense/receiving/week" -->
```python
from griddy.nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.player_receiving_statistics.get_player_receiving_stats_by_week(request={
        "season": 2025,
        "season_type": models.SeasonTypeEnum.REG,
        "week": models.WeekSlugEnum.WEEK_10,
        "sort_value": models.SortOrderEnum.DESC,
        "team_offense": [
            "3900",
            "3200",
        ],
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `request`                                                                                           | [models.GetPlayerReceivingStatsByWeekRequest](../../models/getplayerreceivingstatsbyweekrequest.md) | :heavy_check_mark:                                                                                  | The request object to use for the request.                                                          |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |
| `server_url`                                                                                        | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | An optional server URL to use.                                                                      |

### Response

**[models.ReceivingStatsResponse](../../models/receivingstatsresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |