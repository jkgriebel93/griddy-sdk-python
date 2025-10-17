# FilmroomPlaysResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of plays matching the filter criteria | [optional] 
**plays** | [**List[FilmroomPlay]**](FilmroomPlay.md) | Array of play data matching the filter criteria | [optional] 

## Example

```python
from src.griddy.nfl.models.filmroom_plays_response import FilmroomPlaysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilmroomPlaysResponse from a JSON string
filmroom_plays_response_instance = FilmroomPlaysResponse.from_json(json)
# print the JSON string representation of the object
print(FilmroomPlaysResponse.to_json())

# convert the object into a dict
filmroom_plays_response_dict = filmroom_plays_response_instance.to_dict()
# create an instance of FilmroomPlaysResponse from a dict
filmroom_plays_response_from_dict = FilmroomPlaysResponse.from_dict(filmroom_plays_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


