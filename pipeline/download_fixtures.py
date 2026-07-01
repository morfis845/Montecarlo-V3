from extract.fixtures import FixtureExtractor

from transform.fixtures import FixtureTransformer

from loaders.duckdb_loader import DuckDBLoader


class DownloadFixturesPipeline:

    def run(self, league_id, season):

        print("\nDownloading fixtures...\n")

        response = FixtureExtractor().download(

            league_id,
            season

        )["response"]

        fixture_df = FixtureTransformer().transform(response)

        print(f"Fixtures: {len(fixture_df)}")

        loader = DuckDBLoader()

        loader.insert_dataframe(

            fixture_df,

            "fact_fixture"

        )

        loader.close()
        print(fixture_df.head())

        print("\nDone.\n")