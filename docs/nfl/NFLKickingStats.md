# NFLKickingStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_points_attempted** | **int** |  | [optional] 
**extra_points_made** | **int** |  | [optional] 
**field_goal_pct** | **float** |  | [optional] 
**field_goals_attempted** | **int** |  | [optional] 
**field_goals_made** | **int** |  | [optional] 
**long_field_goal** | **int** |  | [optional] 
**points** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_kicking_stats import NFLKickingStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLKickingStats from a JSON string
nfl_kicking_stats_instance = NFLKickingStats.from_json(json)
# print the JSON string representation of the object
print(NFLKickingStats.to_json())

# convert the object into a dict
nfl_kicking_stats_dict = nfl_kicking_stats_instance.to_dict()
# create an instance of NFLKickingStats from a dict
nfl_kicking_stats_from_dict = NFLKickingStats.from_dict(nfl_kicking_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


