# NFLExperienceTeamsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | [**List[NFLNFLTeam]**](NFLTeam.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_experience_teams_response import NFLExperienceTeamsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLExperienceTeamsResponse from a JSON string
nfl_experience_teams_response_instance = NFLExperienceTeamsResponse.from_json(json)
# print the JSON string representation of the object
print(NFLExperienceTeamsResponse.to_json())

# convert the object into a dict
nfl_experience_teams_response_dict = nfl_experience_teams_response_instance.to_dict()
# create an instance of NFLExperienceTeamsResponse from a dict
nfl_experience_teams_response_from_dict = NFLExperienceTeamsResponse.from_dict(nfl_experience_teams_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


