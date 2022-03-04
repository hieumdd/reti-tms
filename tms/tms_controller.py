from tms import pipeline, tms_service


def tms_controller(body: dict[str, str]):
    return tms_service.pipeline_service(
        pipeline.pipelines[body["table"]],
        body.get("start"),
        body.get("end"),
    )
