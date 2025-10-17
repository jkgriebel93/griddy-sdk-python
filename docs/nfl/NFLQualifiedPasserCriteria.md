# NFLQualifiedPasserCriteria

Criteria for qualified passer designation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Explanation of qualification criteria | [optional] 
**minimum_attempts** | **int** | Minimum passing attempts required | [optional] 
**minimum_attempts_per_game** | **float** | Minimum attempts per team game | [optional] 
**season_type** | [**NFLNFLSeasonTypeEnum**](NFLSeasonTypeEnum.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_qualified_passer_criteria import NFLQualifiedPasserCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of NFLQualifiedPasserCriteria from a JSON string
nfl_qualified_passer_criteria_instance = NFLQualifiedPasserCriteria.from_json(json)
# print the JSON string representation of the object
print(NFLQualifiedPasserCriteria.to_json())

# convert the object into a dict
nfl_qualified_passer_criteria_dict = nfl_qualified_passer_criteria_instance.to_dict()
# create an instance of NFLQualifiedPasserCriteria from a dict
nfl_qualified_passer_criteria_from_dict = NFLQualifiedPasserCriteria.from_dict(nfl_qualified_passer_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


