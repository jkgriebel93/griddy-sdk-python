# LinkParams

Parameters for constructing film room link


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `dropback`                                                 | *Optional[int]*                                            | :heavy_minus_sign:                                         | Dropback indicator (1 for yes)                             |
| `nfl_id`                                                   | *Optional[str]*                                            | :heavy_minus_sign:                                         | NFL player identifier                                      |
| `passer_id`                                                | *Optional[str]*                                            | :heavy_minus_sign:                                         | Passer ID for QB film                                      |
| `rusher_id`                                                | *Optional[str]*                                            | :heavy_minus_sign:                                         | Rusher ID for RB film                                      |
| `season`                                                   | *Optional[str]*                                            | :heavy_minus_sign:                                         | Season year                                                |
| `target_id`                                                | *Optional[str]*                                            | :heavy_minus_sign:                                         | Target ID for receiver film                                |
| `week_slug`                                                | [Optional[models.WeekSlugEnum]](../models/weekslugenum.md) | :heavy_minus_sign:                                         | Week identifier slug                                       |