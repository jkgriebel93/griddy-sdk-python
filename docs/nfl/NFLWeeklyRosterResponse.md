# NFLWeeklyRosterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** | Season year | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 
**team** | [**NFLNFLTeamInfo**](NFLTeamInfo.md) |  | [optional] 
**team_players** | [**List[NFLNFLWeeklyPlayer]**](NFLWeeklyPlayer.md) |  | [optional] 
**week** | **int** | Week number | [optional] 

## Example

```python
from nfl.models.nfl_weekly_roster_response import NFLWeeklyRosterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLWeeklyRosterResponse from a JSON string
nfl_weekly_roster_response_instance = NFLWeeklyRosterResponse.from_json(json)
# print the JSON string representation of the object
print(NFLWeeklyRosterResponse.to_json())

# convert the object into a dict
nfl_weekly_roster_response_dict = nfl_weekly_roster_response_instance.to_dict()
# create an instance of NFLWeeklyRosterResponse from a dict
nfl_weekly_roster_response_from_dict = NFLWeeklyRosterResponse.from_dict(nfl_weekly_roster_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


