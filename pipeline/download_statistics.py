import pandas as pd

from core.database import DatabaseManager

from extract.statistics import StatisticsExtractor
from transform.statistics import StatisticsTransformer
from loaders.duckdb_loader import DuckDBLoader


class DownloadStatisticsPipeline:

    def run(self):

        print("\nDownloading statistics...\n")

        db = DatabaseManager()

        fixtures = db.execute("""

            SELECT fixture_id

            FROM fact_fixture

            ORDER BY fixture_id

        """).fetchall()

        extractor = StatisticsExtractor()
        transformer = StatisticsTransformer()
        loader = DuckDBLoader()

        all_data = []

        for fixture in fixtures:

            fixture_id = fixture[0]

            try:

                response = extractor.download(
                    fixture_id
                )["response"]

                df = transformer.transform(
                    fixture_id,
                    response
                )

                all_data.append(df)

                print(
                    f"Fixture {fixture_id}: {len(df)} teams"
                )

            except Exception as e:

                print(
                    f"Error in fixture {fixture_id}: {e}"
                )

        if all_data:

            final_df = pd.concat(
                all_data,
                ignore_index=True
            )

            loader.insert_dataframe(
                final_df,
                "fact_team_match"
            )

            print(
                f"\nInserted {len(final_df)} rows."
            )

        else:

            print("\nNo statistics found.")

        loader.close()
        db.close()

        print("\nDone.\n")