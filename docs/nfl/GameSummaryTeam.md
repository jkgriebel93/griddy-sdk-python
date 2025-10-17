# GameSummaryTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **str** |  | [optional] 
**has_possession** | **bool** |  | [optional] 
**score** | [**GameSummaryTeamScore**](GameSummaryTeamScore.md) |  | [optional] 
**timeouts** | [**GameSummaryTeamTimeouts**](GameSummaryTeamTimeouts.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.game_summary_team import GameSummaryTeam

# TODO update the JSON string below
json = "{}"
# create an instance of GameSummaryTeam from a JSON string
game_summary_team_instance = GameSummaryTeam.from_json(json)
# print the JSON string representation of the object
print(GameSummaryTeam.to_json())

# convert the object into a dict
game_summary_team_dict = game_summary_team_instance.to_dict()
# create an instance of GameSummaryTeam from a dict
game_summary_team_from_dict = GameSummaryTeam.from_dict(game_summary_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


