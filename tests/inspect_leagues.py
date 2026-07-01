import json

from extract.leagues import LeagueExtractor


data = LeagueExtractor().download()

print(json.dumps(

    data["response"][0],

    indent=4,

    ensure_ascii=False

))