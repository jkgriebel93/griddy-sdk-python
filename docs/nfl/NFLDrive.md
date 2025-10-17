# NFLDrive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drive_number** | **int** |  | [optional] 
**end_time** | **str** | Game clock at drive end | [optional] 
**end_yard_line** | **str** | Ending field position | [optional] 
**plays** | [**List[NFLNFLPlay]**](NFLPlay.md) |  | [optional] 
**quarter** | **int** |  | [optional] 
**result** | [**NFLNFLDriveResultEnum**](NFLDriveResultEnum.md) |  | [optional] 
**start_time** | **str** | Game clock at drive start | [optional] 
**start_yard_line** | **str** | Starting field position | [optional] 
**team** | [**NFLNFLTeam**](NFLTeam.md) |  | [optional] 
**time_of_possession** | **str** | Drive duration (MM:SS) | [optional] 
**total_plays** | **int** |  | [optional] 
**total_yards** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_drive import NFLDrive

# TODO update the JSON string below
json = "{}"
# create an instance of NFLDrive from a JSON string
nfl_drive_instance = NFLDrive.from_json(json)
# print the JSON string representation of the object
print(NFLDrive.to_json())

# convert the object into a dict
nfl_drive_dict = nfl_drive_instance.to_dict()
# create an instance of NFLDrive from a dict
nfl_drive_from_dict = NFLDrive.from_dict(nfl_drive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


