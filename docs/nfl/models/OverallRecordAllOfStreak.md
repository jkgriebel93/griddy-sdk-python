# OverallRecordAllOfStreak


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **int** | Length of current streak | [optional] 
**type** | [**GameResultEnum**](GameResultEnum.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.overall_record_all_of_streak import OverallRecordAllOfStreak

# TODO update the JSON string below
json = "{}"
# create an instance of OverallRecordAllOfStreak from a JSON string
overall_record_all_of_streak_instance = OverallRecordAllOfStreak.from_json(json)
# print the JSON string representation of the object
print(OverallRecordAllOfStreak.to_json())

# convert the object into a dict
overall_record_all_of_streak_dict = overall_record_all_of_streak_instance.to_dict()
# create an instance of OverallRecordAllOfStreak from a dict
overall_record_all_of_streak_from_dict = OverallRecordAllOfStreak.from_dict(overall_record_all_of_streak_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


