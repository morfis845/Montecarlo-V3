from core.api_client import APIClient


class StatisticsExtractor:

    def __init__(self):

        self.client = APIClient()

    def download(self, fixture_id):

        return self.client.get(

            "fixtures/statistics",

            params={

                "fixture": fixture_id

            }

        )