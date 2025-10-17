# NFLReplayIds

Related entity identifiers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**away_team_id** | **str** |  | [optional] 
**game_id** | **str** |  | [optional] 
**home_team_id** | **str** |  | [optional] 
**play_id** | **str** |  | [optional] 

## Example

```python
from nfl.models.nfl_replay_ids import NFLReplayIds

# TODO update the JSON string below
json = "{}"
# create an instance of NFLReplayIds from a JSON string
nfl_replay_ids_instance = NFLReplayIds.from_json(json)
# print the JSON string representation of the object
print(NFLReplayIds.to_json())

# convert the object into a dict
nfl_replay_ids_dict = nfl_replay_ids_instance.to_dict()
# create an instance of NFLReplayIds from a dict
nfl_replay_ids_from_dict = NFLReplayIds.from_dict(nfl_replay_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


