# Plays
(*plays*)

## Overview

Play-by-play data and film room analysis

### Available Operations

* [get_summary_play](#get_summary_play) - Get Play Summary

## get_summary_play

Retrieves detailed information about a specific play in a game including play description,
statistics, involved players, win probability, and expected points.


### Example Usage

<!-- UsageSnippet language="python" operationID="getSummaryPlay" method="get" path="/api/plays/summaryPlay" -->
```python
from griddy_nfl import GriddyNFL


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.plays.get_summary_play(game_id="f665fc10-311e-11f0-b670-ae1250fadad1", play_id=40)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `game_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Game identifier (UUID format)                                       | f665fc10-311e-11f0-b670-ae1250fadad1                                |
| `play_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | Play identifier within the game                                     | 40                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PlaySummaryResponse](../../models/playsummaryresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |