# ReceivingStatsResponse


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
**receivers** | [**List[PlayerReceivingStats]**](PlayerReceivingStats.md) |  | [optional] 
**qualified_receiver** | **bool** | Whether results are filtered to qualified receivers only | [optional] 
**team_offense** | **str** | Team filter applied (if any) | [optional] 
**week** | [**WeekSlugEnum**](WeekSlugEnum.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.receiving_stats_response import ReceivingStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReceivingStatsResponse from a JSON string
receiving_stats_response_instance = ReceivingStatsResponse.from_json(json)
# print the JSON string representation of the object
print(ReceivingStatsResponse.to_json())

# convert the object into a dict
receiving_stats_response_dict = receiving_stats_response_instance.to_dict()
# create an instance of ReceivingStatsResponse from a dict
receiving_stats_response_from_dict = ReceivingStatsResponse.from_dict(receiving_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


