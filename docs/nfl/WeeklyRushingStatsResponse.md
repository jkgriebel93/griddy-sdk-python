# WeeklyRushingStatsResponse


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
**rushers** | [**List[WeeklyPlayerRushingStats]**](WeeklyPlayerRushingStats.md) |  | [optional] 
**qualified_rusher** | **bool** | Whether results are filtered to qualified rushers only | [optional] 
**team_offense** | **str** | Team filter applied (if any) | [optional] 
**week** | [**WeekSlugEnum**](WeekSlugEnum.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.weekly_rushing_stats_response import WeeklyRushingStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WeeklyRushingStatsResponse from a JSON string
weekly_rushing_stats_response_instance = WeeklyRushingStatsResponse.from_json(json)
# print the JSON string representation of the object
print(WeeklyRushingStatsResponse.to_json())

# convert the object into a dict
weekly_rushing_stats_response_dict = weekly_rushing_stats_response_instance.to_dict()
# create an instance of WeeklyRushingStatsResponse from a dict
weekly_rushing_stats_response_from_dict = WeeklyRushingStatsResponse.from_dict(weekly_rushing_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


