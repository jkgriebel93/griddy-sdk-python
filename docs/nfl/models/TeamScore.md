# TeamScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**point_ot** | **int** | Overtime points | [optional] 
**point_q1** | **int** | First quarter points | [optional] 
**point_q2** | **int** | Second quarter points | [optional] 
**point_q3** | **int** | Third quarter points | [optional] 
**point_q4** | **int** | Fourth quarter points | [optional] 
**point_total** | **int** | Total points scored | [optional] 
**timeouts_remaining** | **int** | Timeouts left | [optional] 

## Example

```python
from src.griddy.nfl.models.team_score import TeamScore

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScore from a JSON string
team_score_instance = TeamScore.from_json(json)
# print the JSON string representation of the object
print(TeamScore.to_json())

# convert the object into a dict
team_score_dict = team_score_instance.to_dict()
# create an instance of TeamScore from a dict
team_score_from_dict = TeamScore.from_dict(team_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


