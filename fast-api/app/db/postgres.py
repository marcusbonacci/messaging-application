from typing import Optional

import psycopg_pool
import os

from app.core import CONFIG

_pool: Optional[psycopg_pool.AsyncConnectionPool] = None

async def init_pool():
    global _pool
    _pool = psycopg_pool.AsyncConnectionPool(CONFIG.POSTGRES_URI, open=False)
    await _pool.open()

async def close_pool():
    global _pool
    if _pool:
        await _pool.close()

def get_conn():
    global _pool
    return _pool.connection()