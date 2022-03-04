from typing import Any
import os

import psycopg2
import psycopg2.extras


def get_connection() -> psycopg2.connection:
    return psycopg2.connect(
        dbname="reti_production_ver2",
        host=os.getenv("PG_HOST", ""),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PWD"),
        cursor_factory=psycopg2.extras.RealDictCursor,
    )


def query(sql: str):
    def _query(*args) -> list[dict[str, Any]]:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
    return _query
