from core.api_client import APIClient


class TeamExtractor:

    def __init__(self):
        self.client = APIClient()

    def download(self, league_id, season):

        return self.client.get(

            "teams",

            params={

                "league": league_id,

                "season": season

            }

        )