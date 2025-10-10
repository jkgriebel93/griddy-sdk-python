# BoxScoreResponse


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `game`                                                              | [Optional[models.Game]](../models/game.md)                          | :heavy_minus_sign:                                                  | NFL game information including teams, scheduling, and venue details |
| `player_stats`                                                      | [Optional[models.PlayerStats]](../models/playerstats.md)            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `scoring_summary`                                                   | List[[models.ScoringPlay](../models/scoringplay.md)]                | :heavy_minus_sign:                                                  | N/A                                                                 |
| `team_stats`                                                        | [Optional[models.TeamStats]](../models/teamstats.md)                | :heavy_minus_sign:                                                  | N/A                                                                 |