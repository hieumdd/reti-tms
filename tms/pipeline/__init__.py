from tms.pipeline.deals import deals

pipelines = {
    i.table: i
    for i in [
        deals,
    ]
}
