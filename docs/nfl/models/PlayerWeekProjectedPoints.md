# PlayerWeekProjectedPoints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**PlayerWeekProjectedPointsAttributes**](PlayerWeekProjectedPointsAttributes.md) |  | [optional] 
**id** | **str** | Unique identifier for this projection | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.player_week_projected_points import PlayerWeekProjectedPoints

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerWeekProjectedPoints from a JSON string
player_week_projected_points_instance = PlayerWeekProjectedPoints.from_json(json)
# print the JSON string representation of the object
print(PlayerWeekProjectedPoints.to_json())

# convert the object into a dict
player_week_projected_points_dict = player_week_projected_points_instance.to_dict()
# create an instance of PlayerWeekProjectedPoints from a dict
player_week_projected_points_from_dict = PlayerWeekProjectedPoints.from_dict(player_week_projected_points_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


