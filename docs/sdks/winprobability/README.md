# WinProbability
(*win_probability*)

## Overview

Game and play-level win probability analytics

### Available Operations

* [get_plays_win_probability](#get_plays_win_probability) - Get Game Win Probability by Plays
* [get_win_probability_min](#get_win_probability_min) - Get Minimal Win Probability Data

## get_plays_win_probability

Retrieves comprehensive win probability data for every play in specified games.
Returns pre-game win probabilities and detailed play-by-play probability changes,
including Win Probability Added (WPA) metrics for each play. This advanced analytics
endpoint tracks how each play impacts the probability of each team winning the game.
Supports querying multiple games simultaneously.


### Example Usage

<!-- UsageSnippet language="python" operationID="getPlaysWinProbability" method="get" path="/api/secured/plays/winProbability" -->
```python
from griddy_nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.win_probability.get_plays_win_probability(game_id=[
        "2025092800",
        "2025092104",
    ])

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `game_id`                                                                                                              | [models.GameID](../../models/gameid.md)                                                                                | :heavy_check_mark:                                                                                                     | Game identifier(s) in 10-digit format (YYYYMMDDNN). Can be a single game ID or multiple game IDs for batch retrieval.  |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |

### Response

**[models.GetPlaysWinProbabilityResponseBody](../../models/getplayswinprobabilityresponsebody.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |

## get_win_probability_min

Retrieves minimal win probability data for specified games, including pregame
win probabilities and play-by-play probability changes throughout the game.
This endpoint provides essential win probability metrics with optimized data
structure for performance. Supports multiple games in a single request.


### Example Usage

<!-- UsageSnippet language="python" operationID="getWinProbabilityMin" method="get" path="/api/secured/plays/winProbabilityMin" -->
```python
from griddy_nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.win_probability.get_win_probability_min(fapi_game_id=[
        "f666051f-311e-11f0-b670-ae1250fadad1",
        "f6660056-311e-11f0-b670-ae1250fadad1",
        "f665fc10-311e-11f0-b670-ae1250fadad1",
    ])

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  | Example                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `fapi_game_id`                                                                                                                               | List[*str*]                                                                                                                                  | :heavy_check_mark:                                                                                                                           | Football API game identifiers (UUID format). Supports multiple game IDs<br/>to retrieve win probability data for multiple games simultaneously.<br/> | [<br/>"f666051f-311e-11f0-b670-ae1250fadad1",<br/>"f6660056-311e-11f0-b670-ae1250fadad1",<br/>"f665fc10-311e-11f0-b670-ae1250fadad1"<br/>]   |
| `retries`                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                             | :heavy_minus_sign:                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                          |                                                                                                                                              |

### Response

**[models.WinProbabilityResponse](../../models/winprobabilityresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |