# NFLBoxscoreTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbr** | **str** |  | [optional] 
**city_state** | **str** |  | [optional] 
**conference_abbr** | [**NFLNFLConferenceEnum**](NFLConferenceEnum.md) |  | [optional] 
**division_abbr** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**nick** | **str** |  | [optional] 
**smart_id** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**team_type** | [**NFLNFLTeamTypeEnum**](NFLTeamTypeEnum.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_boxscore_team import NFLBoxscoreTeam

# TODO update the JSON string below
json = "{}"
# create an instance of NFLBoxscoreTeam from a JSON string
nfl_boxscore_team_instance = NFLBoxscoreTeam.from_json(json)
# print the JSON string representation of the object
print(NFLBoxscoreTeam.to_json())

# convert the object into a dict
nfl_boxscore_team_dict = nfl_boxscore_team_instance.to_dict()
# create an instance of NFLBoxscoreTeam from a dict
nfl_boxscore_team_from_dict = NFLBoxscoreTeam.from_dict(nfl_boxscore_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


