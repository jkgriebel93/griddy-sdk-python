# Replay

Replay video information for a game

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiser_id** | **str** |  | [optional] 
**author** | **str** |  | [optional] 
**authorizations** | **object** | Authorization requirements for different NFL+ tiers | [optional] 
**background** | **object** | Background metadata | [optional] 
**camera_source** | **str** |  | [optional] 
**clip_type** | **str** |  | [optional] 
**ctas** | **List[object]** | Call-to-action buttons | [optional] 
**cta_link** | **str** |  | [optional] 
**cta_target** | **str** |  | [optional] 
**cta_text** | **str** |  | [optional] 
**description** | **str** | Video description | [optional] 
**display_title** | **str** |  | [optional] 
**duration** | **str** | Video duration in seconds (as string) | [optional] 
**end_date** | **str** |  | [optional] 
**entitlement** | **str** |  | [optional] 
**episode_number** | **int** |  | [optional] 
**expiration_date** | **str** |  | [optional] 
**external_id** | **str** | External identifier for the video | [optional] 
**fantasy_link** | **str** |  | [optional] 
**host_network** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**ids** | [**ReplayIds**](ReplayIds.md) |  | [optional] 
**images** | **List[object]** | Associated images | [optional] 
**intended_audience** | **str** |  | [optional] 
**intro_end** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 
**mcp_playback_id** | **str** | Media Content Platform playback identifier | [optional] 
**mobile_link** | **str** |  | [optional] 
**mobile_title** | **str** |  | [optional] 
**original_air_date** | **str** |  | [optional] 
**outro_start** | **str** |  | [optional] 
**play_ids** | **List[str]** | Associated play identifiers | [optional] 
**pre_roll_disabled** | **bool** | Whether pre-roll ads are disabled | [optional] 
**promo_assets** | **List[object]** | Promotional assets | [optional] 
**promo_link** | **str** |  | [optional] 
**promo_target** | **str** | Link target for promotional content | [optional] 
**promo_text** | **str** |  | [optional] 
**publish_date** | **datetime** | Video publish date | [optional] 
**radio_station** | **str** |  | [optional] 
**series** | **str** |  | [optional] 
**series_season** | **str** |  | [optional] 
**series_title** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**sub_type** | **str** | Video subtype | [optional] 
**summary** | **str** |  | [optional] 
**tags** | [**List[ReplayTagsInner]**](ReplayTagsInner.md) | Video tags for categorization | [optional] 
**thumbnail** | [**ReplayThumbnail**](ReplayThumbnail.md) |  | [optional] 
**title** | **str** | Video title | [optional] 
**type** | **str** | Content type | [optional] 
**videos** | **List[object]** | Associated video content | [optional] 
**web_link** | **str** |  | [optional] 

## Example

```python
from src.griddy.nfl.models.replay import Replay

# TODO update the JSON string below
json = "{}"
# create an instance of Replay from a JSON string
replay_instance = Replay.from_json(json)
# print the JSON string representation of the object
print(Replay.to_json())

# convert the object into a dict
replay_dict = replay_instance.to_dict()
# create an instance of Replay from a dict
replay_from_dict = Replay.from_dict(replay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


