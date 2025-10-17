# Play


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**distance** | **int** |  | [optional] 
**down** | **int** |  | [optional] 
**game_clock** | **str** |  | [optional] 
**penalties** | [**List[Penalty]**](Penalty.md) |  | [optional] 
**play_id** | **str** |  | [optional] 
**play_number** | **int** |  | [optional] 
**play_type** | [**PlayTypeEnum**](PlayTypeEnum.md) |  | [optional] 
**players** | [**List[PlayParticipant]**](PlayParticipant.md) |  | [optional] 
**quarter** | **int** |  | [optional] 
**result** | **str** |  | [optional] 
**yard_line** | **str** |  | [optional] 
**yards_gained** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.play import Play

# TODO update the JSON string below
json = "{}"
# create an instance of Play from a JSON string
play_instance = Play.from_json(json)
# print the JSON string representation of the object
print(Play.to_json())

# convert the object into a dict
play_dict = play_instance.to_dict()
# create an instance of Play from a dict
play_from_dict = Play.from_dict(play_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


