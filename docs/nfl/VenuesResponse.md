# VenuesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**venues** | [**List[Venue]**](Venue.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.venues_response import VenuesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VenuesResponse from a JSON string
venues_response_instance = VenuesResponse.from_json(json)
# print the JSON string representation of the object
print(VenuesResponse.to_json())

# convert the object into a dict
venues_response_dict = venues_response_instance.to_dict()
# create an instance of VenuesResponse from a dict
venues_response_from_dict = VenuesResponse.from_dict(venues_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


