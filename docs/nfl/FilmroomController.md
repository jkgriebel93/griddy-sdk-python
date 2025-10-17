# src.griddy.nfl.FilmroomController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_filmroom_plays**](FilmroomController.md#get_filmroom_plays) | **GET** /api/secured/videos/filmroom/plays | Get Filmroom Plays with Advanced Filtering


# **get_filmroom_plays**
> FilmroomPlaysResponse get_filmroom_plays(game_id=game_id, week_slug=week_slug, season=season, season_type=season_type, nfl_id=nfl_id, quarter=quarter, down=down, yards_to_go_type=yards_to_go_type, touchdown=touchdown, rush10_plus_yards=rush10_plus_yards, fumble_lost=fumble_lost, fumble=fumble, qb_alignment=qb_alignment, redzone=redzone, goal_to_go=goal_to_go, pass_play=pass_play, run_play=run_play, play_type=play_type, attempt=attempt, completion=completion, interception=interception, reception=reception, sack=sack, rec_motion=rec_motion, target_location=target_location, air_yard_type=air_yard_type, dropback_time_type=dropback_time_type, pressure=pressure, blitz=blitz, play_action=play_action, rush_direction=rush_direction, run_stuff=run_stuff, receiver_alignment=receiver_alignment, separation_type=separation_type, personnel=personnel, defenders_in_the_box_type=defenders_in_the_box_type, def_coverage_type=def_coverage_type)

Get Filmroom Plays with Advanced Filtering

Retrieves detailed play-by-play data with extensive filtering capabilities for film study.
Returns comprehensive play information including formations, personnel packages, game situations,
and detailed play descriptions. This endpoint supports advanced filtering by game situation,
player involvement, formation types, and tactical elements.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.binary_flag_enum import BinaryFlagEnum
from src.griddy.nfl.models.filmroom_plays_response import FilmroomPlaysResponse
from src.griddy.nfl.models.play_type_enum import PlayTypeEnum
from src.griddy.nfl.models.season_type_enum import SeasonTypeEnum
from src.griddy.nfl.models.week_slug_enum import WeekSlugEnum
from src.griddy.nfl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = src.griddy.nfl.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: NFLAuth
configuration = src.griddy.nfl.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with src.griddy.nfl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = src.griddy.nfl.FilmroomController(api_client)
    game_id = ['[\"f665fc10-311e-11f0-b670-ae1250fadad1\"]'] # List[str] | Filter by specific game IDs (supports multiple values) (optional)
    week_slug = [src.griddy.nfl.WeekSlugEnum()] # List[WeekSlugEnum] | Filter by week identifier (supports multiple values) (optional)
    season = [[2025]] # List[int] | Filter by season year (supports multiple values) (optional)
    season_type = [src.griddy.nfl.SeasonTypeEnum()] # List[SeasonTypeEnum] | Filter by season type (optional)
    nfl_id = ['[\"54517\"]'] # List[str] | Filter by player NFL ID (optional)
    quarter = [[1]] # List[int] | Filter by quarter (optional)
    down = [[1]] # List[int] | Filter by down (optional)
    yards_to_go_type = ['[\"SHORT\"]'] # List[str] | Filter by yards to go category (optional)
    touchdown = [src.griddy.nfl.BinaryFlagEnum()] # List[BinaryFlagEnum] | Filter for touchdown plays (1 = yes, 0 = no) (optional)
    rush10_plus_yards = [src.griddy.nfl.BinaryFlagEnum()] # List[BinaryFlagEnum] | Filter for rushing plays of 10+ yards (optional)
    fumble_lost = [src.griddy.nfl.BinaryFlagEnum()] # List[BinaryFlagEnum] | Filter for plays with fumbles lost (optional)
    fumble = [src.griddy.nfl.BinaryFlagEnum()] # List[BinaryFlagEnum] | Filter for plays with fumbles (optional)
    qb_alignment = ['[\"SHOTGUN\"]'] # List[str] | Filter by quarterback alignment (optional)
    redzone = [src.griddy.nfl.BinaryFlagEnum()] # List[BinaryFlagEnum] | Filter for red zone plays (optional)
    goal_to_go = [src.griddy.nfl.BinaryFlagEnum()] # List[BinaryFlagEnum] | Filter for goal-to-go situations (optional)
    pass_play = [src.griddy.nfl.BinaryFlagEnum()] # List[BinaryFlagEnum] | Filter for passing plays (optional)
    run_play = [src.griddy.nfl.BinaryFlagEnum()] # List[BinaryFlagEnum] | Filter for running plays (optional)
    play_type = [src.griddy.nfl.PlayTypeEnum()] # List[PlayTypeEnum] | Filter by specific play types (optional)
    attempt = [src.griddy.nfl.BinaryFlagEnum()] # List[BinaryFlagEnum] | Filter for passing attempts (optional)
    completion = [src.griddy.nfl.BinaryFlagEnum()] # List[BinaryFlagEnum] | Filter for completed passes (optional)
    interception = [src.griddy.nfl.BinaryFlagEnum()] # List[BinaryFlagEnum] | Filter for interceptions (optional)
    reception = [src.griddy.nfl.BinaryFlagEnum()] # List[BinaryFlagEnum] | Filter for receptions (optional)
    sack = [src.griddy.nfl.BinaryFlagEnum()] # List[BinaryFlagEnum] | Filter for sacks (optional)
    rec_motion = [src.griddy.nfl.BinaryFlagEnum()] # List[BinaryFlagEnum] | Filter by receiver motion (optional)
    target_location = ['[\"BETWEEN_HASHES\"]'] # List[str] | Filter by target location on field (optional)
    air_yard_type = ['[\"SHORT\"]'] # List[str] | Filter by air yards category (optional)
    dropback_time_type = ['[\"QUICK\"]'] # List[str] | Filter by dropback time (optional)
    pressure = [src.griddy.nfl.BinaryFlagEnum()] # List[BinaryFlagEnum] | Filter by quarterback pressure (optional)
    blitz = [src.griddy.nfl.BinaryFlagEnum()] # List[BinaryFlagEnum] | Filter by defensive blitz (optional)
    play_action = [src.griddy.nfl.BinaryFlagEnum()] # List[BinaryFlagEnum] | Filter by play action usage (optional)
    rush_direction = ['[\"INSIDE\"]'] # List[str] | Filter by rush direction (optional)
    run_stuff = [src.griddy.nfl.BinaryFlagEnum()] # List[BinaryFlagEnum] | Filter for stuffed runs (optional)
    receiver_alignment = ['[\"SLOT\"]'] # List[str] | Filter by receiver alignment (optional)
    separation_type = ['[\"OPEN\"]'] # List[str] | Filter by receiver separation (optional)
    personnel = ['[\"NICKEL\"]'] # List[str] | Filter by defensive personnel package (optional)
    defenders_in_the_box_type = ['[\"STACKED\"]'] # List[str] | Filter by defenders in the box (optional)
    def_coverage_type = ['[\"PRESS\"]'] # List[str] | Filter by defensive coverage type (optional)

    try:
        # Get Filmroom Plays with Advanced Filtering
        api_response = api_instance.get_filmroom_plays(game_id=game_id, week_slug=week_slug, season=season, season_type=season_type, nfl_id=nfl_id, quarter=quarter, down=down, yards_to_go_type=yards_to_go_type, touchdown=touchdown, rush10_plus_yards=rush10_plus_yards, fumble_lost=fumble_lost, fumble=fumble, qb_alignment=qb_alignment, redzone=redzone, goal_to_go=goal_to_go, pass_play=pass_play, run_play=run_play, play_type=play_type, attempt=attempt, completion=completion, interception=interception, reception=reception, sack=sack, rec_motion=rec_motion, target_location=target_location, air_yard_type=air_yard_type, dropback_time_type=dropback_time_type, pressure=pressure, blitz=blitz, play_action=play_action, rush_direction=rush_direction, run_stuff=run_stuff, receiver_alignment=receiver_alignment, separation_type=separation_type, personnel=personnel, defenders_in_the_box_type=defenders_in_the_box_type, def_coverage_type=def_coverage_type)
        print("The response of FilmroomController->get_filmroom_plays:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilmroomController->get_filmroom_plays: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | [**List[str]**](str.md)| Filter by specific game IDs (supports multiple values) | [optional] 
 **week_slug** | [**List[WeekSlugEnum]**](WeekSlugEnum.md)| Filter by week identifier (supports multiple values) | [optional] 
 **season** | [**List[int]**](int.md)| Filter by season year (supports multiple values) | [optional] 
 **season_type** | [**List[SeasonTypeEnum]**](SeasonTypeEnum.md)| Filter by season type | [optional] 
 **nfl_id** | [**List[str]**](str.md)| Filter by player NFL ID | [optional] 
 **quarter** | [**List[int]**](int.md)| Filter by quarter | [optional] 
 **down** | [**List[int]**](int.md)| Filter by down | [optional] 
 **yards_to_go_type** | [**List[str]**](str.md)| Filter by yards to go category | [optional] 
 **touchdown** | [**List[BinaryFlagEnum]**](BinaryFlagEnum.md)| Filter for touchdown plays (1 &#x3D; yes, 0 &#x3D; no) | [optional] 
 **rush10_plus_yards** | [**List[BinaryFlagEnum]**](BinaryFlagEnum.md)| Filter for rushing plays of 10+ yards | [optional] 
 **fumble_lost** | [**List[BinaryFlagEnum]**](BinaryFlagEnum.md)| Filter for plays with fumbles lost | [optional] 
 **fumble** | [**List[BinaryFlagEnum]**](BinaryFlagEnum.md)| Filter for plays with fumbles | [optional] 
 **qb_alignment** | [**List[str]**](str.md)| Filter by quarterback alignment | [optional] 
 **redzone** | [**List[BinaryFlagEnum]**](BinaryFlagEnum.md)| Filter for red zone plays | [optional] 
 **goal_to_go** | [**List[BinaryFlagEnum]**](BinaryFlagEnum.md)| Filter for goal-to-go situations | [optional] 
 **pass_play** | [**List[BinaryFlagEnum]**](BinaryFlagEnum.md)| Filter for passing plays | [optional] 
 **run_play** | [**List[BinaryFlagEnum]**](BinaryFlagEnum.md)| Filter for running plays | [optional] 
 **play_type** | [**List[PlayTypeEnum]**](PlayTypeEnum.md)| Filter by specific play types | [optional] 
 **attempt** | [**List[BinaryFlagEnum]**](BinaryFlagEnum.md)| Filter for passing attempts | [optional] 
 **completion** | [**List[BinaryFlagEnum]**](BinaryFlagEnum.md)| Filter for completed passes | [optional] 
 **interception** | [**List[BinaryFlagEnum]**](BinaryFlagEnum.md)| Filter for interceptions | [optional] 
 **reception** | [**List[BinaryFlagEnum]**](BinaryFlagEnum.md)| Filter for receptions | [optional] 
 **sack** | [**List[BinaryFlagEnum]**](BinaryFlagEnum.md)| Filter for sacks | [optional] 
 **rec_motion** | [**List[BinaryFlagEnum]**](BinaryFlagEnum.md)| Filter by receiver motion | [optional] 
 **target_location** | [**List[str]**](str.md)| Filter by target location on field | [optional] 
 **air_yard_type** | [**List[str]**](str.md)| Filter by air yards category | [optional] 
 **dropback_time_type** | [**List[str]**](str.md)| Filter by dropback time | [optional] 
 **pressure** | [**List[BinaryFlagEnum]**](BinaryFlagEnum.md)| Filter by quarterback pressure | [optional] 
 **blitz** | [**List[BinaryFlagEnum]**](BinaryFlagEnum.md)| Filter by defensive blitz | [optional] 
 **play_action** | [**List[BinaryFlagEnum]**](BinaryFlagEnum.md)| Filter by play action usage | [optional] 
 **rush_direction** | [**List[str]**](str.md)| Filter by rush direction | [optional] 
 **run_stuff** | [**List[BinaryFlagEnum]**](BinaryFlagEnum.md)| Filter for stuffed runs | [optional] 
 **receiver_alignment** | [**List[str]**](str.md)| Filter by receiver alignment | [optional] 
 **separation_type** | [**List[str]**](str.md)| Filter by receiver separation | [optional] 
 **personnel** | [**List[str]**](str.md)| Filter by defensive personnel package | [optional] 
 **defenders_in_the_box_type** | [**List[str]**](str.md)| Filter by defenders in the box | [optional] 
 **def_coverage_type** | [**List[str]**](str.md)| Filter by defensive coverage type | [optional] 

### Return type

[**FilmroomPlaysResponse**](FilmroomPlaysResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved filmroom plays |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**403** | Forbidden - Insufficient permissions for secured content |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

