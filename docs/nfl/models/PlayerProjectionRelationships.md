# PlayerProjectionRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**week_points** | [**List[PlayerProjectionRelationshipsWeekPointsInner]**](PlayerProjectionRelationshipsWeekPointsInner.md) |  | [optional] 
**week_stats** | [**List[PlayerProjectionRelationshipsWeekStatsInner]**](PlayerProjectionRelationshipsWeekStatsInner.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.player_projection_relationships import PlayerProjectionRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerProjectionRelationships from a JSON string
player_projection_relationships_instance = PlayerProjectionRelationships.from_json(json)
# print the JSON string representation of the object
print(PlayerProjectionRelationships.to_json())

# convert the object into a dict
player_projection_relationships_dict = player_projection_relationships_instance.to_dict()
# create an instance of PlayerProjectionRelationships from a dict
player_projection_relationships_from_dict = PlayerProjectionRelationships.from_dict(player_projection_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


