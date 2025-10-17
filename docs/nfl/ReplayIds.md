# ReplayIds

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
from src.griddy.nfl.models.replay_ids import ReplayIds

# TODO update the JSON string below
json = "{}"
# create an instance of ReplayIds from a JSON string
replay_ids_instance = ReplayIds.from_json(json)
# print the JSON string representation of the object
print(ReplayIds.to_json())

# convert the object into a dict
replay_ids_dict = replay_ids_instance.to_dict()
# create an instance of ReplayIds from a dict
replay_ids_from_dict = ReplayIds.from_dict(replay_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


