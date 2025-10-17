# ProjectedStatsResponsePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Token for next page of results | [optional] 

## Example

```python
from src.griddy.nfl.models.projected_stats_response_pagination import ProjectedStatsResponsePagination

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectedStatsResponsePagination from a JSON string
projected_stats_response_pagination_instance = ProjectedStatsResponsePagination.from_json(json)
# print the JSON string representation of the object
print(ProjectedStatsResponsePagination.to_json())

# convert the object into a dict
projected_stats_response_pagination_dict = projected_stats_response_pagination_instance.to_dict()
# create an instance of ProjectedStatsResponsePagination from a dict
projected_stats_response_pagination_from_dict = ProjectedStatsResponsePagination.from_dict(projected_stats_response_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


