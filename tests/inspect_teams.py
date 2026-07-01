import json

from core.api_client import APIClient


client = APIClient()

data = client.get(

    "teams",

    params={

        "league":39,

        "season":2025

    }

)

print(

    f"Teams returned: {data['results']}"

)

print()

print(

    json.dumps(

        data["response"][0],

        indent=4,

        ensure_ascii=False

    )

)