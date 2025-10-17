# PlayerWeekProjectedStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**PlayerWeekProjectedStatsAttributes**](PlayerWeekProjectedStatsAttributes.md) |  | [optional] 
**id** | **str** | Unique identifier for these stats | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.player_week_projected_stats import PlayerWeekProjectedStats

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerWeekProjectedStats from a JSON string
player_week_projected_stats_instance = PlayerWeekProjectedStats.from_json(json)
# print the JSON string representation of the object
print(PlayerWeekProjectedStats.to_json())

# convert the object into a dict
player_week_projected_stats_dict = player_week_projected_stats_instance.to_dict()
# create an instance of PlayerWeekProjectedStats from a dict
player_week_projected_stats_from_dict = PlayerWeekProjectedStats.from_dict(player_week_projected_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


