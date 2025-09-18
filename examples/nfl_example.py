"""
Example usage of the NFL module in Griddy SDK.

This script demonstrates how to use the NFL client to retrieve
games, teams, players, and statistics.
"""

from griddy import nfl
from griddy.core.exceptions import GriddyError


def main():
    """Main example function."""
    # Initialize the NFL client
    client = nfl.Client()

    print("=== Griddy SDK - NFL Example ===\n")

    try:
        # Example 1: Get games for a specific week
        print("1. Getting NFL games for Week 1, 2024 season:")
        games = client.get_games(season=2024, week=1, season_type="regular")

        if games:
            for game in games[:3]:  # Show first 3 games
                print(f"   {game.away_team} @ {game.home_team}")
                if game.home_score is not None and game.away_score is not None:
                    print(f"   Score: {game.away_score} - {game.home_score}")
                print(f"   Status: {game.status}")
                if game.start_time:
                    print(f"   Time: {game.start_time}")
                print()
        else:
            print("   No games found or API unavailable")

        # Example 2: Get all NFL teams
        print("\n2. Getting NFL teams:")
        teams = client.get_teams()

        if teams:
            print(f"   Found {len(teams)} teams")
            for team in teams[:5]:  # Show first 5 teams
                print(f"   - {team.name} ({team.abbreviation})")
        else:
            print("   No teams found or API unavailable")

        # Example 3: Get players for a specific team
        print("\n3. Getting players for Kansas City Chiefs:")
        players = client.get_players(team="KC", position="QB")

        if players:
            for player in players:
                print(f"   - {player.name} (#{player.jersey_number}) - {player.position}")
                if player.college:
                    print(f"     College: {player.college}")
        else:
            print("   No players found or API unavailable")

        # Example 4: Get player statistics
        print("\n4. Getting player statistics:")
        # Note: This would need a real player ID in a real implementation
        stats = client.get_player_stats("sample_player_id", season=2024, week=1)

        if stats:
            for stat in stats:
                print(f"   Week {stat.week} stats:")
                if stat.passing_yards:
                    print(f"   - Passing yards: {stat.passing_yards}")
                if stat.passing_touchdowns:
                    print(f"   - Passing TDs: {stat.passing_touchdowns}")
                if stat.rushing_yards:
                    print(f"   - Rushing yards: {stat.rushing_yards}")
        else:
            print("   No statistics found or API unavailable")

        # Example 5: Get NFL schedule
        print("\n5. Getting NFL schedule for Week 1:")
        schedule = client.get_schedule(season=2024, week=1)

        if schedule.games:
            print(f"   Week {schedule.week}, {schedule.season} {schedule.season_type} season")
            print(f"   {len(schedule.games)} games scheduled")
        else:
            print("   No schedule found or API unavailable")

        # Example 6: Get NFL standings
        print("\n6. Getting NFL standings:")
        standings = client.get_standings(season=2024)

        if standings:
            print(f"   Found {len(standings)} divisions")
            for standing in standings[:2]:  # Show first 2 divisions
                print(f"   {standing.conference} {standing.division}:")
                for team in standing.teams[:3]:  # Show top 3 teams
                    record = f"{team.wins}-{team.losses}" if team.wins is not None else "N/A"
                    print(f"     - {team.name}: {record}")
        else:
            print("   No standings found or API unavailable")

        # Example 7: Get NFL news
        print("\n7. Getting NFL news:")
        news = client.get_news(limit=3)

        if news:
            for article in news:
                print(f"   - {article.title}")
                if article.published_date:
                    print(f"     Published: {article.published_date}")
                if article.summary:
                    print(f"     Summary: {article.summary[:100]}...")
                print()
        else:
            print("   No news found or API unavailable")

    except GriddyError as e:
        print(f"Griddy SDK Error: {e}")
        print(f"Status Code: {e.status_code}")
        if e.response_data:
            print(f"Response Data: {e.response_data}")

    except Exception as e:
        print(f"Unexpected error: {e}")

    finally:
        # Clean up
        client.close()
        print("\n=== Example completed ===")


if __name__ == "__main__":
    main()