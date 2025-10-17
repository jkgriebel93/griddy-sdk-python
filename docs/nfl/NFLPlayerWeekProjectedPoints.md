# NFLPlayerWeekProjectedPoints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**NFLNFLPlayerWeekProjectedPointsAttributes**](NFLPlayerWeekProjectedPointsAttributes.md) |  | [optional] 
**id** | **str** | Unique identifier for this projection | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from nfl.models.nfl_player_week_projected_points import NFLPlayerWeekProjectedPoints

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPlayerWeekProjectedPoints from a JSON string
nfl_player_week_projected_points_instance = NFLPlayerWeekProjectedPoints.from_json(json)
# print the JSON string representation of the object
print(NFLPlayerWeekProjectedPoints.to_json())

# convert the object into a dict
nfl_player_week_projected_points_dict = nfl_player_week_projected_points_instance.to_dict()
# create an instance of NFLPlayerWeekProjectedPoints from a dict
nfl_player_week_projected_points_from_dict = NFLPlayerWeekProjectedPoints.from_dict(nfl_player_week_projected_points_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


