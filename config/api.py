import os

from dotenv import load_dotenv

load_dotenv()


API_BASE_URL = "https://v3.football.api-sports.io"

API_KEY = os.getenv("API_FOOTBALL_KEY")

HEADERS = {

    "x-apisports-key": API_KEY

}

REQUEST_TIMEOUT = 30

MAX_RETRIES = 3

RETRY_DELAY = 2