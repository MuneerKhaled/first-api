```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Simple Task API")


class TaskData(BaseModel):
    title: str
    description: str
    completed: bool = False


database = []


def find_task(task_id: int):
    for task in database:
        if task["id"] == task_id:
            return task
    return None


@app.get("/")
def index():
    return {"message": "Welcome to the Task API"}


@app.get("/tasks")
def all_tasks():
    return {"tasks": database}


@app.post("/tasks")
def add_task(data: TaskData):

    task_id = len(database) + 1

    new_task = {
        "id": task_id,
        "title": data.title,
        "description": data.description,
        "completed": data.completed
    }

    database.append(new_task)

    return {
        "message": "New task added",
        "task": new_task
    }


@app.get("/tasks/{task_id}")
def single_task(task_id: int):

    task = find_task(task_id)

    if task is None:
        return {"message": "No such task"}

    return task


@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):

    task = find_task(task_id)

    if task is None:
        return {"message": "No such task"}

    database.remove(task)

    return {
        "message": "Task removed successfully",
        "deleted": task
    }
```
