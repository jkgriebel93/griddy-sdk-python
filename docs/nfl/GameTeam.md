# GameTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_logo** | **str** | URL to team logo (may contain formatInstructions placeholder) | [optional] 
**full_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**score** | [**GameTeamScore**](GameTeamScore.md) |  | [optional] 
**team_id** | **str** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.game_team import GameTeam

# TODO update the JSON string below
json = "{}"
# create an instance of GameTeam from a JSON string
game_team_instance = GameTeam.from_json(json)
# print the JSON string representation of the object
print(GameTeam.to_json())

# convert the object into a dict
game_team_dict = game_team_instance.to_dict()
# create an instance of GameTeam from a dict
game_team_from_dict = GameTeam.from_dict(game_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


