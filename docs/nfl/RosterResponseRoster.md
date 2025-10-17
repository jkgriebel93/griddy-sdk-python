# RosterResponseRoster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defense** | [**List[Player]**](Player.md) |  | [optional] 
**injured_reserve** | [**List[Player]**](Player.md) |  | [optional] 
**offense** | [**List[Player]**](Player.md) |  | [optional] 
**practice_squad** | [**List[Player]**](Player.md) |  | [optional] 
**special_teams** | [**List[Player]**](Player.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.roster_response_roster import RosterResponseRoster

# TODO update the JSON string below
json = "{}"
# create an instance of RosterResponseRoster from a JSON string
roster_response_roster_instance = RosterResponseRoster.from_json(json)
# print the JSON string representation of the object
print(RosterResponseRoster.to_json())

# convert the object into a dict
roster_response_roster_dict = roster_response_roster_instance.to_dict()
# create an instance of RosterResponseRoster from a dict
roster_response_roster_from_dict = RosterResponseRoster.from_dict(roster_response_roster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


