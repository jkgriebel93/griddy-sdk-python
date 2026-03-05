"""Shared column metadata registry for PFR parsers.

Centralises the ``int_columns``, ``float_columns``, and ``pct_columns``
definitions that were previously scattered across individual parser modules.
Each :class:`ColumnMetadata` instance describes the type-casting rules for
a single PFR HTML table.
"""

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class ColumnMetadata:
    """Immutable descriptor for the numeric columns of a PFR HTML table.

    Attributes:
        int_columns: Column ``data-stat`` names whose text values should be
            cast to ``int`` via :func:`safe_int`.
        float_columns: Column names whose text values should be cast to
            ``float`` via :func:`safe_float`.
        pct_columns: Column names whose text values contain a trailing ``%``
            sign and should be cast via :func:`safe_pct`.
    """

    int_columns: frozenset[str] = field(default_factory=frozenset)
    float_columns: frozenset[str] = field(default_factory=frozenset)
    pct_columns: frozenset[str] = field(default_factory=frozenset)


# ── Schedule ──────────────────────────────────────────────────────────

SCHEDULE = ColumnMetadata(
    int_columns=frozenset(
        {"pts_win", "pts_lose", "yards_win", "to_win", "yards_lose", "to_lose"}
    ),
)

# ── Draft ─────────────────────────────────────────────────────────────

DRAFT = ColumnMetadata(
    int_columns=frozenset(
        {
            "draft_round",
            "draft_pick",
            "age",
            "year_max",
            "all_pros_first_team",
            "pro_bowls",
            "years_as_primary_starter",
            "career_av",
            "draft_av",
            "g",
            "pass_cmp",
            "pass_att",
            "pass_yds",
            "pass_td",
            "pass_int",
            "rush_att",
            "rush_yds",
            "rush_td",
            "rec",
            "rec_yds",
            "rec_td",
            "tackles_solo",
            "def_int",
            "weight",
            "bench_reps",
            "broad_jump",
        }
    ),
    float_columns=frozenset(
        {
            "sacks",
            "forty_yd",
            "vertical",
            "cone",
            "shuttle",
        }
    ),
)

# ── Awards / HOF / Pro Bowl ───────────────────────────────────────────

AWARDS = ColumnMetadata(
    int_columns=frozenset(
        {
            "all_pros_first_team",
            "pro_bowls",
            "years_as_primary_starter",
            "career_av",
            "g",
            "gs",
            "pass_cmp",
            "pass_att",
            "pass_yds",
            "pass_td",
            "pass_long",
            "pass_int",
            "pass_sacked",
            "pass_sacked_yds",
            "rush_att",
            "rush_yds",
            "rush_td",
            "rush_long",
            "rec",
            "rec_yds",
            "rec_td",
            "rec_long",
            "all_purpose_yds",
            "all_td",
            "tackles_combined",
            "tackles_solo",
            "def_int",
            "age",
            "experience",
            "year_min",
            "year_max",
        }
    ),
    float_columns=frozenset({"sacks"}),
)

# ── Fantasy ───────────────────────────────────────────────────────────

FANTASY_TOP_PLAYERS = ColumnMetadata(
    int_columns=frozenset(
        {
            "g",
            "gs",
            "pass_cmp",
            "pass_att",
            "pass_yds",
            "pass_td",
            "pass_int",
            "rush_att",
            "rush_yds",
            "rush_td",
            "targets",
            "rec",
            "rec_yds",
            "rec_td",
            "fumbles",
            "fumbles_lost",
            "all_td",
            "two_pt_md",
            "two_pt_pass",
            "vbd",
            "fantasy_rank_pos",
            "fantasy_rank_overall",
        }
    ),
    float_columns=frozenset(
        {
            "rush_yds_per_att",
            "rec_yds_per_rec",
            "fantasy_points",
            "fantasy_points_ppr",
            "draftkings_points",
            "fanduel_points",
        }
    ),
)

FANTASY_MATCHUPS = ColumnMetadata(
    int_columns=frozenset(
        {
            "g",
            "gs",
            "fantasy_points_proj_rank",
            "draftkings_points_proj_rank",
            "fanduel_points_proj_rank",
        }
    ),
    float_columns=frozenset(
        {
            "pass_cmp",
            "pass_att",
            "pass_yds",
            "pass_td",
            "pass_int",
            "pass_sacked",
            "rush_att",
            "rush_yds",
            "rush_td",
            "targets",
            "rec",
            "rec_yds",
            "rec_td",
            "fantasy_points_per_game",
            "draftkings_points_per_game",
            "fanduel_points_per_game",
            "opp_fantasy_points_per_game",
            "opp_draftkings_points_per_game",
            "opp_fanduel_points_per_game",
        }
    ),
)

FANTASY_POINTS_ALLOWED = ColumnMetadata(
    int_columns=frozenset(
        {
            "g",
            "pass_cmp",
            "pass_att",
            "pass_yds",
            "pass_td",
            "pass_int",
            "two_pt_pass",
            "pass_sacked",
            "rush_att",
            "rush_yds",
            "rush_td",
            "targets",
            "rec",
            "rec_yds",
            "rec_td",
            "two_pt_md",
            "fumbles_lost",
        }
    ),
    float_columns=frozenset(
        {
            "fantasy_points",
            "draftkings_points",
            "fanduel_points",
            "fantasy_points_per_game",
            "draftkings_points_per_game",
            "fanduel_points_per_game",
        }
    ),
)

FANTASY_RZ_PASSING = ColumnMetadata(
    int_columns=frozenset(
        {
            "pass_cmp",
            "pass_att",
            "pass_yds",
            "pass_td",
            "pass_int",
            "pass_cmp_in_10",
            "pass_att_in_10",
            "pass_yds_in_10",
            "pass_td_in_10",
            "pass_int_in_10",
        }
    ),
    float_columns=frozenset(
        {
            "pass_cmp_perc",
            "pass_cmp_perc_in_10",
        }
    ),
)

FANTASY_RZ_RECEIVING = ColumnMetadata(
    int_columns=frozenset(
        {
            "targets",
            "rec",
            "rec_yds",
            "rec_td",
            "targets_in_10",
            "rec_in_10",
            "rec_yds_in_10",
            "rec_td_in_10",
        }
    ),
    pct_columns=frozenset(
        {
            "catch_pct",
            "targets_pct",
            "catch_pct_in_10",
            "targets_in_10_pct",
        }
    ),
)

FANTASY_RZ_RUSHING = ColumnMetadata(
    int_columns=frozenset(
        {
            "rush_att",
            "rush_yds",
            "rush_td",
            "rush_att_in_10",
            "rush_yds_in_10",
            "rush_td_in_10",
            "rush_att_in_5",
            "rush_yds_in_5",
            "rush_td_in_5",
        }
    ),
    pct_columns=frozenset(
        {
            "rush_att_pct",
            "rush_att_in_10_pct",
            "rush_att_in_5_pct",
        }
    ),
)

# ── Team Franchise ────────────────────────────────────────────────────

TEAM_FRANCHISE = ColumnMetadata(
    int_columns=frozenset(
        {
            "wins",
            "losses",
            "ties",
            "points",
            "points_opp",
            "points_diff",
            "rank_off_pts",
            "rank_off_yds",
            "rank_def_pts",
            "rank_def_yds",
            "rank_takeaway_giveaway",
            "rank_points_diff",
            "rank_yds_diff",
            "teams_in_league",
        }
    ),
    float_columns=frozenset(
        {"mov", "sos_total", "srs_total", "srs_offense", "srs_defense"}
    ),
)

# ── Team Season ───────────────────────────────────────────────────────

TEAM_SEASON_GAMES = ColumnMetadata(
    int_columns=frozenset(
        {
            "pts_off",
            "pts_def",
            "first_down_off",
            "yards_off",
            "pass_yds_off",
            "rush_yds_off",
            "to_off",
            "first_down_def",
            "yards_def",
            "pass_yds_def",
            "rush_yds_def",
            "to_def",
        }
    ),
    float_columns=frozenset({"exp_pts_off", "exp_pts_def", "exp_pts_st"}),
)

# ── Birthplaces ───────────────────────────────────────────────────────

BIRTHPLACES_LANDING = ColumnMetadata(
    int_columns=frozenset(
        {
            "players",
            "players_active",
            "hofers",
            "g",
            "td",
            "most_td",
            "most_g",
        }
    ),
)

BIRTHPLACES_FILTERED = ColumnMetadata(
    int_columns=frozenset(
        {
            "year_min",
            "year_max",
            "all_pros_first_team",
            "pro_bowls",
            "years_as_primary_starter",
            "career_av",
            "g",
            "pass_cmp",
            "pass_att",
            "pass_yds",
            "pass_td",
            "pass_long",
            "pass_int",
            "pass_sacked",
            "pass_sacked_yds",
            "rush_att",
            "rush_yds",
            "rush_td",
            "rush_long",
            "rec",
            "rec_yds",
            "rec_td",
            "rec_long",
        }
    ),
)

# ── Official Profile ─────────────────────────────────────────────────

OFFICIAL_STATS = ColumnMetadata(
    int_columns=frozenset(
        {
            "g",
            "g_playoffs",
            "home",
            "visitor",
            "pen_total",
            "pen_yds",
        }
    ),
    float_columns=frozenset(
        {
            "home_pct",
            "home_wpct",
            "pen_per_g",
            "pen_yds_per_g",
            "lg_home_pct",
            "lg_home_wpct",
            "lg_pen_per_g",
            "lg_pen_yds_per_g",
            "rel_home_pct",
            "rel_home_wpct",
            "rel_pen_per_g",
            "rel_pen_yds_per_g",
        }
    ),
)

OFFICIAL_GAMES = ColumnMetadata(
    int_columns=frozenset(
        {
            "points_opp",
            "penalties_opp",
            "penalties_yds_opp",
            "points",
            "penalties",
            "penalties_yds",
        }
    ),
)

# ── Coach Profile ─────────────────────────────────────────────────────

COACH_RESULTS = ColumnMetadata(
    int_columns=frozenset(
        {
            "age",
            "g",
            "wins",
            "losses",
            "ties",
            "g_playoffs",
            "wins_playoffs",
            "losses_playoffs",
            "rank_team",
            "chall_num",
            "chall_won",
        }
    ),
    float_columns=frozenset({"srs_total", "srs_offense", "srs_defense"}),
)

COACH_RESULTS_FOOTER = ColumnMetadata(
    int_columns=frozenset(
        {
            "g",
            "wins",
            "losses",
            "ties",
            "g_playoffs",
            "wins_playoffs",
            "losses_playoffs",
            "chall_num",
            "chall_won",
        }
    ),
    float_columns=frozenset({"rank_avg"}),
)

COACH_RANKS = ColumnMetadata(
    int_columns=frozenset(
        {
            "teams_in_league",
            "rank_win_percentage",
            "rank_takeaway_giveaway",
            "rank_points_diff",
            "rank_yds_diff",
            "rank_off_yds",
            "rank_off_pts",
            "rank_off_turnovers",
            "rank_off_rush_att",
            "rank_off_rush_yds",
            "rank_off_rush_td",
            "rank_off_rush_yds_per_att",
            "rank_off_fumbles_lost",
            "rank_off_pass_att",
            "rank_off_pass_yds",
            "rank_off_pass_td",
            "rank_off_pass_int",
            "rank_off_pass_net_yds_per_att",
            "rank_def_yds",
            "rank_def_pts",
            "rank_def_turnovers",
            "rank_def_rush_att",
            "rank_def_rush_yds",
            "rank_def_rush_td",
            "rank_def_rush_yds_per_att",
            "rank_def_fumbles_rec",
            "rank_def_pass_att",
            "rank_def_pass_yds",
            "rank_def_pass_td",
            "rank_def_pass_int",
            "rank_def_pass_net_yds_per_att",
        }
    ),
)

COACH_HISTORY = ColumnMetadata(
    int_columns=frozenset({"coach_age"}),
)

COACH_CHALLENGES = ColumnMetadata(
    int_columns=frozenset({"down", "yds_to_go"}),
)

# ── Season Overview ───────────────────────────────────────────────────

SEASON_STANDINGS = ColumnMetadata(
    int_columns=frozenset({"wins", "losses", "points", "points_opp", "points_diff"}),
)

SEASON_PLAYOFF_STANDINGS = ColumnMetadata(
    int_columns=frozenset({"wins", "losses", "ties"}),
)

SEASON_PLAYOFF_RESULTS = ColumnMetadata(
    int_columns=frozenset({"pts_win", "pts_lose"}),
)
