# NFLWeeksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**NFLNFLPagination**](NFLPagination.md) |  | [optional] 
**weeks** | [**List[NFLNFLWeek]**](NFLWeek.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_weeks_response import NFLWeeksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLWeeksResponse from a JSON string
nfl_weeks_response_instance = NFLWeeksResponse.from_json(json)
# print the JSON string representation of the object
print(NFLWeeksResponse.to_json())

# convert the object into a dict
nfl_weeks_response_dict = nfl_weeks_response_instance.to_dict()
# create an instance of NFLWeeksResponse from a dict
nfl_weeks_response_from_dict = NFLWeeksResponse.from_dict(nfl_weeks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


