# FilmCardLinkParams

Parameters for constructing film room link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dropback** | **int** | Dropback indicator (1 for yes) | [optional] 
**nfl_id** | **str** | NFL player identifier | [optional] 
**passer_id** | **str** | Passer ID for QB film | [optional] 
**rusher_id** | **str** | Rusher ID for RB film | [optional] 
**season** | **str** | Season year | [optional] 
**target_id** | **str** | Target ID for receiver film | [optional] 
**week_slug** | [**WeekSlugEnum**](WeekSlugEnum.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.film_card_link_params import FilmCardLinkParams

# TODO update the JSON string below
json = "{}"
# create an instance of FilmCardLinkParams from a JSON string
film_card_link_params_instance = FilmCardLinkParams.from_json(json)
# print the JSON string representation of the object
print(FilmCardLinkParams.to_json())

# convert the object into a dict
film_card_link_params_dict = film_card_link_params_instance.to_dict()
# create an instance of FilmCardLinkParams from a dict
film_card_link_params_from_dict = FilmCardLinkParams.from_dict(film_card_link_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


