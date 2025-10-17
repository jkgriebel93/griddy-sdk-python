# BoxscoreTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbr** | **str** |  | [optional] 
**city_state** | **str** |  | [optional] 
**conference_abbr** | [**ConferenceEnum**](ConferenceEnum.md) |  | [optional] 
**division_abbr** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**nick** | **str** |  | [optional] 
**smart_id** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**team_type** | [**TeamTypeEnum**](TeamTypeEnum.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.boxscore_team import BoxscoreTeam

# TODO update the JSON string below
json = "{}"
# create an instance of BoxscoreTeam from a JSON string
boxscore_team_instance = BoxscoreTeam.from_json(json)
# print the JSON string representation of the object
print(BoxscoreTeam.to_json())

# convert the object into a dict
boxscore_team_dict = boxscore_team_instance.to_dict()
# create an instance of BoxscoreTeam from a dict
boxscore_team_from_dict = BoxscoreTeam.from_dict(boxscore_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


