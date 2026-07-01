from dataclasses import dataclass, field


@dataclass
class Column:
    name: str
    data_type: str
    nullable: bool = True
    primary_key: bool = False
    unique: bool = False
    default: str | None = None


@dataclass
class ForeignKey:
    column: str
    reference_table: str
    reference_column: str


@dataclass
class Index:
    name: str
    columns: list[str]
    unique: bool = False


@dataclass
class TableDefinition:
    name: str
    description: str

    columns: list[Column] = field(default_factory=list)
    foreign_keys: list[ForeignKey] = field(default_factory=list)
    indexes: list[Index] = field(default_factory=list)