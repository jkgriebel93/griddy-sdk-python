# NFLTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbreviation** | **str** | Three-letter team abbreviation | [optional] 
**conference_abbr** | [**NFLNFLConferenceEnum**](NFLConferenceEnum.md) |  | [optional] 
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
**socials** | [**List[NFLNFLSocialMedia]**](NFLSocialMedia.md) |  | [optional] 
**team_type** | [**NFLNFLTeamTypeEnum**](NFLTeamTypeEnum.md) |  | [optional] 
**venues** | [**List[NFLNFLVenue]**](NFLVenue.md) |  | [optional] 
**year_established** | **int** | Year team was established | [optional] 

## Example

```python
from nfl.models.nfl_team import NFLTeam

# TODO update the JSON string below
json = "{}"
# create an instance of NFLTeam from a JSON string
nfl_team_instance = NFLTeam.from_json(json)
# print the JSON string representation of the object
print(NFLTeam.to_json())

# convert the object into a dict
nfl_team_dict = nfl_team_instance.to_dict()
# create an instance of NFLTeam from a dict
nfl_team_from_dict = NFLTeam.from_dict(nfl_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


