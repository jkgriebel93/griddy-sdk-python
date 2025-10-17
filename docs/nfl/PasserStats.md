# PasserStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempts** | **int** |  | [optional] 
**completions** | **int** |  | [optional] 
**game_id** | **str** |  | [optional] 
**interceptions** | **int** |  | [optional] 
**pass_yards** | **int** |  | [optional] 
**touchdowns** | **int** |  | [optional] 
**zones** | [**List[PassingZoneStats]**](PassingZoneStats.md) |  | [optional] 
**nfl_id** | **int** |  | [optional] 
**gsis_id** | **str** |  | [optional] 
**esb_id** | **str** |  | [optional] 
**jersey_number** | **int** |  | [optional] 
**player_name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**headshot** | **str** | URL to player headshot image (contains formatInstructions placeholder) | [optional] 
**position** | [**NextGenStatsPositionEnum**](NextGenStatsPositionEnum.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.passer_stats import PasserStats

# TODO update the JSON string below
json = "{}"
# create an instance of PasserStats from a JSON string
passer_stats_instance = PasserStats.from_json(json)
# print the JSON string representation of the object
print(PasserStats.to_json())

# convert the object into a dict
passer_stats_dict = passer_stats_instance.to_dict()
# create an instance of PasserStats from a dict
passer_stats_from_dict = PasserStats.from_dict(passer_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


