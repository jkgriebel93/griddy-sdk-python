# ProjectedStatsResponseMetaPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | Current page number | [optional] 
**size** | **int** | Page size | [optional] 

## Example

```python
from src.griddy.nfl.models.projected_stats_response_meta_page import ProjectedStatsResponseMetaPage

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectedStatsResponseMetaPage from a JSON string
projected_stats_response_meta_page_instance = ProjectedStatsResponseMetaPage.from_json(json)
# print the JSON string representation of the object
print(ProjectedStatsResponseMetaPage.to_json())

# convert the object into a dict
projected_stats_response_meta_page_dict = projected_stats_response_meta_page_instance.to_dict()
# create an instance of ProjectedStatsResponseMetaPage from a dict
projected_stats_response_meta_page_from_dict = ProjectedStatsResponseMetaPage.from_dict(projected_stats_response_meta_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


