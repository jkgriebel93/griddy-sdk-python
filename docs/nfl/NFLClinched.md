# NFLClinched


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bye** | **bool** | Clinched first-round bye | [optional] 
**division** | **bool** | Clinched division title | [optional] 
**eliminated** | **bool** | Eliminated from playoff contention | [optional] 
**home_field** | **bool** | Clinched home field advantage | [optional] 
**playoff** | **bool** | Clinched playoff berth | [optional] 
**wild_card** | **bool** | Clinched wild card berth | [optional] 

## Example

```python
from nfl.models.nfl_clinched import NFLClinched

# TODO update the JSON string below
json = "{}"
# create an instance of NFLClinched from a JSON string
nfl_clinched_instance = NFLClinched.from_json(json)
# print the JSON string representation of the object
print(NFLClinched.to_json())

# convert the object into a dict
nfl_clinched_dict = nfl_clinched_instance.to_dict()
# create an instance of NFLClinched from a dict
nfl_clinched_from_dict = NFLClinched.from_dict(nfl_clinched_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


