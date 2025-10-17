# Clinched


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
from src.griddy.nfl.models.clinched import Clinched

# TODO update the JSON string below
json = "{}"
# create an instance of Clinched from a JSON string
clinched_instance = Clinched.from_json(json)
# print the JSON string representation of the object
print(Clinched.to_json())

# convert the object into a dict
clinched_dict = clinched_instance.to_dict()
# create an instance of Clinched from a dict
clinched_from_dict = Clinched.from_dict(clinched_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


