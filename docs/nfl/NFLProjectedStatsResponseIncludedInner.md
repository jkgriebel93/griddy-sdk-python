# NFLProjectedStatsResponseIncludedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**NFLNFLPlayerWeekProjectedStatsAttributes**](NFLPlayerWeekProjectedStatsAttributes.md) |  | [optional] 
**id** | **str** | Unique identifier for these stats | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from nfl.models.nfl_projected_stats_response_included_inner import NFLProjectedStatsResponseIncludedInner

# TODO update the JSON string below
json = "{}"
# create an instance of NFLProjectedStatsResponseIncludedInner from a JSON string
nfl_projected_stats_response_included_inner_instance = NFLProjectedStatsResponseIncludedInner.from_json(json)
# print the JSON string representation of the object
print(NFLProjectedStatsResponseIncludedInner.to_json())

# convert the object into a dict
nfl_projected_stats_response_included_inner_dict = nfl_projected_stats_response_included_inner_instance.to_dict()
# create an instance of NFLProjectedStatsResponseIncludedInner from a dict
nfl_projected_stats_response_included_inner_from_dict = NFLProjectedStatsResponseIncludedInner.from_dict(nfl_projected_stats_response_included_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


