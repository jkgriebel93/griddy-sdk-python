# NFLTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compensation_details** | **str** | Trade compensation or contract details | [optional] 
**var_date** | **datetime** |  | [optional] 
**details** | **str** | Transaction details | [optional] 
**id** | **str** |  | [optional] 
**player** | [**NFLNFLPlayer**](NFLPlayer.md) |  | [optional] 
**related_team** | [**NFLNFLTeam**](NFLTeam.md) |  | [optional] 
**team** | [**NFLNFLTeam**](NFLTeam.md) |  | [optional] 
**type** | [**NFLNFLTransactionTypeEnum**](NFLTransactionTypeEnum.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_transaction import NFLTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of NFLTransaction from a JSON string
nfl_transaction_instance = NFLTransaction.from_json(json)
# print the JSON string representation of the object
print(NFLTransaction.to_json())

# convert the object into a dict
nfl_transaction_dict = nfl_transaction_instance.to_dict()
# create an instance of NFLTransaction from a dict
nfl_transaction_from_dict = NFLTransaction.from_dict(nfl_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


