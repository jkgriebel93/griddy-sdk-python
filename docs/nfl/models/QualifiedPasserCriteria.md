# QualifiedPasserCriteria

Criteria for qualified passer designation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Explanation of qualification criteria | [optional] 
**minimum_attempts** | **int** | Minimum passing attempts required | [optional] 
**minimum_attempts_per_game** | **float** | Minimum attempts per team game | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.qualified_passer_criteria import QualifiedPasserCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of QualifiedPasserCriteria from a JSON string
qualified_passer_criteria_instance = QualifiedPasserCriteria.from_json(json)
# print the JSON string representation of the object
print(QualifiedPasserCriteria.to_json())

# convert the object into a dict
qualified_passer_criteria_dict = qualified_passer_criteria_instance.to_dict()
# create an instance of QualifiedPasserCriteria from a dict
qualified_passer_criteria_from_dict = QualifiedPasserCriteria.from_dict(qualified_passer_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


