# Delete Route :Deleteing the data

from fastapi import FastAPI

app = FastAPI()
@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    return {
        "message": "User deleted",
        "user_id": user_id
    }
