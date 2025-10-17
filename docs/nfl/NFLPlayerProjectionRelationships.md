# NFLPlayerProjectionRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**week_points** | [**List[NFLNFLPlayerProjectionRelationshipsWeekPointsInner]**](NFLPlayerProjectionRelationshipsWeekPointsInner.md) |  | [optional] 
**week_stats** | [**List[NFLNFLPlayerProjectionRelationshipsWeekStatsInner]**](NFLPlayerProjectionRelationshipsWeekStatsInner.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_player_projection_relationships import NFLPlayerProjectionRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPlayerProjectionRelationships from a JSON string
nfl_player_projection_relationships_instance = NFLPlayerProjectionRelationships.from_json(json)
# print the JSON string representation of the object
print(NFLPlayerProjectionRelationships.to_json())

# convert the object into a dict
nfl_player_projection_relationships_dict = nfl_player_projection_relationships_instance.to_dict()
# create an instance of NFLPlayerProjectionRelationships from a dict
nfl_player_projection_relationships_from_dict = NFLPlayerProjectionRelationships.from_dict(nfl_player_projection_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


