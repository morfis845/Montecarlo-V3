import pandas as pd


class TeamTransformer:

    def transform(self, response):

        records = []

        for item in response:

            team = item["team"]

            records.append({

                "team_id": team["id"],

                "team_name": team["name"],

                "team_code": team["code"],

                "country": team["country"],

                "founded": team["founded"],

                "national": team["national"],

                "logo": team["logo"]

            })

        return (
            pd.DataFrame(records)
            .drop_duplicates(subset=["team_id"])
            .reset_index(drop=True)
        )