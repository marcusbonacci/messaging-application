from contextlib import asynccontextmanager
from dotenv import load_dotenv

from fastapi import FastAPI, Response
from app.db import postgres

from psycopg.rows import dict_row

import uuid

# Routers
from . import api
from . import middleware

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

@app.get("/favicon.ico")
async def favicon():
    return Response(status_code=204)