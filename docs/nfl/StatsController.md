# src.griddy.nfl.StatsController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_game_team_rankings**](StatsController.md#get_game_team_rankings) | **GET** /api/stats/game/team-rankings | Get Team Rankings for Game
[**get_gamecenter**](StatsController.md#get_gamecenter) | **GET** /api/stats/gamecenter | Get Gamecenter Statistics
[**get_multiple_rankings_all_teams**](StatsController.md#get_multiple_rankings_all_teams) | **GET** /api/stats/multiple-rankings/all-teams | Get Multiple Rankings for All Teams
[**get_stats_boxscore**](StatsController.md#get_stats_boxscore) | **GET** /api/stats/boxscore | Get Game Boxscore (Stats API)


# **get_game_team_rankings**
> TeamRankingsResponse get_game_team_rankings(season, season_type, away_team_id, home_team_id, week)

Get Team Rankings for Game

Retrieves comprehensive statistical rankings for both teams in a specific game.
Returns 300+ statistical categories with rankings for offensive, defensive, and special teams performance.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.season_type_enum import SeasonTypeEnum
from src.griddy.nfl.models.team_rankings_response import TeamRankingsResponse
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
    api_instance = src.griddy.nfl.StatsController(api_client)
    season = 2025 # int | Season year
    season_type = src.griddy.nfl.SeasonTypeEnum() # SeasonTypeEnum | Type of season
    away_team_id = '10403000-5851-f9d5-da45-78365a05b6b0' # str | Away team UUID
    home_team_id = '10403900-8251-6892-d81c-4348525c2d47' # str | Home team UUID
    week = 4 # int | Week number

    try:
        # Get Team Rankings for Game
        api_response = api_instance.get_game_team_rankings(season, season_type, away_team_id, home_team_id, week)
        print("The response of StatsController->get_game_team_rankings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsController->get_game_team_rankings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**SeasonTypeEnum**](.md)| Type of season | 
 **away_team_id** | **str**| Away team UUID | 
 **home_team_id** | **str**| Home team UUID | 
 **week** | **int**| Week number | 

### Return type

[**TeamRankingsResponse**](TeamRankingsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved team rankings |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gamecenter**
> GamecenterResponse get_gamecenter(game_id)

Get Gamecenter Statistics

Retrieves advanced game statistics including passer zones, receiver separation,
pass rush metrics, and performance leaders for a specific game.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.gamecenter_response import GamecenterResponse
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
    api_instance = src.griddy.nfl.StatsController(api_client)
    game_id = '2025092800' # str | Game identifier

    try:
        # Get Gamecenter Statistics
        api_response = api_instance.get_gamecenter(game_id)
        print("The response of StatsController->get_gamecenter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsController->get_gamecenter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**| Game identifier | 

### Return type

[**GamecenterResponse**](GamecenterResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved gamecenter data |  -  |
**400** | Invalid game ID |  -  |
**401** | Unauthorized |  -  |
**404** | Game not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multiple_rankings_all_teams**
> List[MultipleRankingsCategory] get_multiple_rankings_all_teams(season, season_type, stat0, stat1=stat1, stat2=stat2, stat3=stat3, stat4=stat4)

Get Multiple Rankings for All Teams

Retrieves rankings for all 32 NFL teams across multiple specified statistical categories.
Allows comparison of teams across up to 5 different statistics simultaneously.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.multiple_rankings_category import MultipleRankingsCategory
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
    api_instance = src.griddy.nfl.StatsController(api_client)
    season = 2025 # int | Season year
    season_type = src.griddy.nfl.SeasonTypeEnum() # SeasonTypeEnum | Type of season
    stat0 = 'scoring-averagePointsScored' # str | First statistical category
    stat1 = 'offense-yardsPerGame' # str | Second statistical category (optional)
    stat2 = 'offense-rushYardsPerGame' # str | Third statistical category (optional)
    stat3 = 'offense-passYardsPerGame' # str | Fourth statistical category (optional)
    stat4 = 'misc-netTurnovers' # str | Fifth statistical category (optional)

    try:
        # Get Multiple Rankings for All Teams
        api_response = api_instance.get_multiple_rankings_all_teams(season, season_type, stat0, stat1=stat1, stat2=stat2, stat3=stat3, stat4=stat4)
        print("The response of StatsController->get_multiple_rankings_all_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsController->get_multiple_rankings_all_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**SeasonTypeEnum**](.md)| Type of season | 
 **stat0** | **str**| First statistical category | 
 **stat1** | **str**| Second statistical category | [optional] 
 **stat2** | **str**| Third statistical category | [optional] 
 **stat3** | **str**| Fourth statistical category | [optional] 
 **stat4** | **str**| Fifth statistical category | [optional] 

### Return type

[**List[MultipleRankingsCategory]**](MultipleRankingsCategory.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved rankings |  -  |
**400** | Invalid parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats_boxscore**
> TeamBoxScore get_stats_boxscore(game_id)

Get Game Boxscore (Stats API)

Retrieves comprehensive boxscore data for a specific game including team statistics,
individual player statistics, and scoring summary. Returns empty arrays for future games.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.team_box_score import TeamBoxScore
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
    api_instance = src.griddy.nfl.StatsController(api_client)
    game_id = '2025092800' # str | Game identifier (10-digit format YYYYMMDDNN)

    try:
        # Get Game Boxscore (Stats API)
        api_response = api_instance.get_stats_boxscore(game_id)
        print("The response of StatsController->get_stats_boxscore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsController->get_stats_boxscore: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**| Game identifier (10-digit format YYYYMMDDNN) | 

### Return type

[**TeamBoxScore**](TeamBoxScore.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved boxscore |  -  |
**400** | Invalid game ID |  -  |
**401** | Unauthorized |  -  |
**404** | Game not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

