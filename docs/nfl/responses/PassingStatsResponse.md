# PassingStatsResponse


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
**passers** | [**List[PlayerPassingStats]**](PlayerPassingStats.md) |  | [optional] 
**qualified_passer** | **bool** | Whether results are filtered to qualified passers only | [optional] 

## Example

```python
from src.griddy.nfl.models.passing_stats_response import PassingStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PassingStatsResponse from a JSON string
passing_stats_response_instance = PassingStatsResponse.from_json(json)
# print the JSON string representation of the object
print(PassingStatsResponse.to_json())

# convert the object into a dict
passing_stats_response_dict = passing_stats_response_instance.to_dict()
# create an instance of PassingStatsResponse from a dict
passing_stats_response_from_dict = PassingStatsResponse.from_dict(passing_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


