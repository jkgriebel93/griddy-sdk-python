# VenueInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_code** | **str** |  | [optional] 
**roof_type** | [**RoofTypeEnum**](RoofTypeEnum.md) |  | [optional] 
**site_city** | **str** |  | [optional] 
**site_full_name** | **str** |  | [optional] 
**site_id** | **int** |  | [optional] 
**site_state** | **str** |  | [optional] 
**smart_id** | **str** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.venue_info import VenueInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VenueInfo from a JSON string
venue_info_instance = VenueInfo.from_json(json)
# print the JSON string representation of the object
print(VenueInfo.to_json())

# convert the object into a dict
venue_info_dict = venue_info_instance.to_dict()
# create an instance of VenueInfo from a dict
venue_info_from_dict = VenueInfo.from_dict(venue_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


