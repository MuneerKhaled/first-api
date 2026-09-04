from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task Manager API")


class Task(BaseModel):
    title: str
    description: str
    completed: bool = False


tasks = []


@app.get("/")
def home():
    return {"message": "Task Manager API is running!"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {
        "message": "Task created successfully",
        "task": task
    }


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id >= len(tasks):
        return {"error": "Task not found"}

    return tasks[task_id]


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id >= len(tasks):
        return {"error": "Task not found"}

    deleted_task = tasks.pop(task_id)

    return {
        "message": "Task deleted successfully",
        "task": deleted_task
    }