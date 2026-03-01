# Frivolities and Fun Stuff

## Players

### Players Who Played for Multiple Teams
- URL: https://www.pro-football-reference.com/friv/players-who-played-for-multiple-teams-franchises.fcgi
- Find all the players who played for some combination of teams. Can also request a list of players who played exclusively for those teams.

**Inputs:**
- `level`
- `Franchise 1`
  - `t1`
- `Franchise 2`
  - `t2`
- `Franchise 3`
  - `t3`
- `Franchise 4`
  - `t4`
- `Only these teams`
  - `exclusively` -> Values are `1` or `0`
- [Example HTML](../../data/pfr_frivolities/friv-players-who-played-for-multiple-teams-inputs.html)

**Outputs:**
- A listing of the top five players (by approximate value) that played for the selected teams.
- Table listing passing statistics for all players who threw a pass for each of these franchises
- Table listing rushing statistics for all players who had at least one carry for each of these franchises
- Table listing receiving statistics for all players who had at least one reception for each of these franchises
- Table listing all players who played for each franchise.
- [Example HTML](../../data/pfr_frivolities/friv-players-who-played-for-multiple-teams-results.html)


### Player Statistical Milestones
- URL: https://www.pro-football-reference.com/friv/milestones.cgi
 - [Example HTML](../../data/pfr_frivolities/friv-statistical-milestones.html)
- Pick any of our counting stats and find out who is about to climb the all-time leaderboard, or who is about to cross a significant threshold

  **Inputs**:

  - `stat`
    - `g`
    - `pass_att`
    - `pass_cmp`
    - `pass_yds`
    - `pass_td`
    - `rush_att`
    - `rush_yds`
    - `rush_td`
    - `rec`
    - `rec_yds`
    - `rec_td`
    - `yds_from_scrimmage`
    - `all_purpose_yds`
    - `all_td`
    - `scoring`
    - `sacks`
    - `def_int`
    - `fga`
    - `fgm`
    - `punt`
    - `punt_yds`

  **Outputs:** 

  - A table with a list of milestones (e.g. 300 games played, 275 games, 250 games, etc.) and active players who are approaching said milestones
  - A table with a list of the top 25 career leaders in the selected category

### Upcoming Milestones
- URL: https://www.pro-football-reference.com/friv/upcoming-milestones.htm
- [Example HTML](../../data/pfr_frivolities/friv-upcoming-milestones.html)
- Track players who may achieve certain milestones or ascend the career leaderboard in their next game.

### Players Born Today
- URL: https://www.pro-football-reference.com/friv/birthdays.cgi
- [HTML Example](../../data/pfr_frivolities/friv-birthdays.html)
- Find all players born today or any other day of the year.

- **Inputs:**
- `month`
- `day`

**Outputs:**
A table listing players whose date of birth is the specified month and day, along with selected statistics.

### Random Pages
- URL: https://www.pro-football-reference.com/rand.fcgi
- Search for the term 'Random' or save the link as a bookmark and be sent to a random page on this site.

### Player Birthplaces
- URL: https://www.pro-football-reference.com/friv/birthplaces.htm
- Find players by the state or country of their birth.
- Landing page is a table listing country and state, plus information such as the number of players from that region, number of hall of famers, etc. You can also select a state or country, as detailed next.
  - [Landing Page HTML Example](../../data/pfr_frivolities/friv-player-birthplaces-landing.html)


**Inputs:**

- `country`
- `state`

**Outputs:**

- A table listing players that were born in the selected country and state, along with selected statistics.
- [HTML Example](../../data/pfr_frivolities/friv-player-birthplaces-pa.html)

### Active Players Born Before A Date
- URL: https://www.pro-football-reference.com/friv/age.cgi
- Feeling old? Find active players who were born before a given date.

**Inputs:**
- `month`
- `day`
- `year`

**Outputs:**
- Table listing _active_ players born on or before the specified date, along with select statistics.
- [HTML Example](../../data/pfr_frivolities/friv-players-born-on-or-before-date.html)

### Players By Uniform Number
- URL: https://www.pro-football-reference.com/players/uniform.cgi
- Find players by uniform numbers, for a given team or NFL-wide.

**Inputs:**
- `number`
- `team` (optional)

**Outputs:**
- Table listing players who wore the specified number for the specified franchise (if provided)
- [HTML Example](../../data/pfr_frivolities/friv-player-uniform-num-6-pit.html)

### Quarterback Wins vs. Each Franchise
- URL: https://www.pro-football-reference.com/friv/qb-wins.htm
- See which quarterbacks have beat the most teams in their careers.

**Inputs:**
- None

**Outputs:**
- A table listing `Player`, `Beat`, and `Not Beat` columns. The `Beat` column is an integer 
indicating the number of franchises the QB has beaten, and `Not Beat` lists the franchises he hasn't beaten.
- [HTML Example](../../data/pfr_frivolities/friv-qb-beaten-franchises.html)

### Non-Quarterback Passers
- URL: https://www.pro-football-reference.com/friv/nonqb.htm
- All non-quarterbacks to have played after 1960 and thrown a pass in a game.

**Inputs:**
- None

**Outputs:** 
- Table listing players whose primary position is/was _not_ QB who have thrown a pass in the NFL 
along with select statistics
- [HTML Examples](../../data/pfr_frivolities/friv-non-qb-passers.html)

### Non-Skill Position TD Scorers
- URL: https://www.pro-football-reference.com/friv/odd_td.htm
- Non-skill position players to score an offensive TD in a game.

**Inputs:**
- None

**Outputs:**
- Table listing all instances of non-skill position players scoring a touchdown.
- [HTML Example](../../data/pfr_frivolities/friv-non-skill-pos-td.html)

### Octopus Tracker
- URL: https://www.pro-football-reference.com/friv/octopus-tracker.htm
- All players since 1994 to score the TD and 2pt conversion in a single possession.

**Inputs:**
- None

**Outputs:**
- Table listing all instances of an "Octupus"
- [HTML Example](../../data/pfr_frivolities/friv-octopus-tracker.html)

### Cups of Coffee
- URL: https://www.pro-football-reference.com/friv/coffee.htm
- Players with only one game played in their careers.
**Inputs:**
- None

**Outputs:**
- Table listing all players who played only a single game in the NFL
- [HTML Example](../../data/pfr_frivolities/friv-cups-of-coffee.html)

### Multi-Sport Players
- URL: https://www.pro-football-reference.com/friv/multisport.htm
- Football players who also played other sports professionally.

**Inputs:**
- None

**Outputs:**
- Table listing athletes who played multiple sports professionally
- [HTML Example](../../data/pfr_frivolities/friv-multisport-athletes.html)

### Pronunciation Guide
- URL: https://www.pro-football-reference.com/friv/pronunciation-guide.htm
- A list of all player pronunciations.

**Inputs:**
- None

**Outputs:**
- A list of difficult to pronounce player names
- [HTML Example](../../data/pfr_frivolities/friv-pronunciation-guide.html)


## Teams and Game

### Overtime Ties
- URL: https://www.pro-football-reference.com/friv/nfl-ties.htm
- A list of tied games in the sudden death overtime era (since 1974).

**Inputs:**
- None

**Outputs:**
- Table listing all ties since sudden-death overtime was instituted in 1974
- [HTML Example](../../data/pfr_frivolities/friv-ties.html)

### Last Undefeated Team
- URL: https://www.pro-football-reference.com/friv/last-undefeated.htm
- A list of the last team(s) to be undefeated in every year of the league.

**Inputs:**
- None

**Outputs:**
- Table listing the last undefeated team(s) in every season, along with their season outcomes
- [HTML Examples](../../data/pfr_frivolities/friv-final-undefeated-teams.html)

### Win Probability Calculator
- URL: https://www.pro-football-reference.com/play-index/win_prob.cgi
- Input down, distance, score differential, time remaining and yard line to find out what the Win Probability is for that game situation
- This is actually part of Stathead, and the link doesn't seem to return what it claims to. Skip for now.

### NFL Passer Rating Calculator
- URL: https://www.pro-football-reference.com/about/qb-rating.htm
- Input attempts, completions, yards, touchdowns, and interceptions to calculate an NFL passer rating.
- Could calculate this without using PFR - skip for now.

### Standings on Any Date
- URL: https://www.pro-football-reference.com/boxscores/standings.cgi
- Find NFL or AFL standings on any date in history.

**Inputs:**
- `week` + `year`
- **OR**
- `month` + `day` + `year`

**Outputs:**
- Tables displaying standings as of the week or data specified. Standings include wins, losses, ties, W-L%, 
Points For, Points Against, Point Differential, and Average Margin of Victory
- [HTML Example](../../data/pfr_frivolities/friv-standings-as-of-date.html)