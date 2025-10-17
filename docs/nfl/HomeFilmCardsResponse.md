# HomeFilmCardsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cards** | [**List[FilmCard]**](FilmCard.md) |  | [optional] 
**title** | **str** | Title of the film card collection | [optional] 

## Example

```python
from src.griddy.nfl.models.home_film_cards_response import HomeFilmCardsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HomeFilmCardsResponse from a JSON string
home_film_cards_response_instance = HomeFilmCardsResponse.from_json(json)
# print the JSON string representation of the object
print(HomeFilmCardsResponse.to_json())

# convert the object into a dict
home_film_cards_response_dict = home_film_cards_response_instance.to_dict()
# create an instance of HomeFilmCardsResponse from a dict
home_film_cards_response_from_dict = HomeFilmCardsResponse.from_dict(home_film_cards_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


