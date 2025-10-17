# NFLDivision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbr** | **str** | Division abbreviation | [optional] 
**full_name** | **str** | Full division name | [optional] 
**id** | **str** | Division identifier | [optional] 

## Example

```python
from nfl.models.nfl_division import NFLDivision

# TODO update the JSON string below
json = "{}"
# create an instance of NFLDivision from a JSON string
nfl_division_instance = NFLDivision.from_json(json)
# print the JSON string representation of the object
print(NFLDivision.to_json())

# convert the object into a dict
nfl_division_dict = nfl_division_instance.to_dict()
# create an instance of NFLDivision from a dict
nfl_division_from_dict = NFLDivision.from_dict(nfl_division_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


