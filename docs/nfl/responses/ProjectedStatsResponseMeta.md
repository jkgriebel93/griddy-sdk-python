# ProjectedStatsResponseMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**ProjectedStatsResponseMetaPage**](ProjectedStatsResponseMetaPage.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.projected_stats_response_meta import ProjectedStatsResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectedStatsResponseMeta from a JSON string
projected_stats_response_meta_instance = ProjectedStatsResponseMeta.from_json(json)
# print the JSON string representation of the object
print(ProjectedStatsResponseMeta.to_json())

# convert the object into a dict
projected_stats_response_meta_dict = projected_stats_response_meta_instance.to_dict()
# create an instance of ProjectedStatsResponseMeta from a dict
projected_stats_response_meta_from_dict = ProjectedStatsResponseMeta.from_dict(projected_stats_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


