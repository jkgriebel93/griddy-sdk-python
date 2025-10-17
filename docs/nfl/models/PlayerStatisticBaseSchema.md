# PlayerStatisticBaseSchema


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

## Example

```python
from src.griddy.nfl.models.player_statistic_base_schema import PlayerStatisticBaseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerStatisticBaseSchema from a JSON string
player_statistic_base_schema_instance = PlayerStatisticBaseSchema.from_json(json)
# print the JSON string representation of the object
print(PlayerStatisticBaseSchema.to_json())

# convert the object into a dict
player_statistic_base_schema_dict = player_statistic_base_schema_instance.to_dict()
# create an instance of PlayerStatisticBaseSchema from a dict
player_statistic_base_schema_from_dict = PlayerStatisticBaseSchema.from_dict(player_statistic_base_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


