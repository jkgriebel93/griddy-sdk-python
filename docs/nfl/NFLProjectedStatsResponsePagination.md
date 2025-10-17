# NFLProjectedStatsResponsePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Token for next page of results | [optional] 

## Example

```python
from nfl.models.nfl_projected_stats_response_pagination import NFLProjectedStatsResponsePagination

# TODO update the JSON string below
json = "{}"
# create an instance of NFLProjectedStatsResponsePagination from a JSON string
nfl_projected_stats_response_pagination_instance = NFLProjectedStatsResponsePagination.from_json(json)
# print the JSON string representation of the object
print(NFLProjectedStatsResponsePagination.to_json())

# convert the object into a dict
nfl_projected_stats_response_pagination_dict = nfl_projected_stats_response_pagination_instance.to_dict()
# create an instance of NFLProjectedStatsResponsePagination from a dict
nfl_projected_stats_response_pagination_from_dict = NFLProjectedStatsResponsePagination.from_dict(nfl_projected_stats_response_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


