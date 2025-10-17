# KickingStats


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
from src.griddy.nfl.models.kicking_stats import KickingStats

# TODO update the JSON string below
json = "{}"
# create an instance of KickingStats from a JSON string
kicking_stats_instance = KickingStats.from_json(json)
# print the JSON string representation of the object
print(KickingStats.to_json())

# convert the object into a dict
kicking_stats_dict = kicking_stats_instance.to_dict()
# create an instance of KickingStats from a dict
kicking_stats_from_dict = KickingStats.from_dict(kicking_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


