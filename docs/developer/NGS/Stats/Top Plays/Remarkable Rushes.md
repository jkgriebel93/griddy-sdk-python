---
tags:
  - ngs
  - top_plays
---
Belongs to [[Top Plays]]
## /api/leaders/expectation/ery/season
### Response
```json
{
    "season": 2025,
    "seasonType": "REG",
    "eryLeaders": [
        {
            "leader": {
                "esbId": "TAY431618",
                "firstName": "Jonathan",
                "gsisId": "00-0036223",
                "jerseyNumber": 28,
                "lastName": "Taylor",
                "playerName": "Jonathan Taylor",
                "position": "RB",
                "positionGroup": "RB",
                "rushYards": 83,
                "shortName": "J.Taylor",
                "teamAbbr": "IND",
                "teamId": "2200",
                "week": 10,
                "isTouchdown": true,
                "expectedRushYards": 4.755936784813739,
                "rushYardsOverExpected": 78.24406321518626,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/uwmnrhwtwug0wrgkomjk"
            },
            "play": {
                "gameId": 2025110900,
                "playId": 3414,
                "sequence": 3414,
                "down": 2,
                "gameClock": "06:16",
                "gameKey": 59979,
                "health": null,
                "homeScore": 22,
                "isBigPlay": true,
                "isEndQuarter": false,
                "isGoalToGo": false,
                "isPenalty": false,
                "isSTPlay": false,
                "isScoring": true,
                "playDescription": "(6:16) J.Taylor up the middle for 83 yards, TOUCHDOWN.",
                "playState": "APPROVED",
                "playStats": [
                    {
                        "playId": 3414,
                        "clubCode": "IND",
                        "statId": 3,
                        "yards": 0
                    },
                    {
                        "gsisId": "00-0036223",
                        "playId": 3414,
                        "clubCode": "IND",
                        "playerName": "J.Taylor",
                        "statId": 11,
                        "yards": 83
                    }
                ],
                "playType": "play_type_rush",
                "playTypeCode": 2,
                "possessionTeamId": "2200",
                "preSnapHomeScore": 16,
                "preSnapVisitorScore": 17,
                "quarter": 4,
                "timeOfDayUTC": "2025-11-09T17:06:37.000Z",
                "visitorScore": 17,
                "week": 10,
                "yardline": "IND 17",
                "yardlineNumber": 17,
                "yardlineSide": "IND",
                "yardsToGo": 2,
                "absoluteYardlineNumber": 93,
                "actualYardlineForFirstDown": 91.22,
                "actualYardsToGo": 2.35,
                "endGameClock": "6:02",
                "isChangeOfPossession": false,
                "playDirection": "left",
                "startGameClock": "6:17"
            }
        }
    ]
}
```