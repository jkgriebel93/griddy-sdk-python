# NFLVideoAuthorizations

Authorization requirements for video access

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nfl_plus_plus** | [**List[NFLNFLVideoAuthorizationsNflPlusPlusInner]**](NFLVideoAuthorizationsNflPlusPlusInner.md) |  | [optional] 
**nfl_plus_premium** | [**List[NFLNFLVideoAuthorizationsNflPlusPlusInner]**](NFLVideoAuthorizationsNflPlusPlusInner.md) |  | [optional] 
**pro_premium** | [**List[NFLNFLVideoAuthorizationsNflPlusPlusInner]**](NFLVideoAuthorizationsNflPlusPlusInner.md) |  | [optional] 

## Example

```python
from nfl.models.nfl_video_authorizations import NFLVideoAuthorizations

# TODO update the JSON string below
json = "{}"
# create an instance of NFLVideoAuthorizations from a JSON string
nfl_video_authorizations_instance = NFLVideoAuthorizations.from_json(json)
# print the JSON string representation of the object
print(NFLVideoAuthorizations.to_json())

# convert the object into a dict
nfl_video_authorizations_dict = nfl_video_authorizations_instance.to_dict()
# create an instance of NFLVideoAuthorizations from a dict
nfl_video_authorizations_from_dict = NFLVideoAuthorizations.from_dict(nfl_video_authorizations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


