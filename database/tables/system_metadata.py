from database.table_definition import (
    Column,
    TableDefinition
)

TABLE = TableDefinition(

    name="system_metadata",

    description="Stores database metadata.",

    columns=[

        Column("key","VARCHAR",False,True),

        Column("value","VARCHAR"),

        Column("updated_at","TIMESTAMP",False,default="CURRENT_TIMESTAMP")

    ]

)