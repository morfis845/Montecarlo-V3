import pandas as pd


class FixtureTransformer:

    def transform(self, response):

        records = []

        for item in response:

            fixture = item["fixture"]
            league = item["league"]
            status = fixture["status"]
            venue = fixture["venue"]
            teams = item["teams"]
            goals = item["goals"]
            score = item["score"]

            home_goals = goals["home"]
            away_goals = goals["away"]

            # Variables derivadas
            total_goals = home_goals + away_goals
            goal_difference = home_goals - away_goals
            btts = home_goals > 0 and away_goals > 0

            if home_goals > away_goals:
                winner = "HOME"
                result = "1"

            elif away_goals > home_goals:
                winner = "AWAY"
                result = "2"

            else:
                winner = "DRAW"
                result = "X"

            records.append({

                "fixture_id": fixture["id"],

                "league_id": league["id"],

                "season": league["season"],

                "date": fixture["date"],

                "timestamp": fixture["timestamp"],

                "timezone": fixture["timezone"],

                "round": league["round"],

                "status": status["long"],

                "status_short": status["short"],

                "elapsed": status["elapsed"],

                "extra_time": status["extra"],

                "stadium_id": venue["id"],

                "referee_name": fixture["referee"],

                "home_team_id": teams["home"]["id"],

                "away_team_id": teams["away"]["id"],

                "home_goals": home_goals,
                "away_goals": away_goals,

                "ht_home_goals": score["halftime"]["home"],
                "ht_away_goals": score["halftime"]["away"],

                "ft_home_goals": score["fulltime"]["home"],
                "ft_away_goals": score["fulltime"]["away"],

                "et_home_goals": score["extratime"]["home"],
                "et_away_goals": score["extratime"]["away"],

                "pen_home_goals": score["penalty"]["home"],
                "pen_away_goals": score["penalty"]["away"],

                # Variables derivadas
                "winner": winner,
                "result": result,
                "goal_difference": goal_difference,
                "total_goals": total_goals,
                "btts": btts,

            })

        return (
            pd.DataFrame(records)
            .drop_duplicates(subset=["fixture_id"])
            .reset_index(drop=True)
        )