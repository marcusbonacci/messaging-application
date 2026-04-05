from contextlib import asynccontextmanager

from fastapi import FastAPI
from db import postgres

from psycopg.rows import dict_row

import uuid

# Routers
import api

@asynccontextmanager
async def lifespan(app: FastAPI):
    await postgres.init_pool()
    yield
    await postgres.close_pool()

app = FastAPI(lifespan=lifespan)
app.include_router(api.health_router)
app.include_router(api.users_router)

@app.get("/")
def index():
    return "Server is online!"