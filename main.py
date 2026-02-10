from fastapi import FastAPI
from Models import User
from typing import List
app = FastAPI()

users = [
    User(id= 1, name= "Mani"),
    User(id= 2, name= "Mini")
]

@app.get("/users/{user_id}")
def get_user(user_id:int):
    return {"message":"created","user_id":user_id}