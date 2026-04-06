from contextlib import asynccontextmanager
from dotenv import load_dotenv

from fastapi import FastAPI
from app.db import postgres

from psycopg.rows import dict_row

import uuid

# Routers
from . import api
from . import middleware

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await postgres.init_pool()
    yield
    await postgres.close_pool()

app = FastAPI(lifespan=lifespan)

app.middleware("http")(middleware.process_time_header)

app.include_router(api.health_router)
app.include_router(api.users_router)
app.include_router(api.audience_router)

@app.get("/")
def index():
    return "Server is online!"