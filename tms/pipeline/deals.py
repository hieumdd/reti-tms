from tms.pipeline.tms import Pipeline

deals = Pipeline(
    "deals",
    """
    SELECT
        id,
        labels,
        updated_at
    FROM
        deals
    """,
    [
        {"name": "id", "type": "NUMERIC"},
        {"name": "labels", "type": "STRING", "mode": "REPEATED"},
        {"name": "updated_at", "type": "TIMESTAMP"},
    ],
    lambda rows: [
        {
            "id": row["id"],
            "labels": row["labels"],
            "updated_at": row["updated_at"].isoformat(timespec="seconds"),
        }
        for row in rows
    ],
)
