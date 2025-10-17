# NFLPlayerWeekProjectedStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**NFLNFLPlayerWeekProjectedStatsAttributes**](NFLPlayerWeekProjectedStatsAttributes.md) |  | [optional] 
**id** | **str** | Unique identifier for these stats | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from nfl.models.nfl_player_week_projected_stats import NFLPlayerWeekProjectedStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPlayerWeekProjectedStats from a JSON string
nfl_player_week_projected_stats_instance = NFLPlayerWeekProjectedStats.from_json(json)
# print the JSON string representation of the object
print(NFLPlayerWeekProjectedStats.to_json())

# convert the object into a dict
nfl_player_week_projected_stats_dict = nfl_player_week_projected_stats_instance.to_dict()
# create an instance of NFLPlayerWeekProjectedStats from a dict
nfl_player_week_projected_stats_from_dict = NFLPlayerWeekProjectedStats.from_dict(nfl_player_week_projected_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


