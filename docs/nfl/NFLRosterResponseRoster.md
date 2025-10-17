# NFLRosterResponseRoster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defense** | [**List[NFLNFLPlayer]**](NFLPlayer.md) |  | [optional] 
**injured_reserve** | [**List[NFLNFLPlayer]**](NFLPlayer.md) |  | [optional] 
**offense** | [**List[NFLNFLPlayer]**](NFLPlayer.md) |  | [optional] 
**practice_squad** | [**List[NFLNFLPlayer]**](NFLPlayer.md) |  | [optional] 
**special_teams** | [**List[NFLNFLPlayer]**](NFLPlayer.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_roster_response_roster import NFLRosterResponseRoster

# TODO update the JSON string below
json = "{}"
# create an instance of NFLRosterResponseRoster from a JSON string
nfl_roster_response_roster_instance = NFLRosterResponseRoster.from_json(json)
# print the JSON string representation of the object
print(NFLRosterResponseRoster.to_json())

# convert the object into a dict
nfl_roster_response_roster_dict = nfl_roster_response_roster_instance.to_dict()
# create an instance of NFLRosterResponseRoster from a dict
nfl_roster_response_roster_from_dict = NFLRosterResponseRoster.from_dict(nfl_roster_response_roster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


