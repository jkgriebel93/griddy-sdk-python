# Penalty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted** | **bool** |  | [optional] 
**no_play** | **bool** |  | [optional] 
**player** | [**Player**](Player.md) |  | [optional] 
**team** | [**Team**](Team.md) |  | [optional] 
**type** | **str** |  | [optional] 
**yards** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.penalty import Penalty

# TODO update the JSON string below
json = "{}"
# create an instance of Penalty from a JSON string
penalty_instance = Penalty.from_json(json)
# print the JSON string representation of the object
print(Penalty.to_json())

# convert the object into a dict
penalty_dict = penalty_instance.to_dict()
# create an instance of Penalty from a dict
penalty_from_dict = Penalty.from_dict(penalty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


