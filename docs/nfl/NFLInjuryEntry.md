# NFLInjuryEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_status** | [**NFLNFLInjuredPlayerGameStatusEnum**](NFLInjuredPlayerGameStatusEnum.md) |  | [optional] 
**injury** | **str** | Injury description | [optional] 
**player** | [**NFLNFLPlayer**](NFLPlayer.md) |  | [optional] 
**practice_status** | [**NFLNFLInjuryEntryPracticeStatus**](NFLInjuryEntryPracticeStatus.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_injury_entry import NFLInjuryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of NFLInjuryEntry from a JSON string
nfl_injury_entry_instance = NFLInjuryEntry.from_json(json)
# print the JSON string representation of the object
print(NFLInjuryEntry.to_json())

# convert the object into a dict
nfl_injury_entry_dict = nfl_injury_entry_instance.to_dict()
# create an instance of NFLInjuryEntry from a dict
nfl_injury_entry_from_dict = NFLInjuryEntry.from_dict(nfl_injury_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


