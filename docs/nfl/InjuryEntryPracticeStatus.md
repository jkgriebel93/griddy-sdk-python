# InjuryEntryPracticeStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**friday** | [**PracticeStatusEnum**](PracticeStatusEnum.md) |  | [optional] 
**thursday** | [**PracticeStatusEnum**](PracticeStatusEnum.md) |  | [optional] 
**wednesday** | [**PracticeStatusEnum**](PracticeStatusEnum.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.injury_entry_practice_status import InjuryEntryPracticeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of InjuryEntryPracticeStatus from a JSON string
injury_entry_practice_status_instance = InjuryEntryPracticeStatus.from_json(json)
# print the JSON string representation of the object
print(InjuryEntryPracticeStatus.to_json())

# convert the object into a dict
injury_entry_practice_status_dict = injury_entry_practice_status_instance.to_dict()
# create an instance of InjuryEntryPracticeStatus from a dict
injury_entry_practice_status_from_dict = InjuryEntryPracticeStatus.from_dict(injury_entry_practice_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


