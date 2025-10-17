# SocialMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** | URL to social media profile | [optional] 
**platform** | **str** | Social media platform name | [optional] 

## Example

```python
from src.griddy.nfl.models.social_media import SocialMedia

# TODO update the JSON string below
json = "{}"
# create an instance of SocialMedia from a JSON string
social_media_instance = SocialMedia.from_json(json)
# print the JSON string representation of the object
print(SocialMedia.to_json())

# convert the object into a dict
social_media_dict = social_media_instance.to_dict()
# create an instance of SocialMedia from a dict
social_media_from_dict = SocialMedia.from_dict(social_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


