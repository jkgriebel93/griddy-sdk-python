# LiveGameAwayTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbreviation** | **str** |  | [optional] 
**score** | **int** |  | [optional] 
**team_id** | **str** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.live_game_away_team import LiveGameAwayTeam

# TODO update the JSON string below
json = "{}"
# create an instance of LiveGameAwayTeam from a JSON string
live_game_away_team_instance = LiveGameAwayTeam.from_json(json)
# print the JSON string representation of the object
print(LiveGameAwayTeam.to_json())

# convert the object into a dict
live_game_away_team_dict = live_game_away_team_instance.to_dict()
# create an instance of LiveGameAwayTeam from a dict
live_game_away_team_from_dict = LiveGameAwayTeam.from_dict(live_game_away_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


