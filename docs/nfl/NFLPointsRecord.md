# NFLPointsRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**losses** | **int** |  | [optional] 
**ties** | **int** |  | [optional] 
**wins** | **int** |  | [optional] 
**points** | [**NFLNFLPointsRecordAllOfPoints**](NFLPointsRecordAllOfPoints.md) |  | [optional] 
**win_pct** | **float** |  | [optional] 

## Example

```python
from nfl.models.nfl_points_record import NFLPointsRecord

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPointsRecord from a JSON string
nfl_points_record_instance = NFLPointsRecord.from_json(json)
# print the JSON string representation of the object
print(NFLPointsRecord.to_json())

# convert the object into a dict
nfl_points_record_dict = nfl_points_record_instance.to_dict()
# create an instance of NFLPointsRecord from a dict
nfl_points_record_from_dict = NFLPointsRecord.from_dict(nfl_points_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


