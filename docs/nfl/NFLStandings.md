# NFLStandings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clinched** | [**NFLNFLClinched**](NFLClinched.md) |  | [optional] 
**close_games** | [**NFLNFLRecord**](NFLRecord.md) |  | [optional] 
**conference** | [**NFLNFLStandingsRecord**](NFLStandingsRecord.md) |  | [optional] 
**division** | [**NFLNFLStandingsRecord**](NFLStandingsRecord.md) |  | [optional] 
**home** | [**NFLNFLPointsRecord**](NFLPointsRecord.md) |  | [optional] 
**last5** | [**NFLNFLPointsRecord**](NFLPointsRecord.md) |  | [optional] 
**overall** | [**NFLNFLOverallRecord**](NFLOverallRecord.md) |  | [optional] 
**road** | [**NFLNFLPointsRecord**](NFLPointsRecord.md) |  | [optional] 
**team** | [**NFLNFLStandingsTeam**](NFLStandingsTeam.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_standings import NFLStandings

# TODO update the JSON string below
json = "{}"
# create an instance of NFLStandings from a JSON string
nfl_standings_instance = NFLStandings.from_json(json)
# print the JSON string representation of the object
print(NFLStandings.to_json())

# convert the object into a dict
nfl_standings_dict = nfl_standings_instance.to_dict()
# create an instance of NFLStandings from a dict
nfl_standings_from_dict = NFLStandings.from_dict(nfl_standings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


