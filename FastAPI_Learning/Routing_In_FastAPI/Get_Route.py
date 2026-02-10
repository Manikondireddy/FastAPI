#Get route:Read or fetch the data

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "GET request working"}
