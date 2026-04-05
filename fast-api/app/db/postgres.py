from typing import Optional

import dotenv

import psycopg_pool
import os

database = 'main'
user = 'root'
host = os.environ.get("POSTGRES_HOST", '127.0.0.1')
password = os.environ.get("POSTGRES_PASSWORD")
port = os.environ.get("POSTGRES_PORT", 5432)

print(host, password, port)

DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{database}"

_pool: Optional[psycopg_pool.AsyncConnectionPool] = None

async def init_pool():
    global _pool
    _pool = psycopg_pool.AsyncConnectionPool(DATABASE_URL, open=False)
    await _pool.open()

async def close_pool():
    global _pool
    if _pool:
        await _pool.close()

def get_conn():
    global _pool
    return _pool.connection()