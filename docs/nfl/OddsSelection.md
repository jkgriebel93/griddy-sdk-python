# OddsSelection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decimal** | **float** | Decimal odds for this selection | [optional] 
**is_available** | **bool** | Whether this selection is currently available for betting | [optional] 
**name** | **str** | Team name (e.g., \&quot;KC Chiefs\&quot;, \&quot;BUF Bills\&quot;) | [optional] 

## Example

```python
from src.griddy.nfl.models.odds_selection import OddsSelection

# TODO update the JSON string below
json = "{}"
# create an instance of OddsSelection from a JSON string
odds_selection_instance = OddsSelection.from_json(json)
# print the JSON string representation of the object
print(OddsSelection.to_json())

# convert the object into a dict
odds_selection_dict = odds_selection_instance.to_dict()
# create an instance of OddsSelection from a dict
odds_selection_from_dict = OddsSelection.from_dict(odds_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


