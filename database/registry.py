from database.tables import (
    dim_league,
    dim_season,
    dim_team,
    dim_player,
    dim_coach,
    dim_referee,
    dim_stadium,
    fact_fixture,
    fact_team_match,
    fact_player_match,
    fact_lineup,
    fact_injuries,
    fact_odds,
    system_metadata,
    fact_player_match
)

TABLES = [

    dim_league.TABLE,
    dim_season.TABLE,
    dim_coach.TABLE,
    dim_referee.TABLE,
    dim_stadium.TABLE,
    dim_team.TABLE,
    dim_player.TABLE,
    fact_fixture.TABLE,
    fact_team_match.TABLE,
    fact_player_match.TABLE,
    fact_lineup.TABLE,
    fact_injuries.TABLE,
    fact_odds.TABLE,
    system_metadata.TABLE,

]