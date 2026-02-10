from fastapi import FastAPI
from Models import User, UserCreate

app = FastAPI()

users = [
    User(id=1, name="Mani"),
    User(id=2, name="Mini")
]

@app.post("/users")
def create_user(user: UserCreate):
    new_id = len(users) + 1
    new_user = User(id=new_id, name=user.name)
    users.append(new_user)
    return new_user
