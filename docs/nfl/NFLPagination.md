# NFLPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Maximum items per page | [optional] 
**token** | **str** | Token for next page of results | [optional] 

## Example

```python
from nfl.models.nfl_pagination import NFLPagination

# TODO update the JSON string below
json = "{}"
# create an instance of NFLPagination from a JSON string
nfl_pagination_instance = NFLPagination.from_json(json)
# print the JSON string representation of the object
print(NFLPagination.to_json())

# convert the object into a dict
nfl_pagination_dict = nfl_pagination_instance.to_dict()
# create an instance of NFLPagination from a dict
nfl_pagination_from_dict = NFLPagination.from_dict(nfl_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


