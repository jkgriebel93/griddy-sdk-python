# VideoAuthorizations

Authorization requirements for video access

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nfl_plus_plus** | [**List[VideoAuthorizationsNflPlusPlusInner]**](VideoAuthorizationsNflPlusPlusInner.md) |  | [optional] 
**nfl_plus_premium** | [**List[VideoAuthorizationsNflPlusPlusInner]**](VideoAuthorizationsNflPlusPlusInner.md) |  | [optional] 
**pro_premium** | [**List[VideoAuthorizationsNflPlusPlusInner]**](VideoAuthorizationsNflPlusPlusInner.md) |  | [optional] 

## Example

```python
from src.griddy.nfl.models.video_authorizations import VideoAuthorizations

# TODO update the JSON string below
json = "{}"
# create an instance of VideoAuthorizations from a JSON string
video_authorizations_instance = VideoAuthorizations.from_json(json)
# print the JSON string representation of the object
print(VideoAuthorizations.to_json())

# convert the object into a dict
video_authorizations_dict = video_authorizations_instance.to_dict()
# create an instance of VideoAuthorizations from a dict
video_authorizations_from_dict = VideoAuthorizations.from_dict(video_authorizations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


