from core.api_client import APIClient


class LeagueExtractor:

    def __init__(self):

        self.client = APIClient()

    def download(self):

        return self.client.get(

            "leagues"

        )