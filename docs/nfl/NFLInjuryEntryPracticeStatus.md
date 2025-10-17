# NFLInjuryEntryPracticeStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**friday** | [**NFLNFLPracticeStatusEnum**](NFLPracticeStatusEnum.md) |  | [optional] 
**thursday** | [**NFLNFLPracticeStatusEnum**](NFLPracticeStatusEnum.md) |  | [optional] 
**wednesday** | [**NFLNFLPracticeStatusEnum**](NFLPracticeStatusEnum.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_injury_entry_practice_status import NFLInjuryEntryPracticeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NFLInjuryEntryPracticeStatus from a JSON string
nfl_injury_entry_practice_status_instance = NFLInjuryEntryPracticeStatus.from_json(json)
# print the JSON string representation of the object
print(NFLInjuryEntryPracticeStatus.to_json())

# convert the object into a dict
nfl_injury_entry_practice_status_dict = nfl_injury_entry_practice_status_instance.to_dict()
# create an instance of NFLInjuryEntryPracticeStatus from a dict
nfl_injury_entry_practice_status_from_dict = NFLInjuryEntryPracticeStatus.from_dict(nfl_injury_entry_practice_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


