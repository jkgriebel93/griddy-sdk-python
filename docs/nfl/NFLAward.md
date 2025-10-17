# NFLAward


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**award_type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**year** | **int** |  | [optional] 

## Example

```python
from nfl.models.nfl_award import NFLAward

# TODO update the JSON string below
json = "{}"
# create an instance of NFLAward from a JSON string
nfl_award_instance = NFLAward.from_json(json)
# print the JSON string representation of the object
print(NFLAward.to_json())

# convert the object into a dict
nfl_award_dict = nfl_award_instance.to_dict()
# create an instance of NFLAward from a dict
nfl_award_from_dict = NFLAward.from_dict(nfl_award_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


