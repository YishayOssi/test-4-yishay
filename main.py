from fastapi import FastAPI 
from function import *
import json


app = FastAPI()


@app.get("/test")
def test():
    print("GET /test called")
    return {"msg": "hi from test"}


@app.get("/test/{name}")
def save_name(name: str):
    print(f"Saving name: {name}")
    with open("names.txt", "a") as f:
        f.write(name + "\n")
    return {"msg": "saved user"}