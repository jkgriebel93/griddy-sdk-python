# Award


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**award_type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**year** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.award import Award

# TODO update the JSON string below
json = "{}"
# create an instance of Award from a JSON string
award_instance = Award.from_json(json)
# print the JSON string representation of the object
print(Award.to_json())

# convert the object into a dict
award_dict = award_instance.to_dict()
# create an instance of Award from a dict
award_from_dict = Award.from_dict(award_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


