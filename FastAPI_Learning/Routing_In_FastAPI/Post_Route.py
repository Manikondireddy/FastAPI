#Post Route: Creating new data

from fastapi import FastAPI

app = FastAPI()
@app.post("/user")
def create_user(name: str, age: int):
    return {
        "message": "User created",
        "name": name,
        "age": age
    }
