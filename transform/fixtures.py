import pandas as pd


class FixtureTransformer:

    def transform(self, response):

        records = []

        for item in response:

            fixture = item["fixture"]
            league = item["league"]

            status = fixture["status"]

            venue = fixture["venue"]

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

            })

        return (
            pd.DataFrame(records)
            .drop_duplicates(subset=["fixture_id"])
            .reset_index(drop=True)
        )