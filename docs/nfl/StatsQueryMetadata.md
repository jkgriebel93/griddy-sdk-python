# StatsQueryMetadata

Common pagination and query metadata for stats responses

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

## Example

```python
from src.griddy.nfl.models.stats_query_metadata import StatsQueryMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of StatsQueryMetadata from a JSON string
stats_query_metadata_instance = StatsQueryMetadata.from_json(json)
# print the JSON string representation of the object
print(StatsQueryMetadata.to_json())

# convert the object into a dict
stats_query_metadata_dict = stats_query_metadata_instance.to_dict()
# create an instance of StatsQueryMetadata from a dict
stats_query_metadata_from_dict = StatsQueryMetadata.from_dict(stats_query_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


