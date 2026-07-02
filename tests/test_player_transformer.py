from extract.players import PlayerExtractor
from transform.players import PlayerTransformer

fixture_id = 1378969

response = PlayerExtractor().download(fixture_id)["response"]

player_df, player_match_df = PlayerTransformer().transform(
    fixture_id,
    response
)

print(player_df.head())

print()

print(player_match_df.head())