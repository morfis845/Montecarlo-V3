from core.api_client import APIClient


class PlayerExtractor:

    def __init__(self):

        self.client = APIClient()

    def download(self, fixture_id):

        return self.client.get(

            "fixtures/players",

            params={

                "fixture": fixture_id

            }

        )