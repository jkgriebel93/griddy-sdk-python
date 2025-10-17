# PlayerWeekProjectedPointsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player_id** | **str** | Player SMART ID | [optional] 
**points** | **float** | Projected fantasy points | [optional] 
**season** | **int** | Season year | [optional] 
**settings_code** | **str** | Fantasy settings code | [optional] 
**week** | **int** | Week number | [optional] 

## Example

```python
from src.griddy.nfl.models.player_week_projected_points_attributes import PlayerWeekProjectedPointsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerWeekProjectedPointsAttributes from a JSON string
player_week_projected_points_attributes_instance = PlayerWeekProjectedPointsAttributes.from_json(json)
# print the JSON string representation of the object
print(PlayerWeekProjectedPointsAttributes.to_json())

# convert the object into a dict
player_week_projected_points_attributes_dict = player_week_projected_points_attributes_instance.to_dict()
# create an instance of PlayerWeekProjectedPointsAttributes from a dict
player_week_projected_points_attributes_from_dict = PlayerWeekProjectedPointsAttributes.from_dict(player_week_projected_points_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


