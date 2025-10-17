# src.griddy.nfl.FootballController

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_draft_info**](FootballController.md#get_draft_info) | **GET** /football/v2/draft/{year} | Get Draft Information
[**get_football_box_score**](FootballController.md#get_football_box_score) | **GET** /football/v2/games/{gameId}/boxscore | Get Game Box Score (Football API)
[**get_football_games**](FootballController.md#get_football_games) | **GET** /football/v2/games/season/{season}/seasonType/{seasonType}/week/{week} | Get Games by Season, Type, and Week
[**get_injury_reports**](FootballController.md#get_injury_reports) | **GET** /football/v2/injuries | Get Injury Reports
[**get_live_game_stats**](FootballController.md#get_live_game_stats) | **GET** /football/v2/stats/live/game-summaries | Get Live Game Statistics
[**get_play_by_play**](FootballController.md#get_play_by_play) | **GET** /football/v2/games/{gameId}/playbyplay | Get Play-by-Play Data
[**get_player_details**](FootballController.md#get_player_details) | **GET** /football/v2/players/{playerId} | Get Player Details
[**get_players_team_roster**](FootballController.md#get_players_team_roster) | **GET** /football/v2/players/teams/{teamId}/roster | Get Team Roster
[**get_season_player_stats**](FootballController.md#get_season_player_stats) | **GET** /football/v2/stats/players/season | Get Season Player Statistics
[**get_season_weeks**](FootballController.md#get_season_weeks) | **GET** /football/v2/weeks/season/{season} | Get Season Weeks
[**get_standings**](FootballController.md#get_standings) | **GET** /football/v2/standings | Get Standings
[**get_transactions**](FootballController.md#get_transactions) | **GET** /football/v2/transactions | Get Transactions
[**get_venues**](FootballController.md#get_venues) | **GET** /football/v2/venues | Get NFL Venues
[**get_weekly_game_details**](FootballController.md#get_weekly_game_details) | **GET** /football/v2/experience/weekly-game-details | Get Weekly Game Details with Standings


# **get_draft_info**
> DraftResponse get_draft_info(year, round=round, team_id=team_id)

Get Draft Information

Retrieves draft information for a specific year including all rounds,
picks, traded picks, and compensatory selections.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.draft_response import DraftResponse
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
    api_instance = src.griddy.nfl.FootballController(api_client)
    year = 2025 # int | Draft year
    round = 56 # int | Filter by round (optional)
    team_id = 'team_id_example' # str | Filter by team (optional)

    try:
        # Get Draft Information
        api_response = api_instance.get_draft_info(year, round=round, team_id=team_id)
        print("The response of FootballController->get_draft_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FootballController->get_draft_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Draft year | 
 **round** | **int**| Filter by round | [optional] 
 **team_id** | **str**| Filter by team | [optional] 

### Return type

[**DraftResponse**](DraftResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved draft information |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**404** | Draft year not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_football_box_score**
> BoxScoreResponse get_football_box_score(game_id)

Get Game Box Score (Football API)

Retrieves comprehensive box score data for a specific game including
team statistics, individual player statistics, and scoring summary.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.box_score_response import BoxScoreResponse
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
    api_instance = src.griddy.nfl.FootballController(api_client)
    game_id = 'game_id_example' # str | Game identifier (UUID)

    try:
        # Get Game Box Score (Football API)
        api_response = api_instance.get_football_box_score(game_id)
        print("The response of FootballController->get_football_box_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FootballController->get_football_box_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**| Game identifier (UUID) | 

### Return type

[**BoxScoreResponse**](BoxScoreResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved box score |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**404** | Game not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_football_games**
> FootballGamesResponse get_football_games(season, season_type, week, with_external_ids=with_external_ids)

Get Games by Season, Type, and Week

Retrieves game information for a specific season, season type, and week from the Football API.
This endpoint provides core game data with external IDs.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.football_games_response import FootballGamesResponse
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
    api_instance = src.griddy.nfl.FootballController(api_client)
    season = 2025 # int | Season year
    season_type = src.griddy.nfl.SeasonTypeEnum() # SeasonTypeEnum | Type of season
    week = 4 # int | Week number
    with_external_ids = False # bool | Include external IDs in response (optional) (default to False)

    try:
        # Get Games by Season, Type, and Week
        api_response = api_instance.get_football_games(season, season_type, week, with_external_ids=with_external_ids)
        print("The response of FootballController->get_football_games:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FootballController->get_football_games: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**SeasonTypeEnum**](.md)| Type of season | 
 **week** | **int**| Week number | 
 **with_external_ids** | **bool**| Include external IDs in response | [optional] [default to False]

### Return type

[**FootballGamesResponse**](FootballGamesResponse.md)

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
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_injury_reports**
> InjuryReportResponse get_injury_reports(season, week, team_id=team_id)

Get Injury Reports

Retrieves current injury reports for all teams or specific teams
with injury status, designation, and practice participation.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.injury_report_response import InjuryReportResponse
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
    api_instance = src.griddy.nfl.FootballController(api_client)
    season = 2025 # int | Season year
    week = 4 # int | Week number
    team_id = 'team_id_example' # str | Filter by specific team (optional)

    try:
        # Get Injury Reports
        api_response = api_instance.get_injury_reports(season, week, team_id=team_id)
        print("The response of FootballController->get_injury_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FootballController->get_injury_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **week** | **int**| Week number | 
 **team_id** | **str**| Filter by specific team | [optional] 

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
**200** | Successfully retrieved injury reports |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_live_game_stats**
> GameStatsResponse get_live_game_stats(season, season_type, week)

Get Live Game Statistics

Retrieves live game statistics and summaries for games in progress or completed games.
Provides real-time statistical data for specified season, type, and week.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.game_stats_response import GameStatsResponse
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
    api_instance = src.griddy.nfl.FootballController(api_client)
    season = 2025 # int | Season year
    season_type = src.griddy.nfl.SeasonTypeEnum() # SeasonTypeEnum | Type of season
    week = 4 # int | Week number

    try:
        # Get Live Game Statistics
        api_response = api_instance.get_live_game_stats(season, season_type, week)
        print("The response of FootballController->get_live_game_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FootballController->get_live_game_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**SeasonTypeEnum**](.md)| Type of season | 
 **week** | **int**| Week number | 

### Return type

[**GameStatsResponse**](GameStatsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved game statistics |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_play_by_play**
> PlayByPlayResponse get_play_by_play(game_id, include_penalties=include_penalties, include_formations=include_formations)

Get Play-by-Play Data

Retrieves detailed play-by-play data for a specific game including
all plays, drives, scoring events, and key statistics.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.play_by_play_response import PlayByPlayResponse
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
    api_instance = src.griddy.nfl.FootballController(api_client)
    game_id = 'game_id_example' # str | Game identifier (UUID)
    include_penalties = True # bool | Include penalty details (optional) (default to True)
    include_formations = False # bool | Include offensive/defensive formations (optional) (default to False)

    try:
        # Get Play-by-Play Data
        api_response = api_instance.get_play_by_play(game_id, include_penalties=include_penalties, include_formations=include_formations)
        print("The response of FootballController->get_play_by_play:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FootballController->get_play_by_play: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**| Game identifier (UUID) | 
 **include_penalties** | **bool**| Include penalty details | [optional] [default to True]
 **include_formations** | **bool**| Include offensive/defensive formations | [optional] [default to False]

### Return type

[**PlayByPlayResponse**](PlayByPlayResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved play-by-play data |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**404** | Game not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_details**
> PlayerDetail get_player_details(player_id, season=season)

Get Player Details

Retrieves detailed information about a specific player including biography,
career statistics, and current season performance.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.player_detail import PlayerDetail
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
    api_instance = src.griddy.nfl.FootballController(api_client)
    player_id = '2560726' # str | Player identifier
    season = 2025 # int | Season for statistics (defaults to current) (optional)

    try:
        # Get Player Details
        api_response = api_instance.get_player_details(player_id, season=season)
        print("The response of FootballController->get_player_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FootballController->get_player_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| Player identifier | 
 **season** | **int**| Season for statistics (defaults to current) | [optional] 

### Return type

[**PlayerDetail**](PlayerDetail.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved player details |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**404** | Player not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_players_team_roster**
> RosterResponse get_players_team_roster(team_id, season, include_stats=include_stats)

Get Team Roster

Retrieves the complete roster for a specific team including active, practice squad, and injured reserve players with detailed player information.

### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.roster_response import RosterResponse
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
    api_instance = src.griddy.nfl.FootballController(api_client)
    team_id = '10403800-517c-7b8c-65a3-c61b95d86123' # str | Team identifier (UUID)
    season = 2025 # int | Season year
    include_stats = False # bool | Include current season statistics (optional) (default to False)

    try:
        # Get Team Roster
        api_response = api_instance.get_players_team_roster(team_id, season, include_stats=include_stats)
        print("The response of FootballController->get_players_team_roster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FootballController->get_players_team_roster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| Team identifier (UUID) | 
 **season** | **int**| Season year | 
 **include_stats** | **bool**| Include current season statistics | [optional] [default to False]

### Return type

[**RosterResponse**](RosterResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved roster |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**404** | Team not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_season_player_stats**
> PlayerStatsResponse get_season_player_stats(season, season_type, position=position, team_id=team_id, stat_category=stat_category, sort=sort, limit=limit, offset=offset)

Get Season Player Statistics

Retrieves aggregated player statistics for a specific season with filtering
options by position, team, and statistical categories.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.player_stats_response import PlayerStatsResponse
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
    api_instance = src.griddy.nfl.FootballController(api_client)
    season = 2025 # int | Season year
    season_type = src.griddy.nfl.SeasonTypeEnum() # SeasonTypeEnum | Type of season
    position = 'position_example' # str | Filter by position group (optional)
    team_id = 'team_id_example' # str | Filter by team (optional)
    stat_category = 'passing' # str | Statistical category to retrieve (optional)
    sort = 'passingYards:desc' # str | Sort field and order (optional)
    limit = 50 # int | Maximum number of results (optional) (default to 50)
    offset = 0 # int | Offset for pagination (optional) (default to 0)

    try:
        # Get Season Player Statistics
        api_response = api_instance.get_season_player_stats(season, season_type, position=position, team_id=team_id, stat_category=stat_category, sort=sort, limit=limit, offset=offset)
        print("The response of FootballController->get_season_player_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FootballController->get_season_player_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**SeasonTypeEnum**](.md)| Type of season | 
 **position** | **str**| Filter by position group | [optional] 
 **team_id** | **str**| Filter by team | [optional] 
 **stat_category** | **str**| Statistical category to retrieve | [optional] 
 **sort** | **str**| Sort field and order | [optional] 
 **limit** | **int**| Maximum number of results | [optional] [default to 50]
 **offset** | **int**| Offset for pagination | [optional] [default to 0]

### Return type

[**PlayerStatsResponse**](PlayerStatsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved player statistics |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_season_weeks**
> WeeksResponse get_season_weeks(season, limit=limit)

Get Season Weeks

Retrieves all weeks for a specific season including preseason, regular season, and postseason. Includes bye team information for each week.

### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.weeks_response import WeeksResponse
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
    api_instance = src.griddy.nfl.FootballController(api_client)
    season = 2025 # int | Season year
    limit = 20 # int | Maximum number of weeks to return (optional) (default to 20)

    try:
        # Get Season Weeks
        api_response = api_instance.get_season_weeks(season, limit=limit)
        print("The response of FootballController->get_season_weeks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FootballController->get_season_weeks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **limit** | **int**| Maximum number of weeks to return | [optional] [default to 20]

### Return type

[**WeeksResponse**](WeeksResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved weeks |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_standings**
> StandingsResponse get_standings(season, season_type, week, limit=limit)

Get Standings

Retrieves team standings for a specific season, season type, and week.
Includes division, conference, and overall standings with detailed statistics.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.season_type_enum import SeasonTypeEnum
from src.griddy.nfl.models.standings_response import StandingsResponse
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
    api_instance = src.griddy.nfl.FootballController(api_client)
    season = 2025 # int | Season year
    season_type = src.griddy.nfl.SeasonTypeEnum() # SeasonTypeEnum | Type of season
    week = 3 # int | Week number
    limit = 20 # int | Maximum number of results to return (optional) (default to 20)

    try:
        # Get Standings
        api_response = api_instance.get_standings(season, season_type, week, limit=limit)
        print("The response of FootballController->get_standings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FootballController->get_standings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **season_type** | [**SeasonTypeEnum**](.md)| Type of season | 
 **week** | **int**| Week number | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 20]

### Return type

[**StandingsResponse**](StandingsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved standings |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> TransactionsResponse get_transactions(start_date=start_date, end_date=end_date, team_id=team_id, transaction_type=transaction_type, limit=limit)

Get Transactions

Retrieves recent transactions including trades, signings, releases,
practice squad moves, and injured reserve designations.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.transactions_response import TransactionsResponse
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
    api_instance = src.griddy.nfl.FootballController(api_client)
    start_date = 'Tue Dec 31 19:00:00 EST 2024' # date | Start date for transactions (ISO 8601) (optional)
    end_date = 'Tue Sep 23 20:00:00 EDT 2025' # date | End date for transactions (ISO 8601) (optional)
    team_id = 'team_id_example' # str | Filter by team (optional)
    transaction_type = 'transaction_type_example' # str | Type of transaction (optional)
    limit = 20 # int | Maximum number of results (optional) (default to 20)

    try:
        # Get Transactions
        api_response = api_instance.get_transactions(start_date=start_date, end_date=end_date, team_id=team_id, transaction_type=transaction_type, limit=limit)
        print("The response of FootballController->get_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FootballController->get_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**| Start date for transactions (ISO 8601) | [optional] 
 **end_date** | **date**| End date for transactions (ISO 8601) | [optional] 
 **team_id** | **str**| Filter by team | [optional] 
 **transaction_type** | **str**| Type of transaction | [optional] 
 **limit** | **int**| Maximum number of results | [optional] [default to 20]

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved transactions |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_venues**
> VenuesResponse get_venues(season, limit=limit)

Get NFL Venues

Retrieves information about all NFL stadiums and venues, including international venues.
Provides venue details such as addresses, locations, and territories.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.venues_response import VenuesResponse
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
    api_instance = src.griddy.nfl.FootballController(api_client)
    season = 2025 # int | Season year
    limit = 20 # int | Maximum number of venues to return (optional) (default to 20)

    try:
        # Get NFL Venues
        api_response = api_instance.get_venues(season, limit=limit)
        print("The response of FootballController->get_venues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FootballController->get_venues: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **limit** | **int**| Maximum number of venues to return | [optional] [default to 20]

### Return type

[**VenuesResponse**](VenuesResponse.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved venues |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_weekly_game_details**
> List[WeeklyGameDetail] get_weekly_game_details(season, type, week, include_drive_chart=include_drive_chart, include_replays=include_replays, include_standings=include_standings, include_tagged_videos=include_tagged_videos)

Get Weekly Game Details with Standings

Retrieves detailed game information for a specific week including team standings,
drive charts, replays, and tagged videos.


### Example

* Bearer Authentication (NFLAuth):

```python
import src.griddy.nfl
from src.griddy.nfl.models.season_type_enum import SeasonTypeEnum
from src.griddy.nfl.models.weekly_game_detail import WeeklyGameDetail
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
    api_instance = src.griddy.nfl.FootballController(api_client)
    season = 2025 # int | Season year
    type = src.griddy.nfl.SeasonTypeEnum() # SeasonTypeEnum | Season type
    week = 4 # int | Week number
    include_drive_chart = False # bool | Include drive chart data (optional) (default to False)
    include_replays = False # bool | Include replay videos (optional) (default to False)
    include_standings = False # bool | Include team standings (optional) (default to False)
    include_tagged_videos = False # bool | Include tagged video content (optional) (default to False)

    try:
        # Get Weekly Game Details with Standings
        api_response = api_instance.get_weekly_game_details(season, type, week, include_drive_chart=include_drive_chart, include_replays=include_replays, include_standings=include_standings, include_tagged_videos=include_tagged_videos)
        print("The response of FootballController->get_weekly_game_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FootballController->get_weekly_game_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season year | 
 **type** | [**SeasonTypeEnum**](.md)| Season type | 
 **week** | **int**| Week number | 
 **include_drive_chart** | **bool**| Include drive chart data | [optional] [default to False]
 **include_replays** | **bool**| Include replay videos | [optional] [default to False]
 **include_standings** | **bool**| Include team standings | [optional] [default to False]
 **include_tagged_videos** | **bool**| Include tagged video content | [optional] [default to False]

### Return type

[**List[WeeklyGameDetail]**](WeeklyGameDetail.md)

### Authorization

[NFLAuth](../README.md#NFLAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved weekly game details |  -  |
**400** | Invalid request parameters |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

