# PlayByPlayResponse


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `current_drive`                                                     | [Optional[models.Drive]](../models/drive.md)                        | :heavy_minus_sign:                                                  | N/A                                                                 |
| `drives`                                                            | List[[models.Drive](../models/drive.md)]                            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `game`                                                              | [Optional[models.Game]](../models/game.md)                          | :heavy_minus_sign:                                                  | NFL game information including teams, scheduling, and venue details |
| `last_play`                                                         | [Optional[models.Play]](../models/play.md)                          | :heavy_minus_sign:                                                  | N/A                                                                 |
| `scoring_summary`                                                   | List[[models.ScoringPlay](../models/scoringplay.md)]                | :heavy_minus_sign:                                                  | N/A                                                                 |