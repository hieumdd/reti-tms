from tms import pipeline
from tasks import cloud_tasks


def tasks_service(body: dict[str, str]):
    return {
        "tasks": cloud_tasks.create_tasks(
            [
                {
                    "table": i,
                    "start": body.get("start"),
                    "end": body.get("end"),
                }
                for i in pipeline.pipelines.keys()
            ],
            lambda x: x["table"],
        )
    }
