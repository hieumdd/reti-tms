from typing import Any
from tms.tms_controller import tms_controller
from tasks.tasks_service import task_service

def main(request):
    data: dict[str, Any] = request.get_json()

    print(data)

    if "table" in data:
        response = tms_controller(data)
    elif "tasks" in data:
        response = task_service(data)
    else:
        raise ValueError(data)

    print(response)

    return response

