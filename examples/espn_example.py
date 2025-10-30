"""
Example usage of the ESPN module in Griddy SDK.

This script demonstrates how to use the ESPN client to retrieve
live scores, team information, and news.
"""

from datetime import datetime

from griddy import espn
from griddy.core.exceptions import GriddyError


def main():
    """Main example function."""
    # Initialize the ESPN client
    client = espn.Client()

    print("=== Griddy SDK - ESPN Example ===\n")

    try:
        # Example 1: Get current scoreboard
        print("1. Getting current NFL scoreboard:")
        scoreboard = client.get_scoreboard()

        if scoreboard:
            print(f"   Date: {scoreboard.date.strftime('%Y-%m-%d')}")
            print(f"   Season: {scoreboard.season} {scoreboard.season_type}")
            if scoreboard.week:
                print(f"   Week: {scoreboard.week}")
            print(f"   Games: {len(scoreboard.games)}")

            for game in scoreboard.games[:3]:  # Show first 3 games
                print(f"\n   {game.away_team} @ {game.home_team}")
                if game.home_score is not None and game.away_score is not None:
                    print(f"   Score: {game.away_score} - {game.home_score}")
                print(f"   Status: {game.status}")
                if game.venue_name:
                    print(f"   Venue: {game.venue_name}")
                if game.broadcast_network:
                    print(f"   TV: {game.broadcast_network}")
        else:
            print("   Scoreboard not available")

        # Example 2: Get live scores
        print("\n2. Getting live scores:")
        live_games = client.get_live_scores()

        if live_games:
            print(f"   {len(live_games)} games currently live:")
            for game in live_games:
                print(
                    f"   - {game.away_team} {game.away_score} - {game.home_score} {game.home_team}"
                )
                print(f"     Status: {game.status}")
        else:
            print("   No live games or data unavailable")

        # Example 3: Get all NFL teams
        print("\n3. Getting NFL teams from ESPN:")
        teams = client.get_teams()

        if teams:
            print(f"   Found {len(teams)} teams")
            for team in teams[:5]:  # Show first 5 teams
                print(f"   - {team.display_name or team.name} ({team.abbreviation})")
                if team.record:
                    print(f"     Record: {team.record}")
                if team.conference and team.division:
                    print(f"     Division: {team.conference} {team.division}")
        else:
            print("   Teams not available")

        # Example 4: Get specific team information
        print("\n4. Getting Kansas City Chiefs information:")
        # Note: Would need actual ESPN team ID
        team = client.get_team("KC")

        if team:
            print(f"   Name: {team.display_name or team.name}")
            print(f"   Abbreviation: {team.abbreviation}")
            if team.record:
                print(f"   Record: {team.record}")
            if team.color:
                print(f"   Primary Color: #{team.color}")
            if team.logo:
                print(f"   Logo: {team.logo}")
        else:
            print("   Team information not available")

        # Example 5: Get team roster
        print("\n5. Getting team roster:")
        roster = client.get_team_roster("KC")

        if roster:
            print(f"   Found {len(roster)} players")
            quarterbacks = [p for p in roster if p.position == "QB"]
            if quarterbacks:
                print("   Quarterbacks:")
                for qb in quarterbacks:
                    print(f"     - #{qb.jersey_number} {qb.name}")
                    if qb.height and qb.weight:
                        print(f"       {qb.height}, {qb.weight} lbs")
                    if qb.college:
                        print(f"       College: {qb.college}")
        else:
            print("   Roster not available")

        # Example 6: Get detailed athlete information
        print("\n6. Getting athlete information:")
        # Note: Would need actual ESPN athlete ID
        athlete = client.get_athlete("sample_athlete_id")

        if athlete:
            print(f"   Name: {athlete.full_name}")
            print(f"   Position: {athlete.position}")
            if athlete.height and athlete.weight:
                print(f"   Size: {athlete.display_height}, {athlete.display_weight}")
            if athlete.age:
                print(f"   Age: {athlete.age}")
            if athlete.college:
                print(f"   College: {athlete.college['name']}")
            if athlete.team:
                print(f"   Team: {athlete.team['displayName']}")
        else:
            print("   Athlete information not available")

        # Example 7: Get NFL standings
        print("\n7. Getting NFL standings:")
        standings = client.get_standings()

        if standings:
            print(f"   Found {len(standings)} standings groups")
            for standing in standings[:2]:  # Show first 2 groups
                print(f"   {standing.season} {standing.season_type} season")
                if standing.groups:
                    for group in standing.groups[:2]:  # Show first 2 groups
                        print(f"     Conference/Division standings available")
        else:
            print("   Standings not available")

        # Example 8: Get NFL news
        print("\n8. Getting NFL news:")
        news = client.get_news(limit=5)

        if news:
            print(f"   Found {len(news)} articles:")
            for article in news:
                print(f"   - {article.headline}")
                if article.published:
                    print(
                        f"     Published: {article.published.strftime('%Y-%m-%d %H:%M')}"
                    )
                if article.description:
                    print(f"     Description: {article.description[:100]}...")
                if article.byline:
                    print(f"     By: {article.byline}")
                print()
        else:
            print("   News not available")

        # Example 9: Get game details
        print("\n9. Getting detailed game information:")
        # Note: Would need actual ESPN game ID
        game_details = client.get_game_details("sample_game_id")

        if game_details:
            print(f"   Game: {game_details.name}")
            print(f"   Date: {game_details.date.strftime('%Y-%m-%d %H:%M')}")
            if game_details.weather:
                print(f"   Weather: {game_details.weather}")
            if game_details.broadcasts:
                print(f"   Broadcast: {len(game_details.broadcasts)} networks")
            if game_details.odds:
                print(f"   Betting odds available")
        else:
            print("   Game details not available")

        # Example 10: Get schedule
        print("\n10. Getting NFL schedule:")
        schedule = client.get_schedule(
            season=2024, season_type=2, week=1
        )  # Regular season week 1

        if schedule:
            print(f"   Found {len(schedule)} scheduled games")
            for game in schedule[:3]:  # Show first 3 games
                print(f"   - {game.away_team} @ {game.home_team}")
                if game.start_time:
                    print(f"     Time: {game.start_time.strftime('%Y-%m-%d %H:%M')}")
                print(f"     Status: {game.status}")
        else:
            print("   Schedule not available")

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
