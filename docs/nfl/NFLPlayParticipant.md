# NFLPlayParticipant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | [**NFLNFLPlayer**](NFLPlayer.md) |  | [optional] 
**role** | [**NFLNFLPlayParticipantRoleEnum**](NFLPlayParticipantRoleEnum.md) |  | [optional] 
**stats** | **object** | Play-specific statistics | [optional] 

## Example

```python
from nfl.models.nfl_play_participant import NFLPlayParticipant

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPlayParticipant from a JSON string
nfl_play_participant_instance = NFLPlayParticipant.from_json(json)
# print the JSON string representation of the object
print(NFLPlayParticipant.to_json())

# convert the object into a dict
nfl_play_participant_dict = nfl_play_participant_instance.to_dict()
# create an instance of NFLPlayParticipant from a dict
nfl_play_participant_from_dict = NFLPlayParticipant.from_dict(nfl_play_participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


