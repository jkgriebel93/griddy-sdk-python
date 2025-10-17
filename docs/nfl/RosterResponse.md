# RosterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roster** | [**RosterResponseRoster**](RosterResponseRoster.md) |  | [optional] 
**season** | **int** |  | [optional] 
**team** | [**Team**](Team.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.roster_response import RosterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RosterResponse from a JSON string
roster_response_instance = RosterResponse.from_json(json)
# print the JSON string representation of the object
print(RosterResponse.to_json())

# convert the object into a dict
roster_response_dict = roster_response_instance.to_dict()
# create an instance of RosterResponse from a dict
roster_response_from_dict = RosterResponse.from_dict(roster_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


