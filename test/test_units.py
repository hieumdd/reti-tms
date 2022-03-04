import pytest

from tms import pipeline, tms_service
# from tasks import tasks_service

TIME_FRAME = [
    ("auto", (None, None)),
    ("manual", ("2020-01-01", "2022-03-01")),
]


@pytest.fixture(
    params=[i[1] for i in TIME_FRAME],
    ids=[i[0] for i in TIME_FRAME],
)
def timeframe(request):
    return request.param


class TestTMS:
    @pytest.mark.parametrize(
        "pipeline",
        pipeline.pipelines.values(),
        ids=pipeline.pipelines.keys(),
    )
    def test_service(self, pipeline, timeframe):
        res = tms_service.pipeline_service(pipeline, *timeframe)
        print(res)
        assert res["output_rows"] >= 0


# class TestTasks:
#     def test_service(self, timeframe):
#         res = tasks_service.create_tasks_service(
#             {
#                 "start": timeframe[0],
#                 "end": timeframe[1],
#             }
#         )
#         print(res)
#         assert res["tasks"] > 0
