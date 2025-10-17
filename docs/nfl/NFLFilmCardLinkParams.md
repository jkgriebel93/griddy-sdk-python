# NFLFilmCardLinkParams

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
**week_slug** | [**NFLNFLWeekSlugEnum**](NFLWeekSlugEnum.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_film_card_link_params import NFLFilmCardLinkParams

# TODO update the JSON string below
json = "{}"
# create an instance of NFLFilmCardLinkParams from a JSON string
nfl_film_card_link_params_instance = NFLFilmCardLinkParams.from_json(json)
# print the JSON string representation of the object
print(NFLFilmCardLinkParams.to_json())

# convert the object into a dict
nfl_film_card_link_params_dict = nfl_film_card_link_params_instance.to_dict()
# create an instance of NFLFilmCardLinkParams from a dict
nfl_film_card_link_params_from_dict = NFLFilmCardLinkParams.from_dict(nfl_film_card_link_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


