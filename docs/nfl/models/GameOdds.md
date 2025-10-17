# GameOdds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **int** | Game identifier (10-digit format YYYYMMDDNN) | [optional] 
**game_key** | **int** | Unique game key identifier | [optional] 
**home_team_abbr** | **str** | Home team abbreviation | [optional] 
**home_team_id** | **str** | Home team identifier | [optional] 
**moneyline** | [**MoneyLine**](MoneyLine.md) |  | [optional] 
**spread** | [**PointSpread**](PointSpread.md) |  | [optional] 
**totals** | [**Totals**](Totals.md) |  | [optional] 
**updated_at** | **datetime** | Timestamp of last odds update | [optional] 
**visitor_team_abbr** | **str** | Visitor team abbreviation | [optional] 
**visitor_team_id** | **str** | Visitor team identifier | [optional] 

## Example

```python
from src.griddy.nfl.models.game_odds import GameOdds

# TODO update the JSON string below
json = "{}"
# create an instance of GameOdds from a JSON string
game_odds_instance = GameOdds.from_json(json)
# print the JSON string representation of the object
print(GameOdds.to_json())

# convert the object into a dict
game_odds_dict = game_odds_instance.to_dict()
# create an instance of GameOdds from a dict
game_odds_from_dict = GameOdds.from_dict(game_odds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


