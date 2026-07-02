import pandas as pd


def parse_int(value):

    if value is None:
        return None

    return int(value)


def parse_float(value):

    if value is None:
        return None

    return float(value)


class PlayerTransformer:

    def transform(self, fixture_id, response):

        player_records = []

        match_records = []

        for team in response:

            team_id = team["team"]["id"]

            for player in team["players"]:

                info = player["player"]

                stats = player["statistics"][0]

                # -----------------------
                # dim_player
                # -----------------------

                player_records.append({

                    "player_id": info["id"],

                    "player_name": info["name"],

                    "photo": info["photo"]

                })

                # -----------------------
                # fact_player_match
                # -----------------------

                match_records.append({

                    "fixture_id": fixture_id,

                    "team_id": team_id,

                    "player_id": info["id"],

                    # Games
                    "minutes": parse_int(stats["games"]["minutes"]),
                    "shirt_number": parse_int(stats["games"]["number"]),
                    "position": stats["games"]["position"],
                    "rating": parse_float(stats["games"]["rating"]),
                    "captain": stats["games"]["captain"],
                    "substitute": stats["games"]["substitute"],

                    # Offsides
                    "offsides": parse_int(stats["offsides"]),

                    # Shots
                    "shots_total": parse_int(stats["shots"]["total"]),
                    "shots_on_target": parse_int(stats["shots"]["on"]),

                    # Goals
                    "goals": parse_int(stats["goals"]["total"]),
                    "assists": parse_int(stats["goals"]["assists"]),
                    "goals_conceded": parse_int(stats["goals"]["conceded"]),
                    "goalkeeper_saves": parse_int(stats["goals"]["saves"]),

                    # Passes
                    "passes_total": parse_int(stats["passes"]["total"]),
                    "passes_key": parse_int(stats["passes"]["key"]),
                    "passes_accuracy": parse_int(stats["passes"]["accuracy"]),

                    # Tackles
                    "tackles": parse_int(stats["tackles"]["total"]),
                    "blocks": parse_int(stats["tackles"]["blocks"]),
                    "interceptions": parse_int(stats["tackles"]["interceptions"]),

                    # Duels
                    "duels_total": parse_int(stats["duels"]["total"]),
                    "duels_won": parse_int(stats["duels"]["won"]),

                    # Dribbles
                    "dribbles_attempts": parse_int(stats["dribbles"]["attempts"]),
                    "dribbles_success": parse_int(stats["dribbles"]["success"]),
                    "dribbled_past": parse_int(stats["dribbles"]["past"]),

                    # Fouls
                    "fouls_drawn": parse_int(stats["fouls"]["drawn"]),
                    "fouls_committed": parse_int(stats["fouls"]["committed"]),

                    # Cards
                    "yellow_cards": parse_int(stats["cards"]["yellow"]),
                    "red_cards": parse_int(stats["cards"]["red"]),

                    # Penalties
                    "penalties_won": parse_int(stats["penalty"]["won"]),
                    "penalties_committed": parse_int(stats["penalty"]["commited"]),
                    "penalties_scored": parse_int(stats["penalty"]["scored"]),
                    "penalties_missed": parse_int(stats["penalty"]["missed"]),
                    "penalties_saved": parse_int(stats["penalty"]["saved"])

                })

        player_df = (
            pd.DataFrame(player_records)
            .drop_duplicates(subset=["player_id"])
            .reset_index(drop=True)
        )

        player_match_df = (
            pd.DataFrame(match_records)
            .drop_duplicates(subset=["fixture_id", "player_id"])
            .reset_index(drop=True)
        )

        return player_df, player_match_df