# NFLPassRusherStats


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
**blitz_count** | **int** |  | [optional] 
**avg_separation_to_qb** | **float** |  | [optional] 
**tackles** | **int** |  | [optional] 
**assists** | **int** |  | [optional] 
**sacks** | **float** |  | [optional] 
**forced_fumbles** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_pass_rusher_stats import NFLPassRusherStats

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPassRusherStats from a JSON string
nfl_pass_rusher_stats_instance = NFLPassRusherStats.from_json(json)
# print the JSON string representation of the object
print(NFLPassRusherStats.to_json())

# convert the object into a dict
nfl_pass_rusher_stats_dict = nfl_pass_rusher_stats_instance.to_dict()
# create an instance of NFLPassRusherStats from a dict
nfl_pass_rusher_stats_from_dict = NFLPassRusherStats.from_dict(nfl_pass_rusher_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


