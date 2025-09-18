"""
Example usage of the Pro Football Reference module in Griddy SDK.

This script demonstrates how to use the PFR client to retrieve
historical player data, career statistics, and draft information.
"""

from griddy import pfr
from griddy.core.exceptions import GriddyError


def main():
    """Main example function."""
    # Initialize the PFR client
    client = pfr.Client()

    print("=== Griddy SDK - Pro Football Reference Example ===\n")

    try:
        # Example 1: Search for players
        print("1. Searching for players named 'Brady':")
        players = client.search_players("Brady", position="QB")

        if players:
            for player in players[:3]:  # Show first 3 results
                print(f"   - {player.name}")
                if player.position:
                    print(f"     Position: {player.position}")
                if player.college:
                    print(f"     College: {player.college}")
                if player.career_start and player.career_end:
                    print(f"     Career: {player.career_start}-{player.career_end}")
                if player.hall_of_fame:
                    print(f"     🏆 Hall of Fame")
                print()
        else:
            print("   No players found or API unavailable")

        # Example 2: Get detailed player information
        print("\n2. Getting detailed player information:")
        # Note: This would need a real player ID in a real implementation
        player = client.get_player("sample_player_id")

        if player:
            print(f"   Name: {player.name}")
            if player.position:
                print(f"   Position: {player.position}")
            if player.height_inches:
                feet = player.height_inches // 12
                inches = player.height_inches % 12
                print(f"   Height: {feet}'{inches}\"")
            if player.weight:
                print(f"   Weight: {player.weight} lbs")
            if player.draft_year and player.draft_round:
                print(f"   Draft: {player.draft_year} Round {player.draft_round}")
            if player.pro_bowls:
                print(f"   Pro Bowls: {player.pro_bowls}")
        else:
            print("   Player not found or API unavailable")

        # Example 3: Get season statistics
        print("\n3. Getting player season statistics:")
        season_stats = client.get_player_season_stats("sample_player_id", 2023)

        if season_stats:
            print(f"   {season_stats.season} Season - {season_stats.team}")
            print(f"   Age: {season_stats.age}")
            print(f"   Games Played: {season_stats.games_played}")
            if season_stats.games_started:
                print(f"   Games Started: {season_stats.games_started}")

            stats = season_stats.stats
            if stats.pass_yards:
                print(f"   Passing Yards: {stats.pass_yards}")
            if stats.pass_touchdowns:
                print(f"   Passing TDs: {stats.pass_touchdowns}")
            if stats.passer_rating:
                print(f"   Passer Rating: {stats.passer_rating}")
        else:
            print("   Season statistics not found or API unavailable")

        # Example 4: Get career statistics
        print("\n4. Getting career statistics:")
        career_stats = client.get_player_career_stats("sample_player_id")

        if career_stats:
            print(f"   Career spanning {len(career_stats.seasons)} seasons")
            print(f"   Hall of Fame: {'Yes' if career_stats.hall_of_fame else 'No'}")
            print(f"   Retired: {'Yes' if career_stats.retired else 'Active'}")

            totals = career_stats.career_totals
            if totals.pass_yards:
                print(f"   Career Passing Yards: {totals.pass_yards:,}")
            if totals.pass_touchdowns:
                print(f"   Career Passing TDs: {totals.pass_touchdowns}")
            if totals.approximate_value:
                print(f"   Approximate Value: {totals.approximate_value}")

            # Show recent seasons
            if career_stats.seasons:
                print(f"\n   Recent seasons:")
                for season in career_stats.seasons[-3:]:  # Last 3 seasons
                    print(f"     {season.season}: {season.team}")
        else:
            print("   Career statistics not found or API unavailable")

        # Example 5: Get game-by-game statistics
        print("\n5. Getting game-by-game statistics:")
        game_stats = client.get_player_game_stats("sample_player_id", 2023, week=1)

        if game_stats:
            for stat in game_stats[:3]:  # Show first 3 games
                print(f"   Week {stat.week}:")
                if stat.pass_yards:
                    print(
                        f"     Passing: {stat.pass_completions}/{stat.pass_attempts}, {stat.pass_yards} yards"
                    )
                if stat.pass_touchdowns:
                    print(f"     Passing TDs: {stat.pass_touchdowns}")
                if stat.interceptions:
                    print(f"     Interceptions: {stat.interceptions}")
        else:
            print("   Game statistics not found or API unavailable")

        # Example 6: Get team statistics
        print("\n6. Getting team statistics:")
        team_stats = client.get_team_stats("NE", 2023)

        if team_stats:
            print(f"   {team_stats.team_id} - {team_stats.season} season")
            print(f"   Record: {team_stats.wins}-{team_stats.losses}")
            if team_stats.win_percentage:
                print(f"   Win Percentage: {team_stats.win_percentage:.3f}")
            if team_stats.points_for and team_stats.points_against:
                print(
                    f"   Points: {team_stats.points_for} for, {team_stats.points_against} against"
                )
            if team_stats.point_differential:
                print(f"   Point Differential: {team_stats.point_differential:+}")
        else:
            print("   Team statistics not found or API unavailable")

        # Example 7: Get draft information
        print("\n7. Getting 2023 NFL Draft information:")
        draft_picks = client.get_draft_class(2023)

        if draft_picks:
            print(f"   Found {len(draft_picks)} draft picks")
            print("   First round picks:")
            first_round = [pick for pick in draft_picks if pick.round == 1]
            for pick in first_round[:5]:  # First 5 picks
                print(
                    f"     {pick.pick}. {pick.player_name} - {pick.position} ({pick.college})"
                )
                print(f"        Drafted by: {pick.team}")
        else:
            print("   Draft information not found or API unavailable")

        # Example 8: Get statistical leaders
        print("\n8. Getting 2023 passing yards leaders:")
        leaders = client.get_season_leaders(
            2023, "passing_yards", position="QB", limit=5
        )

        if leaders:
            print("   Top 5 passing yards leaders:")
            for i, leader in enumerate(leaders, 1):
                print(f"     {i}. Player ID: {leader.player_id}")
                if leader.pass_yards:
                    print(f"        Passing Yards: {leader.pass_yards:,}")
        else:
            print("   Statistical leaders not found or API unavailable")

        # Example 9: Get Hall of Fame players
        print("\n9. Getting Hall of Fame players:")
        hof_players = client.get_hall_of_fame_players()

        if hof_players:
            print(f"   Found {len(hof_players)} Hall of Fame players")
            print("   Recent inductees:")
            for player in hof_players[:5]:  # First 5 in the list
                print(f"     - {player.name}")
                if player.position:
                    print(f"       Position: {player.position}")
                if player.career_start and player.career_end:
                    print(f"       Career: {player.career_start}-{player.career_end}")
        else:
            print("   Hall of Fame data not found or API unavailable")

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
