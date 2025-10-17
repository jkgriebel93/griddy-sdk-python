# NFLProjectedStatsResponse

JSON:API formatted response for projected statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NFLNFLPlayerProjection]**](NFLPlayerProjection.md) | Primary player data with relationships | [optional] 
**included** | [**List[NFLNFLProjectedStatsResponseIncludedInner]**](NFLProjectedStatsResponseIncludedInner.md) | Related data included in response | [optional] 
**meta** | [**NFLNFLProjectedStatsResponseMeta**](NFLProjectedStatsResponseMeta.md) |  | [optional] 
**pagination** | [**NFLNFLProjectedStatsResponsePagination**](NFLProjectedStatsResponsePagination.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_projected_stats_response import NFLProjectedStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLProjectedStatsResponse from a JSON string
nfl_projected_stats_response_instance = NFLProjectedStatsResponse.from_json(json)
# print the JSON string representation of the object
print(NFLProjectedStatsResponse.to_json())

# convert the object into a dict
nfl_projected_stats_response_dict = nfl_projected_stats_response_instance.to_dict()
# create an instance of NFLProjectedStatsResponse from a dict
nfl_projected_stats_response_from_dict = NFLProjectedStatsResponse.from_dict(nfl_projected_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


