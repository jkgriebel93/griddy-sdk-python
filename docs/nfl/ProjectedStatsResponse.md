# ProjectedStatsResponse

JSON:API formatted response for projected statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlayerProjection]**](PlayerProjection.md) | Primary player data with relationships | [optional] 
**included** | [**List[ProjectedStatsResponseIncludedInner]**](ProjectedStatsResponseIncludedInner.md) | Related data included in response | [optional] 
**meta** | [**ProjectedStatsResponseMeta**](ProjectedStatsResponseMeta.md) |  | [optional] 
**pagination** | [**ProjectedStatsResponsePagination**](ProjectedStatsResponsePagination.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.projected_stats_response import ProjectedStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectedStatsResponse from a JSON string
projected_stats_response_instance = ProjectedStatsResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectedStatsResponse.to_json())

# convert the object into a dict
projected_stats_response_dict = projected_stats_response_instance.to_dict()
# create an instance of ProjectedStatsResponse from a dict
projected_stats_response_from_dict = ProjectedStatsResponse.from_dict(projected_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


