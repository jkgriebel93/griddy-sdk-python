# NFLOddsSelection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decimal** | **float** | Decimal odds for this selection | [optional] 
**is_available** | **bool** | Whether this selection is currently available for betting | [optional] 
**name** | **str** | Team name (e.g., \&quot;KC Chiefs\&quot;, \&quot;BUF Bills\&quot;) | [optional] 

## Example

```python
from nfl.models.nfl_odds_selection import NFLOddsSelection

# TODO update the JSON string below
json = "{}"
# create an instance of NFLOddsSelection from a JSON string
nfl_odds_selection_instance = NFLOddsSelection.from_json(json)
# print the JSON string representation of the object
print(NFLOddsSelection.to_json())

# convert the object into a dict
nfl_odds_selection_dict = nfl_odds_selection_instance.to_dict()
# create an instance of NFLOddsSelection from a dict
nfl_odds_selection_from_dict = NFLOddsSelection.from_dict(nfl_odds_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


