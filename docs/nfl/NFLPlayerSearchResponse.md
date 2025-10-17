# NFLPlayerSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**players** | [**List[NFLNFLPlayerSearchResult]**](NFLPlayerSearchResult.md) | Array of players matching search criteria | [optional] 
**term** | **str** | Search term used | [optional] 

## Example

```python
from nfl.models.nfl_player_search_response import NFLPlayerSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPlayerSearchResponse from a JSON string
nfl_player_search_response_instance = NFLPlayerSearchResponse.from_json(json)
# print the JSON string representation of the object
print(NFLPlayerSearchResponse.to_json())

# convert the object into a dict
nfl_player_search_response_dict = nfl_player_search_response_instance.to_dict()
# create an instance of NFLPlayerSearchResponse from a dict
nfl_player_search_response_from_dict = NFLPlayerSearchResponse.from_dict(nfl_player_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


