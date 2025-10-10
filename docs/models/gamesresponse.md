# GamesResponse


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `games`                                                        | List[[models.Game](../models/game.md)]                         | :heavy_minus_sign:                                             | N/A                                                            |                                                                |
| `season`                                                       | *Optional[str]*                                                | :heavy_minus_sign:                                             | Season year                                                    | 2025                                                           |
| `season_type`                                                  | [Optional[models.SeasonTypeEnum]](../models/seasontypeenum.md) | :heavy_minus_sign:                                             | Type of NFL season                                             | REG                                                            |
| `week`                                                         | *Optional[str]*                                                | :heavy_minus_sign:                                             | Week number                                                    | 3                                                              |