# PointsRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**losses** | **int** |  | [optional] 
**ties** | **int** |  | [optional] 
**wins** | **int** |  | [optional] 
**points** | [**PointsRecordAllOfPoints**](PointsRecordAllOfPoints.md) |  | [optional] 
**win_pct** | **float** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.points_record import PointsRecord

# TODO update the JSON string below
json = "{}"
# create an instance of PointsRecord from a JSON string
points_record_instance = PointsRecord.from_json(json)
# print the JSON string representation of the object
print(PointsRecord.to_json())

# convert the object into a dict
points_record_dict = points_record_instance.to_dict()
# create an instance of PointsRecord from a dict
points_record_from_dict = PointsRecord.from_dict(points_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


