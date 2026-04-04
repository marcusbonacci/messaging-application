from contextlib import asynccontextmanager

from fastapi import FastAPI
from database import postgres

from psycopg.rows import dict_row

import uuid

@asynccontextmanager
async def lifespan(app: FastAPI):
    await postgres.init_pool()
    yield
    await postgres.close_pool()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def index():
    return "Server is online!"

@app.get("/users")
async def get_users(limit: int = 10, skip: int = 0):
    query = "SELECT * FROM users LIMIT %s OFFSET %s"
    async with postgres.get_conn() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute(query, (limit, skip))
            rows = await cur.fetchall()
            return {"users": rows}

@app.get("/users/{user_id}")
async def get_user(user_id: uuid.UUID):
    query = "SELECT * FROM users WHERE user_id = %s"
    async with postgres.get_conn() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute(query, (str(user_id),))
            row = await cur.fetchall()
            return row