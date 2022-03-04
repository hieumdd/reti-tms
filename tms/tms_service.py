from typing import Union, Optional
from compose import compose

from tms.pipeline import tms
from db.postgres import query
from db.bigquery import get_last_timestamp, load


def pipeline_service(
    pipeline: tms.Pipeline,
    start: Optional[str],
    end: Optional[str],
) -> dict[str, Union[str, int]]:
    return compose(
        lambda x: {
            "table": pipeline.table,
            "start": start,
            "end": end,
            "output_rows": x,
        },
        load(pipeline.table, pipeline.schema, pipeline.id_key, pipeline.cursor_key),
        pipeline.transform,
        query(pipeline.sql),
        lambda x: {"start": x[0], "end": x[1]},
        get_last_timestamp(pipeline.table, pipeline.cursor_key),
    )((start, end))
