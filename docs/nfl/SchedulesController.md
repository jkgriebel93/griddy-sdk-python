# src.griddy.nfl.SchedulesController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_game_matchup_rankings**](SchedulesController.md#get_game_matchup_rankings) | **GET** /api/schedules/game/matchup/rankings | Get Game Matchup Rankings
[**get_scheduled_game**](SchedulesController.md#get_scheduled_game) | **GET** /api/schedules/game | Get Single Game Details
[**get_scheduled_games**](SchedulesController.md#get_scheduled_games) | **GET** /api/schedules/games | Get Games by Week
[**get_team_injuries**](SchedulesController.md#get_team_injuries) | **GET** /api/schedules/game/team/injuries | Get Team Injuries for Game Week


# **get_game_matchup_rankings**
> MatchupRankingsResponse get_game_matchup_rankings(game_id)

Get Game Matchup Rankings

Retrieves comprehensive matchup rankings and statistical comparisons for both teams in a specific game.
Returns offensive, defensive, and special teams rankings with Z-scores and advantage ratings
for various statistical categories.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.matchup_rankings_response import MatchupRankingsResponse
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
    api_instance = src.griddy.nfl.SchedulesController(api_client)
    game_id = '2025092500' # str | Game identifier (10-digit format YYYYMMDDNN)

    try:
        # Get Game Matchup Rankings
        api_response = api_instance.get_game_matchup_rankings(game_id)
        print("The response of SchedulesController->get_game_matchup_rankings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesController->get_game_matchup_rankings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**| Game identifier (10-digit format YYYYMMDDNN) | 

### Return type

[**MatchupRankingsResponse**](MatchupRankingsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved matchup rankings |  -  |
**400** | Invalid game ID |  -  |
**401** | Unauthorized |  -  |
**404** | Game not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled_game**
> GameDetail get_scheduled_game(game_id)

Get Single Game Details

Retrieves detailed information for a specific game by its ID.
Returns comprehensive game data including teams, score, venue, broadcast information,
and current game status.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.game_detail import GameDetail
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
    api_instance = src.griddy.nfl.SchedulesController(api_client)
    game_id = 'f665fc10-311e-11f0-b670-ae1250fadad1' # str | Game identifier (UUID format)

    try:
        # Get Single Game Details
        api_response = api_instance.get_scheduled_game(game_id)
        print("The response of SchedulesController->get_scheduled_game:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesController->get_scheduled_game: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**| Game identifier (UUID format) | 

### Return type

[**GameDetail**](GameDetail.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved game details |  -  |
**400** | Invalid game ID |  -  |
**401** | Unauthorized |  -  |
**404** | Game not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled_games**
> GamesResponse get_scheduled_games(season, season_type, week)

Get Games by Week

Retrieves all games for a specific season, season type, and week.
Returns comprehensive game data including teams, venues, broadcast information,
and ticket details for all games in the specified week.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.games_response import GamesResponse
from src.griddy.nfl.models.season_type_enum import SeasonTypeEnum
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
    api_instance = src.griddy.nfl.SchedulesController(api_client)
    season = 2025 # int | Season year
    season_type = src.griddy.nfl.SeasonTypeEnum() # SeasonTypeEnum | Type of season
    week = 3 # int | Week number within the season

    try:
        # Get Games by Week
        api_response = api_instance.get_scheduled_games(season, season_type, week)
        print("The response of SchedulesController->get_scheduled_games:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesController->get_scheduled_games: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**SeasonTypeEnum**](.md)| Type of season | 
 **week** | **int**| Week number within the season | 

### Return type

[**GamesResponse**](GamesResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved games |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized - Invalid or missing authentication token |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_injuries**
> InjuryReportResponse get_team_injuries(season, season_type, team_id, week)

Get Team Injuries for Game Week

Retrieves injury report information for a specific team in a given week.
Returns player injury status and details for the specified team and week.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.injury_report_response import InjuryReportResponse
from src.griddy.nfl.models.season_type_enum import SeasonTypeEnum
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
    api_instance = src.griddy.nfl.SchedulesController(api_client)
    season = 2025 # int | Season year
    season_type = src.griddy.nfl.SeasonTypeEnum() # SeasonTypeEnum | Type of season
    team_id = '10403000-5851-f9d5-da45-78365a05b6b0' # str | Team identifier (UUID format)
    week = 4 # int | Week number within the season

    try:
        # Get Team Injuries for Game Week
        api_response = api_instance.get_team_injuries(season, season_type, team_id, week)
        print("The response of SchedulesController->get_team_injuries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesController->get_team_injuries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**SeasonTypeEnum**](.md)| Type of season | 
 **team_id** | **str**| Team identifier (UUID format) | 
 **week** | **int**| Week number within the season | 

### Return type

[**InjuryReportResponse**](InjuryReportResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved injury report |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**404** | Team not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

