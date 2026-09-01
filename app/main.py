from fastapi import FastAPI

app = FastAPI(
    title="My First FastAPI",
    description="A simple REST API built with FastAPI",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to my first FastAPI!",
        "status": "API is running"
    }


@app.get("/about")
def about():
    return {
        "project": "My First FastAPI",
        "author": "Muneer",
        "technology": "Python + FastAPI"
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": "Muneer",
        "role": "Computer Engineering Student"
    }


@app.get("/add")
def add_numbers(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b
    }