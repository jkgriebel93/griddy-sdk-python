# NFLParticipantPlayerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**gsis_id** | **str** | GSIS player ID | [optional] 
**last_name** | **str** |  | [optional] 
**nfl_id** | **int** | NFL player ID | [optional] 
**player_name** | **str** | Full player name | [optional] 
**position** | **str** | Player position | [optional] 
**position_group** | **str** | Position group | [optional] 
**team_id** | **str** | Team ID | [optional] 
**uniform_number** | **str** | Jersey number | [optional] 

## Example

```python
from nfl.models.nfl_participant_player_info import NFLParticipantPlayerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NFLParticipantPlayerInfo from a JSON string
nfl_participant_player_info_instance = NFLParticipantPlayerInfo.from_json(json)
# print the JSON string representation of the object
print(NFLParticipantPlayerInfo.to_json())

# convert the object into a dict
nfl_participant_player_info_dict = nfl_participant_player_info_instance.to_dict()
# create an instance of NFLParticipantPlayerInfo from a dict
nfl_participant_player_info_from_dict = NFLParticipantPlayerInfo.from_dict(nfl_participant_player_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


