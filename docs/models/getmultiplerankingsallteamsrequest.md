# GetMultipleRankingsAllTeamsRequest


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `season`                                             | *int*                                                | :heavy_check_mark:                                   | Season year                                          | 2025                                                 |
| `season_type`                                        | [models.SeasonTypeEnum](../models/seasontypeenum.md) | :heavy_check_mark:                                   | Type of season                                       | REG                                                  |
| `stat0`                                              | *str*                                                | :heavy_check_mark:                                   | First statistical category                           | scoring-averagePointsScored                          |
| `stat1`                                              | *Optional[str]*                                      | :heavy_minus_sign:                                   | Second statistical category                          | offense-yardsPerGame                                 |
| `stat2`                                              | *Optional[str]*                                      | :heavy_minus_sign:                                   | Third statistical category                           | offense-rushYardsPerGame                             |
| `stat3`                                              | *Optional[str]*                                      | :heavy_minus_sign:                                   | Fourth statistical category                          | offense-passYardsPerGame                             |
| `stat4`                                              | *Optional[str]*                                      | :heavy_minus_sign:                                   | Fifth statistical category                           | misc-netTurnovers                                    |