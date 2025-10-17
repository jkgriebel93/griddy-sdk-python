# NFLPlayByPlayResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_drive** | [**NFLNFLDrive**](NFLDrive.md) |  | [optional] 
**drives** | [**List[NFLNFLDrive]**](NFLDrive.md) |  | [optional] 
**game** | [**NFLNFLGame**](NFLGame.md) |  | [optional] 
**last_play** | [**NFLNFLPlay**](NFLPlay.md) |  | [optional] 
**scoring_summary** | [**List[NFLNFLScoringPlay]**](NFLScoringPlay.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_play_by_play_response import NFLPlayByPlayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPlayByPlayResponse from a JSON string
nfl_play_by_play_response_instance = NFLPlayByPlayResponse.from_json(json)
# print the JSON string representation of the object
print(NFLPlayByPlayResponse.to_json())

# convert the object into a dict
nfl_play_by_play_response_dict = nfl_play_by_play_response_instance.to_dict()
# create an instance of NFLPlayByPlayResponse from a dict
nfl_play_by_play_response_from_dict = NFLPlayByPlayResponse.from_dict(nfl_play_by_play_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


