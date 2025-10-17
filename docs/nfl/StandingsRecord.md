# StandingsRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**losses** | **int** |  | [optional] 
**ties** | **int** |  | [optional] 
**wins** | **int** |  | [optional] 
**points** | [**StandingsRecordAllOfPoints**](StandingsRecordAllOfPoints.md) |  | [optional] 
**rank** | **int** | Ranking within group | [optional] 
**win_pct** | **float** | Win percentage | [optional] 

## Example

```python
from src.griddy.nfl.models.standings_record import StandingsRecord

# TODO update the JSON string below
json = "{}"
# create an instance of StandingsRecord from a JSON string
standings_record_instance = StandingsRecord.from_json(json)
# print the JSON string representation of the object
print(StandingsRecord.to_json())

# convert the object into a dict
standings_record_dict = standings_record_instance.to_dict()
# create an instance of StandingsRecord from a dict
standings_record_from_dict = StandingsRecord.from_dict(standings_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


