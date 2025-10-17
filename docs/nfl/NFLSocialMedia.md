# NFLSocialMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** | URL to social media profile | [optional] 
**platform** | **str** | Social media platform name | [optional] 

## Example

```python
from nfl.models.nfl_social_media import NFLSocialMedia

# TODO update the JSON string below
json = "{}"
# create an instance of NFLSocialMedia from a JSON string
nfl_social_media_instance = NFLSocialMedia.from_json(json)
# print the JSON string representation of the object
print(NFLSocialMedia.to_json())

# convert the object into a dict
nfl_social_media_dict = nfl_social_media_instance.to_dict()
# create an instance of NFLSocialMedia from a dict
nfl_social_media_from_dict = NFLSocialMedia.from_dict(nfl_social_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


