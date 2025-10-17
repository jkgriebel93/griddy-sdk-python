# WeeklyPassingStatsResponse


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
**passers** | [**List[WeeklyPlayerPassingStats]**](WeeklyPlayerPassingStats.md) |  | [optional] 
**qualified_passer** | **bool** | Whether results are filtered to qualified passers only | [optional] 
**team_offense** | **str** | Team filter applied (if any) | [optional] 
**week** | **str** | Week identifier | [optional] 

## Example

```python
from src.griddy.nfl.models.weekly_passing_stats_response import WeeklyPassingStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WeeklyPassingStatsResponse from a JSON string
weekly_passing_stats_response_instance = WeeklyPassingStatsResponse.from_json(json)
# print the JSON string representation of the object
print(WeeklyPassingStatsResponse.to_json())

# convert the object into a dict
weekly_passing_stats_response_dict = weekly_passing_stats_response_instance.to_dict()
# create an instance of WeeklyPassingStatsResponse from a dict
weekly_passing_stats_response_from_dict = WeeklyPassingStatsResponse.from_dict(weekly_passing_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


