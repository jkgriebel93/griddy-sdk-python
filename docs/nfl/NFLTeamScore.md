# NFLTeamScore


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
from nfl.models.nfl_team_score import NFLTeamScore

# TODO update the JSON string below
json = "{}"
# create an instance of NFLTeamScore from a JSON string
nfl_team_score_instance = NFLTeamScore.from_json(json)
# print the JSON string representation of the object
print(NFLTeamScore.to_json())

# convert the object into a dict
nfl_team_score_dict = nfl_team_score_instance.to_dict()
# create an instance of NFLTeamScore from a dict
nfl_team_score_from_dict = NFLTeamScore.from_dict(nfl_team_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


