# Scores
(*scores*)

## Overview

Real-time scoring and game status endpoints

### Available Operations

* [get_live_game_scores](#get_live_game_scores) - Get Live Game Scores

## get_live_game_scores

Retrieves real-time scores and game status for all games in a specified week.
This endpoint updates frequently (15-second cache) to provide live scoring updates
during active games. Returns an empty array when no games are currently being played.


### Example Usage

<!-- UsageSnippet language="python" operationID="getLiveGameScores" method="get" path="/api/scores/live/games" -->
```python
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.scores.get_live_game_scores(season=2025, season_type="REG", week=4)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `season`                                                            | *int*                                                               | :heavy_check_mark:                                                  | Season year                                                         | 2025                                                                |
| `season_type`                                                       | [models.SeasonTypeEnum](../../models/seasontypeenum.md)             | :heavy_check_mark:                                                  | Type of season                                                      | REG                                                                 |
| `week`                                                              | *int*                                                               | :heavy_check_mark:                                                  | Week number                                                         | 4                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      | http://localhost:8080                                               |

### Response

**[models.LiveScoresResponse](../../models/livescoresresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |