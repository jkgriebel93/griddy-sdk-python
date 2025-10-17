# NFLProjectedStatsResponseMetaPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | Current page number | [optional] 
**size** | **int** | Page size | [optional] 

## Example

```python
from nfl.models.nfl_projected_stats_response_meta_page import NFLProjectedStatsResponseMetaPage

# TODO update the JSON string below
json = "{}"
# create an instance of NFLProjectedStatsResponseMetaPage from a JSON string
nfl_projected_stats_response_meta_page_instance = NFLProjectedStatsResponseMetaPage.from_json(json)
# print the JSON string representation of the object
print(NFLProjectedStatsResponseMetaPage.to_json())

# convert the object into a dict
nfl_projected_stats_response_meta_page_dict = nfl_projected_stats_response_meta_page_instance.to_dict()
# create an instance of NFLProjectedStatsResponseMetaPage from a dict
nfl_projected_stats_response_meta_page_from_dict = NFLProjectedStatsResponseMetaPage.from_dict(nfl_projected_stats_response_meta_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


