import json
import os

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

app = FastAPI()

# PROVISIONAL HANDLING OF THE "FAKE" DATABASE
# TODO: make sure the name is correct and where in the project locate it.
# I guess that it should be ignored by git.
TODOs_FILE = "todos.json"
TODOs_DATABASE = []

if os.path.exists(TODOs_FILE):
    with open(TODOs_FILE, "r") as f:
        TODOs_DATABASE = json.load(f)

# /
@app.get("/")
async def root():
    return {"message": "Hello World"}


# /list-todos
@app.get("/list-todos")
def list_books():
    return {"todos": TODOs_DATABASE}

# /add-todo
@app.post("/add-todo")
def add_book(title, description):
    todo = {"title": title, "description": description}
    json_book = jsonable_encoder(todo)
    TODOs_DATABASE.append(json_book)
    with open(TODOs_FILE, "w") as f:
        json.dump(TODOs_DATABASE, f)
    return {"message": f"TODO {title} was added.", "description": description}
