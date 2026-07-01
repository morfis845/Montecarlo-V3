from core.api_client import APIClient


class FixtureExtractor:

    def __init__(self):
        self.client = APIClient()

    def download(self, league_id: int, season: int):

        return self.client.get(
            "fixtures",
            params={
                "league": league_id,
                "season": season
            }
        )