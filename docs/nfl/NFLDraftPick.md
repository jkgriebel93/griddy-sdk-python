# NFLDraftPick


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**college** | **str** |  | [optional] 
**is_compensatory** | **bool** |  | [optional] 
**original_team** | [**NFLNFLTeam**](NFLTeam.md) |  | [optional] 
**overall_pick** | **int** |  | [optional] 
**pick** | **int** |  | [optional] 
**player** | [**NFLNFLPlayer**](NFLPlayer.md) |  | [optional] 
**position** | **str** |  | [optional] 
**round** | **int** |  | [optional] 
**team** | [**NFLNFLTeam**](NFLTeam.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_draft_pick import NFLDraftPick

# TODO update the JSON string below
json = "{}"
# create an instance of NFLDraftPick from a JSON string
nfl_draft_pick_instance = NFLDraftPick.from_json(json)
# print the JSON string representation of the object
print(NFLDraftPick.to_json())

# convert the object into a dict
nfl_draft_pick_dict = nfl_draft_pick_instance.to_dict()
# create an instance of NFLDraftPick from a dict
nfl_draft_pick_from_dict = NFLDraftPick.from_dict(nfl_draft_pick_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


