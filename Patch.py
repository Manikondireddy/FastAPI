from fastapi import FastAPI
from Models import User, UserUpdate

app = FastAPI()

users = [
    User(id=1, name="Mani"),
    User(id=2, name="Mini")
]

@app.patch("/users/{user_id}")
def patch_user(user_id: int, user: UserUpdate):
    for u in users:
        if u.id == user_id:
            if user.name:
                u.name = user.name
            return u
    return {"error": "User not found"}
