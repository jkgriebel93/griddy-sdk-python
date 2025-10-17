# NFLFilmCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_params** | [**NFLNFLFilmCardLinkParams**](NFLFilmCardLinkParams.md) |  | [optional] 
**team_id** | **str** | Team identifier | [optional] 
**title** | **str** | Title of the film content | [optional] 

## Example

```python
from nfl.models.nfl_film_card import NFLFilmCard

# TODO update the JSON string below
json = "{}"
# create an instance of NFLFilmCard from a JSON string
nfl_film_card_instance = NFLFilmCard.from_json(json)
# print the JSON string representation of the object
print(NFLFilmCard.to_json())

# convert the object into a dict
nfl_film_card_dict = nfl_film_card_instance.to_dict()
# create an instance of NFLFilmCard from a dict
nfl_film_card_from_dict = NFLFilmCard.from_dict(nfl_film_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


