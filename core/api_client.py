import time
import requests

from config.api import (
    API_BASE_URL,
    HEADERS,
    REQUEST_TIMEOUT,
    MAX_RETRIES,
    RETRY_DELAY
)


class APIClient:

    def get(self, endpoint, params=None):

        url = f"{API_BASE_URL}/{endpoint}"

        for attempt in range(MAX_RETRIES):

            try:

                response = requests.get(

                    url,

                    headers=HEADERS,

                    params=params,

                    timeout=REQUEST_TIMEOUT

                )

                response.raise_for_status()

                return response.json()

            except requests.RequestException as error:

                if attempt == MAX_RETRIES - 1:

                    raise error

                time.sleep(RETRY_DELAY)