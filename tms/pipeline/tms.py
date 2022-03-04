from dataclasses import dataclass
from typing import Callable, Any


@dataclass
class Pipeline:
    table: str
    sql: str
    schema: list[dict[str, Any]]
    transform: Callable[[list[dict[str, Any]]], list[dict[str, Any]]] = lambda rows: rows
    cursor_key: str = "updated_at"
    id_key: str = "id"
