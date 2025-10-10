# GetPlayByPlayRequest


## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `game_id`                              | *str*                                  | :heavy_check_mark:                     | Game identifier (UUID)                 |
| `include_penalties`                    | *Optional[bool]*                       | :heavy_minus_sign:                     | Include penalty details                |
| `include_formations`                   | *Optional[bool]*                       | :heavy_minus_sign:                     | Include offensive/defensive formations |