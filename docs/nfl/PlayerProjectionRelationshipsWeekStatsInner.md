# PlayerProjectionRelationshipsWeekStatsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Reference to projected stats | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.player_projection_relationships_week_stats_inner import PlayerProjectionRelationshipsWeekStatsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerProjectionRelationshipsWeekStatsInner from a JSON string
player_projection_relationships_week_stats_inner_instance = PlayerProjectionRelationshipsWeekStatsInner.from_json(json)
# print the JSON string representation of the object
print(PlayerProjectionRelationshipsWeekStatsInner.to_json())

# convert the object into a dict
player_projection_relationships_week_stats_inner_dict = player_projection_relationships_week_stats_inner_instance.to_dict()
# create an instance of PlayerProjectionRelationshipsWeekStatsInner from a dict
player_projection_relationships_week_stats_inner_from_dict = PlayerProjectionRelationshipsWeekStatsInner.from_dict(player_projection_relationships_week_stats_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


