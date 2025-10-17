# NFLTeamInfo

Basic team information included in roster responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbr** | **str** |  | [optional] 
**city_state** | **str** |  | [optional] 
**conference** | [**NFLNFLConference**](NFLConference.md) |  | [optional] 
**conference_abbr** | [**NFLNFLConferenceEnum**](NFLConferenceEnum.md) |  | [optional] 
**division** | [**NFLNFLDivision**](NFLDivision.md) |  | [optional] 
**full_name** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**nick** | **str** |  | [optional] 
**season** | **int** |  | [optional] 
**smart_id** | **str** |  | [optional] 
**stadium_name** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**team_site_ticket_url** | **str** |  | [optional] 
**team_site_url** | **str** |  | [optional] 
**team_type** | [**NFLNFLTeamTypeEnum**](NFLTeamTypeEnum.md) |  | [optional] 
**ticket_phone_number** | **str** |  | [optional] 
**year_found** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_team_info import NFLTeamInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NFLTeamInfo from a JSON string
nfl_team_info_instance = NFLTeamInfo.from_json(json)
# print the JSON string representation of the object
print(NFLTeamInfo.to_json())

# convert the object into a dict
nfl_team_info_dict = nfl_team_info_instance.to_dict()
# create an instance of NFLTeamInfo from a dict
nfl_team_info_from_dict = NFLTeamInfo.from_dict(nfl_team_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


