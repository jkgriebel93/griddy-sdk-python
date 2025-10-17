# NFLPassingStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Maximum number of results returned | [optional] 
**offset** | **int** | Number of records skipped | [optional] 
**season** | **int** | Season year | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**sort_key** | **str** | Field used for sorting | [optional] 
**sort_value** | [**NFLNFLSortOrderEnum**](NFLSortOrderEnum.md) |  | [optional] 
**total** | **int** | Total number of items matching the criteria | [optional] 
**passers** | [**List[NFLNFLPlayerPassingStats]**](NFLPlayerPassingStats.md) |  | [optional] 
**qualified_passer** | **bool** | Whether results are filtered to qualified passers only | [optional] 

## Example

```python
from nfl.models.nfl_passing_stats_response import NFLPassingStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPassingStatsResponse from a JSON string
nfl_passing_stats_response_instance = NFLPassingStatsResponse.from_json(json)
# print the JSON string representation of the object
print(NFLPassingStatsResponse.to_json())

# convert the object into a dict
nfl_passing_stats_response_dict = nfl_passing_stats_response_instance.to_dict()
# create an instance of NFLPassingStatsResponse from a dict
nfl_passing_stats_response_from_dict = NFLPassingStatsResponse.from_dict(nfl_passing_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


