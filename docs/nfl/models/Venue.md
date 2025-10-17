# Venue


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
from src.griddy.nfl.models.venue import Venue

# TODO update the JSON string below
json = "{}"
# create an instance of Venue from a JSON string
venue_instance = Venue.from_json(json)
# print the JSON string representation of the object
print(Venue.to_json())

# convert the object into a dict
venue_dict = venue_instance.to_dict()
# create an instance of Venue from a dict
venue_from_dict = Venue.from_dict(venue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


