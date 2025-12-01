---
tags:
  - ngs
  - highlights
---
[[Next Gen Stats]]

## /api/plays/highlights
### Query Params

| Name   | Value |
| ------ | ----- |
| limit  | 16    |
| season | 2025  |
### Response
```json
{
    "season": 2025,
    "highlights": [
        {
            "gameId": 2025113010,
            "playId": 5062,
            "play": {
                "playType": "play_type_pass",
                "gameId": 2025113010,
                "gameKey": 60035,
                "yardlineSide": "DEN",
                "absoluteYardlineNumber": 13,
                "yardlineNumber": 3,
                "timeOfDayUTC": "2025-12-01T04:59:06.000Z",
                "isPenalty": false,
                "homeScore": 26,
                "visitorScore": 27,
                "playStats": [
                    {
                        "playId": 5062,
                        "clubCode": "WAS",
                        "statId": 4,
                        "yards": 0
                    },
                    {
                        "playId": 5062,
                        "clubCode": "WAS",
                        "statId": 8,
                        "yards": 0
                    },
                    {
                        "playId": 5062,
                        "clubCode": "WAS",
                        "playerName": "M.Mariota",
                        "statId": 16,
                        "yards": 3,
                        "gsisId": "00-0032268"
                    },
                    {
                        "playId": 5062,
                        "clubCode": "WAS",
                        "playerName": "M.Mariota",
                        "statId": 111,
                        "yards": 3,
                        "gsisId": "00-0032268"
                    },
                    {
                        "playId": 5062,
                        "clubCode": "WAS",
                        "playerName": "T.McLaurin",
                        "statId": 22,
                        "yards": 3,
                        "gsisId": "00-0035659"
                    },
                    {
                        "playId": 5062,
                        "clubCode": "WAS",
                        "playerName": "T.McLaurin",
                        "statId": 115,
                        "yards": 0,
                        "gsisId": "00-0035659"
                    },
                    {
                        "playId": 5062,
                        "clubCode": "WAS",
                        "playerName": "T.McLaurin",
                        "statId": 113,
                        "yards": 0,
                        "gsisId": "00-0035659"
                    }
                ],
                "playId": 5062,
                "playDescription": "(2:50) (No Huddle, Shotgun) M.Mariota pass short left to T.McLaurin for 3 yards, TOUCHDOWN.",
                "playTypeCode": 2,
                "quarter": 5,
                "down": 4,
                "yardsToGo": 3,
                "actualYardsToGo": 4.29,
                "actualYardlineForFirstDown": 10,
                "possessionTeamId": "5110",
                "isGoalToGo": true,
                "endGameClock": "2:48",
                "startGameClock": "2:50",
                "playState": "APPROVED",
                "preSnapHomeScore": 20,
                "preSnapVisitorScore": 27,
                "sequence": 5062,
                "gameClock": "02:50",
                "yardline": "DEN 3",
                "isScoring": true,
                "isEndQuarter": false,
                "isSTPlay": false,
                "playDirection": "left",
                "isBigPlay": true,
                "isChangeOfPossession": false
            },
            "players": [
                {
                    "season": 2025,
                    "seasonType": "REG",
                    "week": 13,
                    "esbId": "MAR186347",
                    "gsisId": "00-0032268",
                    "smartId": "32004d41-5218-6347-2b09-64276fa61f68",
                    "jerseyNumber": 8,
                    "uniformNumber": "08",
                    "lastName": "Mariota",
                    "footballName": "Marcus",
                    "firstName": "Marcus",
                    "shortName": "M.Mariota",
                    "position": "QB",
                    "ngsPosition": "QB",
                    "ngsPositionGroup": "QB",
                    "entryYear": 2015,
                    "rookieYear": 2015,
                    "height": "6-4",
                    "weight": 222,
                    "birthDate": "1993-10-30",
                    "draftClub": "TEN",
                    "draftNumber": 2,
                    "teamAbbr": "WAS",
                    "collegeName": "Oregon",
                    "collegeConference": "Pacific Twelve Conference",
                    "statusDescriptionAbbr": "A01",
                    "statusShortDescription": "Active",
                    "currentTeamId": "5110",
                    "positionGroup": "QB",
                    "yearsOfExperience": 11,
                    "status": "ACT",
                    "displayName": "Marcus Mariota",
                    "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/b9ribxqudeehvmjlw0va",
                    "gsisItId": 42345
                },
                {
                    "season": 2025,
                    "seasonType": "REG",
                    "week": 13,
                    "esbId": "MCL278328",
                    "gsisId": "00-0035659",
                    "smartId": "32004d43-4c27-8328-8097-b130ba0e8060",
                    "jerseyNumber": 17,
                    "uniformNumber": "17",
                    "lastName": "McLaurin",
                    "footballName": "Terry",
                    "firstName": "Terry",
                    "shortName": "T.McLaurin",
                    "position": "WR",
                    "ngsPosition": "WR",
                    "ngsPositionGroup": "WR",
                    "entryYear": 2019,
                    "rookieYear": 2019,
                    "height": "6-0",
                    "weight": 210,
                    "birthDate": "1995-09-15",
                    "draftClub": "WAS",
                    "draftNumber": 76,
                    "teamAbbr": "WAS",
                    "collegeName": "Ohio State",
                    "collegeConference": "Big Ten Conference",
                    "statusDescriptionAbbr": "A01",
                    "statusShortDescription": "Active",
                    "currentTeamId": "5110",
                    "positionGroup": "WR",
                    "yearsOfExperience": 7,
                    "status": "ACT",
                    "displayName": "Terry McLaurin",
                    "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/wokz1etv1wj1vhbmvxgs",
                    "gsisItId": 47859
                }
            ],
            "season": 2025,
            "seasonType": "REG",
            "teamAbbr": "WAS",
            "teamId": "5110",
            "week": 13
        }
    ],
    "total": 1852,
    "count": 16,
    "offset": 0,
    "limit": 16
}
```
