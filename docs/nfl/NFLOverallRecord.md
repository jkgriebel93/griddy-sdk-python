# NFLOverallRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**losses** | **int** |  | [optional] 
**ties** | **int** |  | [optional] 
**wins** | **int** |  | [optional] 
**points** | [**NFLNFLPointsRecordAllOfPoints**](NFLPointsRecordAllOfPoints.md) |  | [optional] 
**win_pct** | **float** |  | [optional] 
**games** | **int** | Total games played | [optional] 
**streak** | [**NFLNFLOverallRecordAllOfStreak**](NFLOverallRecordAllOfStreak.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_overall_record import NFLOverallRecord

# TODO update the JSON string below
json = "{}"
# create an instance of NFLOverallRecord from a JSON string
nfl_overall_record_instance = NFLOverallRecord.from_json(json)
# print the JSON string representation of the object
print(NFLOverallRecord.to_json())

# convert the object into a dict
nfl_overall_record_dict = nfl_overall_record_instance.to_dict()
# create an instance of NFLOverallRecord from a dict
nfl_overall_record_from_dict = NFLOverallRecord.from_dict(nfl_overall_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


