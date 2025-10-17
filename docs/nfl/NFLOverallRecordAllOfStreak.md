# NFLOverallRecordAllOfStreak


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **int** | Length of current streak | [optional] 
**type** | [**NFLNFLGameResultEnum**](NFLGameResultEnum.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_overall_record_all_of_streak import NFLOverallRecordAllOfStreak

# TODO update the JSON string below
json = "{}"
# create an instance of NFLOverallRecordAllOfStreak from a JSON string
nfl_overall_record_all_of_streak_instance = NFLOverallRecordAllOfStreak.from_json(json)
# print the JSON string representation of the object
print(NFLOverallRecordAllOfStreak.to_json())

# convert the object into a dict
nfl_overall_record_all_of_streak_dict = nfl_overall_record_all_of_streak_instance.to_dict()
# create an instance of NFLOverallRecordAllOfStreak from a dict
nfl_overall_record_all_of_streak_from_dict = NFLOverallRecordAllOfStreak.from_dict(nfl_overall_record_all_of_streak_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


