from database.table_definition import *

TABLE = TableDefinition(

    name="dim_coach",

    description="Stores football coaches.",

    columns=[

        Column("coach_id","INTEGER",False,True),

        Column("coach_name","VARCHAR",False),

        Column("nationality","VARCHAR"),

        Column("birth_date","DATE"),

        Column("photo","VARCHAR")

    ]

)