from typing import Optional

import psycopg_pool
import os

database = 'main'
user = 'root'
host = '127.0.0.1'
password = os.environ["POSTGRES_PASSWORD"] or None
port = 5432

DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{database}"

_pool = Optional[psycopg_pool.AsyncConnectionPool]

async def init_pool():
    global _pool
    _pool = psycopg_pool.AsyncConnectionPool(DATABASE_URL)

async def close_pool():
    global _pool
    if _pool:
        await _pool.close()

def get_conn():
    global _pool
    return _pool.connection()