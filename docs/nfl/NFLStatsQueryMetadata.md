# NFLStatsQueryMetadata

Common pagination and query metadata for stats responses

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

## Example

```python
from nfl.models.nfl_stats_query_metadata import NFLStatsQueryMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of NFLStatsQueryMetadata from a JSON string
nfl_stats_query_metadata_instance = NFLStatsQueryMetadata.from_json(json)
# print the JSON string representation of the object
print(NFLStatsQueryMetadata.to_json())

# convert the object into a dict
nfl_stats_query_metadata_dict = nfl_stats_query_metadata_instance.to_dict()
# create an instance of NFLStatsQueryMetadata from a dict
nfl_stats_query_metadata_from_dict = NFLStatsQueryMetadata.from_dict(nfl_stats_query_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


