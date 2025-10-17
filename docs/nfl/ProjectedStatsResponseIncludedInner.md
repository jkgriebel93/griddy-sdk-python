# ProjectedStatsResponseIncludedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**PlayerWeekProjectedStatsAttributes**](PlayerWeekProjectedStatsAttributes.md) |  | [optional] 
**id** | **str** | Unique identifier for these stats | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.projected_stats_response_included_inner import ProjectedStatsResponseIncludedInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectedStatsResponseIncludedInner from a JSON string
projected_stats_response_included_inner_instance = ProjectedStatsResponseIncludedInner.from_json(json)
# print the JSON string representation of the object
print(ProjectedStatsResponseIncludedInner.to_json())

# convert the object into a dict
projected_stats_response_included_inner_dict = projected_stats_response_included_inner_instance.to_dict()
# create an instance of ProjectedStatsResponseIncludedInner from a dict
projected_stats_response_included_inner_from_dict = ProjectedStatsResponseIncludedInner.from_dict(projected_stats_response_included_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


