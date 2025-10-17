# NFLProjectedStatsResponseMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**NFLNFLProjectedStatsResponseMetaPage**](NFLProjectedStatsResponseMetaPage.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_projected_stats_response_meta import NFLProjectedStatsResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of NFLProjectedStatsResponseMeta from a JSON string
nfl_projected_stats_response_meta_instance = NFLProjectedStatsResponseMeta.from_json(json)
# print the JSON string representation of the object
print(NFLProjectedStatsResponseMeta.to_json())

# convert the object into a dict
nfl_projected_stats_response_meta_dict = nfl_projected_stats_response_meta_instance.to_dict()
# create an instance of NFLProjectedStatsResponseMeta from a dict
nfl_projected_stats_response_meta_from_dict = NFLProjectedStatsResponseMeta.from_dict(nfl_projected_stats_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


