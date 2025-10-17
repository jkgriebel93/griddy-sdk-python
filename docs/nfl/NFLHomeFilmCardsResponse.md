# NFLHomeFilmCardsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cards** | [**List[NFLNFLFilmCard]**](NFLFilmCard.md) |  | [optional] 
**title** | **str** | Title of the film card collection | [optional] 

## Example

```python
from nfl.models.nfl_home_film_cards_response import NFLHomeFilmCardsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLHomeFilmCardsResponse from a JSON string
nfl_home_film_cards_response_instance = NFLHomeFilmCardsResponse.from_json(json)
# print the JSON string representation of the object
print(NFLHomeFilmCardsResponse.to_json())

# convert the object into a dict
nfl_home_film_cards_response_dict = nfl_home_film_cards_response_instance.to_dict()
# create an instance of NFLHomeFilmCardsResponse from a dict
nfl_home_film_cards_response_from_dict = NFLHomeFilmCardsResponse.from_dict(nfl_home_film_cards_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


