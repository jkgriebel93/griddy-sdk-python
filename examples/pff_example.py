"""
Example usage of the Pro Football Focus (PFF) module in Griddy SDK.

This script demonstrates how to use the PFF client to retrieve
player grades, advanced analytics, team evaluations, and draft analysis.
"""

from griddy import pff
from griddy.core.exceptions import GriddyError


def main():
    """Main example function."""
    # Initialize the PFF client (optionally with API key)
    # client = pff.Client(api_key="your_pff_api_key_here")
    client = pff.Client()

    print("=== Griddy SDK - Pro Football Focus Example ===\n")

    try:
        # Example 1: Get player grades for a specific week
        print("1. Getting PFF player grades for Week 1, 2024:")
        player_grades = client.get_player_grades(
            "sample_player_id", season=2024, week=1
        )

        if player_grades:
            print(f"   Player: {player_grades.player_id}")
            print(f"   Position: {player_grades.position}")
            print(f"   Team: {player_grades.team}")
            print(f"   Overall Grade: {player_grades.overall_grade}")
            print(f"   Overall Rank: {player_grades.overall_rank or 'N/A'}")
            print(f"   Snaps Played: {player_grades.snaps_played}")
            print(f"   Snap Percentage: {player_grades.snap_percentage or 'N/A'}%")

            # Show position-specific grades
            if player_grades.passing:
                print(f"\n   Passing Grades:")
                print(f"   - Overall: {player_grades.passing.overall_grade}")
                print(f"   - Accuracy: {player_grades.passing.accuracy_grade}")
                print(f"   - Deep Ball: {player_grades.passing.deep_ball_grade}")
                print(f"   - Big Time Throws: {player_grades.passing.big_time_throws}")
                print(
                    f"   - Turnover Worthy Plays: {player_grades.passing.turnover_worthy_plays}"
                )

            if player_grades.defense:
                print(f"\n   Defensive Grades:")
                print(f"   - Overall: {player_grades.defense.overall_grade}")
                print(f"   - Pass Rush: {player_grades.defense.pass_rush_grade}")
                print(f"   - Coverage: {player_grades.defense.coverage_grade}")
                print(
                    f"   - Pass Rush Win Rate: {player_grades.defense.pass_rush_win_rate}%"
                )
        else:
            print("   Player grades not found or API unavailable")

        # Example 2: Get season-long player grades
        print("\n2. Getting season-long player grades:")
        season_grades = client.get_player_grades("sample_player_id", season=2024)

        if season_grades:
            print(f"   Season Overall Grade: {season_grades.overall_grade}")
            print(f"   Total Snaps: {season_grades.snaps_played}")
            if season_grades.receiving:
                print(f"   Receiving Grade: {season_grades.receiving.overall_grade}")
                print(f"   Drop Rate: {season_grades.receiving.drop_rate}%")
                print(
                    f"   YAC per Reception: {season_grades.receiving.yards_after_catch}"
                )
        else:
            print("   Season grades not found or API unavailable")

        # Example 3: Get team grades
        print("\n3. Getting team grades:")
        team_grades = client.get_team_grades("KC", season=2024, week=1)

        if team_grades:
            print(f"   Team: {team_grades.team_id}")
            print(f"   Overall Offense Grade: {team_grades.overall_offense_grade}")
            print(f"   Overall Defense Grade: {team_grades.overall_defense_grade}")
            print(f"   Special Teams Grade: {team_grades.overall_special_teams_grade}")

            if team_grades.passing_offense_grade:
                print(f"   Passing Offense: {team_grades.passing_offense_grade}")
            if team_grades.run_defense_grade:
                print(f"   Run Defense: {team_grades.run_defense_grade}")
            if team_grades.pressure_rate:
                print(f"   Pressure Rate: {team_grades.pressure_rate}%")
            if team_grades.red_zone_efficiency:
                print(f"   Red Zone Efficiency: {team_grades.red_zone_efficiency}%")
        else:
            print("   Team grades not found or API unavailable")

        # Example 4: Get position rankings
        print("\n4. Getting quarterback rankings:")
        qb_rankings = client.get_position_rankings("QB", season=2024, limit=10)

        if qb_rankings:
            print(f"   Top {len(qb_rankings)} Quarterbacks:")
            for i, qb in enumerate(qb_rankings, 1):
                print(f"   {i}. Player {qb.player_id}: {qb.overall_grade}")
                if qb.passing and qb.passing.big_time_throws:
                    print(f"      Big Time Throws: {qb.passing.big_time_throws}")
        else:
            print("   QB rankings not found or API unavailable")

        # Example 5: Get player metrics
        print("\n5. Getting advanced player metrics:")
        metrics = client.get_player_metrics("sample_player_id", season=2024)

        if metrics:
            print(f"   Player: {metrics.player_id}")
            if metrics.third_down_grade:
                print(f"   Third Down Grade: {metrics.third_down_grade}")
            if metrics.red_zone_grade:
                print(f"   Red Zone Grade: {metrics.red_zone_grade}")
            if metrics.clutch_rating:
                print(f"   Clutch Rating: {metrics.clutch_rating}")
            if metrics.consistency_score:
                print(f"   Consistency Score: {metrics.consistency_score}")
            if metrics.win_rate:
                print(f"   Win Rate: {metrics.win_rate}%")
        else:
            print("   Player metrics not found or API unavailable")

        # Example 6: Get season summary
        print("\n6. Getting season summary:")
        summary = client.get_season_summary("sample_player_id", 2024)

        if summary:
            print(f"   Player: {summary.player_id}")
            print(f"   Position: {summary.position}")
            print(f"   Team: {summary.team}")
            print(f"   Games Played: {summary.games_played}")
            print(f"   Overall Grade: {summary.overall_grade}")
            print(f"   Position Rank: {summary.position_rank or 'N/A'}")

            if summary.pff_all_pro:
                print(f"   🏆 PFF All-Pro: {summary.pff_all_pro}")
            if summary.team_of_the_week_awards:
                print(f"   Team of the Week Awards: {summary.team_of_the_week_awards}")
            if summary.highest_graded_game:
                print(f"   Highest Graded Game: {summary.highest_graded_game}")
            if summary.consistency_rating:
                print(f"   Consistency Rating: {summary.consistency_rating}")
        else:
            print("   Season summary not found or API unavailable")

        # Example 7: Get All-Pro teams
        print("\n7. Getting PFF All-Pro teams:")
        all_pro_teams = client.get_all_pro_teams(2024)

        if all_pro_teams:
            for team_level, players in all_pro_teams.items():
                print(f"   {team_level.replace('_', ' ').title()}:")
                for player in players[:5]:  # Show first 5 players
                    print(f"   - {player.name} ({player.position})")
        else:
            print("   All-Pro teams not found or API unavailable")

        # Example 8: Get Team of the Week
        print("\n8. Getting Team of the Week:")
        totw = client.get_team_of_the_week(2024, 1)

        if totw:
            print(f"   Week 1 Team of the Week ({len(totw)} players):")
            for player in totw:
                print(f"   - {player.name} ({player.position})")
        else:
            print("   Team of the Week not found or API unavailable")

        # Example 9: Get draft board
        print("\n9. Getting 2024 NFL Draft board:")
        draft_board = client.get_draft_board(2024, limit=10)

        if draft_board:
            print(f"   Top {len(draft_board)} prospects:")
            for i, prospect in enumerate(draft_board, 1):
                print(
                    f"   {i}. {prospect.name} - {prospect.position} ({prospect.college})"
                )
                print(f"      PFF Grade: {prospect.pff_grade}")
                if prospect.round_projection:
                    print(f"      Projected Round: {prospect.round_projection}")
                if prospect.strengths:
                    print(f"      Strengths: {', '.join(prospect.strengths[:3])}")
        else:
            print("   Draft board not found or API unavailable")

        # Example 10: Get mock draft
        print("\n10. Getting PFF mock draft:")
        mock_draft = client.get_mock_draft(2024, round=1)

        if mock_draft:
            print(f"   First round mock draft ({len(mock_draft)} picks):")
            for pick in mock_draft[:5]:  # Show first 5 picks
                print(
                    f"   {pick.pick}. {pick.team} - {pick.prospect.name} ({pick.prospect.position})"
                )
                if pick.analysis:
                    print(f"      Analysis: {pick.analysis[:100]}...")
                if pick.grade:
                    print(f"      Pick Grade: {pick.grade}")
        else:
            print("   Mock draft not found or API unavailable")

        # Example 11: Get pressure leaders
        print("\n11. Getting pass rush pressure leaders:")
        pressure_leaders = client.get_pressure_leaders(2024, position="EDGE", limit=5)

        if pressure_leaders:
            print(f"   Top {len(pressure_leaders)} pass rushers:")
            for i, leader in enumerate(pressure_leaders, 1):
                print(f"   {i}. Player {leader.player_id}: {leader.overall_grade}")
                if leader.defense:
                    print(f"      Pass Rush Grade: {leader.defense.pass_rush_grade}")
                    print(f"      Pressure Rate: {leader.defense.pressure_rate}%")
        else:
            print("   Pressure leaders not found or API unavailable")

        # Example 12: Get coverage leaders
        print("\n12. Getting coverage leaders:")
        coverage_leaders = client.get_coverage_leaders(2024, position="CB", limit=5)

        if coverage_leaders:
            print(f"   Top {len(coverage_leaders)} cornerbacks:")
            for i, leader in enumerate(coverage_leaders, 1):
                print(f"   {i}. Player {leader.player_id}: {leader.overall_grade}")
                if leader.defense:
                    print(f"      Coverage Grade: {leader.defense.coverage_grade}")
                    if leader.defense.passer_rating_allowed:
                        print(
                            f"      Passer Rating Allowed: {leader.defense.passer_rating_allowed}"
                        )
        else:
            print("   Coverage leaders not found or API unavailable")

        # Example 13: Get injury report
        print("\n13. Getting injury report:")
        injuries = client.get_injury_report(team="KC")

        if injuries:
            print(f"   Kansas City Chiefs injury report ({len(injuries)} players):")
            for injury in injuries:
                print(f"   - Player {injury.player_id}: {injury.injury_type}")
                print(f"     Severity: {injury.severity}")
                if injury.expected_recovery_time:
                    print(f"     Expected Recovery: {injury.expected_recovery_time}")
                if injury.games_missed_projection:
                    print(
                        f"     Games Missed Projection: {injury.games_missed_projection}"
                    )
        else:
            print("   Injury report not found or API unavailable")

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
