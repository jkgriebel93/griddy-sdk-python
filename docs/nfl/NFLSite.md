# NFLSite

Stadium or venue information for a game

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_code** | **str** |  | [optional] 
**roof_type** | [**NFLNFLRoofTypeEnum**](NFLRoofTypeEnum.md) |  | [optional] 
**site_city** | **str** |  | [optional] 
**site_full_name** | **str** | Stadium name | [optional] 
**site_id** | **int** |  | [optional] 
**site_state** | **str** |  | [optional] 
**smart_id** | **str** |  | [optional] 

## Example

```python
from nfl.models.nfl_site import NFLSite

# TODO update the JSON string below
json = "{}"
# create an instance of NFLSite from a JSON string
nfl_site_instance = NFLSite.from_json(json)
# print the JSON string representation of the object
print(NFLSite.to_json())

# convert the object into a dict
nfl_site_dict = nfl_site_instance.to_dict()
# create an instance of NFLSite from a dict
nfl_site_from_dict = NFLSite.from_dict(nfl_site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


