from fastapi import FastAPI
from database import get_async_pool

import uuid

app = FastAPI()

pool = get_async_pool()

@app.get("/")
def index():
    return "Server is online!"

@app.get("/users")
async def get_users(skip: int = 0, limit: int = 10):
    async with pool.connection() as conn:
        await conn.execute("SELECT * FROM users LIMIT %s OFFSET %s", (limit, skip))
        rows = conn.cursor.fetchall()
        return {"users": rows}

# @app.get("/users/{user_id}")
# def get_user(user_id: uuid.UUID):
#     cursor.execute("SELECT * FROM users WHERE user_id = %s", (str(user_id),))
#     row = cursor.fetchone()
#     return row