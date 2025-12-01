---
tags:
  - ngs
  - top_plays
---
Belongs to [[Top Plays]]
## /api/leaders/distance/ballCarrier

### Query Params
| Name       | Value |
| ---------- | ----- |
| limit      | 20    |
| season     | 2025  |
| seasonType | REG   |
| week       | 2     |
### Response
```json
{
    "season": 2025,
    "seasonType": "REG",
    "leaders": [
        {
            "leader": {
                "nflId": 58308,
                "esbId": "DIK189231",
                "firstName": "Chimere",
                "gsisId": "00-0040705",
                "jerseyNumber": 17,
                "lastName": "Dike",
                "playerName": "Chimere Dike",
                "position": "WR",
                "positionGroup": "WR",
                "shortName": "C.Dike",
                "teamAbbr": "TEN",
                "teamId": "2100",
                "week": 12,
                "yards": 90,
                "inPlayDist": 142.3300000000001,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/njdduv9jx7c8vlrll8ex"
            },
            "play": {
                "gameId": 2025112306,
                "playId": 2535,
                "sequence": 2535,
                "down": 4,
                "gameClock": "10:44",
                "gameKey": 60014,
                "health": null,
                "homeScore": 9,
                "isBigPlay": true,
                "isEndQuarter": false,
                "isGoalToGo": false,
                "isPenalty": false,
                "isSTPlay": true,
                "isScoring": true,
                "playDescription": "(10:44) M.Dickson punts 60 yards to TEN 10, Center-C.Stoll. C.Dike for 90 yards, TOUCHDOWN.",
                "playState": "APPROVED",
                "playStats": [
                    {
                        "gsisId": "00-0034160",
                        "playId": 2535,
                        "clubCode": "SEA",
                        "playerName": "M.Dickson",
                        "statId": 29,
                        "yards": 60
                    },
                    {
                        "gsisId": "00-0040705",
                        "playId": 2535,
                        "clubCode": "TEN",
                        "playerName": "C.Dike",
                        "statId": 34,
                        "yards": 90
                    }
                ],
                "playType": "play_type_punt",
                "playTypeCode": 2,
                "possessionTeamId": "4600",
                "preSnapHomeScore": 3,
                "preSnapVisitorScore": 23,
                "quarter": 3,
                "timeOfDayUTC": "2025-11-23T19:57:33.000Z",
                "visitorScore": 23,
                "yardline": "SEA 30",
                "yardlineNumber": 30,
                "yardlineSide": "SEA",
                "yardsToGo": 2,
                "absoluteYardlineNumber": 40,
                "actualYardlineForFirstDown": 41.43,
                "actualYardsToGo": 2.29,
                "endGameClock": "10:23",
                "isChangeOfPossession": true,
                "playDirection": "right",
                "startGameClock": "10:44"
            }
        }
    ]
}
```