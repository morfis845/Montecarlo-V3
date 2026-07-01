import pandas as pd


class SeasonTransformer:

    def transform(self, response):

        records = []

        for item in response:

            league_id = item["league"]["id"]

            for season in item["seasons"]:

                coverage = season["coverage"]

                records.append({

                    "league_id": league_id,

                    "season": season["year"],

                    "start_date": season["start"],

                    "end_date": season["end"],

                    "current": season["current"],

                    "coverage_events": coverage["fixtures"]["events"],

                    "coverage_lineups": coverage["fixtures"]["lineups"],

                    "coverage_fixture_statistics": coverage["fixtures"]["statistics_fixtures"],

                    "coverage_player_statistics": coverage["fixtures"]["statistics_players"],

                    "coverage_standings": coverage["standings"],

                    "coverage_players": coverage["players"],

                    "coverage_top_scorers": coverage["top_scorers"],

                    "coverage_top_assists": coverage["top_assists"],

                    "coverage_top_cards": coverage["top_cards"],

                    "coverage_injuries": coverage["injuries"],

                    "coverage_predictions": coverage["predictions"],

                    "coverage_odds": coverage["odds"]

                })

        # ===== Todo esto va FUERA de los for =====

        df = (
            pd.DataFrame(records)
            .drop_duplicates(subset=["league_id", "season"])
            .reset_index(drop=True)
        )

        return df