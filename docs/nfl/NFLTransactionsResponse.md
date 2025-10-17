# NFLTransactionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**NFLNFLPagination**](NFLPagination.md) |  | [optional] 
**transactions** | [**List[NFLNFLTransaction]**](NFLTransaction.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_transactions_response import NFLTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NFLTransactionsResponse from a JSON string
nfl_transactions_response_instance = NFLTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(NFLTransactionsResponse.to_json())

# convert the object into a dict
nfl_transactions_response_dict = nfl_transactions_response_instance.to_dict()
# create an instance of NFLTransactionsResponse from a dict
nfl_transactions_response_from_dict = NFLTransactionsResponse.from_dict(nfl_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


