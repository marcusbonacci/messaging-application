from fastapi import FastAPI
from database import cursor

import uuid

app = FastAPI()

@app.get("/")
def index():
    return "Server is online!"

@app.get("/users")
def get_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    return rows

@app.get("/users/{user_id}")
def get_user(user_id: str):
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    row = cursor.fetchone()
    return row