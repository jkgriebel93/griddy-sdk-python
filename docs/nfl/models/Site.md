# Site

Stadium or venue information for a game

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_code** | **str** |  | [optional] 
**roof_type** | [**RoofTypeEnum**](RoofTypeEnum.md) |  | [optional] 
**site_city** | **str** |  | [optional] 
**site_full_name** | **str** | Stadium name | [optional] 
**site_id** | **int** |  | [optional] 
**site_state** | **str** |  | [optional] 
**smart_id** | **str** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.site import Site

# TODO update the JSON string below
json = "{}"
# create an instance of Site from a JSON string
site_instance = Site.from_json(json)
# print the JSON string representation of the object
print(Site.to_json())

# convert the object into a dict
site_dict = site_instance.to_dict()
# create an instance of Site from a dict
site_from_dict = Site.from_dict(site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


