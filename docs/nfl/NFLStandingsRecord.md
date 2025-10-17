# NFLStandingsRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**losses** | **int** |  | [optional] 
**ties** | **int** |  | [optional] 
**wins** | **int** |  | [optional] 
**points** | [**NFLNFLStandingsRecordAllOfPoints**](NFLStandingsRecordAllOfPoints.md) |  | [optional] 
**rank** | **int** | Ranking within group | [optional] 
**win_pct** | **float** | Win percentage | [optional] 

## Example

```python
from nfl.models.nfl_standings_record import NFLStandingsRecord

# TODO update the JSON string below
json = "{}"
# create an instance of NFLStandingsRecord from a JSON string
nfl_standings_record_instance = NFLStandingsRecord.from_json(json)
# print the JSON string representation of the object
print(NFLStandingsRecord.to_json())

# convert the object into a dict
nfl_standings_record_dict = nfl_standings_record_instance.to_dict()
# create an instance of NFLStandingsRecord from a dict
nfl_standings_record_from_dict = NFLStandingsRecord.from_dict(nfl_standings_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


