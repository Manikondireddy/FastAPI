from fastapi import FastAPI
from Models import User

app = FastAPI()

users = [
    User(id=1, name="Mani"),
    User(id=2, name="Mini")
]

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for u in users:
        if u.id == user_id:
            users.remove(u)
            return {"message": "User deleted"}
    return {"error": "User not found"}

