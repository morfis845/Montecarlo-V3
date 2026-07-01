import pandas as pd


class LeagueTransformer:

    def transform(self, response):

        records = []

        for item in response:

            league = item["league"]
            country = item["country"]

            records.append({

                "league_id": league["id"],
                "league_name": league["name"],
                "country": country["name"],
                "country_code": country["code"],
                "country_flag": country["flag"],
                "type": league["type"],
                "logo": league["logo"]

            })

        return pd.DataFrame(records)