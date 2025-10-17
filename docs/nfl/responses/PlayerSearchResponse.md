# PlayerSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**players** | [**List[PlayerSearchResult]**](PlayerSearchResult.md) | Array of players matching search criteria | [optional] 
**term** | **str** | Search term used | [optional] 

## Example

```python
from src.griddy.nfl.models.player_search_response import PlayerSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSearchResponse from a JSON string
player_search_response_instance = PlayerSearchResponse.from_json(json)
# print the JSON string representation of the object
print(PlayerSearchResponse.to_json())

# convert the object into a dict
player_search_response_dict = player_search_response_instance.to_dict()
# create an instance of PlayerSearchResponse from a dict
player_search_response_from_dict = PlayerSearchResponse.from_dict(player_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


