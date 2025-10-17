# DefensiveStatsResponse


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
**defenders** | [**List[DefensivePlayerStats]**](DefensivePlayerStats.md) |  | [optional] 
**qualified_defender** | **bool** | Whether results are filtered to qualified defenders only | [optional] 

## Example

```python
from src.griddy.nfl.models.defensive_stats_response import DefensiveStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DefensiveStatsResponse from a JSON string
defensive_stats_response_instance = DefensiveStatsResponse.from_json(json)
# print the JSON string representation of the object
print(DefensiveStatsResponse.to_json())

# convert the object into a dict
defensive_stats_response_dict = defensive_stats_response_instance.to_dict()
# create an instance of DefensiveStatsResponse from a dict
defensive_stats_response_from_dict = DefensiveStatsResponse.from_dict(defensive_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


