# NFLFilmroomPlaysResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of plays matching the filter criteria | [optional] 
**plays** | [**List[NFLNFLFilmroomPlay]**](NFLFilmroomPlay.md) | Array of play data matching the filter criteria | [optional] 

## Example

```python
from nfl.models.nfl_filmroom_plays_response import NFLFilmroomPlaysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLFilmroomPlaysResponse from a JSON string
nfl_filmroom_plays_response_instance = NFLFilmroomPlaysResponse.from_json(json)
# print the JSON string representation of the object
print(NFLFilmroomPlaysResponse.to_json())

# convert the object into a dict
nfl_filmroom_plays_response_dict = nfl_filmroom_plays_response_instance.to_dict()
# create an instance of NFLFilmroomPlaysResponse from a dict
nfl_filmroom_plays_response_from_dict = NFLFilmroomPlaysResponse.from_dict(nfl_filmroom_plays_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


