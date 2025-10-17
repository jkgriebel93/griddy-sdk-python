# TeamBoxScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away** | [**TeamBoxscore**](TeamBoxscore.md) |  | [optional] 
**game_id** | **str** | Game identifier | [optional] 
**home** | [**TeamBoxscore**](TeamBoxscore.md) |  | [optional] 
**schedule** | [**BoxscoreSchedule**](BoxscoreSchedule.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.team_box_score import TeamBoxScore

# TODO update the JSON string below
json = "{}"
# create an instance of TeamBoxScore from a JSON string
team_box_score_instance = TeamBoxScore.from_json(json)
# print the JSON string representation of the object
print(TeamBoxScore.to_json())

# convert the object into a dict
team_box_score_dict = team_box_score_instance.to_dict()
# create an instance of TeamBoxScore from a dict
team_box_score_from_dict = TeamBoxScore.from_dict(team_box_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


