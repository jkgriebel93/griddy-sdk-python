# NFLProTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbr** | **str** | Three-letter team abbreviation | [optional] 
**alt_color** | **str** | Alternate team color in hex format | [optional] 
**city** | **str** | Team city/location | [optional] 
**city_state** | **str** | Team city and state | [optional] 
**conference** | [**NFLNFLConference**](NFLConference.md) |  | [optional] 
**conference_abbr** | [**NFLNFLConferenceEnum**](NFLConferenceEnum.md) |  | [optional] 
**dark_color** | **str** | Dark team color in hex format | [optional] 
**division** | [**NFLNFLDivision**](NFLDivision.md) |  | [optional] 
**domain** | **str** | Team website domain prefix | [optional] 
**full_name** | **str** | Full team name | [optional] 
**is_pro_bowl** | **bool** | Whether this is a Pro Bowl team | [optional] [default to False]
**logo** | **str** | URL to team logo (may contain formatInstructions placeholder) | [optional] 
**name** | **str** | Team name | [optional] 
**nick** | **str** | Team nickname (short form) | [optional] 
**nickname** | **str** | Team nickname | [optional] 
**primary_color** | **str** | Primary team color in hex format | [optional] 
**season** | **int** | Current season year | [optional] 
**secondary_color** | **str** | Secondary team color in hex format | [optional] 
**slug** | **str** | URL-friendly team identifier | [optional] 
**smart_id** | **str** | Unique smart identifier for the team | [optional] 
**stadium_name** | **str** | Name of the team&#39;s home stadium | [optional] 
**team_id** | **str** | Team identifier (4-digit string) | [optional] 
**team_site_ticket_url** | **str** | URL to team&#39;s ticket purchase page | [optional] 
**team_site_url** | **str** | Team&#39;s official website URL | [optional] 
**team_type** | [**NFLNFLTeamTypeEnum**](NFLTeamTypeEnum.md) |  | [optional] 
**tertiary_color** | **str** | Tertiary team color in hex format | [optional] 
**ticket_phone_number** | **str** | Phone number for ticket purchases | [optional] 
**year_found** | **int** | Year the team was founded | [optional] 

## Example

```python
from nfl.models.nfl_pro_team import NFLProTeam

# TODO update the JSON string below
json = "{}"
# create an instance of NFLProTeam from a JSON string
nfl_pro_team_instance = NFLProTeam.from_json(json)
# print the JSON string representation of the object
print(NFLProTeam.to_json())

# convert the object into a dict
nfl_pro_team_dict = nfl_pro_team_instance.to_dict()
# create an instance of NFLProTeam from a dict
nfl_pro_team_from_dict = NFLProTeam.from_dict(nfl_pro_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


