# Standings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clinched** | [**Clinched**](Clinched.md) |  | [optional] 
**close_games** | [**Record**](Record.md) |  | [optional] 
**conference** | [**StandingsRecord**](StandingsRecord.md) |  | [optional] 
**division** | [**StandingsRecord**](StandingsRecord.md) |  | [optional] 
**home** | [**PointsRecord**](PointsRecord.md) |  | [optional] 
**last5** | [**PointsRecord**](PointsRecord.md) |  | [optional] 
**overall** | [**OverallRecord**](OverallRecord.md) |  | [optional] 
**road** | [**PointsRecord**](PointsRecord.md) |  | [optional] 
**team** | [**StandingsTeam**](StandingsTeam.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.standings import Standings

# TODO update the JSON string below
json = "{}"
# create an instance of Standings from a JSON string
standings_instance = Standings.from_json(json)
# print the JSON string representation of the object
print(Standings.to_json())

# convert the object into a dict
standings_dict = standings_instance.to_dict()
# create an instance of Standings from a dict
standings_from_dict = Standings.from_dict(standings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


