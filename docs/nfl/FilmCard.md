# FilmCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_params** | [**FilmCardLinkParams**](FilmCardLinkParams.md) |  | [optional] 
**team_id** | **str** | Team identifier | [optional] 
**title** | **str** | Title of the film content | [optional] 

## Example

```python
from src.griddy.nfl.models.film_card import FilmCard

# TODO update the JSON string below
json = "{}"
# create an instance of FilmCard from a JSON string
film_card_instance = FilmCard.from_json(json)
# print the JSON string representation of the object
print(FilmCard.to_json())

# convert the object into a dict
film_card_dict = film_card_instance.to_dict()
# create an instance of FilmCard from a dict
film_card_from_dict = FilmCard.from_dict(film_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


