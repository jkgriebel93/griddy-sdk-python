# GameSummaryTeamScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**q1** | **int** |  | [optional] 
**q2** | **int** |  | [optional] 
**q3** | **int** |  | [optional] 
**q4** | **int** |  | [optional] 
**ot** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.game_summary_team_score import GameSummaryTeamScore

# TODO update the JSON string below
json = "{}"
# create an instance of GameSummaryTeamScore from a JSON string
game_summary_team_score_instance = GameSummaryTeamScore.from_json(json)
# print the JSON string representation of the object
print(GameSummaryTeamScore.to_json())

# convert the object into a dict
game_summary_team_score_dict = game_summary_team_score_instance.to_dict()
# create an instance of GameSummaryTeamScore from a dict
game_summary_team_score_from_dict = GameSummaryTeamScore.from_dict(game_summary_team_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


