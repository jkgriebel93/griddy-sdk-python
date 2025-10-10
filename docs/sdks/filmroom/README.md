# Filmroom
(*filmroom*)

## Overview

Advanced play analysis and film study data

### Available Operations

* [get_filmroom_plays](#get_filmroom_plays) - Get Filmroom Plays with Advanced Filtering

## get_filmroom_plays

Retrieves detailed play-by-play data with extensive filtering capabilities for film study.
Returns comprehensive play information including formations, personnel packages, game situations,
and detailed play descriptions. This endpoint supports advanced filtering by game situation,
player involvement, formation types, and tactical elements.


### Example Usage

<!-- UsageSnippet language="python" operationID="getFilmroomPlays" method="get" path="/api/secured/videos/filmroom/plays" -->
```python
from griddy_nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as gn_client:

    res = gn_client.filmroom.get_filmroom_plays(request={
        "game_id": [
            "f665fc10-311e-11f0-b670-ae1250fadad1",
        ],
        "season": [
            2025,
        ],
        "season_type": [
            models.SeasonTypeEnum.REG,
        ],
        "nfl_id": [
            "54517",
        ],
        "quarter": [
            1,
        ],
        "down": [
            1,
        ],
        "yards_to_go_type": [
            models.YardsToGoType.SHORT,
        ],
        "touchdown": [
            models.BinaryFlagEnum.ONE,
        ],
        "rush10_plus_yards": [
            models.BinaryFlagEnum.ONE,
        ],
        "fumble_lost": [
            models.BinaryFlagEnum.ONE,
        ],
        "fumble": [
            models.BinaryFlagEnum.ONE,
        ],
        "qb_alignment": [
            models.QbAlignment.SHOTGUN,
        ],
        "redzone": [
            models.BinaryFlagEnum.ONE,
        ],
        "goal_to_go": [
            models.BinaryFlagEnum.ONE,
        ],
        "pass_play": [
            models.BinaryFlagEnum.ONE,
        ],
        "run_play": [
            models.BinaryFlagEnum.ONE,
        ],
        "play_type": [
            models.PlayTypeEnum.PLAY_TYPE_RUSH,
        ],
        "attempt": [
            models.BinaryFlagEnum.ONE,
        ],
        "completion": [
            models.BinaryFlagEnum.ONE,
        ],
        "interception": [
            models.BinaryFlagEnum.ONE,
        ],
        "reception": [
            models.BinaryFlagEnum.ONE,
        ],
        "sack": [
            models.BinaryFlagEnum.ONE,
        ],
        "rec_motion": [
            models.BinaryFlagEnum.ONE,
        ],
        "target_location": [
            models.TargetLocation.BETWEEN_HASHES,
        ],
        "air_yard_type": [
            models.AirYardType.SHORT,
        ],
        "dropback_time_type": [
            models.DropbackTimeType.QUICK,
        ],
        "pressure": [
            models.BinaryFlagEnum.ONE,
        ],
        "blitz": [
            models.BinaryFlagEnum.ONE,
        ],
        "play_action": [
            models.BinaryFlagEnum.ONE,
        ],
        "rush_direction": [
            models.RushDirection.INSIDE,
        ],
        "run_stuff": [
            models.BinaryFlagEnum.ONE,
        ],
        "receiver_alignment": [
            models.ReceiverAlignment.SLOT,
        ],
        "separation_type": [
            models.SeparationType.OPEN,
        ],
        "personnel": [
            models.Personnel.NICKEL,
        ],
        "defenders_in_the_box_type": [
            models.DefendersInTheBoxType.STACKED,
        ],
        "def_coverage_type": [
            models.DefCoverageType.PRESS,
        ],
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.GetFilmroomPlaysRequest](../../models/getfilmroomplaysrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.FilmroomPlaysResponse](../../models/filmroomplaysresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |