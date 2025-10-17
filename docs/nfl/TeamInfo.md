# TeamInfo

Basic team information included in roster responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbr** | **str** |  | [optional] 
**city_state** | **str** |  | [optional] 
**conference** | [**Conference**](Conference.md) |  | [optional] 
**conference_abbr** | [**ConferenceEnum**](ConferenceEnum.md) |  | [optional] 
**division** | [**Division**](Division.md) |  | [optional] 
**full_name** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**nick** | **str** |  | [optional] 
**season** | **int** |  | [optional] 
**smart_id** | **str** |  | [optional] 
**stadium_name** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**team_site_ticket_url** | **str** |  | [optional] 
**team_site_url** | **str** |  | [optional] 
**team_type** | [**TeamTypeEnum**](TeamTypeEnum.md) |  | [optional] 
**ticket_phone_number** | **str** |  | [optional] 
**year_found** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.team_info import TeamInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TeamInfo from a JSON string
team_info_instance = TeamInfo.from_json(json)
# print the JSON string representation of the object
print(TeamInfo.to_json())

# convert the object into a dict
team_info_dict = team_info_instance.to_dict()
# create an instance of TeamInfo from a dict
team_info_from_dict = TeamInfo.from_dict(team_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


