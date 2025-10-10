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
from griddy.nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.filmroom.get_filmroom_plays(game_id=[
        "f665fc10-311e-11f0-b670-ae1250fadad1",
    ], season=[
        2025,
    ], season_type=[
        models.SeasonTypeEnum.REG,
    ], nfl_id=[
        "54517",
    ], quarter=[
        1,
    ], down=[
        1,
    ], yards_to_go_type=[
        models.YardsToGoType.SHORT,
    ], touchdown=[
        models.BinaryFlagEnum.ONE,
    ], rush10_plus_yards=[
        models.BinaryFlagEnum.ONE,
    ], fumble_lost=[
        models.BinaryFlagEnum.ONE,
    ], fumble=[
        models.BinaryFlagEnum.ONE,
    ], qb_alignment=[
        models.QbAlignment.SHOTGUN,
    ], redzone=[
        models.BinaryFlagEnum.ONE,
    ], goal_to_go=[
        models.BinaryFlagEnum.ONE,
    ], pass_play=[
        models.BinaryFlagEnum.ONE,
    ], run_play=[
        models.BinaryFlagEnum.ONE,
    ], play_type=[
        models.PlayTypeEnum.PLAY_TYPE_RUSH,
    ], attempt=[
        models.BinaryFlagEnum.ONE,
    ], completion=[
        models.BinaryFlagEnum.ONE,
    ], interception=[
        models.BinaryFlagEnum.ONE,
    ], reception=[
        models.BinaryFlagEnum.ONE,
    ], sack=[
        models.BinaryFlagEnum.ONE,
    ], rec_motion=[
        models.BinaryFlagEnum.ONE,
    ], target_location=[
        models.TargetLocation.BETWEEN_HASHES,
    ], air_yard_type=[
        models.AirYardType.SHORT,
    ], dropback_time_type=[
        models.DropbackTimeType.QUICK,
    ], pressure=[
        models.BinaryFlagEnum.ONE,
    ], blitz=[
        models.BinaryFlagEnum.ONE,
    ], play_action=[
        models.BinaryFlagEnum.ONE,
    ], rush_direction=[
        models.RushDirection.INSIDE,
    ], run_stuff=[
        models.BinaryFlagEnum.ONE,
    ], receiver_alignment=[
        models.ReceiverAlignment.SLOT,
    ], separation_type=[
        models.SeparationType.OPEN,
    ], personnel=[
        models.Personnel.NICKEL,
    ], defenders_in_the_box_type=[
        models.DefendersInTheBoxType.STACKED,
    ], def_coverage_type=[
        models.DefCoverageType.PRESS,
    ])

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `game_id`                                                                   | List[*str*]                                                                 | :heavy_minus_sign:                                                          | Filter by specific game IDs (supports multiple values)                      | [<br/>"f665fc10-311e-11f0-b670-ae1250fadad1"<br/>]                          |
| `week_slug`                                                                 | List[[models.WeekSlugEnum](../../models/weekslugenum.md)]                   | :heavy_minus_sign:                                                          | Filter by week identifier (supports multiple values)                        |                                                                             |
| `season`                                                                    | List[*int*]                                                                 | :heavy_minus_sign:                                                          | Filter by season year (supports multiple values)                            | [<br/>2025<br/>]                                                            |
| `season_type`                                                               | List[[models.SeasonTypeEnum](../../models/seasontypeenum.md)]               | :heavy_minus_sign:                                                          | Filter by season type                                                       | [<br/>"REG"<br/>]                                                           |
| `nfl_id`                                                                    | List[*str*]                                                                 | :heavy_minus_sign:                                                          | Filter by player NFL ID                                                     | [<br/>"54517"<br/>]                                                         |
| `quarter`                                                                   | List[*int*]                                                                 | :heavy_minus_sign:                                                          | Filter by quarter                                                           | [<br/>1<br/>]                                                               |
| `down`                                                                      | List[*int*]                                                                 | :heavy_minus_sign:                                                          | Filter by down                                                              | [<br/>1<br/>]                                                               |
| `yards_to_go_type`                                                          | List[[models.YardsToGoType](../../models/yardstogotype.md)]                 | :heavy_minus_sign:                                                          | Filter by yards to go category                                              | [<br/>"SHORT"<br/>]                                                         |
| `touchdown`                                                                 | List[[models.BinaryFlagEnum](../../models/binaryflagenum.md)]               | :heavy_minus_sign:                                                          | Filter for touchdown plays (1 = yes, 0 = no)                                | [<br/>1<br/>]                                                               |
| `rush10_plus_yards`                                                         | List[[models.BinaryFlagEnum](../../models/binaryflagenum.md)]               | :heavy_minus_sign:                                                          | Filter for rushing plays of 10+ yards                                       | [<br/>1<br/>]                                                               |
| `fumble_lost`                                                               | List[[models.BinaryFlagEnum](../../models/binaryflagenum.md)]               | :heavy_minus_sign:                                                          | Filter for plays with fumbles lost                                          | [<br/>1<br/>]                                                               |
| `fumble`                                                                    | List[[models.BinaryFlagEnum](../../models/binaryflagenum.md)]               | :heavy_minus_sign:                                                          | Filter for plays with fumbles                                               | [<br/>1<br/>]                                                               |
| `qb_alignment`                                                              | List[[models.QbAlignment](../../models/qbalignment.md)]                     | :heavy_minus_sign:                                                          | Filter by quarterback alignment                                             | [<br/>"SHOTGUN"<br/>]                                                       |
| `redzone`                                                                   | List[[models.BinaryFlagEnum](../../models/binaryflagenum.md)]               | :heavy_minus_sign:                                                          | Filter for red zone plays                                                   | [<br/>1<br/>]                                                               |
| `goal_to_go`                                                                | List[[models.BinaryFlagEnum](../../models/binaryflagenum.md)]               | :heavy_minus_sign:                                                          | Filter for goal-to-go situations                                            | [<br/>1<br/>]                                                               |
| `pass_play`                                                                 | List[[models.BinaryFlagEnum](../../models/binaryflagenum.md)]               | :heavy_minus_sign:                                                          | Filter for passing plays                                                    | [<br/>1<br/>]                                                               |
| `run_play`                                                                  | List[[models.BinaryFlagEnum](../../models/binaryflagenum.md)]               | :heavy_minus_sign:                                                          | Filter for running plays                                                    | [<br/>1<br/>]                                                               |
| `play_type`                                                                 | List[[models.PlayTypeEnum](../../models/playtypeenum.md)]                   | :heavy_minus_sign:                                                          | Filter by specific play types                                               | [<br/>"play_type_rush"<br/>]                                                |
| `attempt`                                                                   | List[[models.BinaryFlagEnum](../../models/binaryflagenum.md)]               | :heavy_minus_sign:                                                          | Filter for passing attempts                                                 | [<br/>1<br/>]                                                               |
| `completion`                                                                | List[[models.BinaryFlagEnum](../../models/binaryflagenum.md)]               | :heavy_minus_sign:                                                          | Filter for completed passes                                                 | [<br/>1<br/>]                                                               |
| `interception`                                                              | List[[models.BinaryFlagEnum](../../models/binaryflagenum.md)]               | :heavy_minus_sign:                                                          | Filter for interceptions                                                    | [<br/>1<br/>]                                                               |
| `reception`                                                                 | List[[models.BinaryFlagEnum](../../models/binaryflagenum.md)]               | :heavy_minus_sign:                                                          | Filter for receptions                                                       | [<br/>1<br/>]                                                               |
| `sack`                                                                      | List[[models.BinaryFlagEnum](../../models/binaryflagenum.md)]               | :heavy_minus_sign:                                                          | Filter for sacks                                                            | [<br/>1<br/>]                                                               |
| `rec_motion`                                                                | List[[models.BinaryFlagEnum](../../models/binaryflagenum.md)]               | :heavy_minus_sign:                                                          | Filter by receiver motion                                                   | [<br/>1<br/>]                                                               |
| `target_location`                                                           | List[[models.TargetLocation](../../models/targetlocation.md)]               | :heavy_minus_sign:                                                          | Filter by target location on field                                          | [<br/>"BETWEEN_HASHES"<br/>]                                                |
| `air_yard_type`                                                             | List[[models.AirYardType](../../models/airyardtype.md)]                     | :heavy_minus_sign:                                                          | Filter by air yards category                                                | [<br/>"SHORT"<br/>]                                                         |
| `dropback_time_type`                                                        | List[[models.DropbackTimeType](../../models/dropbacktimetype.md)]           | :heavy_minus_sign:                                                          | Filter by dropback time                                                     | [<br/>"QUICK"<br/>]                                                         |
| `pressure`                                                                  | List[[models.BinaryFlagEnum](../../models/binaryflagenum.md)]               | :heavy_minus_sign:                                                          | Filter by quarterback pressure                                              | [<br/>1<br/>]                                                               |
| `blitz`                                                                     | List[[models.BinaryFlagEnum](../../models/binaryflagenum.md)]               | :heavy_minus_sign:                                                          | Filter by defensive blitz                                                   | [<br/>1<br/>]                                                               |
| `play_action`                                                               | List[[models.BinaryFlagEnum](../../models/binaryflagenum.md)]               | :heavy_minus_sign:                                                          | Filter by play action usage                                                 | [<br/>1<br/>]                                                               |
| `rush_direction`                                                            | List[[models.RushDirection](../../models/rushdirection.md)]                 | :heavy_minus_sign:                                                          | Filter by rush direction                                                    | [<br/>"INSIDE"<br/>]                                                        |
| `run_stuff`                                                                 | List[[models.BinaryFlagEnum](../../models/binaryflagenum.md)]               | :heavy_minus_sign:                                                          | Filter for stuffed runs                                                     | [<br/>1<br/>]                                                               |
| `receiver_alignment`                                                        | List[[models.ReceiverAlignment](../../models/receiveralignment.md)]         | :heavy_minus_sign:                                                          | Filter by receiver alignment                                                | [<br/>"SLOT"<br/>]                                                          |
| `separation_type`                                                           | List[[models.SeparationType](../../models/separationtype.md)]               | :heavy_minus_sign:                                                          | Filter by receiver separation                                               | [<br/>"OPEN"<br/>]                                                          |
| `personnel`                                                                 | List[[models.Personnel](../../models/personnel.md)]                         | :heavy_minus_sign:                                                          | Filter by defensive personnel package                                       | [<br/>"NICKEL"<br/>]                                                        |
| `defenders_in_the_box_type`                                                 | List[[models.DefendersInTheBoxType](../../models/defendersintheboxtype.md)] | :heavy_minus_sign:                                                          | Filter by defenders in the box                                              | [<br/>"STACKED"<br/>]                                                       |
| `def_coverage_type`                                                         | List[[models.DefCoverageType](../../models/defcoveragetype.md)]             | :heavy_minus_sign:                                                          | Filter by defensive coverage type                                           | [<br/>"PRESS"<br/>]                                                         |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |
| `server_url`                                                                | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | An optional server URL to use.                                              | http://localhost:8080                                                       |

### Response

**[models.FilmroomPlaysResponse](../../models/filmroomplaysresponse.md)**

### Errors

| Error Type            | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.GriddyNFLError | 4XX, 5XX              | \*/\*                 |