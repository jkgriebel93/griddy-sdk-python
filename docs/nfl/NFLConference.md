# NFLConference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbr** | [**NFLNFLConferenceEnum**](NFLConferenceEnum.md) |  | [optional] 
**full_name** | **str** | Full conference name | [optional] 
**id** | **str** | Conference identifier | [optional] 

## Example

```python
from nfl.models.nfl_conference import NFLConference

# TODO update the JSON string below
json = "{}"
# create an instance of NFLConference from a JSON string
nfl_conference_instance = NFLConference.from_json(json)
# print the JSON string representation of the object
print(NFLConference.to_json())

# convert the object into a dict
nfl_conference_dict = nfl_conference_instance.to_dict()
# create an instance of NFLConference from a dict
nfl_conference_from_dict = NFLConference.from_dict(nfl_conference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


