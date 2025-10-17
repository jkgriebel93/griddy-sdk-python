# NFLPlay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**distance** | **int** |  | [optional] 
**down** | **int** |  | [optional] 
**game_clock** | **str** |  | [optional] 
**penalties** | [**List[NFLNFLPenalty]**](NFLPenalty.md) |  | [optional] 
**play_id** | **str** |  | [optional] 
**play_number** | **int** |  | [optional] 
**play_type** | [**NFLNFLPlayTypeEnum**](NFLPlayTypeEnum.md) |  | [optional] 
**players** | [**List[NFLNFLPlayParticipant]**](NFLPlayParticipant.md) |  | [optional] 
**quarter** | **int** |  | [optional] 
**result** | **str** |  | [optional] 
**yard_line** | **str** |  | [optional] 
**yards_gained** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_play import NFLPlay

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPlay from a JSON string
nfl_play_instance = NFLPlay.from_json(json)
# print the JSON string representation of the object
print(NFLPlay.to_json())

# convert the object into a dict
nfl_play_dict = nfl_play_instance.to_dict()
# create an instance of NFLPlay from a dict
nfl_play_from_dict = NFLPlay.from_dict(nfl_play_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


