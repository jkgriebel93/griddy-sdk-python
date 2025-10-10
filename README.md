# griddy-nfl

Developer-friendly & type-safe Python SDK specifically catered to leverage *griddy-nfl* API.

<div align="left" style="margin-bottom: 0;">
    <a href="https://www.speakeasy.com/?utm_source=griddy-nfl&utm_campaign=python" class="badge-link">
        <span class="badge-container">
            <span class="badge-icon-section">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 30 30" fill="none" style="vertical-align: middle;"><title>Speakeasy Logo</title><path fill="currentColor" d="m20.639 27.548-19.17-2.724L0 26.1l20.639 2.931 8.456-7.336-1.468-.208-6.988 6.062Z"></path><path fill="currentColor" d="m20.639 23.1 8.456-7.336-1.468-.207-6.988 6.06-6.84-.972-9.394-1.333-2.936-.417L0 20.169l2.937.416L0 23.132l20.639 2.931 8.456-7.334-1.468-.208-6.986 6.062-9.78-1.39 1.468-1.273 8.31 1.18Z"></path><path fill="currentColor" d="m20.639 18.65-19.17-2.724L0 17.201l20.639 2.931 8.456-7.334-1.468-.208-6.988 6.06Z"></path><path fill="currentColor" d="M27.627 6.658 24.69 9.205 20.64 12.72l-7.923-1.126L1.469 9.996 0 11.271l11.246 1.596-1.467 1.275-8.311-1.181L0 14.235l20.639 2.932 8.456-7.334-2.937-.418 2.937-2.549-1.468-.208Z"></path><path fill="currentColor" d="M29.095 3.902 8.456.971 0 8.305l20.639 2.934 8.456-7.337Z"></path></svg>
            </span>
            <span class="badge-text badge-text-section">BUILT BY SPEAKEASY</span>
        </span>
    </a>
    <a href="https://opensource.org/licenses/MIT" class="badge-link">
        <span class="badge-container blue">
            <span class="badge-text badge-text-section">LICENSE // MIT</span>
        </span>
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/thistle-grow/griddy). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

NFL REST APIs: Regular API - NFL's public API for accessing game schedules, team information, standings, statistics, and venue data. This API provides comprehensive access to NFL data including real-time game information, team rosters, seasonal statistics, and historical data. The NFL Pro API is for accessing advanced statistics, film room content, player data, and fantasy information. This API provides comprehensive access to NFL Pro features including Next Gen Stats, Film Room analysis, player projections, and game insights.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [griddy-nfl](#griddy-nfl)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add git+<UNSET>.git
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from griddy-nfl python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "griddy-nfl",
# ]
# ///

from griddy.nfl import GriddyNFL

sdk = GriddyNFL(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from griddy.nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.content.get_game_preview(season=2025, season_type=models.SeasonTypeEnum.REG, week=4, visitor_display_name="Minnesota Vikings", home_display_name="Pittsburgh Steelers")

    assert res is not None

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from griddy.nfl import GriddyNFL, models

async def main():

    async with GriddyNFL(
        server_url="https://api.example.com",
        nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as griddy_nfl:

        res = await griddy_nfl.content.get_game_preview_async(season=2025, season_type=models.SeasonTypeEnum.REG, week=4, visitor_display_name="Minnesota Vikings", home_display_name="Pittsburgh Steelers")

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name       | Type | Scheme      |
| ---------- | ---- | ----------- |
| `nfl_auth` | http | HTTP Bearer |

To authenticate with the API the `nfl_auth` parameter must be set when initializing the SDK client instance. For example:
```python
from griddy.nfl import GriddyNFL, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.content.get_game_preview(season=2025, season_type=models.SeasonTypeEnum.REG, week=4, visitor_display_name="Minnesota Vikings", home_display_name="Pittsburgh Steelers")

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [authentication](docs/sdks/authentication/README.md)

* [generate_token](docs/sdks/authentication/README.md#generate_token) - Generate Initial Access Token
* [refresh_token](docs/sdks/authentication/README.md#refresh_token) - Refresh Access Token

### [betting](docs/sdks/betting/README.md)

* [get_weekly_betting_odds](docs/sdks/betting/README.md#get_weekly_betting_odds) - Get Weekly Betting Odds

### [content](docs/sdks/content/README.md)

* [get_game_preview](docs/sdks/content/README.md#get_game_preview) - Get Game Preview Content
* [get_home_film_cards](docs/sdks/content/README.md#get_home_film_cards) - Get Home Film Cards
* [get_game_insights](docs/sdks/content/README.md#get_game_insights) - Get Game-Specific Insights

### [content_insights](docs/sdks/contentinsights/README.md)

* [get_season_content_insights](docs/sdks/contentinsights/README.md#get_season_content_insights) - Get Season Content Insights

### [defensive_pass_rush_statistics](docs/sdks/defensivepassrushstatistics/README.md)

* [get_defensive_pass_rush_stats_by_season](docs/sdks/defensivepassrushstatistics/README.md#get_defensive_pass_rush_stats_by_season) - Get Defensive Pass Rush Statistics by Season

### [defensive_player_overview](docs/sdks/defensiveplayeroverview/README.md)

* [get_defensive_overview_stats_by_season](docs/sdks/defensiveplayeroverview/README.md#get_defensive_overview_stats_by_season) - Get Defensive Player Overview Statistics by Season

### [defensive_statistics](docs/sdks/defensivestatistics/README.md)

* [get_defensive_stats_by_season](docs/sdks/defensivestatistics/README.md#get_defensive_stats_by_season) - Get Defensive Player Statistics by Season

### [experience](docs/sdks/experience/README.md)

* [get_experience_games](docs/sdks/experience/README.md#get_experience_games) - Get Games by Season and Week
* [get_experience_teams](docs/sdks/experience/README.md#get_experience_teams) - Get All Teams

### [fantasy_statistics](docs/sdks/fantasystatistics/README.md)

* [get_fantasy_stats_by_season](docs/sdks/fantasystatistics/README.md#get_fantasy_stats_by_season) - Get Fantasy Football Statistics by Season

### [filmroom](docs/sdks/filmroom/README.md)

* [get_filmroom_plays](docs/sdks/filmroom/README.md#get_filmroom_plays) - Get Filmroom Plays with Advanced Filtering

### [football](docs/sdks/football/README.md)

* [get_draft_info](docs/sdks/football/README.md#get_draft_info) - Get Draft Information
* [get_weekly_game_details](docs/sdks/football/README.md#get_weekly_game_details) - Get Weekly Game Details with Standings
* [get_football_games](docs/sdks/football/README.md#get_football_games) - Get Games by Season, Type, and Week
* [get_football_box_score](docs/sdks/football/README.md#get_football_box_score) - Get Game Box Score (Football API)
* [get_play_by_play](docs/sdks/football/README.md#get_play_by_play) - Get Play-by-Play Data
* [get_injury_reports](docs/sdks/football/README.md#get_injury_reports) - Get Injury Reports
* [get_players_team_roster](docs/sdks/football/README.md#get_players_team_roster) - Get Team Roster
* [get_player_details](docs/sdks/football/README.md#get_player_details) - Get Player Details
* [get_standings](docs/sdks/football/README.md#get_standings) - Get Standings
* [get_live_game_stats](docs/sdks/football/README.md#get_live_game_stats) - Get Live Game Statistics
* [get_season_player_stats](docs/sdks/football/README.md#get_season_player_stats) - Get Season Player Statistics
* [get_transactions](docs/sdks/football/README.md#get_transactions) - Get Transactions
* [get_venues](docs/sdks/football/README.md#get_venues) - Get NFL Venues
* [get_season_weeks](docs/sdks/football/README.md#get_season_weeks) - Get Season Weeks

### [player_passing_statistics](docs/sdks/playerpassingstatistics/README.md)

* [get_player_passing_stats_by_week](docs/sdks/playerpassingstatistics/README.md#get_player_passing_stats_by_week) - Get Player Passing Statistics by Week

### [player_receiving_statistics](docs/sdks/playerreceivingstatistics/README.md)

* [get_player_receiving_stats_by_season](docs/sdks/playerreceivingstatistics/README.md#get_player_receiving_stats_by_season) - Get Player Receiving Statistics by Season
* [get_player_receiving_stats_by_week](docs/sdks/playerreceivingstatistics/README.md#get_player_receiving_stats_by_week) - Get Player Receiving Statistics by Week

### [player_rushing_statistics](docs/sdks/playerrushingstatistics/README.md)

* [get_player_rushing_stats_by_season](docs/sdks/playerrushingstatistics/README.md#get_player_rushing_stats_by_season) - Get Player Rushing Statistics by Season
* [get_player_rushing_stats_by_week](docs/sdks/playerrushingstatistics/README.md#get_player_rushing_stats_by_week) - Get Player Rushing Statistics by Week

### [player_statistics](docs/sdks/playerstatistics/README.md)

* [get_player_passing_stats_by_season](docs/sdks/playerstatistics/README.md#get_player_passing_stats_by_season) - Get Player Passing Statistics by Season

### [players](docs/sdks/players/README.md)

* [get_player](docs/sdks/players/README.md#get_player) - Get Player Details
* [get_projected_stats](docs/sdks/players/README.md#get_projected_stats) - Get Projected Player Statistics
* [search_players](docs/sdks/players/README.md#search_players) - Search Players

### [plays](docs/sdks/plays/README.md)

* [get_summary_play](docs/sdks/plays/README.md#get_summary_play) - Get Play Summary

### [schedules](docs/sdks/schedules/README.md)

* [get_scheduled_game](docs/sdks/schedules/README.md#get_scheduled_game) - Get Single Game Details
* [get_game_matchup_rankings](docs/sdks/schedules/README.md#get_game_matchup_rankings) - Get Game Matchup Rankings
* [get_team_injuries](docs/sdks/schedules/README.md#get_team_injuries) - Get Team Injuries for Game Week
* [get_scheduled_games](docs/sdks/schedules/README.md#get_scheduled_games) - Get Games by Week

### [schedules_extended](docs/sdks/schedulesextended/README.md)

* [get_current_week_games](docs/sdks/schedulesextended/README.md#get_current_week_games) - Get Current Week Games
* [get_future_betting_odds](docs/sdks/schedulesextended/README.md#get_future_betting_odds) - Get Future Betting Odds
* [get_team_standings](docs/sdks/schedulesextended/README.md#get_team_standings) - Get Team Standings

### [scores](docs/sdks/scores/README.md)

* [get_live_game_scores](docs/sdks/scores/README.md#get_live_game_scores) - Get Live Game Scores

### [season_schedule](docs/sdks/seasonschedule/README.md)

* [get_schedule_season_weeks](docs/sdks/seasonschedule/README.md#get_schedule_season_weeks) - Get Season Weeks

### [secured_videos](docs/sdks/securedvideos/README.md)

* [get_coaches_film_videos](docs/sdks/securedvideos/README.md#get_coaches_film_videos) - Get Coaches Film Videos

### [stats](docs/sdks/stats/README.md)

* [get_stats_boxscore](docs/sdks/stats/README.md#get_stats_boxscore) - Get Game Boxscore (Stats API)
* [get_game_team_rankings](docs/sdks/stats/README.md#get_game_team_rankings) - Get Team Rankings for Game
* [get_gamecenter](docs/sdks/stats/README.md#get_gamecenter) - Get Gamecenter Statistics
* [get_multiple_rankings_all_teams](docs/sdks/stats/README.md#get_multiple_rankings_all_teams) - Get Multiple Rankings for All Teams

### [team_defense_pass_statistics](docs/sdks/teamdefensepassstatistics/README.md)

* [get_team_defense_pass_stats_by_season](docs/sdks/teamdefensepassstatistics/README.md#get_team_defense_pass_stats_by_season) - Get Team Defense Pass Statistics by Season

### [team_defense_rush_statistics](docs/sdks/teamdefenserushstatistics/README.md)

* [get_team_defense_rush_stats_by_season](docs/sdks/teamdefenserushstatistics/README.md#get_team_defense_rush_stats_by_season) - Get Team Defense Rush Statistics by Season

### [team_defense_statistics](docs/sdks/teamdefensestatistics/README.md)

* [get_team_defense_stats_by_season](docs/sdks/teamdefensestatistics/README.md#get_team_defense_stats_by_season) - Get Team Defense Statistics by Season

### [team_offense_overview_statistics](docs/sdks/teamoffenseoverviewstatistics/README.md)

* [get_team_offense_overview_stats_by_season](docs/sdks/teamoffenseoverviewstatistics/README.md#get_team_offense_overview_stats_by_season) - Get Team Offense Overview Statistics by Season

### [team_offense_pass_statistics](docs/sdks/teamoffensepassstatistics/README.md)

* [get_team_offense_pass_stats_by_season](docs/sdks/teamoffensepassstatistics/README.md#get_team_offense_pass_stats_by_season) - Get Team Offense Pass Statistics by Season

### [teams](docs/sdks/teams/README.md)

* [get_all_teams](docs/sdks/teams/README.md#get_all_teams) - Get All Teams
* [get_team_roster](docs/sdks/teams/README.md#get_team_roster) - Get Team Roster
* [get_weekly_team_roster](docs/sdks/teams/README.md#get_weekly_team_roster) - Get Weekly Team Roster
* [get_team_schedule](docs/sdks/teams/README.md#get_team_schedule) - Get Team Schedule

### [win_probability](docs/sdks/winprobability/README.md)

* [get_plays_win_probability](docs/sdks/winprobability/README.md#get_plays_win_probability) - Get Game Win Probability by Plays
* [get_win_probability_min](docs/sdks/winprobability/README.md#get_win_probability_min) - Get Minimal Win Probability Data

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from griddy.nfl import GriddyNFL, models
from griddy.nfl.utils import BackoffStrategy, RetryConfig


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.content.get_game_preview(season=2025, season_type=models.SeasonTypeEnum.REG, week=4, visitor_display_name="Minnesota Vikings", home_display_name="Pittsburgh Steelers",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res is not None

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from griddy.nfl import GriddyNFL, models
from griddy.nfl.utils import BackoffStrategy, RetryConfig


with GriddyNFL(
    server_url="https://api.example.com",
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:

    res = griddy_nfl.content.get_game_preview(season=2025, season_type=models.SeasonTypeEnum.REG, week=4, visitor_display_name="Minnesota Vikings", home_display_name="Pittsburgh Steelers")

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`GriddyNFLBaseError`](./src/griddy/nfl/errors/griddynflbaseerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                            |
| ------------------ | ---------------- | ------------------------------------------------------ |
| `err.message`      | `str`            | Error message                                          |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                     |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                  |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned. |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                      |

### Example
```python
from griddy.nfl import GriddyNFL, errors, models


with GriddyNFL(
    server_url="https://api.example.com",
    nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
) as griddy_nfl:
    res = None
    try:

        res = griddy_nfl.content.get_game_preview(season=2025, season_type=models.SeasonTypeEnum.REG, week=4, visitor_display_name="Minnesota Vikings", home_display_name="Pittsburgh Steelers")

        assert res is not None

        # Handle response
        print(res)


    except errors.GriddyNFLBaseError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

```

### Error Classes
**Primary error:**
* [`GriddyNFLBaseError`](./src/griddy/nfl/errors/griddynflbaseerror.py): The base class for HTTP error responses.

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`GriddyNFLBaseError`](./src/griddy/nfl/errors/griddynflbaseerror.py)**:
* [`ResponseValidationError`](./src/griddy/nfl/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>
<!-- End Error Handling [errors] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from griddy.nfl import GriddyNFL
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = GriddyNFL(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from griddy.nfl import GriddyNFL
from griddy.nfl.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = GriddyNFL(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `GriddyNFL` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from griddy.nfl import GriddyNFL
def main():

    with GriddyNFL(
        server_url="https://api.example.com",
        nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as griddy_nfl:
        # Rest of application here...


# Or when using async:
async def amain():

    async with GriddyNFL(
        server_url="https://api.example.com",
        nfl_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as griddy_nfl:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from griddy.nfl import GriddyNFL
import logging

logging.basicConfig(level=logging.DEBUG)
s = GriddyNFL(server_url="https://example.com", debug_logger=logging.getLogger("griddy.nfl"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=griddy-nfl&utm_campaign=python)

<style>
  :root {
    --badge-gray-bg: #f3f4f6;
    --badge-gray-border: #d1d5db;
    --badge-gray-text: #374151;
    --badge-blue-bg: #eff6ff;
    --badge-blue-border: #3b82f6;
    --badge-blue-text: #3b82f6;
  }

  @media (prefers-color-scheme: dark) {
    :root {
      --badge-gray-bg: #374151;
      --badge-gray-border: #4b5563;
      --badge-gray-text: #f3f4f6;
      --badge-blue-bg: #1e3a8a;
      --badge-blue-border: #3b82f6;
      --badge-blue-text: #93c5fd;
    }
  }
  
  h1 {
    border-bottom: none !important;
    margin-bottom: 4px;
    margin-top: 0;
    letter-spacing: 0.5px;
    font-weight: 600;
  }
  
  .badge-text {
    letter-spacing: 1px;
    font-weight: 300;
  }
  
  .badge-container {
    display: inline-flex;
    align-items: center;
    background: var(--badge-gray-bg);
    border: 1px solid var(--badge-gray-border);
    border-radius: 6px;
    overflow: hidden;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
    font-size: 11px;
    text-decoration: none;
    vertical-align: middle;
  }

  .badge-container.blue {
    background: var(--badge-blue-bg);
    border-color: var(--badge-blue-border);
  }

  .badge-icon-section {
    padding: 4px 8px;
    border-right: 1px solid var(--badge-gray-border);
    display: flex;
    align-items: center;
  }

  .badge-text-section {
    padding: 4px 10px;
    color: var(--badge-gray-text);
    font-weight: 400;
  }

  .badge-container.blue .badge-text-section {
    color: var(--badge-blue-text);
  }
  
  .badge-link {
    text-decoration: none;
    margin-left: 8px;
    display: inline-flex;
    vertical-align: middle;
  }

  .badge-link:hover {
    text-decoration: none;
  }
  
  .badge-link:first-child {
    margin-left: 0;
  }
  
  .badge-icon-section svg {
    color: var(--badge-gray-text);
  }

  .badge-container.blue .badge-icon-section svg {
    color: var(--badge-blue-text);
  }
</style> 