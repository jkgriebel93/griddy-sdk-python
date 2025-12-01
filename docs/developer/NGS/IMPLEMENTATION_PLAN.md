# NGS API Integration Plan

This document outlines the plan to incorporate Next Gen Stats (NGS) endpoints from `nextgenstats.nfl.com` into the Griddy SDK.

## Executive Summary

The NGS API provides 21 endpoints across 6 categories. Analysis shows significant overlap with existing models, allowing for substantial reuse. The integration will require:
- **1 new sub-SDK**: `NextGenStats` (with nested sub-SDKs for organization)
- **~25 new entity models** (many NGS-specific)
- **~21 new request models** (one per endpoint)
- **~15 new response models** (some can share patterns)
- **Reuse of 8+ existing models** directly or with minor extensions

---

## 1. Model Reuse Analysis

### Models That Can Be Reused Directly

| Existing Model | NGS Usage | Notes |
|---------------|-----------|-------|
| `TeamInfo` | NGS Team in schedules/scores | Exact match for `homeTeam`/`visitorTeam` |
| `TeamScore` | Score breakdown by quarter | Exact match |
| `GameScore` | Game score with phase | Exact match |
| `GameSchedule` | NGS schedule response | Already has `ngs_game` flag |
| `VenueInfo` | Site information | Maps to NGS `site` object |
| `PlayerDetail` | Player in highlights/leaders | Has `ngs_position`, `ngs_position_group` |
| `SeasonTypeEnum` | REG/PRE/POST | Exact match |
| `Conference`/`Division` | Team conference/division | Exact match |

### Models That Need Extension or NGS-Specific Variants

| Existing Model | NGS Variant Needed | Differences |
|---------------|-------------------|-------------|
| `Play` | `NgsPlay` | NGS has more fields: `absoluteYardlineNumber`, `actualYardsToGo`, `playDirection`, `isBigPlay`, `isChangeOfPossession`, `playStats[]` |
| `PlayerPassingStats` | `NgsPassingStat` | Different field names (NGS uses longer descriptive names like `avgTimeToThrow` vs `avg_ttt`), different structure |
| `Team` | `NgsTeam` | NGS version has `divisionAbbr` as string, different field structure |

### New Models Required (NGS-Specific)

These have no existing equivalent:

**Stats Entities:**
- `NgsPassingStat` - NGS passing statboard entry
- `NgsReceivingStat` - NGS receiving statboard entry
- `NgsRushingStat` - NGS rushing statboard entry

**Game Center Entities:**
- `NgsPasserInfo` - Passer with passing zones
- `NgsPassingZone` - Zone-based passing breakdown
- `NgsRusherInfo` - Rusher with rush location maps
- `NgsRushInfo` - Rush statistics with location breakdown
- `NgsRushLocationStats` - Location-specific rush stats
- `NgsReceiverInfo` - Receiver with separation metrics
- `NgsReceptionInfo` - Reception statistics
- `NgsPassRusherInfo` - Pass rusher with separation metrics

**Leaders Entities:**
- `NgsSpeedLeader` - Speed leaderboard entry
- `NgsSackLeader` - Sack time leaderboard entry
- `NgsCompletionLeader` - Improbable completion entry
- `NgsYACLeader` - YAC over expectation entry
- `NgsDistanceLeader` - Distance covered entry
- `NgsTackleLeader` - Tackle distance entry
- `NgsERYLeader` - Rush yards over expected entry

**Content Entities:**
- `NgsChart` - Route/pass/carry chart
- `NgsChartPlayer` - Player in chart system
- `NgsHighlight` - Play highlight

**News Entities (api.nfl.com):**
- `NgsContentItem` - Article/video content
- `NgsContentTag` - Content tag with team/player refs
- `NgsThumbnail` - Content thumbnail
- `NgsPagination` - Pagination with JWT token

---

## 2. Sub-SDK Architecture

### Proposed Structure

```
GriddyNFL
└── ngs: NextGenStats                    # New top-level sub-SDK
    ├── league: NgsLeague                # League info endpoints
    │   ├── get_current_schedule()
    │   ├── get_teams()
    │   └── get_schedule()
    │
    ├── games: NgsGames                  # Game center endpoints
    │   ├── get_live_scores()
    │   └── get_game_overview()
    │
    ├── stats: NgsStats                  # Statboard endpoints
    │   ├── get_passing_stats()
    │   ├── get_receiving_stats()
    │   └── get_rushing_stats()
    │
    ├── leaders: NgsLeaders              # Top plays/leaderboards
    │   ├── get_fastest_ball_carriers()
    │   ├── get_fastest_sacks()
    │   ├── get_improbable_completions()
    │   ├── get_incredible_yac()
    │   ├── get_longest_plays()
    │   ├── get_longest_tackles()
    │   └── get_remarkable_rushes()
    │
    ├── content: NgsContent              # Charts & highlights
    │   ├── get_charts()
    │   ├── get_chart_players()
    │   └── get_highlights()
    │
    └── news: NgsNews                    # News (api.nfl.com)
        ├── get_mixed_content()
        ├── get_articles()
        └── get_video_clips()
```

### File Structure

```
src/griddy/nfl/
├── endpoints/
│   └── ngs/                             # NEW DIRECTORY
│       ├── __init__.py                  # NextGenStats sub-SDK
│       ├── basesdk.py                   # NgsBaseSDK (custom server URL)
│       ├── league.py                    # NgsLeague
│       ├── games.py                     # NgsGames
│       ├── stats.py                     # NgsStats
│       ├── leaders.py                   # NgsLeaders
│       ├── content.py                   # NgsContent
│       └── news.py                      # NgsNews (different server)
│
├── models/
│   ├── entities/
│   │   ├── ngs_play.py                  # Extended Play for NGS
│   │   ├── ngs_play_stat.py             # Play stat entry
│   │   ├── ngs_passing_stat.py          # Passing statboard
│   │   ├── ngs_receiving_stat.py        # Receiving statboard
│   │   ├── ngs_rushing_stat.py          # Rushing statboard
│   │   ├── ngs_passer_info.py           # Game center passer
│   │   ├── ngs_passing_zone.py          # Passing zone breakdown
│   │   ├── ngs_rusher_info.py           # Game center rusher
│   │   ├── ngs_rush_info.py             # Rush stats with locations
│   │   ├── ngs_receiver_info.py         # Game center receiver
│   │   ├── ngs_pass_rusher_info.py      # Pass rusher stats
│   │   ├── ngs_speed_leader.py          # Speed leader entry
│   │   ├── ngs_sack_leader.py           # Sack leader entry
│   │   ├── ngs_completion_leader.py     # Completion leader
│   │   ├── ngs_yac_leader.py            # YAC leader
│   │   ├── ngs_distance_leader.py       # Distance leader
│   │   ├── ngs_tackle_leader.py         # Tackle leader
│   │   ├── ngs_ery_leader.py            # ERY leader
│   │   ├── ngs_chart.py                 # Chart data
│   │   ├── ngs_highlight.py             # Highlight play
│   │   ├── ngs_content_item.py          # News content
│   │   └── ngs_content_tag.py           # Content tag
│   │
│   ├── requests/
│   │   ├── get_ngs_current_schedule_op.py
│   │   ├── get_ngs_teams_op.py
│   │   ├── get_ngs_schedule_op.py
│   │   ├── get_ngs_live_scores_op.py
│   │   ├── get_ngs_game_overview_op.py
│   │   ├── get_ngs_passing_stats_op.py
│   │   ├── get_ngs_receiving_stats_op.py
│   │   ├── get_ngs_rushing_stats_op.py
│   │   ├── get_ngs_fastest_ball_carriers_op.py
│   │   ├── get_ngs_fastest_sacks_op.py
│   │   ├── get_ngs_improbable_completions_op.py
│   │   ├── get_ngs_incredible_yac_op.py
│   │   ├── get_ngs_longest_plays_op.py
│   │   ├── get_ngs_longest_tackles_op.py
│   │   ├── get_ngs_remarkable_rushes_op.py
│   │   ├── get_ngs_charts_op.py
│   │   ├── get_ngs_chart_players_op.py
│   │   ├── get_ngs_highlights_op.py
│   │   ├── get_ngs_mixed_content_op.py
│   │   ├── get_ngs_articles_op.py
│   │   └── get_ngs_video_clips_op.py
│   │
│   └── responses/
│       ├── ngs_current_schedule_response.py
│       ├── ngs_teams_response.py         # Just array wrapper
│       ├── ngs_schedule_response.py      # Just array wrapper
│       ├── ngs_live_scores_response.py
│       ├── ngs_game_overview_response.py
│       ├── ngs_passing_stats_response.py
│       ├── ngs_receiving_stats_response.py
│       ├── ngs_rushing_stats_response.py
│       ├── ngs_speed_leaders_response.py
│       ├── ngs_sack_leaders_response.py
│       ├── ngs_completion_leaders_response.py
│       ├── ngs_yac_leaders_response.py
│       ├── ngs_distance_leaders_response.py
│       ├── ngs_tackle_leaders_response.py
│       ├── ngs_ery_leaders_response.py
│       ├── ngs_charts_response.py
│       ├── ngs_chart_players_response.py
│       ├── ngs_highlights_response.py
│       └── ngs_content_response.py       # Shared for news endpoints
```

---

## 3. Implementation Order

### Phase 1: Foundation
1. Create `NgsBaseSDK` with custom server URL handling
2. Create base entity models that are shared across endpoints:
   - `NgsPlay` (extended Play)
   - `NgsPlayStat`
3. Register `NextGenStats` in `GriddyNFL._sub_sdk_map`

### Phase 2: League & Game Center (Core Data)
1. **NgsLeague** sub-SDK:
   - Reuses: `GameSchedule`, `TeamInfo`, `VenueInfo`, `GameScore`
   - New models: Request models only
   - Endpoints: 3

2. **NgsGames** sub-SDK:
   - Reuses: `TeamInfo`, `GameScore`, `TeamScore`
   - New models: `NgsPasserInfo`, `NgsPassingZone`, `NgsRusherInfo`, `NgsRushInfo`, `NgsReceiverInfo`, `NgsPassRusherInfo`
   - Endpoints: 2

### Phase 3: Statistics
1. **NgsStats** sub-SDK:
   - New models: `NgsPassingStat`, `NgsReceivingStat`, `NgsRushingStat`
   - Note: These differ significantly from existing `PlayerPassingStats` etc.
   - Endpoints: 3

### Phase 4: Leaders/Top Plays
1. **NgsLeaders** sub-SDK:
   - Reuses: `NgsPlay`
   - New models: All leader entry types
   - Endpoints: 7

### Phase 5: Content
1. **NgsContent** sub-SDK:
   - New models: `NgsChart`, `NgsChartPlayer`, `NgsHighlight`
   - Endpoints: 3

### Phase 6: News (Different Server)
1. **NgsNews** sub-SDK:
   - Requires server override to `https://api.nfl.com`
   - New models: `NgsContentItem`, `NgsContentTag`, `NgsPagination`
   - Endpoints: 3

---

## 4. Server Configuration

### Primary Server (nextgenstats.nfl.com)
Most NGS endpoints use:
```python
NGS_SERVER_URL = "https://nextgenstats.nfl.com"
```

### Secondary Server (api.nfl.com)
News endpoints require:
```python
NFL_API_SERVER_URL = "https://api.nfl.com"
```

The `NgsNews` sub-SDK should override the server URL per-request or use a separate configuration.

---

## 5. Key Differences from Existing Patterns

### Field Naming
- NGS uses longer, descriptive field names (e.g., `avgTimeToThrow` vs `avgTTT`)
- Need to decide: match NGS exactly or normalize to existing SDK patterns

**Recommendation**: Match NGS field names exactly for NGS-specific models to maintain API fidelity and reduce confusion.

### Nested Player Objects
- NGS stats include embedded `player` objects with full details
- Existing SDK has separate player lookups

**Recommendation**: Keep the nested structure as NGS provides it.

### Authentication
- NGS endpoints appear to be public (no auth required based on docs)
- May need to verify if any endpoints require authentication

---

## 6. Testing Strategy

1. **Unit Tests**: Mock responses using fixtures from the markdown docs
2. **Integration Tests**: Live API calls (mark as `@pytest.mark.integration`)
3. **Model Validation**: Ensure all response fields are correctly mapped

---

## 7. Documentation Updates

1. Update `CLAUDE.md` with NGS sub-SDK information
2. Add NGS examples to any user-facing documentation
3. Document the dual-server configuration for news endpoints

---

## 8. Estimated Scope

| Category | Count |
|----------|-------|
| New Sub-SDKs | 7 (1 parent + 6 children) |
| New Entity Models | ~22 |
| New Request Models | 21 |
| New Response Models | ~15 |
| Reused Models | 8+ |
| Total New Files | ~70 |
| Endpoints | 21 |

---

## 9. Risk Considerations

1. **API Stability**: NGS API is unofficial/undocumented - may change without notice
2. **Rate Limiting**: Unknown rate limits on NGS endpoints
3. **Authentication**: May require auth for some endpoints not documented
4. **Data Freshness**: Live scores/game data freshness unknown

---

## 10. Next Steps

1. [ ] Review and approve this plan
2. [ ] Create `NgsBaseSDK` foundation
3. [ ] Implement Phase 1 (Foundation)
4. [ ] Implement remaining phases in order
5. [ ] Add comprehensive tests
6. [ ] Update documentation
