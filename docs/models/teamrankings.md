# TeamRankings


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `season`                                                       | *Optional[int]*                                                | :heavy_minus_sign:                                             | N/A                                                            | 2025                                                           |
| `season_type`                                                  | [Optional[models.SeasonTypeEnum]](../models/seasontypeenum.md) | :heavy_minus_sign:                                             | Type of NFL season                                             | REG                                                            |
| `statistics`                                                   | List[[models.StatisticRanking](../models/statisticranking.md)] | :heavy_minus_sign:                                             | N/A                                                            |                                                                |
| `team_id`                                                      | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            | 10403000-5851-f9d5-da45-78365a05b6b0                           |