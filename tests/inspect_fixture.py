import json

from core.api_client import APIClient

client = APIClient()

data = client.get(
    "fixtures",
    params={
        "league": 39,
        "season": 2025,
        "round": "Regular Season - 1"
    }
)

print(f"Fixtures returned: {data['results']}")
print()

print(
    json.dumps(
        data["response"][0],
        indent=4,
        ensure_ascii=False
    )
)