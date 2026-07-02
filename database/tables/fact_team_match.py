from database.table_definition import *

TABLE = TableDefinition(

    name="fact_team_match",

    description="Stores team statistics for each fixture.",

    columns=[

        Column("fixture_id", "INTEGER", nullable=False),

        Column("team_id", "INTEGER", nullable=False),

        Column("shots_on_goal", "INTEGER"),

        Column("shots_off_goal", "INTEGER"),

        Column("total_shots", "INTEGER"),

        Column("blocked_shots", "INTEGER"),

        Column("shots_inside_box", "INTEGER"),

        Column("shots_outside_box", "INTEGER"),

        Column("fouls", "INTEGER"),

        Column("corner_kicks", "INTEGER"),

        Column("offsides", "INTEGER"),

        Column("ball_possession", "INTEGER"),

        Column("yellow_cards", "INTEGER"),

        Column("red_cards", "INTEGER"),

        Column("goalkeeper_saves", "INTEGER"),

        Column("total_passes", "INTEGER"),

        Column("accurate_passes", "INTEGER"),

        Column("pass_accuracy", "INTEGER"),

        Column("expected_goals", "DOUBLE"),

        Column("goals_prevented", "DOUBLE"),

    ],

    foreign_keys=[

        ForeignKey(
            "fixture_id",
            "fact_fixture",
            "fixture_id"
        ),

        ForeignKey(
            "team_id",
            "dim_team",
            "team_id"
        )

    ],

    indexes=[

        Index(
            "idx_team_match_fixture",
            ["fixture_id"]
        ),

        Index(
            "idx_team_match_team",
            ["team_id"]
        )

    ]

)