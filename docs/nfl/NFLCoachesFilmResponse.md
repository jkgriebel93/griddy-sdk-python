# NFLCoachesFilmResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NFLNFLCoachesFilmVideo]**](NFLCoachesFilmVideo.md) |  | [optional] 
**metadata** | [**NFLNFLResponseMetadata**](NFLResponseMetadata.md) |  | [optional] 
**pagination** | [**NFLNFLPagination**](NFLPagination.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_coaches_film_response import NFLCoachesFilmResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLCoachesFilmResponse from a JSON string
nfl_coaches_film_response_instance = NFLCoachesFilmResponse.from_json(json)
# print the JSON string representation of the object
print(NFLCoachesFilmResponse.to_json())

# convert the object into a dict
nfl_coaches_film_response_dict = nfl_coaches_film_response_instance.to_dict()
# create an instance of NFLCoachesFilmResponse from a dict
nfl_coaches_film_response_from_dict = NFLCoachesFilmResponse.from_dict(nfl_coaches_film_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


