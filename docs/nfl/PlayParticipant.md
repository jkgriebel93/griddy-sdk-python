# PlayParticipant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | [**Player**](Player.md) |  | [optional] 
**role** | [**PlayParticipantRoleEnum**](PlayParticipantRoleEnum.md) |  | [optional] 
**stats** | **object** | Play-specific statistics | [optional] 

## Example

```python
from src.griddy.nfl.models.play_participant import PlayParticipant

# TODO update the JSON string below
json = "{}"
# create an instance of PlayParticipant from a JSON string
play_participant_instance = PlayParticipant.from_json(json)
# print the JSON string representation of the object
print(PlayParticipant.to_json())

# convert the object into a dict
play_participant_dict = play_participant_instance.to_dict()
# create an instance of PlayParticipant from a dict
play_participant_from_dict = PlayParticipant.from_dict(play_participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


