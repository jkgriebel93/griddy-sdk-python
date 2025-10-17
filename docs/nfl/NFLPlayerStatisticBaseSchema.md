# NFLPlayerStatisticBaseSchema


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

## Example

```python
from nfl.models.nfl_player_statistic_base_schema import NFLPlayerStatisticBaseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPlayerStatisticBaseSchema from a JSON string
nfl_player_statistic_base_schema_instance = NFLPlayerStatisticBaseSchema.from_json(json)
# print the JSON string representation of the object
print(NFLPlayerStatisticBaseSchema.to_json())

# convert the object into a dict
nfl_player_statistic_base_schema_dict = nfl_player_statistic_base_schema_instance.to_dict()
# create an instance of NFLPlayerStatisticBaseSchema from a dict
nfl_player_statistic_base_schema_from_dict = NFLPlayerStatisticBaseSchema.from_dict(nfl_player_statistic_base_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


