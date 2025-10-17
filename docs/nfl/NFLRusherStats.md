# NFLRusherStats


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
**position** | [**NFLNFLNextGenStatsPositionEnum**](NFLNextGenStatsPositionEnum.md) |  | [optional] 
**yards** | **int** |  | [optional] 
**attempts** | **int** |  | [optional] 
**touchdowns** | **int** |  | [optional] 
**rush_info** | [**NFLNFLRushingInfo**](NFLRushingInfo.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_rusher_stats import NFLRusherStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLRusherStats from a JSON string
nfl_rusher_stats_instance = NFLRusherStats.from_json(json)
# print the JSON string representation of the object
print(NFLRusherStats.to_json())

# convert the object into a dict
nfl_rusher_stats_dict = nfl_rusher_stats_instance.to_dict()
# create an instance of NFLRusherStats from a dict
nfl_rusher_stats_from_dict = NFLRusherStats.from_dict(nfl_rusher_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


