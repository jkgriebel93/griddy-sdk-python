# OverallRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**losses** | **int** |  | [optional] 
**ties** | **int** |  | [optional] 
**wins** | **int** |  | [optional] 
**points** | [**PointsRecordAllOfPoints**](PointsRecordAllOfPoints.md) |  | [optional] 
**win_pct** | **float** |  | [optional] 
**games** | **int** | Total games played | [optional] 
**streak** | [**OverallRecordAllOfStreak**](OverallRecordAllOfStreak.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.overall_record import OverallRecord

# TODO update the JSON string below
json = "{}"
# create an instance of OverallRecord from a JSON string
overall_record_instance = OverallRecord.from_json(json)
# print the JSON string representation of the object
print(OverallRecord.to_json())

# convert the object into a dict
overall_record_dict = overall_record_instance.to_dict()
# create an instance of OverallRecord from a dict
overall_record_from_dict = OverallRecord.from_dict(overall_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


