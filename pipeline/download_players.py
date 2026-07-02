from core.database import DatabaseManager

from extract.players import PlayerExtractor

from transform.players import PlayerTransformer

from loaders.duckdb_loader import DuckDBLoader

import pandas as pd


class DownloadPlayersPipeline:

    def run(self):

        print("\nDownloading players...\n")

        db = DatabaseManager()

        fixtures = db.execute("""

            SELECT fixture_id

            FROM fact_fixture

            ORDER BY fixture_id

        """).fetchall()

        extractor = PlayerExtractor()

        transformer = PlayerTransformer()

        loader = DuckDBLoader()

        all_players = []

        all_matches = []

        for fixture in fixtures:

            fixture_id = fixture[0]

            try:

                response = extractor.download(
                    fixture_id
                )["response"]

                player_df, match_df = transformer.transform(
                    fixture_id,
                    response
                )

                all_players.append(player_df)

                all_matches.append(match_df)

                print(
                    f"{fixture_id}: {len(match_df)} players"
                )

            except Exception as e:

                print(
                    fixture_id,
                    e
                )

        players = (
            pd.concat(
                all_players,
                ignore_index=True
            )
            .drop_duplicates(
                subset=["player_id"]
            )
        )

        matches = pd.concat(
            all_matches,
            ignore_index=True
        )

        loader.insert_dataframe(
            players,
            "dim_player"
        )

        loader.insert_dataframe(
            matches,
            "fact_player_match"
        )

        loader.close()

        db.close()

        print("\nDone.\n")