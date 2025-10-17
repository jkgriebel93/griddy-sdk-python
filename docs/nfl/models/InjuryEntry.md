# InjuryEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_status** | [**InjuredPlayerGameStatusEnum**](InjuredPlayerGameStatusEnum.md) |  | [optional] 
**injury** | **str** | Injury description | [optional] 
**player** | [**Player**](Player.md) |  | [optional] 
**practice_status** | [**InjuryEntryPracticeStatus**](InjuryEntryPracticeStatus.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.injury_entry import InjuryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of InjuryEntry from a JSON string
injury_entry_instance = InjuryEntry.from_json(json)
# print the JSON string representation of the object
print(InjuryEntry.to_json())

# convert the object into a dict
injury_entry_dict = injury_entry_instance.to_dict()
# create an instance of InjuryEntry from a dict
injury_entry_from_dict = InjuryEntry.from_dict(injury_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


