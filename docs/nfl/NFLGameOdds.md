# NFLGameOdds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **int** | Game identifier (10-digit format YYYYMMDDNN) | [optional] 
**game_key** | **int** | Unique game key identifier | [optional] 
**home_team_abbr** | **str** | Home team abbreviation | [optional] 
**home_team_id** | **str** | Home team identifier | [optional] 
**moneyline** | [**NFLNFLMoneyLine**](NFLMoneyLine.md) |  | [optional] 
**spread** | [**NFLNFLPointSpread**](NFLPointSpread.md) |  | [optional] 
**totals** | [**NFLNFLTotals**](NFLTotals.md) |  | [optional] 
**updated_at** | **datetime** | Timestamp of last odds update | [optional] 
**visitor_team_abbr** | **str** | Visitor team abbreviation | [optional] 
**visitor_team_id** | **str** | Visitor team identifier | [optional] 

## Example

```python
from nfl.models.nfl_game_odds import NFLGameOdds

# TODO update the JSON string below
json = "{}"
# create an instance of NFLGameOdds from a JSON string
nfl_game_odds_instance = NFLGameOdds.from_json(json)
# print the JSON string representation of the object
print(NFLGameOdds.to_json())

# convert the object into a dict
nfl_game_odds_dict = nfl_game_odds_instance.to_dict()
# create an instance of NFLGameOdds from a dict
nfl_game_odds_from_dict = NFLGameOdds.from_dict(nfl_game_odds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


