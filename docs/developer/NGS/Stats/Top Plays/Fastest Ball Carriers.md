---
tags:
  - ngs
  - top_plays
---
Belongs to [[Top Plays]]

## /api/leaders/speed/ballCarrier
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
                "nflId": 52449,
                "esbId": "TAY431618",
                "firstName": "Jonathan",
                "gsisId": "00-0036223",
                "jerseyNumber": 28,
                "lastName": "Taylor",
                "playerName": "Jonathan Taylor",
                "position": "RB",
                "positionGroup": "RB",
                "shortName": "J.Taylor",
                "teamAbbr": "IND",
                "teamId": "2200",
                "week": 2,
                "yards": 43,
                "inPlayDist": 59.900000000000006,
                "maxSpeed": 22.377272777,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/uwmnrhwtwug0wrgkomjk"
            },
            "play": {
                "gameId": 2025091410,
                "playId": 915,
                "sequence": 915,
                "down": 3,
                "gameClock": "01:50",
                "gameKey": 59870,
                "health": null,
                "homeScore": 6,
                "isBigPlay": true,
                "isEndQuarter": false,
                "isGoalToGo": false,
                "isPenalty": false,
                "isSTPlay": false,
                "isScoring": false,
                "playDescription": "(1:50) (Shotgun) D.Jones pass short right to J.Taylor pushed ob at DEN 11 for 43 yards (P.Surtain).",
                "playState": "APPROVED",
                "playStats": [
                    {
                        "playId": 915,
                        "clubCode": "IND",
                        "statId": 4,
                        "yards": 0
                    },
                    {
                        "playId": 915,
                        "clubCode": "IND",
                        "statId": 6,
                        "yards": 0
                    },
                    {
                        "gsisId": "00-0035710",
                        "playId": 915,
                        "clubCode": "IND",
                        "playerName": "D.Jones",
                        "statId": 15,
                        "yards": 43
                    },
                    {
                        "gsisId": "00-0035710",
                        "playId": 915,
                        "clubCode": "IND",
                        "playerName": "D.Jones",
                        "statId": 111,
                        "yards": 3
                    },
                    {
                        "gsisId": "00-0036223",
                        "playId": 915,
                        "clubCode": "IND",
                        "playerName": "J.Taylor",
                        "statId": 21,
                        "yards": 43
                    },
                    {
                        "gsisId": "00-0036223",
                        "playId": 915,
                        "clubCode": "IND",
                        "playerName": "J.Taylor",
                        "statId": 115,
                        "yards": 0
                    },
                    {
                        "gsisId": "00-0036223",
                        "playId": 915,
                        "clubCode": "IND",
                        "playerName": "J.Taylor",
                        "statId": 113,
                        "yards": 40
                    },
                    {
                        "gsisId": "00-0036874",
                        "playId": 915,
                        "clubCode": "DEN",
                        "playerName": "P.Surtain",
                        "statId": 79,
                        "yards": 0
                    }
                ],
                "playType": "play_type_pass",
                "playTypeCode": 2,
                "possessionTeamId": "2200",
                "preSnapHomeScore": 6,
                "preSnapVisitorScore": 7,
                "quarter": 1,
                "timeOfDayUTC": "2025-09-14T20:41:49.000Z",
                "visitorScore": 7,
                "yardline": "IND 46",
                "yardlineNumber": 46,
                "yardlineSide": "IND",
                "yardsToGo": 2,
                "absoluteYardlineNumber": 64,
                "actualYardlineForFirstDown": 62.46,
                "actualYardsToGo": 2.06,
                "endGameClock": "1:44",
                "isChangeOfPossession": false,
                "playDirection": "left",
                "startGameClock": "1:51"
            }
        }
    ]
}
```