```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Todo Management API")


class Todo(BaseModel):
    title: str
    description: str
    completed: bool = False


todo_list = []
next_id = 1


@app.get("/")
def root():
    return {"status": "Todo API is working"}


@app.get("/todos")
def list_todos():
    return {
        "total": len(todo_list),
        "todos": todo_list
    }


@app.post("/todos")
def add_todo(todo: Todo):
    global next_id

    new_todo = {
        "id": next_id,
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed
    }

    todo_list.append(new_todo)
    next_id += 1

    return {
        "message": "Todo added",
        "data": new_todo
    }


@app.get("/todos/{todo_id}")
def find_todo(todo_id: int):

    for todo in todo_list:
        if todo["id"] == todo_id:
            return todo

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )


@app.delete("/todos/{todo_id}")
def remove_todo(todo_id: int):

    for index, todo in enumerate(todo_list):
        if todo["id"] == todo_id:
            removed = todo_list.pop(index)

            return {
                "message": "Todo removed",
                "data": removed
            }

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )
```
