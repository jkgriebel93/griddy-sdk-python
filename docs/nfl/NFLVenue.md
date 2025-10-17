# NFLVenue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Street address | [optional] 
**city** | **str** | City name | [optional] 
**country** | **str** | Country name | [optional] 
**id** | **str** | Unique venue identifier | [optional] 
**name** | **str** | Venue name | [optional] 
**postal_code** | **str** | Postal/ZIP code | [optional] 
**territory** | **str** | State or territory code | [optional] 

## Example

```python
from nfl.models.nfl_venue import NFLVenue

# TODO update the JSON string below
json = "{}"
# create an instance of NFLVenue from a JSON string
nfl_venue_instance = NFLVenue.from_json(json)
# print the JSON string representation of the object
print(NFLVenue.to_json())

# convert the object into a dict
nfl_venue_dict = nfl_venue_instance.to_dict()
# create an instance of NFLVenue from a dict
nfl_venue_from_dict = NFLVenue.from_dict(nfl_venue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


