# NFLPlayerWeekProjectedPointsAttributes


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
from nfl.models.nfl_player_week_projected_points_attributes import NFLPlayerWeekProjectedPointsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPlayerWeekProjectedPointsAttributes from a JSON string
nfl_player_week_projected_points_attributes_instance = NFLPlayerWeekProjectedPointsAttributes.from_json(json)
# print the JSON string representation of the object
print(NFLPlayerWeekProjectedPointsAttributes.to_json())

# convert the object into a dict
nfl_player_week_projected_points_attributes_dict = nfl_player_week_projected_points_attributes_instance.to_dict()
# create an instance of NFLPlayerWeekProjectedPointsAttributes from a dict
nfl_player_week_projected_points_attributes_from_dict = NFLPlayerWeekProjectedPointsAttributes.from_dict(nfl_player_week_projected_points_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


