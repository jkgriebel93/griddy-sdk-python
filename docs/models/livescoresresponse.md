# LiveScoresResponse


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `games`                                                        | List[[models.LiveGame](../models/livegame.md)]                 | :heavy_minus_sign:                                             | Array of live game data (empty when no games are active)       |                                                                |
| `season`                                                       | *Optional[str]*                                                | :heavy_minus_sign:                                             | Season year                                                    | 2025                                                           |
| `season_type`                                                  | [Optional[models.SeasonTypeEnum]](../models/seasontypeenum.md) | :heavy_minus_sign:                                             | Type of NFL season                                             | REG                                                            |
| `week`                                                         | *Optional[str]*                                                | :heavy_minus_sign:                                             | Week number                                                    | 4                                                              |