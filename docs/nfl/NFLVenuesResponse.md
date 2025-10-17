# NFLVenuesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**NFLNFLPagination**](NFLPagination.md) |  | [optional] 
**venues** | [**List[NFLNFLVenue]**](NFLVenue.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_venues_response import NFLVenuesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLVenuesResponse from a JSON string
nfl_venues_response_instance = NFLVenuesResponse.from_json(json)
# print the JSON string representation of the object
print(NFLVenuesResponse.to_json())

# convert the object into a dict
nfl_venues_response_dict = nfl_venues_response_instance.to_dict()
# create an instance of NFLVenuesResponse from a dict
nfl_venues_response_from_dict = NFLVenuesResponse.from_dict(nfl_venues_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


