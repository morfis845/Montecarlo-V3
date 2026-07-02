import json

from core.api_client import APIClient

client = APIClient()

response = client.get(
    "fixtures/statistics",
    params={
        "fixture": 1378969
    }
)

print(f"Teams returned: {response['results']}\n")

print(
    json.dumps(
        response["response"],
        indent=4,
        ensure_ascii=False
    )
)