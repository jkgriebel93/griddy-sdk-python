# SecuredVideos
(*secured_videos*)

## Overview

Premium coaches film video content with multiple camera angles

### Available Operations

* [get_coaches_film_videos](#get_coaches_film_videos) - Get Coaches Film Videos

## get_coaches_film_videos

Retrieves premium coaches film video content for specified games and plays.
Returns multiple camera angles (endzone, sideline, broadcast) for each play,
providing comprehensive film study material. Requires NFL Plus Premium subscription
and appropriate geographic restrictions apply (US only).


### Example Usage

<!-- UsageSnippet language="python" operationID="getCoachesFilmVideos" method="get" path="/api/secured/videos/coaches" -->
```python
from openapi import SDK


with SDK(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as sdk:

    res = sdk.secured_videos.get_coaches_film_videos(game_id=[
        "f665fc10-311e-11f0-b670-ae1250fadad1",
        "ae9d66f7-1312-11ef-afd1-646009f18b2e",
    ], play_id=[
        "267",
        "1162",
        "496",
        "139",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        | Example                                                                            |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `game_id`                                                                          | List[*str*]                                                                        | :heavy_check_mark:                                                                 | Game identifiers (UUID format, supports multiple games)                            | [<br/>"f665fc10-311e-11f0-b670-ae1250fadad1",<br/>"ae9d66f7-1312-11ef-afd1-646009f18b2e"<br/>] |
| `play_id`                                                                          | List[*str*]                                                                        | :heavy_check_mark:                                                                 | Play identifiers for specific plays within the games                               | [<br/>"267",<br/>"1162",<br/>"496",<br/>"139"<br/>]                                |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |                                                                                    |
| `server_url`                                                                       | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | An optional server URL to use.                                                     | http://localhost:8080                                                              |

### Response

**[models.CoachesFilmResponse](../../models/coachesfilmresponse.md)**

### Errors

| Error Type             | Status Code            | Content Type           |
| ---------------------- | ---------------------- | ---------------------- |
| errors.SDKDefaultError | 4XX, 5XX               | \*/\*                  |