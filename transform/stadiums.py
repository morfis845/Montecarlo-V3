import pandas as pd


class StadiumTransformer:

    def transform(self, response):

        records = []

        for item in response:

            venue = item["venue"]

            records.append({

                "stadium_id": venue["id"],

                "stadium_name": venue["name"],

                "address": venue["address"],

                "city": venue["city"],

                "capacity": venue["capacity"],

                "surface": venue["surface"],

                "image": venue["image"]

            })

        return (
            pd.DataFrame(records)
            .drop_duplicates(subset=["stadium_id"])
            .reset_index(drop=True)
        )