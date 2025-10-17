# NFLExternalId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID in external system | [optional] 
**source** | **str** | External system name | [optional] 

## Example

```python
from nfl.models.nfl_external_id import NFLExternalId

# TODO update the JSON string below
json = "{}"
# create an instance of NFLExternalId from a JSON string
nfl_external_id_instance = NFLExternalId.from_json(json)
# print the JSON string representation of the object
print(NFLExternalId.to_json())

# convert the object into a dict
nfl_external_id_dict = nfl_external_id_instance.to_dict()
# create an instance of NFLExternalId from a dict
nfl_external_id_from_dict = NFLExternalId.from_dict(nfl_external_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


