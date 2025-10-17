# NFLPlayerProjection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Player SMART ID | [optional] 
**relationships** | [**NFLNFLPlayerProjectionRelationships**](NFLPlayerProjectionRelationships.md) |  | [optional] 
**type** | **str** | Resource type | [optional] 

## Example

```python
from nfl.models.nfl_player_projection import NFLPlayerProjection

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPlayerProjection from a JSON string
nfl_player_projection_instance = NFLPlayerProjection.from_json(json)
# print the JSON string representation of the object
print(NFLPlayerProjection.to_json())

# convert the object into a dict
nfl_player_projection_dict = nfl_player_projection_instance.to_dict()
# create an instance of NFLPlayerProjection from a dict
nfl_player_projection_from_dict = NFLPlayerProjection.from_dict(nfl_player_projection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


