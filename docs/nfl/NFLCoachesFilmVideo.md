# NFLCoachesFilmVideo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_id** | **str** | Associated advertiser ID | [optional] 
**author** | **str** | Content author | [optional] 
**authorizations** | [**NFLNFLVideoAuthorizations**](NFLVideoAuthorizations.md) |  | [optional] 
**background** | **object** | Background configuration | [optional] 
**camera_source** | [**NFLNFLCameraSourceEnum**](NFLCameraSourceEnum.md) |  | [optional] 
**clip_type** | **str** | Type of video clip | [optional] 
**cta_link** | **str** | Call-to-action link | [optional] 
**cta_target** | **str** | Call-to-action target | [optional] 
**cta_text** | **str** | Call-to-action text | [optional] 
**ctas** | **List[object]** | Call-to-action elements | [optional] 
**description** | **str** | Play description | [optional] 
**display_title** | **str** | Display title override | [optional] 
**duration** | **int** | Video duration in seconds | [optional] 
**end_date** | **datetime** | Content end date | [optional] 
**entitlement** | **str** | Entitlement information | [optional] 
**episode_number** | **int** | Episode number if part of series | [optional] 
**expiration_date** | **datetime** | Content expiration date | [optional] 
**external_id** | **str** | External video identifier | [optional] 
**fantasy_link** | **str** | Related fantasy content link | [optional] 
**host_network** | **str** | Broadcasting network | [optional] 
**id** | **str** | Internal content ID | [optional] 
**ids** | [**NFLNFLVideoGamePlayIds**](NFLVideoGamePlayIds.md) |  | [optional] 
**images** | **List[object]** | Associated images | [optional] 
**intended_audience** | **str** | Target audience | [optional] 
**intro_end** | **str** | Introduction end timestamp | [optional] 
**language** | **str** | Content language | [optional] 
**last_updated** | **datetime** | Last update timestamp | [optional] 
**mcp_playback_id** | **str** | Media control platform playback ID | [optional] 
**mobile_link** | **str** | Mobile-specific link | [optional] 
**mobile_title** | **str** | Mobile-specific title | [optional] 
**original_air_date** | **datetime** | Original broadcast air date | [optional] 
**outro_start** | **str** | Outro start timestamp | [optional] 
**play_ids** | **List[str]** | Play identifiers associated with this video | [optional] 
**pre_roll_disabled** | **bool** | Whether pre-roll ads are disabled | [optional] [default to False]
**promo_assets** | **List[object]** | Promotional assets | [optional] 
**promo_link** | **str** | Promotional link | [optional] 
**promo_target** | **str** | Promotional link target | [optional] [default to '_self']
**promo_text** | **str** | Promotional text | [optional] 
**publish_date** | **datetime** | Content publish date | [optional] 
**radio_station** | **str** | Associated radio station | [optional] 
**series** | **str** | Series information | [optional] 
**series_season** | **str** | Series season if applicable | [optional] 
**series_title** | **str** | Series title if part of series | [optional] 
**slug** | **str** | URL slug | [optional] 
**start_date** | **datetime** | Content start date | [optional] 
**sub_type** | [**NFLNFLCoachesFileVideoSubTypeEnum**](NFLCoachesFileVideoSubTypeEnum.md) |  | [optional] 
**summary** | **str** | Content summary | [optional] 
**tags** | [**List[NFLNFLVideoTag]**](NFLVideoTag.md) | Content tags and metadata | [optional] 
**thumbnail** | [**NFLNFLVideoThumbnail**](NFLVideoThumbnail.md) |  | [optional] 
**title** | **str** | Video title | [optional] 
**type** | **str** | Content type (always \&quot;video\&quot;) | [optional] 
**videos** | **List[object]** | Additional video information | [optional] 
**web_link** | **str** | Web-specific link | [optional] 

## Example

```python
from nfl.models.nfl_coaches_film_video import NFLCoachesFilmVideo

# TODO update the JSON string below
json = "{}"
# create an instance of NFLCoachesFilmVideo from a JSON string
nfl_coaches_film_video_instance = NFLCoachesFilmVideo.from_json(json)
# print the JSON string representation of the object
print(NFLCoachesFilmVideo.to_json())

# convert the object into a dict
nfl_coaches_film_video_dict = nfl_coaches_film_video_instance.to_dict()
# create an instance of NFLCoachesFilmVideo from a dict
nfl_coaches_film_video_from_dict = NFLCoachesFilmVideo.from_dict(nfl_coaches_film_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


