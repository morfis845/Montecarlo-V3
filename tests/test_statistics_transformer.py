from extract.statistics import StatisticsExtractor
from transform.statistics import StatisticsTransformer


fixture_id = 1378969

response = StatisticsExtractor().download(
    fixture_id
)["response"]

df = StatisticsTransformer().transform(
    fixture_id,
    response
)

print(df)