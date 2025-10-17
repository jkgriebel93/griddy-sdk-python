# WeeksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**weeks** | [**List[Week]**](Week.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.weeks_response import WeeksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WeeksResponse from a JSON string
weeks_response_instance = WeeksResponse.from_json(json)
# print the JSON string representation of the object
print(WeeksResponse.to_json())

# convert the object into a dict
weeks_response_dict = weeks_response_instance.to_dict()
# create an instance of WeeksResponse from a dict
weeks_response_from_dict = WeeksResponse.from_dict(weeks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


