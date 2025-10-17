# Division


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbr** | **str** | Division abbreviation | [optional] 
**full_name** | **str** | Full division name | [optional] 
**id** | **str** | Division identifier | [optional] 

## Example

```python
from src.griddy.nfl.models.division import Division

# TODO update the JSON string below
json = "{}"
# create an instance of Division from a JSON string
division_instance = Division.from_json(json)
# print the JSON string representation of the object
print(Division.to_json())

# convert the object into a dict
division_dict = division_instance.to_dict()
# create an instance of Division from a dict
division_from_dict = Division.from_dict(division_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


