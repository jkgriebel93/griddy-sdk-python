# NFLRosterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roster** | [**NFLNFLRosterResponseRoster**](NFLRosterResponseRoster.md) |  | [optional] 
**season** | **int** |  | [optional] 
**team** | [**NFLNFLTeam**](NFLTeam.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_roster_response import NFLRosterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLRosterResponse from a JSON string
nfl_roster_response_instance = NFLRosterResponse.from_json(json)
# print the JSON string representation of the object
print(NFLRosterResponse.to_json())

# convert the object into a dict
nfl_roster_response_dict = nfl_roster_response_instance.to_dict()
# create an instance of NFLRosterResponse from a dict
nfl_roster_response_from_dict = NFLRosterResponse.from_dict(nfl_roster_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


