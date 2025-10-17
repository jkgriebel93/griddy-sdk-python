# NFLVenueInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_code** | **str** |  | [optional] 
**roof_type** | [**NFLNFLRoofTypeEnum**](NFLRoofTypeEnum.md) |  | [optional] 
**site_city** | **str** |  | [optional] 
**site_full_name** | **str** |  | [optional] 
**site_id** | **int** |  | [optional] 
**site_state** | **str** |  | [optional] 
**smart_id** | **str** |  | [optional] 

## Example

```python
from nfl.models.nfl_venue_info import NFLVenueInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NFLVenueInfo from a JSON string
nfl_venue_info_instance = NFLVenueInfo.from_json(json)
# print the JSON string representation of the object
print(NFLVenueInfo.to_json())

# convert the object into a dict
nfl_venue_info_dict = nfl_venue_info_instance.to_dict()
# create an instance of NFLVenueInfo from a dict
nfl_venue_info_from_dict = NFLVenueInfo.from_dict(nfl_venue_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


