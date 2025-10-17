# RusherStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nfl_id** | **int** |  | [optional] 
**gsis_id** | **str** |  | [optional] 
**esb_id** | **str** |  | [optional] 
**jersey_number** | **int** |  | [optional] 
**player_name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**headshot** | **str** | URL to player headshot image (contains formatInstructions placeholder) | [optional] 
**position** | [**NextGenStatsPositionEnum**](NextGenStatsPositionEnum.md) |  | [optional] 
**yards** | **int** |  | [optional] 
**attempts** | **int** |  | [optional] 
**touchdowns** | **int** |  | [optional] 
**rush_info** | [**RushingInfo**](RushingInfo.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.rusher_stats import RusherStats

# TODO update the JSON string below
json = "{}"
# create an instance of RusherStats from a JSON string
rusher_stats_instance = RusherStats.from_json(json)
# print the JSON string representation of the object
print(RusherStats.to_json())

# convert the object into a dict
rusher_stats_dict = rusher_stats_instance.to_dict()
# create an instance of RusherStats from a dict
rusher_stats_from_dict = RusherStats.from_dict(rusher_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


