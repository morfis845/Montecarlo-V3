from extract.leagues import LeagueExtractor


extractor = LeagueExtractor()

data = extractor.download()

print(data.keys())

print(len(data["response"]))