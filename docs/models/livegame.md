# LiveGame

Live game scoring and status information


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `away_team`                                                    | [Optional[models.AwayTeam]](../models/awayteam.md)             | :heavy_minus_sign:                                             | N/A                                                            |
| `game_id`                                                      | *Optional[str]*                                                | :heavy_minus_sign:                                             | Game identifier                                                |
| `home_team`                                                    | [Optional[models.HomeTeam]](../models/hometeam.md)             | :heavy_minus_sign:                                             | N/A                                                            |
| `last_play`                                                    | *Optional[str]*                                                | :heavy_minus_sign:                                             | Description of last play                                       |
| `possession`                                                   | *Optional[str]*                                                | :heavy_minus_sign:                                             | Team abbreviation with current possession                      |
| `quarter`                                                      | *Optional[str]*                                                | :heavy_minus_sign:                                             | Current quarter/period                                         |
| `red_zone`                                                     | *Optional[bool]*                                               | :heavy_minus_sign:                                             | Whether team is in red zone                                    |
| `status`                                                       | [Optional[models.GameStatusEnum]](../models/gamestatusenum.md) | :heavy_minus_sign:                                             | Game status                                                    |
| `time_remaining`                                               | *Optional[str]*                                                | :heavy_minus_sign:                                             | Time remaining in current period                               |