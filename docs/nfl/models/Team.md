# Team


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbreviation** | **str** | Three-letter team abbreviation | [optional] 
**conference_abbr** | [**ConferenceEnum**](ConferenceEnum.md) |  | [optional] 
**conference_full_name** | **str** | Full conference name | [optional] 
**current_logo** | **str** | URL to team logo (may contain {formatInstructions} placeholder) | [optional] 
**division_full_name** | **str** | Full division name | [optional] 
**full_name** | **str** | Full team name | [optional] 
**id** | **str** | Unique team identifier | [optional] 
**league** | **str** | League name | [optional] 
**location** | **str** | Team location/city | [optional] 
**nfl_shop_url** | **str** | URL to team&#39;s NFL shop | [optional] 
**nick_name** | **str** | Team nickname | [optional] 
**official_website_url** | **str** | Team&#39;s official website | [optional] 
**owners** | **str** | Team ownership information | [optional] 
**primary_color** | **str** | Primary team color (hex) | [optional] 
**season** | **str** | Current season | [optional] 
**secondary_color** | **str** | Secondary team color (hex) | [optional] 
**socials** | [**List[SocialMedia]**](SocialMedia.md) |  | [optional] 
**team_type** | [**TeamTypeEnum**](TeamTypeEnum.md) |  | [optional] 
**venues** | [**List[Venue]**](Venue.md) |  | [optional] 
**year_established** | **int** | Year team was established | [optional] 

## Example

```python
from src.griddy.nfl.models.team import Team

# TODO update the JSON string below
json = "{}"
# create an instance of Team from a JSON string
team_instance = Team.from_json(json)
# print the JSON string representation of the object
print(Team.to_json())

# convert the object into a dict
team_dict = team_instance.to_dict()
# create an instance of Team from a dict
team_from_dict = Team.from_dict(team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


