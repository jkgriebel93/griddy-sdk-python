"""Example script for testing all NGS SDK methods."""

import json
import sys
from pprint import pprint

from griddy.nfl import GriddyNFL
from griddy.settings import NFL

_, *args = sys.argv

#
# # Lamar Jackson = 46101
if len(args) == 1:
    with open(args[0], "r") as infile:
        custom_auth_info = json.load(infile)
    nfl = GriddyNFL(nfl_auth=custom_auth_info)
else:
    nfl = GriddyNFL(
        login_email=NFL["login_email"], login_password=NFL["login_password"]
    )


def print_result(name: str, result):
    """Helper to print results with headers."""
    print(f"\n{'='*60}")
    print(f"  {name}")
    print(f"{'='*60}")
    print(f"Result type: {type(result)}")
    if hasattr(result, "model_dump"):
        data = result.model_dump()
        # Truncate for readability
        print(f"Keys: {list(data.keys()) if isinstance(data, dict) else 'N/A'}")
        pprint(data, indent=2, depth=3)
    elif isinstance(result, list):
        print(f"Count: {len(result)}")
        if result:
            print("First item:")
            if hasattr(result[0], "model_dump"):
                pprint(result[0].model_dump(), indent=2, depth=3)
            else:
                pprint(result[0], indent=2, depth=3)
    else:
        pprint(result, indent=2, depth=3)


# Test parameters
SEASON = 2024
SEASON_TYPE = "REG"
WEEK = 12
GAME_ID = 2024112800  # Example game ID from Week 12

# =============================================================================
# NGS League Endpoints
# =============================================================================

print("\n" + "=" * 60)
print("  NGS LEAGUE ENDPOINTS")
print("=" * 60)

# get_current_schedule
try:
    result = nfl.ngs.league.get_current_schedule()
    print_result("nfl.ngs.league.get_current_schedule()", result)
except Exception as e:
    print(f"ERROR get_current_schedule: {e}")

# get_teams
try:
    result = nfl.ngs.league.get_teams()
    print_result("nfl.ngs.league.get_teams()", result)
except Exception as e:
    print(f"ERROR get_teams: {e}")

# get_schedule
try:
    result = nfl.ngs.league.get_schedule(season=SEASON)
    print_result(f"nfl.ngs.league.get_schedule(season={SEASON})", result)
except Exception as e:
    print(f"ERROR get_schedule: {e}")

# =============================================================================
# NGS Games Endpoints
# =============================================================================

print("\n" + "=" * 60)
print("  NGS GAMES ENDPOINTS")
print("=" * 60)

# get_live_scores
try:
    # result = nfl.ngs.games.get_live_scores(
    #     season=SEASON, season_type=SEASON_TYPE, week=WEEK
    # )
    # print_result(
    #     f"nfl.ngs.games.get_live_scores(season={SEASON}, season_type='{SEASON_TYPE}', week={WEEK})",
    #     result,
    # )
    print("Getting live scores presents auth problems that are yet to be solved")
except Exception as e:
    print(f"ERROR get_live_scores: {e}")

# get_overview
try:
    result = nfl.ngs.games.get_overview(game_id=GAME_ID)
    print_result(f"nfl.ngs.games.get_overview(game_id={GAME_ID})", result)
except Exception as e:
    print(f"ERROR get_overview: {e}")

# =============================================================================
# NGS Stats Endpoints
# =============================================================================

print("\n" + "=" * 60)
print("  NGS STATS ENDPOINTS")
print("=" * 60)

# get_passing_stats (season)
try:
    result = nfl.ngs.stats.get_passing_stats(season=SEASON, season_type=SEASON_TYPE)
    print_result(
        f"nfl.ngs.stats.get_passing_stats(season={SEASON}, season_type='{SEASON_TYPE}')",
        result,
    )
except Exception as e:
    print(f"ERROR get_passing_stats: {e}")

# get_passing_stats (weekly)
try:
    result = nfl.ngs.stats.get_passing_stats(
        season=SEASON, season_type=SEASON_TYPE, week=WEEK
    )
    print_result(
        f"nfl.ngs.stats.get_passing_stats(season={SEASON}, season_type='{SEASON_TYPE}', week={WEEK})",
        result,
    )
except Exception as e:
    print(f"ERROR get_passing_stats (weekly): {e}")

# get_receiving_stats (season)
try:
    result = nfl.ngs.stats.get_receiving_stats(season=SEASON, season_type=SEASON_TYPE)
    print_result(
        f"nfl.ngs.stats.get_receiving_stats(season={SEASON}, season_type='{SEASON_TYPE}')",
        result,
    )
except Exception as e:
    print(f"ERROR get_receiving_stats: {e}")

# get_receiving_stats (weekly)
try:
    result = nfl.ngs.stats.get_receiving_stats(
        season=SEASON, season_type=SEASON_TYPE, week=WEEK
    )
    print_result(
        f"nfl.ngs.stats.get_receiving_stats(season={SEASON}, season_type='{SEASON_TYPE}', week={WEEK})",
        result,
    )
except Exception as e:
    print(f"ERROR get_receiving_stats (weekly): {e}")

# get_rushing_stats (season)
try:
    result = nfl.ngs.stats.get_rushing_stats(season=SEASON, season_type=SEASON_TYPE)
    print_result(
        f"nfl.ngs.stats.get_rushing_stats(season={SEASON}, season_type='{SEASON_TYPE}')",
        result,
    )
except Exception as e:
    print(f"ERROR get_rushing_stats: {e}")

# get_rushing_stats (weekly)
try:
    result = nfl.ngs.stats.get_rushing_stats(
        season=SEASON, season_type=SEASON_TYPE, week=WEEK
    )
    print_result(
        f"nfl.ngs.stats.get_rushing_stats(season={SEASON}, season_type='{SEASON_TYPE}', week={WEEK})",
        result,
    )
except Exception as e:
    print(f"ERROR get_rushing_stats (weekly): {e}")

# =============================================================================
# NGS Leaders Endpoints
# =============================================================================

print("\n" + "=" * 60)
print("  NGS LEADERS ENDPOINTS")
print("=" * 60)

# get_fastest_ball_carriers
try:
    result = nfl.ngs.leaders.get_fastest_ball_carriers(
        season=SEASON, season_type=SEASON_TYPE, limit=10
    )
    print_result(
        f"nfl.ngs.leaders.get_fastest_ball_carriers(season={SEASON}, season_type='{SEASON_TYPE}', limit=10)",
        result,
    )
except Exception as e:
    print(f"ERROR get_fastest_ball_carriers: {e}")

# get_fastest_ball_carriers (weekly)
try:
    result = nfl.ngs.leaders.get_fastest_ball_carriers(
        season=SEASON, season_type=SEASON_TYPE, limit=10, week=WEEK
    )
    print_result(
        f"nfl.ngs.leaders.get_fastest_ball_carriers(season={SEASON}, season_type='{SEASON_TYPE}', limit=10, week={WEEK})",
        result,
    )
except Exception as e:
    print(f"ERROR get_fastest_ball_carriers (weekly): {e}")

# get_fastest_sacks
try:
    result = nfl.ngs.leaders.get_fastest_sacks(
        season=SEASON, season_type=SEASON_TYPE, limit=10
    )
    print_result(
        f"nfl.ngs.leaders.get_fastest_sacks(season={SEASON}, season_type='{SEASON_TYPE}', limit=10)",
        result,
    )
except Exception as e:
    print(f"ERROR get_fastest_sacks: {e}")

# get_fastest_sacks (weekly)
try:
    result = nfl.ngs.leaders.get_fastest_sacks(
        season=SEASON, season_type=SEASON_TYPE, limit=10, week=WEEK
    )
    print_result(
        f"nfl.ngs.leaders.get_fastest_sacks(season={SEASON}, season_type='{SEASON_TYPE}', limit=10, week={WEEK})",
        result,
    )
except Exception as e:
    print(f"ERROR get_fastest_sacks (weekly): {e}")

# get_improbable_completions
try:
    result = nfl.ngs.leaders.get_improbable_completions(
        season=SEASON, season_type=SEASON_TYPE
    )
    print_result(
        f"nfl.ngs.leaders.get_improbable_completions(season={SEASON}, season_type='{SEASON_TYPE}')",
        result,
    )
except Exception as e:
    print(f"ERROR get_improbable_completions: {e}")

# get_incredible_yac
try:
    result = nfl.ngs.leaders.get_incredible_yac(season=SEASON, season_type=SEASON_TYPE)
    print_result(
        f"nfl.ngs.leaders.get_incredible_yac(season={SEASON}, season_type='{SEASON_TYPE}')",
        result,
    )
except Exception as e:
    print(f"ERROR get_incredible_yac: {e}")

# get_longest_plays
try:
    result = nfl.ngs.leaders.get_longest_plays(
        season=SEASON, season_type=SEASON_TYPE, limit=10
    )
    print_result(
        f"nfl.ngs.leaders.get_longest_plays(season={SEASON}, season_type='{SEASON_TYPE}', limit=10)",
        result,
    )
except Exception as e:
    print(f"ERROR get_longest_plays: {e}")

# get_longest_plays (weekly)
try:
    result = nfl.ngs.leaders.get_longest_plays(
        season=SEASON, season_type=SEASON_TYPE, limit=10, week=WEEK
    )
    print_result(
        f"nfl.ngs.leaders.get_longest_plays(season={SEASON}, season_type='{SEASON_TYPE}', limit=10, week={WEEK})",
        result,
    )
except Exception as e:
    print(f"ERROR get_longest_plays (weekly): {e}")

# get_longest_tackles
try:
    result = nfl.ngs.leaders.get_longest_tackles(
        season=SEASON, season_type=SEASON_TYPE, limit=10
    )
    print_result(
        f"nfl.ngs.leaders.get_longest_tackles(season={SEASON}, season_type='{SEASON_TYPE}', limit=10)",
        result,
    )
except Exception as e:
    print(f"ERROR get_longest_tackles: {e}")

# get_longest_tackles (weekly)
try:
    result = nfl.ngs.leaders.get_longest_tackles(
        season=SEASON, season_type=SEASON_TYPE, limit=10, week=WEEK
    )
    print_result(
        f"nfl.ngs.leaders.get_longest_tackles(season={SEASON}, season_type='{SEASON_TYPE}', limit=10, week={WEEK})",
        result,
    )
except Exception as e:
    print(f"ERROR get_longest_tackles (weekly): {e}")

# get_remarkable_rushes
try:
    result = nfl.ngs.leaders.get_remarkable_rushes(
        season=SEASON, season_type=SEASON_TYPE
    )
    print_result(
        f"nfl.ngs.leaders.get_remarkable_rushes(season={SEASON}, season_type='{SEASON_TYPE}')",
        result,
    )
except Exception as e:
    print(f"ERROR get_remarkable_rushes: {e}")

# =============================================================================
# NGS Content Endpoints
# =============================================================================

print("\n" + "=" * 60)
print("  NGS CONTENT ENDPOINTS")
print("=" * 60)

# get_charts
try:
    result = nfl.ngs.content.get_charts(season=SEASON, count=5)
    print_result(f"nfl.ngs.content.get_charts(season={SEASON}, count=5)", result)
except Exception as e:
    print(f"ERROR get_charts: {e}")

# get_charts (filtered by chart_type)
try:
    result = nfl.ngs.content.get_charts(season=SEASON, count=5, chart_type="route")
    print_result(
        f"nfl.ngs.content.get_charts(season={SEASON}, count=5, chart_type='route')",
        result,
    )
except Exception as e:
    print(f"ERROR get_charts (route): {e}")

# # get_players
try:
    result = nfl.ngs.content.get_players()
    print_result("nfl.ngs.content.get_players()", result)
except Exception as e:
    print(f"ERROR get_players: {e}")

# get_highlights
try:
    result = nfl.ngs.content.get_highlights(season=SEASON, limit=5)
    print_result(f"nfl.ngs.content.get_highlights(season={SEASON}, limit=5)", result)
except Exception as e:
    print(f"ERROR get_highlights: {e}")

# =============================================================================
# NGS News Endpoints
# =============================================================================

print("\n" + "=" * 60)
print("  NGS NEWS ENDPOINTS")
print("=" * 60)

# get_mixed_content
try:
    result = nfl.ngs.news.get_mixed_content(limit=5)
    print_result("nfl.ngs.news.get_mixed_content(limit=5)", result)
except Exception as e:
    print(f"ERROR get_mixed_content: {e}")

# get_articles
try:
    result = nfl.ngs.news.get_articles(limit=5)
    print_result("nfl.ngs.news.get_articles(limit=5)", result)
except Exception as e:
    print(f"ERROR get_articles: {e}")

# get_video_clips
try:
    result = nfl.ngs.news.get_video_clips(limit=5)
    print_result("nfl.ngs.news.get_video_clips(limit=5)", result)
except Exception as e:
    print(f"ERROR get_video_clips: {e}")

print("\n" + "=" * 60)
print("  ALL NGS ENDPOINT TESTS COMPLETE")
print("=" * 60 + "\n")
