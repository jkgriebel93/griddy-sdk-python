# RushingStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Maximum number of results returned | [optional] 
**offset** | **int** | Number of records skipped | [optional] 
**season** | **int** | Season year | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**sort_key** | **str** | Field used for sorting | [optional] 
**sort_value** | [**SortOrderEnum**](SortOrderEnum.md) |  | [optional] 
**total** | **int** | Total number of items matching the criteria | [optional] 
**rushers** | [**List[PlayerRushingStats]**](PlayerRushingStats.md) |  | [optional] 
**qualified_rusher** | **bool** | Whether results are filtered to qualified rushers only | [optional] 
**team_offense** | **str** | Team filter applied (if any) | [optional] 

## Example

```python
from src.griddy.nfl.models.rushing_stats_response import RushingStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RushingStatsResponse from a JSON string
rushing_stats_response_instance = RushingStatsResponse.from_json(json)
# print the JSON string representation of the object
print(RushingStatsResponse.to_json())

# convert the object into a dict
rushing_stats_response_dict = rushing_stats_response_instance.to_dict()
# create an instance of RushingStatsResponse from a dict
rushing_stats_response_from_dict = RushingStatsResponse.from_dict(rushing_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


