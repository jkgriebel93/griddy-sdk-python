# GameSummaryTeamTimeouts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remaining** | **int** |  | [optional] 
**used** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.game_summary_team_timeouts import GameSummaryTeamTimeouts

# TODO update the JSON string below
json = "{}"
# create an instance of GameSummaryTeamTimeouts from a JSON string
game_summary_team_timeouts_instance = GameSummaryTeamTimeouts.from_json(json)
# print the JSON string representation of the object
print(GameSummaryTeamTimeouts.to_json())

# convert the object into a dict
game_summary_team_timeouts_dict = game_summary_team_timeouts_instance.to_dict()
# create an instance of GameSummaryTeamTimeouts from a dict
game_summary_team_timeouts_from_dict = GameSummaryTeamTimeouts.from_dict(game_summary_team_timeouts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


