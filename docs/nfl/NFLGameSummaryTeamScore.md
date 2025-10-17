# NFLGameSummaryTeamScore


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
from nfl.models.nfl_game_summary_team_score import NFLGameSummaryTeamScore

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGameSummaryTeamScore from a JSON string
nfl_game_summary_team_score_instance = NFLGameSummaryTeamScore.from_json(json)
# print the JSON string representation of the object
print(NFLGameSummaryTeamScore.to_json())

# convert the object into a dict
nfl_game_summary_team_score_dict = nfl_game_summary_team_score_instance.to_dict()
# create an instance of NFLGameSummaryTeamScore from a dict
nfl_game_summary_team_score_from_dict = NFLGameSummaryTeamScore.from_dict(nfl_game_summary_team_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


