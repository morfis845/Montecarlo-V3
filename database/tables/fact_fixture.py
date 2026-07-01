from database.table_definition import *

TABLE = TableDefinition(

    name="fact_fixture",

    description="Stores football fixtures.",

    columns=[

        Column(
            "fixture_id",
            "INTEGER",
            primary_key=True,
            nullable=False
        ),

        Column(
            "league_id",
            "INTEGER",
            nullable=False
        ),

        Column(
            "season",
            "INTEGER",
            nullable=False
        ),

        Column(
            "date",
            "TIMESTAMP",
            nullable=False
        ),

        Column(
            "timestamp",
            "BIGINT",
            nullable=False
        ),

        Column(
            "timezone",
            "VARCHAR",
            nullable=False
        ),

        Column(
            "round",
            "VARCHAR",
            nullable=False
        ),

        Column(
            "status",
            "VARCHAR"
        ),

        Column(
            "status_short",
            "VARCHAR"
        ),

        Column(
            "elapsed",
            "INTEGER"
        ),

        Column(
            "extra_time",
            "INTEGER"
        ),
        Column(
            "stadium_id",
            "INTEGER"
        ),

        Column(
            "referee_name",
            "VARCHAR"
        ),
        Column(
            "home_team_id",
            "INTEGER",
            nullable=False
        ),

        Column(
            "away_team_id",
            "INTEGER",
            nullable=False
        ),
        Column("home_goals", "INTEGER"),
        Column("away_goals", "INTEGER"),

        Column("ht_home_goals", "INTEGER"),
        Column("ht_away_goals", "INTEGER"),

        Column("ft_home_goals", "INTEGER"),
        Column("ft_away_goals", "INTEGER"),

        Column("et_home_goals", "INTEGER"),
        Column("et_away_goals", "INTEGER"),

        Column("pen_home_goals", "INTEGER"),
        Column("pen_away_goals", "INTEGER"),

        Column("winner", "VARCHAR"),

        Column("result", "VARCHAR"),

        Column("goal_difference", "INTEGER"),

        Column("total_goals", "INTEGER"),

        Column("btts", "BOOLEAN"),

    ],

    foreign_keys=[

        ForeignKey(
            "league_id",
            "dim_league",
            "league_id"
        ),
        ForeignKey(
            "stadium_id",
            "dim_stadium",
            "stadium_id"
        ),
        ForeignKey(
            "home_team_id",
            "dim_team",
            "team_id"
        ),

        ForeignKey(
            "away_team_id",
            "dim_team",
            "team_id"
        ),

    ],

    indexes=[

        Index(
            "idx_fixture_date",
            ["date"]
        ),

        Index(
            "idx_fixture_league",
            ["league_id"]
        )

    ]

)