# ExperienceTeamsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | [**List[Team]**](Team.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.experience_teams_response import ExperienceTeamsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExperienceTeamsResponse from a JSON string
experience_teams_response_instance = ExperienceTeamsResponse.from_json(json)
# print the JSON string representation of the object
print(ExperienceTeamsResponse.to_json())

# convert the object into a dict
experience_teams_response_dict = experience_teams_response_instance.to_dict()
# create an instance of ExperienceTeamsResponse from a dict
experience_teams_response_from_dict = ExperienceTeamsResponse.from_dict(experience_teams_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


