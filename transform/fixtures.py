import pandas as pd


class FixtureTransformer:

    def transform(self, response):

        records = []

        for item in response:

            fixture = item["fixture"]
            league = item["league"]

            records.append({

                "fixture_id": fixture["id"],

                "league_id": league["id"],

                "season": league["season"],

                "date": fixture["date"],

                "timestamp": fixture["timestamp"],

                "timezone": fixture["timezone"],

                "round": league["round"]

            })

        return (
            pd.DataFrame(records)
            .drop_duplicates(subset=["fixture_id"])
            .reset_index(drop=True)
        )