# PlayerProjection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Player SMART ID | [optional] 
**relationships** | [**PlayerProjectionRelationships**](PlayerProjectionRelationships.md) |  | [optional] 
**type** | **str** | Resource type | [optional] 

## Example

```python
from src.griddy.nfl.models.player_projection import PlayerProjection

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerProjection from a JSON string
player_projection_instance = PlayerProjection.from_json(json)
# print the JSON string representation of the object
print(PlayerProjection.to_json())

# convert the object into a dict
player_projection_dict = player_projection_instance.to_dict()
# create an instance of PlayerProjection from a dict
player_projection_from_dict = PlayerProjection.from_dict(player_projection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


