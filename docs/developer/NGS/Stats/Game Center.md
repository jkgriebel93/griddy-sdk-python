---
tags:
  - ngs
  - stats
---
[[Stats]]

## /api/live/games/scores
### Query Params

| Name       | Value |
| ---------- | ----- |
| season     | 2025  |
| seasonType | REG   |
| week       | 13    |

### Response
```json
{
    "season": 2025,
    "seasonType": "REG",
    "week": 13,
    "scores": [
        {
            "gameId": 2025113001,
            "gameKey": 60026,
            "gameSmartId": "f8575f89-311e-11f0-b670-ae1250fadad1",
            "homeTeamId": "1050",
            "homeTeamAbbr": "CLE",
            "homeScore": 8,
            "awayTeamId": "4500",
            "awayTeamAbbr": "SF",
            "awayScore": 26,
            "gameClock": "00:00",
            "gameStatus": "F",
            "score": {
                "time": "00:00",
                "phase": "FINAL",
                "visitorTeamScore": {
                    "pointTotal": 26,
                    "pointQ1": 7,
                    "pointQ2": 3,
                    "pointQ3": 7,
                    "pointQ4": 9,
                    "pointOT": 0,
                    "timeoutsRemaining": 1
                },
                "homeTeamScore": {
                    "pointTotal": 8,
                    "pointQ1": 0,
                    "pointQ2": 8,
                    "pointQ3": 0,
                    "pointQ4": 0,
                    "pointOT": 0,
                    "timeoutsRemaining": 0
                }
            },
            "gameDate": "11/30/2025",
            "gameTimeEastern": "13:00:00",
            "gameTime": "2025-11-30T18:00:00Z",
            "visitorTeam": {
                "teamId": "4500",
                "smartId": "10404500-e7cb-7fce-3f10-4eeb269bd179",
                "logo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/SF",
                "abbr": "SF",
                "cityState": "San Francisco",
                "fullName": "San Francisco 49ers",
                "nick": "49ers",
                "teamType": "TEAM",
                "conferenceAbbr": "NFC",
                "divisionAbbr": "NCW"
            },
            "homeTeam": {
                "teamId": "1050",
                "smartId": "10401050-5e38-b907-1be1-55b91b19c057",
                "logo": "https://static.www.nfl.com/{formatInstructions}/league/api/clubs/logos/CLE",
                "abbr": "CLE",
                "cityState": "Cleveland",
                "fullName": "Cleveland Browns",
                "nick": "Browns",
                "teamType": "TEAM",
                "conferenceAbbr": "AFC",
                "divisionAbbr": "ACN"
            }
        }
    ]
}
```

## /api/gamecenter/overview
### Query Params

| Name   | Value      |
| ------ | ---------- |
| gameId | 2025112700 |

### Response
```json
{
    "schedule": {
        "gameKey": 60021,
        "gameDate": "11/27/2025",
        "gameId": 2025112700,
        "gameTimeEastern": "13:00:00",
        "homeTeamAbbr": "DET",
        "homeTeamId": "1540",
        "season": 2025,
        "seasonType": "REG",
        "visitorTeamAbbr": "GB",
        "visitorTeamId": "1800",
        "week": 13
    },
    "passers": {
        "home": {
            "gameId": 2025112700,
            "esbId": "GOF219636",
            "teamId": "1540",
            "teamAbbr": "DET",
            "shortName": "J.Goff",
            "position": "QB",
            "jerseyNumber": 16,
            "playerName": "Jared Goff",
            "zones": [
                {
                    "type": "threeColumns",
                    "lineOfScrimmageDistance": "behindLOS",
                    "section": "leftThird",
                    "attempts": 1,
                    "completionPct": 1,
                    "completions": 1,
                    "interceptions": 0,
                    "qbRating": 158.33333333333331,
                    "touchdowns": 1,
                    "yards": 22,
                    "qbRatingSuccessLevel": "ABOVE"
                },
                {
                    "type": "threeColumns",
                    "lineOfScrimmageDistance": "10To19",
                    "section": "rightThird",
                    "attempts": 1,
                    "completionPct": 0,
                    "completions": 0,
                    "interceptions": 0,
                    "qbRating": 39.58333333333333,
                    "touchdowns": 0,
                    "yards": 0,
                    "qbRatingSuccessLevel": "BELOW"
                },
                {
                    "type": "threeColumns",
                    "lineOfScrimmageDistance": "losTo9",
                    "section": "middleThird",
                    "attempts": 7,
                    "completionPct": 0.8571428571428571,
                    "completions": 6,
                    "interceptions": 0,
                    "qbRating": 84.52380952380952,
                    "touchdowns": 0,
                    "yards": 30,
                    "qbRatingSuccessLevel": "AVERAGE"
                },
                {
                    "type": "threeColumns",
                    "lineOfScrimmageDistance": "10To19",
                    "section": "leftThird",
                    "attempts": 3,
                    "completionPct": 0.6666666666666666,
                    "completions": 2,
                    "interceptions": 0,
                    "qbRating": 103.47222222222221,
                    "touchdowns": 0,
                    "yards": 33,
                    "qbRatingSuccessLevel": "ABOVE"
                },
                {
                    "type": "threeColumns",
                    "lineOfScrimmageDistance": "behindLOS",
                    "section": "rightThird",
                    "attempts": 1,
                    "completionPct": 1,
                    "completions": 1,
                    "interceptions": 0,
                    "qbRating": 79.16666666666666,
                    "touchdowns": 0,
                    "yards": 3,
                    "qbRatingSuccessLevel": "BELOW"
                },
                {
                    "type": "threeColumns",
                    "lineOfScrimmageDistance": "behindLOS",
                    "section": "middleThird",
                    "attempts": 2,
                    "completionPct": 0.5,
                    "completions": 1,
                    "interceptions": 0,
                    "qbRating": 62.5,
                    "touchdowns": 0,
                    "yards": 9,
                    "qbRatingSuccessLevel": "BELOW"
                },
                {
                    "type": "threeColumns",
                    "lineOfScrimmageDistance": "losTo9",
                    "section": "leftThird",
                    "attempts": 2,
                    "completionPct": 1,
                    "completions": 2,
                    "interceptions": 0,
                    "qbRating": 108.33333333333333,
                    "touchdowns": 0,
                    "yards": 20,
                    "qbRatingSuccessLevel": "ABOVE"
                },
                {
                    "type": "threeColumns",
                    "lineOfScrimmageDistance": "10To19",
                    "section": "middleThird",
                    "attempts": 6,
                    "completionPct": 0.8333333333333334,
                    "completions": 5,
                    "interceptions": 0,
                    "qbRating": 158.33333333333331,
                    "touchdowns": 1,
                    "yards": 131,
                    "qbRatingSuccessLevel": "ABOVE"
                },
                {
                    "type": "threeColumns",
                    "lineOfScrimmageDistance": "losTo9",
                    "section": "rightThird",
                    "attempts": 3,
                    "completionPct": 0.6666666666666666,
                    "completions": 2,
                    "interceptions": 0,
                    "qbRating": 70.13888888888889,
                    "touchdowns": 0,
                    "yards": 8,
                    "qbRatingSuccessLevel": "BELOW"
                }
            ],
            "passYards": 256,
            "touchdowns": 2,
            "interceptions": 0,
            "attempts": 26,
            "completions": 20,
            "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/yggfwr4ak4po9byj0qor"
        },
        "visitor": {
            "gameId": 2025112700,
            "esbId": "LOV130776",
            "teamId": "1800",
            "teamAbbr": "GB",
            "shortName": "J.Love",
            "position": "QB",
            "jerseyNumber": 10,
            "playerName": "Jordan Love",
            "zones": [
                {
                    "type": "threeColumns",
                    "lineOfScrimmageDistance": "10To19",
                    "section": "rightThird",
                    "attempts": 3,
                    "completionPct": 0.3333333333333333,
                    "completions": 1,
                    "interceptions": 0,
                    "qbRating": 53.47222222222222,
                    "touchdowns": 0,
                    "yards": 17,
                    "qbRatingSuccessLevel": "BELOW"
                },
                {
                    "type": "threeColumns",
                    "lineOfScrimmageDistance": "10To19",
                    "section": "leftThird",
                    "attempts": 3,
                    "completionPct": 0.6666666666666666,
                    "completions": 2,
                    "interceptions": 0,
                    "qbRating": 104.86111111111111,
                    "touchdowns": 0,
                    "yards": 34,
                    "qbRatingSuccessLevel": "ABOVE"
                },
                {
                    "type": "threeColumns",
                    "lineOfScrimmageDistance": "losTo9",
                    "section": "middleThird",
                    "attempts": 5,
                    "completionPct": 0.6,
                    "completions": 3,
                    "interceptions": 0,
                    "qbRating": 67.08333333333334,
                    "touchdowns": 0,
                    "yards": 18,
                    "qbRatingSuccessLevel": "BELOW"
                },
                {
                    "type": "threeColumns",
                    "lineOfScrimmageDistance": "behindLOS",
                    "section": "leftThird",
                    "attempts": 1,
                    "completionPct": 1,
                    "completions": 1,
                    "interceptions": 0,
                    "qbRating": 118.75,
                    "touchdowns": 1,
                    "yards": 1,
                    "qbRatingSuccessLevel": "ABOVE"
                },
                {
                    "type": "threeColumns",
                    "lineOfScrimmageDistance": "behindLOS",
                    "section": "rightThird",
                    "attempts": 1,
                    "completionPct": 1,
                    "completions": 1,
                    "interceptions": 0,
                    "qbRating": 87.5,
                    "touchdowns": 0,
                    "yards": 5,
                    "qbRatingSuccessLevel": "AVERAGE"
                },
                {
                    "type": "threeColumns",
                    "lineOfScrimmageDistance": "20Plus",
                    "section": "rightThird",
                    "attempts": 4,
                    "completionPct": 0.5,
                    "completions": 2,
                    "interceptions": 0,
                    "qbRating": 135.41666666666669,
                    "touchdowns": 1,
                    "yards": 74,
                    "qbRatingSuccessLevel": "ABOVE"
                },
                {
                    "type": "threeColumns",
                    "lineOfScrimmageDistance": "20Plus",
                    "section": "middleThird",
                    "attempts": 1,
                    "completionPct": 1,
                    "completions": 1,
                    "interceptions": 0,
                    "qbRating": 118.75,
                    "touchdowns": 0,
                    "yards": 30,
                    "qbRatingSuccessLevel": "ABOVE"
                },
                {
                    "type": "threeColumns",
                    "lineOfScrimmageDistance": "losTo9",
                    "section": "leftThird",
                    "attempts": 2,
                    "completionPct": 1,
                    "completions": 2,
                    "interceptions": 0,
                    "qbRating": 127.08333333333333,
                    "touchdowns": 1,
                    "yards": 10,
                    "qbRatingSuccessLevel": "ABOVE"
                },
                {
                    "type": "threeColumns",
                    "lineOfScrimmageDistance": "20Plus",
                    "section": "leftThird",
                    "attempts": 1,
                    "completionPct": 1,
                    "completions": 1,
                    "interceptions": 0,
                    "qbRating": 158.33333333333331,
                    "touchdowns": 1,
                    "yards": 22,
                    "qbRatingSuccessLevel": "ABOVE"
                },
                {
                    "type": "threeColumns",
                    "lineOfScrimmageDistance": "10To19",
                    "section": "middleThird",
                    "attempts": 2,
                    "completionPct": 0,
                    "completions": 0,
                    "interceptions": 0,
                    "qbRating": 39.58333333333333,
                    "touchdowns": 0,
                    "yards": 0,
                    "qbRatingSuccessLevel": "BELOW"
                },
                {
                    "type": "threeColumns",
                    "lineOfScrimmageDistance": "losTo9",
                    "section": "rightThird",
                    "attempts": 6,
                    "completionPct": 0.6666666666666666,
                    "completions": 4,
                    "interceptions": 0,
                    "qbRating": 73.6111111111111,
                    "touchdowns": 0,
                    "yards": 23,
                    "qbRatingSuccessLevel": "BELOW"
                }
            ],
            "passYards": 234,
            "touchdowns": 4,
            "interceptions": 0,
            "attempts": 30,
            "completions": 18,
            "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/uneiwen9drvci9ahuebp"
        }
    },
    "rushers": {
        "home": [
            {
                "esbId": "GIB198578",
                "jerseyNumber": 0,
                "playerName": "Jahmyr Gibbs",
                "position": "RB",
                "rushYards": 68,
                "shortName": "J.Gibbs",
                "teamId": "1540",
                "yards": 86,
                "rushInfo": {
                    "yards": 68,
                    "attempts": 20,
                    "touchdowns": 0,
                    "distance": 410.53000000000003,
                    "avgYards": 3.4,
                    "avgDistance": 20.526500000000002,
                    "avgTimeToLos": 2.9174499999999997,
                    "rushLocationMap": {
                        "OUTSIDE_LEFT": {
                            "yards": 35,
                            "attempts": 8,
                            "touchdowns": 0,
                            "distance": 154.75,
                            "avgYards": 4.375,
                            "avgDistance": 19.34375,
                            "avgTimeToLos": 3.0505
                        },
                        "INSIDE_LEFT": {
                            "yards": 29,
                            "attempts": 5,
                            "touchdowns": 0,
                            "distance": 132.66,
                            "avgYards": 5.8,
                            "avgDistance": 26.532,
                            "avgTimeToLos": 2.7844
                        },
                        "INSIDE_RIGHT": {
                            "yards": 9,
                            "attempts": 3,
                            "touchdowns": 0,
                            "distance": 44.580000000000005,
                            "avgYards": 3,
                            "avgDistance": 14.860000000000001,
                            "avgTimeToLos": 2.586
                        },
                        "OUTSIDE_RIGHT": {
                            "yards": -5,
                            "attempts": 4,
                            "touchdowns": 0,
                            "distance": 78.53999999999999,
                            "avgYards": -1.25,
                            "avgDistance": 19.634999999999998,
                            "avgTimeToLos": 3.06625
                        }
                    },
                    "preSnapRushLocationMap": {
                        "OUTSIDE_LEFT": {
                            "yards": 52,
                            "attempts": 6,
                            "touchdowns": 0,
                            "distance": 161.20000000000002,
                            "avgYards": 8.666666666666666,
                            "avgDistance": 26.86666666666667,
                            "avgTimeToLos": 3.0208333333333335
                        },
                        "INSIDE_LEFT": {
                            "yards": 4,
                            "attempts": 4,
                            "touchdowns": 0,
                            "distance": 49.19,
                            "avgYards": 1,
                            "avgDistance": 12.2975,
                            "avgTimeToLos": 2.871
                        },
                        "INSIDE_RIGHT": {
                            "yards": 6,
                            "attempts": 4,
                            "touchdowns": 0,
                            "distance": 56.55000000000001,
                            "avgYards": 1.5,
                            "avgDistance": 14.137500000000003,
                            "avgTimeToLos": 2.689
                        },
                        "OUTSIDE_RIGHT": {
                            "yards": 6,
                            "attempts": 6,
                            "touchdowns": 0,
                            "distance": 143.59,
                            "avgYards": 1,
                            "avgDistance": 23.93166666666667,
                            "avgTimeToLos": 2.997333333333333
                        }
                    }
                },
                "attempts": 20,
                "touchdowns": 0,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/hjxk3judytgsxkqiilre"
            },
            {
                "esbId": "MON487374",
                "jerseyNumber": 5,
                "playerName": "David Montgomery",
                "position": "RB",
                "rushYards": 32,
                "shortName": "D.Montgomery",
                "teamId": "1540",
                "yards": 48,
                "rushInfo": {
                    "yards": 32,
                    "attempts": 8,
                    "touchdowns": 1,
                    "distance": 117.79,
                    "avgYards": 4,
                    "avgDistance": 14.72375,
                    "avgTimeToLos": 2.793125,
                    "rushLocationMap": {
                        "OUTSIDE_LEFT": {
                            "yards": 0,
                            "attempts": 1,
                            "touchdowns": 0,
                            "distance": 22.389999999999997,
                            "avgYards": 0,
                            "avgDistance": 22.389999999999997,
                            "avgTimeToLos": 4.44
                        },
                        "INSIDE_LEFT": {
                            "yards": 13,
                            "attempts": 4,
                            "touchdowns": 1,
                            "distance": 46.24999999999999,
                            "avgYards": 3.25,
                            "avgDistance": 11.562499999999998,
                            "avgTimeToLos": 2.60075
                        },
                        "INSIDE_RIGHT": {
                            "yards": 19,
                            "attempts": 3,
                            "touchdowns": 0,
                            "distance": 49.150000000000006,
                            "avgYards": 6.333333333333333,
                            "avgDistance": 16.383333333333336,
                            "avgTimeToLos": 2.500666666666666
                        }
                    },
                    "preSnapRushLocationMap": {
                        "OUTSIDE_LEFT": {
                            "yards": 0,
                            "attempts": 1,
                            "touchdowns": 0,
                            "distance": 22.389999999999997,
                            "avgYards": 0,
                            "avgDistance": 22.389999999999997,
                            "avgTimeToLos": 4.44
                        },
                        "INSIDE_RIGHT": {
                            "yards": 7,
                            "attempts": 3,
                            "touchdowns": 1,
                            "distance": 30.400000000000002,
                            "avgYards": 2.3333333333333335,
                            "avgDistance": 10.133333333333335,
                            "avgTimeToLos": 2.257
                        },
                        "OUTSIDE_RIGHT": {
                            "yards": 25,
                            "attempts": 4,
                            "touchdowns": 0,
                            "distance": 65,
                            "avgYards": 6.25,
                            "avgDistance": 16.25,
                            "avgTimeToLos": 2.7835
                        }
                    }
                },
                "attempts": 8,
                "touchdowns": 1,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/xeb6fq4zimgkksq7uari"
            },
            {
                "esbId": "GOF219636",
                "jerseyNumber": 16,
                "playerName": "Jared Goff",
                "position": "QB",
                "rushYards": 24,
                "shortName": "J.Goff",
                "teamId": "1540",
                "yards": 24,
                "rushInfo": {
                    "yards": 24,
                    "attempts": 1,
                    "touchdowns": 0,
                    "distance": 47.91000000000001,
                    "avgYards": 24,
                    "avgDistance": 47.91000000000001,
                    "avgTimeToLos": 5.299,
                    "rushLocationMap": {
                        "OUTSIDE_LEFT": {
                            "yards": 24,
                            "attempts": 1,
                            "touchdowns": 0,
                            "distance": 47.91000000000001,
                            "avgYards": 24,
                            "avgDistance": 47.91000000000001,
                            "avgTimeToLos": 5.299
                        }
                    },
                    "preSnapRushLocationMap": {
                        "OUTSIDE_LEFT": {
                            "yards": 24,
                            "attempts": 1,
                            "touchdowns": 0,
                            "distance": 47.91000000000001,
                            "avgYards": 24,
                            "avgDistance": 47.91000000000001,
                            "avgTimeToLos": 5.299
                        }
                    }
                },
                "touchdowns": 0,
                "attempts": 1,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/yggfwr4ak4po9byj0qor"
            }
        ],
        "visitor": [
            {
                "esbId": "JAC734615",
                "jerseyNumber": 8,
                "playerName": "Josh Jacobs",
                "position": "RB",
                "rushYards": 83,
                "shortName": "J.Jacobs",
                "teamId": "1800",
                "yards": 91,
                "rushInfo": {
                    "yards": 83,
                    "attempts": 17,
                    "touchdowns": 0,
                    "distance": 271.01,
                    "avgYards": 4.882352941176471,
                    "avgDistance": 15.941764705882353,
                    "avgTimeToLos": 2.757294117647059,
                    "rushLocationMap": {
                        "OUTSIDE_LEFT": {
                            "yards": 39,
                            "attempts": 5,
                            "touchdowns": 0,
                            "distance": 92.97999999999999,
                            "avgYards": 7.8,
                            "avgDistance": 18.595999999999997,
                            "avgTimeToLos": 2.7534
                        },
                        "INSIDE_LEFT": {
                            "yards": 29,
                            "attempts": 6,
                            "touchdowns": 0,
                            "distance": 99.97000000000001,
                            "avgYards": 4.833333333333333,
                            "avgDistance": 16.66166666666667,
                            "avgTimeToLos": 2.539166666666667
                        },
                        "INSIDE_RIGHT": {
                            "yards": 5,
                            "attempts": 3,
                            "touchdowns": 0,
                            "distance": 32.800000000000004,
                            "avgYards": 1.6666666666666667,
                            "avgDistance": 10.933333333333335,
                            "avgTimeToLos": 3.104333333333333
                        },
                        "OUTSIDE_RIGHT": {
                            "yards": 10,
                            "attempts": 3,
                            "touchdowns": 0,
                            "distance": 45.260000000000005,
                            "avgYards": 3.3333333333333335,
                            "avgDistance": 15.086666666666668,
                            "avgTimeToLos": 2.853
                        }
                    },
                    "preSnapRushLocationMap": {
                        "OUTSIDE_LEFT": {
                            "yards": 12,
                            "attempts": 4,
                            "touchdowns": 0,
                            "distance": 58.08,
                            "avgYards": 3,
                            "avgDistance": 14.52,
                            "avgTimeToLos": 2.751
                        },
                        "INSIDE_LEFT": {
                            "yards": 60,
                            "attempts": 6,
                            "touchdowns": 0,
                            "distance": 124.50999999999999,
                            "avgYards": 10,
                            "avgDistance": 20.751666666666665,
                            "avgTimeToLos": 2.462
                        },
                        "INSIDE_RIGHT": {
                            "yards": 1,
                            "attempts": 3,
                            "touchdowns": 0,
                            "distance": 31.27,
                            "avgYards": 0.3333333333333333,
                            "avgDistance": 10.423333333333334,
                            "avgTimeToLos": 3.0500000000000003
                        },
                        "OUTSIDE_RIGHT": {
                            "yards": 10,
                            "attempts": 4,
                            "touchdowns": 0,
                            "distance": 57.150000000000006,
                            "avgYards": 2.5,
                            "avgDistance": 14.287500000000001,
                            "avgTimeToLos": 2.987
                        }
                    }
                },
                "attempts": 17,
                "touchdowns": 0,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/drtobqw2mk7yw3edjgwo"
            },
            {
                "esbId": "LOV130776",
                "jerseyNumber": 10,
                "playerName": "Jordan Love",
                "position": "QB",
                "rushYards": 4,
                "shortName": "J.Love",
                "teamId": "1800",
                "yards": 4,
                "rushInfo": {
                    "yards": 4,
                    "attempts": 5,
                    "touchdowns": 0,
                    "distance": 43.81,
                    "avgYards": 0.8,
                    "avgDistance": 8.762,
                    "avgTimeToLos": 4.9275,
                    "rushLocationMap": {
                        "UNKNOWN": {
                            "yards": -3,
                            "attempts": 3,
                            "touchdowns": 0,
                            "distance": 0.5000000000000001,
                            "avgYards": -1,
                            "avgDistance": 0.1666666666666667
                        },
                        "INSIDE_RIGHT": {
                            "yards": 7,
                            "attempts": 2,
                            "touchdowns": 0,
                            "distance": 43.31,
                            "avgYards": 3.5,
                            "avgDistance": 21.655,
                            "avgTimeToLos": 4.9275
                        }
                    },
                    "preSnapRushLocationMap": {
                        "UNKNOWN": {
                            "yards": -3,
                            "attempts": 3,
                            "touchdowns": 0,
                            "distance": 0.5000000000000001,
                            "avgYards": -1,
                            "avgDistance": 0.1666666666666667
                        },
                        "INSIDE_RIGHT": {
                            "yards": 2,
                            "attempts": 1,
                            "touchdowns": 0,
                            "distance": 13.639999999999999,
                            "avgYards": 2,
                            "avgDistance": 13.639999999999999,
                            "avgTimeToLos": 4.116
                        },
                        "OUTSIDE_RIGHT": {
                            "yards": 5,
                            "attempts": 1,
                            "touchdowns": 0,
                            "distance": 29.670000000000005,
                            "avgYards": 5,
                            "avgDistance": 29.670000000000005,
                            "avgTimeToLos": 5.739
                        }
                    }
                },
                "touchdowns": 0,
                "attempts": 5,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/uneiwen9drvci9ahuebp"
            },
            {
                "esbId": "WIL682260",
                "jerseyNumber": 23,
                "playerName": "Emanuel Wilson",
                "position": "RB",
                "rushYards": 14,
                "shortName": "E.Wilson",
                "teamId": "1800",
                "yards": 14,
                "rushInfo": {
                    "yards": 14,
                    "attempts": 4,
                    "touchdowns": 0,
                    "distance": 59.20000000000001,
                    "avgYards": 3.5,
                    "avgDistance": 14.800000000000002,
                    "avgTimeToLos": 2.73525,
                    "rushLocationMap": {
                        "INSIDE_RIGHT": {
                            "yards": 5,
                            "attempts": 1,
                            "touchdowns": 0,
                            "distance": 24.48,
                            "avgYards": 5,
                            "avgDistance": 24.48,
                            "avgTimeToLos": 3.769
                        },
                        "OUTSIDE_RIGHT": {
                            "yards": 9,
                            "attempts": 3,
                            "touchdowns": 0,
                            "distance": 34.720000000000006,
                            "avgYards": 3,
                            "avgDistance": 11.573333333333336,
                            "avgTimeToLos": 2.3906666666666667
                        }
                    },
                    "preSnapRushLocationMap": {
                        "INSIDE_RIGHT": {
                            "yards": 9,
                            "attempts": 3,
                            "touchdowns": 0,
                            "distance": 34.720000000000006,
                            "avgYards": 3,
                            "avgDistance": 11.573333333333336,
                            "avgTimeToLos": 2.3906666666666667
                        },
                        "OUTSIDE_RIGHT": {
                            "yards": 5,
                            "attempts": 1,
                            "touchdowns": 0,
                            "distance": 24.48,
                            "avgYards": 5,
                            "avgDistance": 24.48,
                            "avgTimeToLos": 3.769
                        }
                    }
                },
                "attempts": 4,
                "touchdowns": 0,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/xni9gnwmhdex7h1ey3jq"
            }
        ]
    },
    "passRushers": {
        "leagueAverageSeparationToQb": {
            "avg": 4.575749105308826
        },
        "home": [
            {
                "esbId": "MCN611247",
                "gsisId": "00-0036624",
                "teamId": "1540",
                "playerName": "Alim McNeill",
                "shortName": "A.McNeill",
                "jerseyNumber": 54,
                "position": "DT",
                "blitzCount": 26,
                "avgSeparationToQb": 3.8261208916940697,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/udieb8v70ple2vt3zyof",
                "tackles": 0,
                "assists": 0,
                "sacks": 0,
                "forcedFumbles": 0
            },
            {
                "esbId": "HUT099869",
                "gsisId": "00-0037236",
                "teamId": "1540",
                "playerName": "Aidan Hutchinson",
                "shortName": "A.Hutchinson",
                "jerseyNumber": 97,
                "position": "DE",
                "blitzCount": 26,
                "avgSeparationToQb": 4.429501446091816,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/mnv2cpjveex9rtrkkaly",
                "tackles": 3,
                "assists": 3,
                "sacks": 0,
                "forcedFumbles": 0
            },
            {
                "esbId": "LOP508807",
                "gsisId": "00-0036568",
                "teamId": "1540",
                "playerName": "Roy Lopez",
                "shortName": "R.Lopez",
                "jerseyNumber": 51,
                "position": "NT",
                "blitzCount": 13,
                "avgSeparationToQb": 5.120942584585574,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/i4a37cibk9pwjjgq4rla",
                "tackles": 1,
                "assists": 0,
                "sacks": 0,
                "forcedFumbles": 0
            },
            {
                "esbId": "REA148116",
                "gsisId": "00-0032424",
                "teamId": "1540",
                "playerName": "DJ Reader",
                "shortName": "D.Reader",
                "jerseyNumber": 98,
                "position": "NT",
                "blitzCount": 11,
                "avgSeparationToQb": 4.609742304157193,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/gbbbyrh2pgibo9w8ahd6",
                "tackles": 0,
                "assists": 1,
                "sacks": 0,
                "forcedFumbles": 0
            }
        ],
        "visitor": [
            {
                "esbId": "PAR753418",
                "gsisId": "00-0036932",
                "teamId": "1800",
                "playerName": "Micah Parsons",
                "shortName": "M.Parsons",
                "jerseyNumber": 1,
                "position": "OLB",
                "blitzCount": 21,
                "avgSeparationToQb": 2.5548948176435986,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/igbkpnpsezgrvngnf5ck",
                "tackles": 4,
                "assists": 4,
                "sacks": 2.5,
                "forcedFumbles": 0
            },
            {
                "esbId": "GAR766759",
                "gsisId": "00-0034967",
                "teamId": "1800",
                "playerName": "Rashan Gary",
                "shortName": "R.Gary",
                "jerseyNumber": 52,
                "position": "DE",
                "blitzCount": 20,
                "avgSeparationToQb": 3.750465079981081,
                "headshot": "https://static.www.nfl.com/image/private/{formatInstructions}/league/t4clz4xe8sfxszmvohfo",
                "tackles": 1,
                "assists": 1,
                "sacks": 0,
                "forcedFumbles": 0
            },
            {
                "esbId": "WYA279831",
                "gsisId": "00-0037075",
                "teamId": "1800",
                "playerName": "Devonte Wyatt",
                "shortName": "D.Wyatt",
                "jerseyNumber": 95,
                "position": "DT",
                "blitzCount": 15,
                "avgSeparationToQb": 4.147912880149822,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/p1oupvtm9kcm0wpuhape",
                "tackles": 3,
                "assists": 1,
                "sacks": 0,
                "forcedFumbles": 0
            },
            {
                "esbId": "BRI485289",
                "gsisId": "00-0040016",
                "teamId": "1800",
                "playerName": "Warren Brinson",
                "shortName": "W.Brinson",
                "jerseyNumber": 91,
                "position": "DT",
                "blitzCount": 15,
                "avgSeparationToQb": 3.7731736199744903,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/wbsv4uzbd2wytxysgznq",
                "tackles": 1,
                "assists": 0,
                "sacks": 0,
                "forcedFumbles": 0
            }
        ]
    },
    "receivers": {
        "leagueAverageReceiverSeparation": {
            "avg": 2.984067837299754
        },
        "home": [
            {
                "esbId": "WIL344909",
                "jerseyNumber": 1,
                "playerName": "Jameson Williams",
                "position": "WR",
                "recYards": 144,
                "shortName": "J.Williams",
                "teamId": "1540",
                "receptionInfo": {
                    "avgAirYards": 8.072,
                    "avgCushion": 6.367,
                    "avgSeparation": 3.0777230616953037,
                    "targets": 10,
                    "receptions": 7,
                    "touchdowns": 1
                },
                "targets": 10,
                "receptions": 7,
                "touchdowns": 1,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/gpjarmglg1jhwq5wr1uu"
            },
            {
                "esbId": "KEN614625",
                "jerseyNumber": 85,
                "playerName": "Tom Kennedy",
                "position": "WR",
                "recYards": 36,
                "shortName": "T.Kennedy",
                "teamId": "1540",
                "receptionInfo": {
                    "avgAirYards": 7.635,
                    "avgCushion": 6.8975,
                    "avgSeparation": 3.635565463727188,
                    "targets": 4,
                    "receptions": 4,
                    "touchdowns": 0
                },
                "targets": 4,
                "receptions": 4,
                "touchdowns": 0,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/gvqhhlipkpytuu4lqnps"
            },
            {
                "esbId": "DWE397627",
                "jerseyNumber": 82,
                "playerName": "Ross Dwelley",
                "position": "TE",
                "recYards": 3,
                "shortName": "R.Dwelley",
                "teamId": "1540",
                "receptionInfo": {
                    "avgAirYards": 4.6333333333333355,
                    "avgCushion": 6.533333333333334,
                    "avgSeparation": 2.24648701262254,
                    "targets": 3,
                    "receptions": 1,
                    "touchdowns": 0
                },
                "targets": 3,
                "receptions": 1,
                "touchdowns": 0,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/wf9ynmqonmnaosslkwdl"
            },
            {
                "esbId": "TES116936",
                "jerseyNumber": 18,
                "playerName": "Isaac TeSlaa",
                "position": "WR",
                "recYards": 35,
                "shortName": "I.TeSlaa",
                "teamId": "1540",
                "receptionInfo": {
                    "avgAirYards": 16.585,
                    "avgCushion": 7.315,
                    "avgSeparation": 2.7129184028466335,
                    "targets": 2,
                    "receptions": 2,
                    "touchdowns": 1
                },
                "targets": 2,
                "receptions": 2,
                "touchdowns": 1,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/wa4sruqazyqobmepi6vi"
            },
            {
                "esbId": "STB415291",
                "jerseyNumber": 14,
                "playerName": "Amon-Ra St. Brown",
                "position": "WR",
                "recYards": 0,
                "shortName": "A.St. Brown",
                "teamId": "1540",
                "receptionInfo": {
                    "avgAirYards": 16.71,
                    "avgCushion": 8.73,
                    "avgSeparation": 5.529059594542278,
                    "targets": 1,
                    "receptions": 0,
                    "touchdowns": 0
                },
                "targets": 1,
                "receptions": 0,
                "touchdowns": 0,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/fd8nwhm6pvxfyzphzl6i"
            }
        ],
        "visitor": [
            {
                "esbId": "WAT316591",
                "jerseyNumber": 9,
                "playerName": "Christian Watson",
                "position": "WR",
                "recYards": 80,
                "shortName": "C.Watson",
                "teamId": "1800",
                "receptionInfo": {
                    "avgAirYards": 18.183,
                    "avgCushion": 3.406,
                    "avgSeparation": 1.1334836857571955,
                    "targets": 10,
                    "receptions": 4,
                    "touchdowns": 1
                },
                "targets": 10,
                "receptions": 4,
                "touchdowns": 1,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/syljognztlbghfeqyqn1"
            },
            {
                "esbId": "WIC622867",
                "jerseyNumber": 13,
                "playerName": "Dontayvion Wicks",
                "position": "WR",
                "recYards": 94,
                "shortName": "D.Wicks",
                "teamId": "1800",
                "receptionInfo": {
                    "avgAirYards": 12.174285714285714,
                    "avgCushion": 4.468571428571429,
                    "avgSeparation": 2.33325098437064,
                    "targets": 7,
                    "receptions": 6,
                    "touchdowns": 2
                },
                "targets": 7,
                "receptions": 6,
                "touchdowns": 2,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/er7pbyq82nsbw1w3wyor"
            },
            {
                "esbId": "DOU043165",
                "jerseyNumber": 87,
                "playerName": "Romeo Doubs",
                "position": "WR",
                "recYards": 20,
                "shortName": "R.Doubs",
                "teamId": "1800",
                "receptionInfo": {
                    "avgAirYards": 2.9400000000000013,
                    "avgCushion": 6.5675,
                    "avgSeparation": 2.536084591701447,
                    "targets": 4,
                    "receptions": 4,
                    "touchdowns": 1
                },
                "targets": 4,
                "receptions": 4,
                "touchdowns": 1,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/ov2llp1bfetznmngqybi"
            },
            {
                "esbId": "HEA759997",
                "jerseyNumber": 18,
                "playerName": "Malik Heath",
                "position": "WR",
                "recYards": 0,
                "shortName": "M.Heath",
                "teamId": "1800",
                "receptionInfo": {
                    "avgAirYards": 7.619999999999997,
                    "avgCushion": 7.25,
                    "avgSeparation": 2.9954966199279904,
                    "targets": 1,
                    "receptions": 0,
                    "touchdowns": 0
                },
                "targets": 1,
                "receptions": 0,
                "touchdowns": 0,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/gtvkkadrxfzlj1qxshhx"
            },
            {
                "esbId": "FIT782415",
                "jerseyNumber": 86,
                "playerName": "John FitzPatrick",
                "position": "TE",
                "recYards": 0,
                "shortName": "J.FitzPatrick",
                "teamId": "1800",
                "receptionInfo": {
                    "avgAirYards": 3.719999999999999,
                    "avgCushion": 3.42,
                    "avgSeparation": 0.5131276644267003,
                    "targets": 1,
                    "receptions": 0,
                    "touchdowns": 0
                },
                "targets": 1,
                "receptions": 0,
                "touchdowns": 0,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/kopyksw2p51nivtldayc"
            }
        ]
    },
    "leaders": {
        "speedLeaders": {
            "home": {
                "gsisPlayId": 3595,
                "esbId": "WIL344909",
                "jerseyNumber": 1,
                "playerName": "Jameson Williams",
                "position": "WR",
                "shortName": "J.Williams",
                "teamId": "1540",
                "maxSpeed": 19.9840909535,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/gpjarmglg1jhwq5wr1uu"
            },
            "visitor": {
                "gsisPlayId": 2400,
                "esbId": "WAT316591",
                "jerseyNumber": 9,
                "playerName": "Christian Watson",
                "position": "WR",
                "shortName": "C.Watson",
                "teamId": "1800",
                "maxSpeed": 20.1477273175,
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/syljognztlbghfeqyqn1"
            }
        },
        "timeToSackLeaders": {
            "visitor": {
                "gsisPlayId": 3497,
                "esbId": "PAR753418",
                "jerseyNumber": 1,
                "playerName": "Micah Parsons",
                "position": "OLB",
                "shortName": "M.Parsons",
                "teamId": "1800",
                "tackleInfo": {
                    "timeToTackle": 2.884
                },
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/igbkpnpsezgrvngnf5ck"
            }
        },
        "passDistanceLeaders": {
            "home": {
                "gsisPlayId": 3000,
                "esbId": "GOF219636",
                "jerseyNumber": 16,
                "playerName": "Jared Goff",
                "position": "QB",
                "shortName": "J.Goff",
                "teamId": "1540",
                "passInfo": {
                    "airDistance": 31.53730806521064
                },
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/yggfwr4ak4po9byj0qor"
            },
            "visitor": {
                "gsisPlayId": 2400,
                "esbId": "LOV130776",
                "jerseyNumber": 10,
                "playerName": "Jordan Love",
                "position": "QB",
                "shortName": "J.Love",
                "teamId": "1800",
                "passInfo": {
                    "airDistance": 58.2006254261928
                },
                "headshot": "https://static.www.nfl.com/image/upload/{formatInstructions}/league/uneiwen9drvci9ahuebp"
            }
        }
    }
}
```