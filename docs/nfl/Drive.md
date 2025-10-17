# Drive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drive_number** | **int** |  | [optional] 
**end_time** | **str** | Game clock at drive end | [optional] 
**end_yard_line** | **str** | Ending field position | [optional] 
**plays** | [**List[Play]**](Play.md) |  | [optional] 
**quarter** | **int** |  | [optional] 
**result** | [**DriveResultEnum**](DriveResultEnum.md) |  | [optional] 
**start_time** | **str** | Game clock at drive start | [optional] 
**start_yard_line** | **str** | Starting field position | [optional] 
**team** | [**Team**](Team.md) |  | [optional] 
**time_of_possession** | **str** | Drive duration (MM:SS) | [optional] 
**total_plays** | **int** |  | [optional] 
**total_yards** | **int** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.drive import Drive

# TODO update the JSON string below
json = "{}"
# create an instance of Drive from a JSON string
drive_instance = Drive.from_json(json)
# print the JSON string representation of the object
print(Drive.to_json())

# convert the object into a dict
drive_dict = drive_instance.to_dict()
# create an instance of Drive from a dict
drive_from_dict = Drive.from_dict(drive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


