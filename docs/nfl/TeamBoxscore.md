# TeamBoxscore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_points** | [**List[BoxScorePlayerExtraPointsStatistic]**](BoxScorePlayerExtraPointsStatistic.md) |  | [optional] 
**field_goals** | [**List[BoxScorePlayerFieldGoalsStatistic]**](BoxScorePlayerFieldGoalsStatistic.md) |  | [optional] 
**fumbles** | [**List[BoxScorePlayerFumblesStatistic]**](BoxScorePlayerFumblesStatistic.md) |  | [optional] 
**kick_return** | [**List[BoxScorePlayerKickReturnStatistic]**](BoxScorePlayerKickReturnStatistic.md) |  | [optional] 
**kicking** | [**List[BoxScorePlayerKickingStatistic]**](BoxScorePlayerKickingStatistic.md) |  | [optional] 
**passing** | [**List[BoxScorePlayerPassingStatistic]**](BoxScorePlayerPassingStatistic.md) |  | [optional] 
**punt_return** | [**List[BoxScorePlayerPuntReturnStatistic]**](BoxScorePlayerPuntReturnStatistic.md) |  | [optional] 
**punting** | [**List[BoxScorePlayerPuntingStatistic]**](BoxScorePlayerPuntingStatistic.md) |  | [optional] 
**receiving** | [**List[BoxScorePlayerReceivingStatistic]**](BoxScorePlayerReceivingStatistic.md) |  | [optional] 
**rushing** | [**List[BoxScorePlayerRushingStatistic]**](BoxScorePlayerRushingStatistic.md) |  | [optional] 
**tackles** | [**List[BoxScorePlayerTacklesStatistic]**](BoxScorePlayerTacklesStatistic.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.team_boxscore import TeamBoxscore

# TODO update the JSON string below
json = "{}"
# create an instance of TeamBoxscore from a JSON string
team_boxscore_instance = TeamBoxscore.from_json(json)
# print the JSON string representation of the object
print(TeamBoxscore.to_json())

# convert the object into a dict
team_boxscore_dict = team_boxscore_instance.to_dict()
# create an instance of TeamBoxscore from a dict
team_boxscore_from_dict = TeamBoxscore.from_dict(team_boxscore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


