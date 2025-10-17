# NFLPenalty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted** | **bool** |  | [optional] 
**no_play** | **bool** |  | [optional] 
**player** | [**NFLNFLPlayer**](NFLPlayer.md) |  | [optional] 
**team** | [**NFLNFLTeam**](NFLTeam.md) |  | [optional] 
**type** | **str** |  | [optional] 
**yards** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_penalty import NFLPenalty

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPenalty from a JSON string
nfl_penalty_instance = NFLPenalty.from_json(json)
# print the JSON string representation of the object
print(NFLPenalty.to_json())

# convert the object into a dict
nfl_penalty_dict = nfl_penalty_instance.to_dict()
# create an instance of NFLPenalty from a dict
nfl_penalty_from_dict = NFLPenalty.from_dict(nfl_penalty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


