from database.table_definition import TableDefinition


def build_create_table(table: TableDefinition) -> str:

    definitions = []

    primary_keys = []

    for column in table.columns:

        sql = f"{column.name} {column.data_type}"

        if not column.nullable:
            sql += " NOT NULL"

        if column.unique:
            sql += " UNIQUE"

        if column.default is not None:
            sql += f" DEFAULT {column.default}"

        definitions.append(sql)

        if column.primary_key:
            primary_keys.append(column.name)

    if primary_keys:

        definitions.append(

            f"PRIMARY KEY ({', '.join(primary_keys)})"

        )

    for fk in table.foreign_keys:

        definitions.append(

            f"FOREIGN KEY ({fk.column}) "
            f"REFERENCES {fk.reference_table}({fk.reference_column})"

        )

    return f"""
CREATE TABLE IF NOT EXISTS {table.name} (

    {',\n    '.join(definitions)}

);
""".strip()

def build_indexes(table: TableDefinition) -> list[str]:

    sql = []

    for index in table.indexes:

        unique = "UNIQUE " if index.unique else ""

        sql.append(

            f"""
CREATE {unique}INDEX IF NOT EXISTS {index.name}

ON {table.name}

({", ".join(index.columns)});
""".strip()

        )

    return sql