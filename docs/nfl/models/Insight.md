# Insight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Content creation timestamp | [optional] 
**created_by** | **str** | Content creator identifier | [optional] 
**var_date** | **date** | Content publication date | [optional] 
**esb_id** | **str** | ESB player identifier | [optional] 
**evergreen** | **bool** | Whether content is evergreen (timeless) or time-sensitive | [optional] [default to False]
**game_id** | **int** | Game identifier (10-digit format YYYYMMDDNN) | [optional] 
**gsis_id** | **str** | GSIS player identifier | [optional] 
**headshot** | **str** | URL to player headshot image (contains formatInstructions placeholder) | [optional] 
**id** | **str** | Unique content identifier | [optional] 
**image_url** | **str** | Associated image or chart URL (optional) | [optional] 
**jersey_number** | **int** | Player&#39;s jersey number | [optional] 
**nfl_id** | **int** | NFL player identifier | [optional] 
**player_name** | **str** | Player&#39;s full name | [optional] 
**position** | [**PositionGroupEnum**](PositionGroupEnum.md) |  | [optional] 
**season** | **int** | Season year | [optional] 
**season_type** | [**SeasonTypeEnum**](SeasonTypeEnum.md) |  | [optional] 
**second_team_abbr** | **str** | Opponent or related team abbreviation | [optional] 
**second_team_id** | **str** | Opponent or related team identifier | [optional] 
**second_team_type** | **str** | Context of the second team (typically \&quot;defense\&quot; for opponent) | [optional] 
**smart_id** | **str** | Smart player identifier | [optional] 
**sub_note1** | **str** | Detailed insight content and analysis | [optional] 
**tags** | **List[str]** | Content classification tags | [optional] 
**team_abbr** | **str** | Player&#39;s team abbreviation | [optional] 
**team_id** | **str** | Player&#39;s team identifier | [optional] 
**title** | **str** | Main insight headline or title | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 
**updated_by** | **str** | Last editor identifier | [optional] 
**week** | **int** | Week number (if applicable) | [optional] 

## Example

```python
from src.griddy.nfl.models.insight import Insight

# TODO update the JSON string below
json = "{}"
# create an instance of Insight from a JSON string
insight_instance = Insight.from_json(json)
# print the JSON string representation of the object
print(Insight.to_json())

# convert the object into a dict
insight_dict = insight_instance.to_dict()
# create an instance of Insight from a dict
insight_from_dict = Insight.from_dict(insight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


