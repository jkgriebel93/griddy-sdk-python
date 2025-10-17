# CoachesFilmResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CoachesFilmVideo]**](CoachesFilmVideo.md) |  | [optional] 
**metadata** | [**ResponseMetadata**](ResponseMetadata.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.coaches_film_response import CoachesFilmResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CoachesFilmResponse from a JSON string
coaches_film_response_instance = CoachesFilmResponse.from_json(json)
# print the JSON string representation of the object
print(CoachesFilmResponse.to_json())

# convert the object into a dict
coaches_film_response_dict = coaches_film_response_instance.to_dict()
# create an instance of CoachesFilmResponse from a dict
coaches_film_response_from_dict = CoachesFilmResponse.from_dict(coaches_film_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


