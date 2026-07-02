import pandas as pd


STAT_MAPPING = {

    "Shots on Goal": "shots_on_goal",
    "Shots off Goal": "shots_off_goal",
    "Total Shots": "total_shots",
    "Blocked Shots": "blocked_shots",
    "Shots insidebox": "shots_inside_box",
    "Shots outsidebox": "shots_outside_box",
    "Fouls": "fouls",
    "Corner Kicks": "corner_kicks",
    "Offsides": "offsides",
    "Ball Possession": "ball_possession",
    "Yellow Cards": "yellow_cards",
    "Red Cards": "red_cards",
    "Goalkeeper Saves": "goalkeeper_saves",
    "Total passes": "total_passes",
    "Passes accurate": "accurate_passes",
    "Passes %": "pass_accuracy",
    "expected_goals": "expected_goals",
    "goals_prevented": "goals_prevented"

}


def parse_percentage(value):

    if value is None:
        return None

    return int(str(value).replace("%", ""))


def parse_float(value):

    if value is None:
        return None

    return float(value)


class StatisticsTransformer:

    def transform(self, fixture_id, response):

        records = []

        for team_data in response:

            team = team_data["team"]
            statistics = team_data["statistics"]

            record = {

                "fixture_id": fixture_id,

                "team_id": team["id"]

            }

            for stat in statistics:

                column = STAT_MAPPING.get(stat["type"])

                if column is None:
                    continue

                value = stat["value"]

                if column in [

                    "ball_possession",
                    "pass_accuracy"

                ]:

                    value = parse_percentage(value)

                elif column in [

                    "expected_goals",
                    "goals_prevented"

                ]:

                    value = parse_float(value)

                record[column] = value

            records.append(record)

        return (
            pd.DataFrame(records)
            .drop_duplicates(
                subset=["fixture_id", "team_id"]
            )
            .reset_index(drop=True)
        )