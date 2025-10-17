# NFLTeamRosterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** | Season year | [optional] 
**team** | [**NFLNFLTeamInfo**](NFLTeamInfo.md) |  | [optional] 
**team_players** | [**List[NFLNFLPlayer]**](NFLPlayer.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_team_roster_response import NFLTeamRosterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLTeamRosterResponse from a JSON string
nfl_team_roster_response_instance = NFLTeamRosterResponse.from_json(json)
# print the JSON string representation of the object
print(NFLTeamRosterResponse.to_json())

# convert the object into a dict
nfl_team_roster_response_dict = nfl_team_roster_response_instance.to_dict()
# create an instance of NFLTeamRosterResponse from a dict
nfl_team_roster_response_from_dict = NFLTeamRosterResponse.from_dict(nfl_team_roster_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


