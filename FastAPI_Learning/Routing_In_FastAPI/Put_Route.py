#Put Route: Updating the existing Data

from fastapi import FastAPI

app = FastAPI()
@app.put("/user/{user_id}")
def update_user(user_id: int, name: str):
    return {
        "message": "User updated",
        "user_id": user_id,
        "updated_name": name 
    }
 