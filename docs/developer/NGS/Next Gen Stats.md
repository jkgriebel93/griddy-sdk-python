---
tags:
  - ngs
---

![[Pasted image 20251201083002.png]]



Browser URL: https://nextgenstats.nfl.com
(Relevant) API Calls:

## /api/content/microsite/chart

### Query Params

| Name     | Value  |
| -------- | ------ |
| `count`  | `12`   |
| `week`   | `all`  |
| `type`   | `all`  |
| `teamId` | `all`  |
| `esbId`  | `all`  |
| `season` | `2025` |
### Response
```
{
    "charts": [
        {
            "imageName": "route-chart_KIT388290_2025-REG-12_1764043740054.jpeg",
            "esbId": "KIT388290",
            "firstName": "George",
            "gameId": 2025112400,
            "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/ztz3xqjaqgok9m4nylgs",
            "lastName": "Kittle",
            "playerName": "George Kittle",
            "position": "TE",
            "receivingYards": 78,
            "receptions": 6,
            "season": 2025,
            "seasonType": "REG",
            "teamId": "4500",
            "timestamp": 1764043741013,
            "touchdowns": 0,
            "type": "route",
            "week": 12,
            "extraLargeImg": "//charts-cdn-b.nextgenstats.nfl.com/static-charts/1200/route-chart_KIT388290_2025-REG-12_1764043740054.jpeg",
            "playerNameSlug": "george-kittle",
            "smallImg": "//charts-cdn-b.nextgenstats.nfl.com/static-charts/300/route-chart_KIT388290_2025-REG-12_1764043740054.jpeg",
            "mediumImg": "//charts-cdn-b.nextgenstats.nfl.com/static-charts/600/route-chart_KIT388290_2025-REG-12_1764043740054.jpeg",
            "largeImg": "//charts-cdn-b.nextgenstats.nfl.com/static-charts/900/route-chart_KIT388290_2025-REG-12_1764043740054.jpeg"
        },
        {
            "imageName": "carry-chart_MCC035988_2025-REG-12_1764043729881.jpeg",
            "carries": 24,
            "esbId": "MCC035988",
            "firstName": "Christian",
            "gameId": 2025112400,
            "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/resjdwihunsqckohcorj",
            "lastName": "McCaffrey",
            "playerName": "Christian McCaffrey",
            "position": "RB",
            "rushingYards": 89,
            "season": 2025,
            "seasonType": "REG",
            "teamId": "4500",
            "timestamp": 1764043731888,
            "touchdowns": 1,
            "type": "carry",
            "week": 12,
            "extraLargeImg": "//charts-cdn-b.nextgenstats.nfl.com/static-charts/1200/carry-chart_MCC035988_2025-REG-12_1764043729881.jpeg",
            "playerNameSlug": "christian-mccaffrey",
            "smallImg": "//charts-cdn-b.nextgenstats.nfl.com/static-charts/300/carry-chart_MCC035988_2025-REG-12_1764043729881.jpeg",
            "mediumImg": "//charts-cdn-b.nextgenstats.nfl.com/static-charts/600/carry-chart_MCC035988_2025-REG-12_1764043729881.jpeg",
            "largeImg": "//charts-cdn-b.nextgenstats.nfl.com/static-charts/900/carry-chart_MCC035988_2025-REG-12_1764043729881.jpeg"
        }
    ],
    "count": 12,
    "offset": 0,
    "total": 1043,
    "season": "2025",
    "teamId": "all",
    "type": "all",
    "week": "all",
    "seasonType": "all"
}
```

## /api/plays/highlights

### Query Params

| Name     | Value  |
| -------- | ------ |
| `limit`  | `16`   |
| `season` | `2025` |
### Response
```
{
    "season": 2025,
    "highlights": [
        {
            "gameId": 2025112400,
            "playId": 3114,
            "play": {
                "playType": "play_type_pass",
                "gameId": 2025112400,
                "gameKey": 60020,
                "yardlineSide": "SF",
                "absoluteYardlineNumber": 43,
                "yardlineNumber": 33,
                "timeOfDayUTC": "2025-11-25T03:36:09.000Z",
                "isPenalty": false,
                "homeScore": 20,
                "visitorScore": 9,
                "playStats": [
                    {
                        "playId": 3114,
                        "clubCode": "CAR",
                        "playerName": "B.Young",
                        "statId": 19,
                        "yards": 0,
                        "gsisId": "00-0039150"
                    },
                    {
                        "playId": 3114,
                        "clubCode": "CAR",
                        "playerName": "T.McMillan",
                        "statId": 115,
                        "yards": 0,
                        "gsisId": "00-0040124"
                    },
                    {
                        "playId": 3114,
                        "clubCode": "CAR",
                        "playerName": "B.Young",
                        "statId": 112,
                        "yards": 11,
                        "gsisId": "00-0039150"
                    },
                    {
                        "playId": 3114,
                        "clubCode": "SF",
                        "playerName": "J.Brown",
                        "statId": 25,
                        "yards": 4,
                        "gsisId": "00-0038554"
                    },
                    {
                        "playId": 3114,
                        "clubCode": "SF",
                        "playerName": "J.Brown",
                        "statId": 85,
                        "yards": 0,
                        "gsisId": "00-0038554"
                    },
                    {
                        "playId": 3114,
                        "clubCode": "CAR",
                        "playerName": "T.McMillan",
                        "statId": 79,
                        "yards": 0,
                        "gsisId": "00-0040124"
                    }
                ],
                "playId": 3114,
                "playDescription": "(6:33) (Shotgun) B.Young pass short middle intended for T.McMillan INTERCEPTED by J.Brown at SF 22. J.Brown to SF 26 for 4 yards (T.McMillan).",
                "playTypeCode": 2,
                "quarter": 4,
                "down": 2,
                "yardsToGo": 8,
                "actualYardsToGo": 8.28,
                "actualYardlineForFirstDown": 35.68,
                "possessionTeamId": "0750",
                "isGoalToGo": false,
                "endGameClock": "6:29",
                "startGameClock": "6:34",
                "playState": "APPROVED",
                "preSnapHomeScore": 20,
                "preSnapVisitorScore": 9,
                "sequence": 3114,
                "gameClock": "06:33",
                "yardline": "SF 33",
                "isScoring": false,
                "isEndQuarter": false,
                "isSTPlay": false,
                "playDirection": "left",
                "isBigPlay": true,
                "isChangeOfPossession": true
            },
            "players": [
                {
                    "season": 2025,
                    "seasonType": "REG",
                    "week": 12,
                    "esbId": "BRO492777",
                    "gsisId": "00-0038554",
                    "smartId": "32004252-4f49-2777-600c-5206658f7fd5",
                    "jerseyNumber": 27,
                    "uniformNumber": "27",
                    "lastName": "Brown",
                    "footballName": "Ji'Ayir",
                    "firstName": "Ji'Ayir",
                    "shortName": "J.Brown",
                    "position": "SS",
                    "ngsPosition": "SAFETY",
                    "ngsPositionGroup": "DB",
                    "entryYear": 2023,
                    "rookieYear": 2023,
                    "height": "5-11",
                    "weight": 202,
                    "birthDate": "2000-01-25",
                    "draftClub": "SF",
                    "draftNumber": 87,
                    "teamAbbr": "SF",
                    "collegeName": "Penn State",
                    "collegeConference": "Big Ten Conference",
                    "statusDescriptionAbbr": "A01",
                    "statusShortDescription": "Active",
                    "currentTeamId": "4500",
                    "positionGroup": "DB",
                    "yearsOfExperience": 3,
                    "status": "ACT",
                    "displayName": "Ji'Ayir Brown",
                    "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/gmgewszcsvxdb63dmqby",
                    "gsisItId": 55952
                }
            ],
            "season": 2025,
            "seasonType": "REG",
            "teamAbbr": "SF",
            "teamId": "4500",
            "week": 12
        }
    ]
}
```
